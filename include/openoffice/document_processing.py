"""
B2UConverter — UNO extension for OpenOffice.org
File: include/openoffice/document_processing.py

Copyright ©2009  Ministry of Science and Technology of Vietnam
License: GNU Lesser General Public License version 2.1
Authors: Jean Christophe André <jcandre@hanoilug.org>
         Lê Quốc Thái <lqthai@hanoilug.org>
         Võ Đức Phương <vdphuong@hanoilug.org>
"""

import uno
import unohelper
from com.sun.star.lang import Locale

def processTextPortion(text):
    old = text.getString()
    new = None
    upper = False
    convert = None
    encoding = None
    properties = {}
    fontName = text.getPropertyValue("CharFontName")
    logging.debug("processing text portion [%s] with font [%s]", old, fontName)
    # XXX: sometime fontName==None ?!? see test file from IFI
    # XXX: manage situation where the fontname has got wrong letter case
    #      (eg: .vntime for .VnTime)
    if not fontName: return # XXX wrong wrong wrong

    if fontName.startswith('.Vn'):
        upper = fontName.endswith('H')
        convert = convertVietnameseString
        encoding = 'internal_vntime_tcvn'
        if fontName.startswith('.VnCourier New'):
            properties["CharFontName"] = "Courier New"
        elif fontName.startswith('.VnArial'):
            properties["CharFontName"] = "Arial"
        else:
            properties["CharFontName"] = "Times New Roman"
        properties["CharLocale"] = Locale('vi', 'VN', '')
    elif fontName.startswith('VNI'):
        upper = False
        convert = convertVietnameseString
        encoding = 'internal_vni'
        if fontName == 'VNI-Couri':
            properties["CharFontName"] = "Courier New"
        elif fontName == 'VNI-Arial':
            properties["CharFontName"] = "Arial"
        else:
            properties["CharFontName"] = "Times New Roman"
        properties["CharLocale"] = Locale('vi', 'VN', '')

    if convert is not None:
        try:
            new = convert(old, encoding, upper=upper)
        except:
            global _error_count
            _error_count += 1
            new = None
            properties = {}
            if hasattr(text, 'CharBackColor'):
                properties["CharBackColor"] = 0xFF0000
            elif hasattr(text, 'CharColor'):
                properties["CharColor"] = 0xFF0000

    # FIXME: using setString makes loose all properties!!!
    # FIXME: may be use text.getPropertyValues() & text.setPropertyValues ??
    # TODO: - save _all_ properties into an array
    # TODO: - push additionnal properties if any
    # TODO: - update the text string content with setString
    # TODO: - reset properties from properties array
    if new and new != old:
        text.setString(new)
        #text.String = new
    for k,v in properties.items():
        text.setPropertyValue(k, v)

def processTextParagraph(paragraph):
    #logging.debug("dir(paragraph) = ( %s )", ' '.join(dir(paragraph)))
    #logging.debug("  services: %s", ', '.join(paragraph.getSupportedServiceNames()))
    #logging.debug("  hasElements: %s", paragraph.hasElements())
    enum = paragraph.createEnumeration()
    #logging.debug("dir(enum) = ( %s )", ' '.join(dir(enum)))
    # reverse process all portions, since text boundaries
    # get altered when using setString with a longer string
    portions = []
    while (enum.hasMoreElements()):
        portions.append(enum.nextElement())
    for textPortion in reversed(portions):
        type = textPortion.getPropertyValue("TextPortionType")
        logging.debug("processing text paragraph element (type %s) [%s]",
                                            type, textPortion.getString())
        if type == 'Text':
            processTextPortion(textPortion)
        elif type == 'SoftPageBreak':
            pass
        elif type == 'Frame':
            # logging.debug("found a Frame (ignored, parsed later)")
            pass
        else:
            logging.warning("unknown text portion type '%s'", type)

def processTextTable(table):
    for name in table.getCellNames():
        cell = table.getCellByName(name)
        processText(cell)

def processText(text):
    enum = text.createEnumeration()
    while (enum.hasMoreElements()):
        paragraph = enum.nextElement()
        if paragraph.supportsService("com.sun.star.text.TextTable"):
            logging.debug("processing text element (table)")
            # this is a table "paragraph"
            processTextTable(paragraph)
        else:
            logging.debug("processing text element [%s]", paragraph.getString())
            # this is a text paragraph
            processTextParagraph(paragraph)

def processShape(shape):
    type = shape.getShapeType()
    if type == "com.sun.star.drawing.TextShape":
        processText(shape)
    elif type == "com.sun.star.drawing.GroupShape":
        for index in range(shape.getCount()):
            processShape(shape.getByIndex(index))
    #elif type == "FrameShape":
    #    pass
    #elif type == "com.sun.star.drawing.LineShape":
    #    pass
    #elif type == "com.sun.star.drawing.RectangleShape":
    #    pass
    elif type == "com.sun.star.drawing.CustomShape":
        processText(shape)
    elif type == "com.sun.star.presentation.TitleTextShape":
        processText(shape)
    elif type == "com.sun.star.presentation.SubtitleShape":
        processText(shape)
    elif type == "com.sun.star.presentation.OutlinerShape":
        processText(shape)
    else:
        logging.warning("unknown shape type '%s' for object named '%s'",
                                                        type, shape.Name)

def processPageStyle(pageStyle):
    logging.debug("processing page style '%s'", pageStyle.Name)
    if pageStyle.HeaderIsOn:
        if pageStyle.HeaderText:
            processText(pageStyle.HeaderText)
        if pageStyle.HeaderTextLeft:
            processText(pageStyle.HeaderTextLeft)
        if pageStyle.HeaderTextRight:
            processText(pageStyle.HeaderTextRight)
    if pageStyle.FooterIsOn:
        if pageStyle.FooterText:
            processText(pageStyle.FooterText)
        if pageStyle.FooterTextLeft:
            processText(pageStyle.FooterTextLeft)
        if pageStyle.FooterTextRight:
            processText(pageStyle.FooterTextRight)

def processTextDocument(doc):
    # convert text body
    text = doc.Text
    processText(text)
    # convert text frames
    frames = doc.getTextFrames()
    for index in range(frames.getCount()):
        frame = frames.getByIndex(index)
        processText(frame)
    # convert text shapes (in draw pages)
    drawPages = doc.getDrawPage()
    for index in range(drawPages.getCount()):
        drawPage = drawPages.getByIndex(index)
        processShape(drawPage)
    # convert text footnotes
    footnotes = doc.getFootnotes()
    for index in range(footnotes.getCount()):
        footnote = footnotes.getByIndex(index)
        logging.warning("found footnote '%s' (ignored)", footnote.Name)
        #logging.debug("dir(footnote) : %s", "|".join(dir(footnote)))
        #processText(footnote)
    # convert text sections
    sections = doc.getTextSections()
    #logging.debug("dir(sections) : %s", "|".join(dir(sections)))
    for index in range(sections.getCount()):
        section = sections.getByIndex(index)
        logging.warning("found section '%s' (ignored)", section.Name)
        #logging.debug("dir(section) : %s", "|".join(dir(section)))
        #processText(section)
    # CONVERT PAGE STYLES (mainly for text header & footer)
    pageStyles = doc.getStyleFamilies().getByName("PageStyles")
    for index in range(pageStyles.getCount()):
        pageStyle = pageStyles.getByIndex(index)
        logging.info("found page style '%s'", pageStyle.Name)
        if pageStyle.isInUse():
            processPageStyle(pageStyle)

def processSheet(sheet):
    cursor = sheet.createCursor()
    cursor.gotoEndOfUsedArea(False)
    cursor.gotoStartOfUsedArea(True)
    rangeAddress = cursor.getRangeAddress()
    rows = rangeAddress.EndRow - rangeAddress.StartRow + 1
    columns = rangeAddress.EndColumn - rangeAddress.StartColumn + 1
    logging.debug("rows=%s & columns=%s", str(rows), str(columns))
    for row in range(rows):
        for column in range(columns):
            logging.debug("cell(%s,%s)", str(column), str(row))
            cell = cursor.getCellByPosition(column, row)
            logging.debug("dir(cell) = ( %s )", ' '.join(dir(cell)))
            processText(cell.Text)

def processSpreadsheetDocument(doc):
    # disable automatic-calculation during process
    autoCalc = doc.isAutomaticCalculationEnabled()
    if autoCalc: doc.enableAutomaticCalculation(False)
    # process all sheets
    enum = doc.getSheets().createEnumeration()
    while (enum.hasMoreElements()):
        sheet = enum.nextElement()
        processSheet(sheet)
    # re-enable automatic-calculation if required
    if autoCalc: doc.enableAutomaticCalculation(True)

def processDrawPresentationDocument(doc):
    # process all pages
    drawPages = doc.getDrawPages()
    for index in range(drawPages.getCount()):
        drawPage = drawPages.getByIndex(index)
        # convert page body
        logging.info("converting draw page '%s'", drawPage.getName())
        for index in range(drawPage.getCount()):
            draw = drawPage.getByIndex(index)
            processShape(draw)
        # FIXME: should process text in drawPage.getNotesPage() too
        # convert page name
        # FIXME: should not arbitrary convert from VnTime_TCVN
        # FIXME: should detect if name has already been converted
        drawPage.setName(convertVietnameseString(drawPage.getName(), 'internal_vntime_tcvn'))

def processDocument(doc):
    # XXX: check if it really works
    #doc.RecordChanges = False

    if doc.supportsService("com.sun.star.text.GenericTextDocument"):
        logging.info("this is a text document")
        processTextDocument(doc)
    elif doc.supportsService("com.sun.star.sheet.SpreadsheetDocument"):
        logging.info("this is a spreadsheet document")
        processSpreadsheetDocument(doc)
    elif doc.supportsService("com.sun.star.presentation.PresentationDocument"):
        logging.info("this is a presentation document")
        processDrawPresentationDocument(doc)
    elif doc.supportsService("com.sun.star.drawing.GenericDrawingDocument"):
        logging.info("this is a drawing document")
        processDrawPresentationDocument(doc)
    else:
        logging.warning("unknown document type")

    # convert document title
    info = doc.getDocumentInfo()
    # FIXME: should not arbitrary convert from VnTime_TCVN
    # FIXME: should detect if title has already been converted
    info.Title = convertVietnameseString(info.Title, 'internal_vntime_tcvn')

    # XXX: check if it really works
    #doc.RecordChanges = True

class B2UConverterOOoParser(object):
    """OOo document parser."""

    def __init__(self):
        pass

