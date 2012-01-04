"""
B2UConverter — UNO extension for OpenOffice.org and LibreOffice
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

class OOoVietnameseTextConverter(object):

    def __init__(self, textConverter, removeDiacritics=False):
        self.textConverter = textConverter
        self.removeDiacriticsFlag = removeDiacritics
        self.stats = { 'vntime_tcvn': 0, 'vni': 0 }

    def convertTextPortion(self, text):
        old = text.getString()
        new = None
        properties = {}
        fontName = text.getPropertyValue("CharFontName")
        logging.debug("processing text portion [%s] with font [%s]",
                                                        old, fontName)
        # XXX: sometime fontName==None ?!? see test file from IFI
        # XXX: manage situation where the fontname has got wrong letter case
        #      (eg: .vntime for .VnTime)
        if not fontName: return # XXX wrong wrong wrong

        if fontName.startswith('.Vn'):
            self.stats['vntime_tcvn'] += 1
            new = self.textConverter.convertString(old, 'vntime_tcvn',
                                            upper=fontName.endswith('H'))
            if fontName.startswith('.VnCourier New'):
                properties["CharFontName"] = "Courier New"
            elif fontName.startswith('.VnArial'):
                properties["CharFontName"] = "Arial"
            else:
                properties["CharFontName"] = "Times New Roman"
            properties["CharLocale"] = Locale('vi', 'VN', '')
        elif fontName.startswith('VNI'):
            self.stats['vni'] += 1
            new = self.textConverter.convertString(old, 'vni', upper=False)
            if fontName == 'VNI-Couri':
                properties["CharFontName"] = "Courier New"
            elif fontName == 'VNI-Arial':
                properties["CharFontName"] = "Arial"
            else:
                properties["CharFontName"] = "Times New Roman"
            properties["CharLocale"] = Locale('vi', 'VN', '')

        # remove diacritics as requested...
        if self.removeDiacriticsFlag:
            if new and new != old:
                new = self.textConverter.removeDiacritics(new)
            else:
                new = self.textConverter.removeDiacritics(old)

        # FIXME: using setString makes loose all properties!!!
        # FIXME: may be use text.getPropertyValues() & text.setPropertyValues ??
        # TODO: - save _all_ properties into an array
        # TODO: - push additionnal properties if any
        # TODO: - update the text string content with setString
        # TODO: - reset properties from properties array
        if new and new != old:
            textStart = text.getStart()
            textEnd = text.getEnd()
            docText = textStart.getText()
            textCurs = docText.createTextCursorByRange(textStart)
            docText.insertString(textEnd, new, False)
            textCurs.goRight(len(old), True)
            textCurs.setString("")
            #text.setString(new)
            #text.String = new
        for k,v in properties.items():
            text.setPropertyValue(k, v)
 
    def mostUsedEncoding(self):
        if self.stats['vntime_tcvn'] > self.stats['vni']:
            return 'vntime_tcvn'
        else:
            return 'vni'


class OOoDocumentParser(object):
    """OpenOffice.org and LibreOffice document parser."""

    def __init__(self, textPortionConverter=None):
        self.stats = { }
        self.setTextPortionConverter(textPortionConverter)

    def _reset_stats(self):
        self.stats['errors'] = 0

    def setTextPortionConverter(self, textPortionConverter):
        self._reset_stats()
        if textPortionConverter:
            self.textPortionConverter = textPortionConverter
            self.textConverter = textPortionConverter.textConverter
        else:
            self.textPortionConverter = None
            self.textConverter = None

    def processTextPortion(self, text):
        if not self.textPortionConverter:
            # TODO: shall we log that void processing?
            return
        try:
            self.textPortionConverter.convertTextPortion(text)
        except:
            logging.exception("Error during conversion:")
            self.stats['errors'] += 1
            if hasattr(text, 'CharBackColor'):
                text.setPropertyValue('CharBackColor', 0xFF0000)
            elif hasattr(text, 'CharColor'):
                text.setPropertyValue('CharColor', 0xFF0000)

    def processTextParagraph(self, paragraph):
        #logging.debug("dir(paragraph) = ( %s )", ' '.join(dir(paragraph)))
        #logging.debug("  services: %s", ', '.join(paragraph.getSupportedServiceNames()))
        #logging.debug("  hasElements: %s", paragraph.hasElements())
        enum = paragraph.createEnumeration()
        #logging.debug("dir(enum) = ( %s )", ' '.join(dir(enum)))
        # XXX: warning: text boundaries get altered when using setString
        #      with a longer string; should probably use a cursor here...
        while (enum.hasMoreElements()):
            textPortion = enum.nextElement()
            type = textPortion.getPropertyValue("TextPortionType")
            logging.debug("processing text paragraph element (type %s) [%s]",
                                                type, textPortion.getString())
            if type == 'Text':
                self.processTextPortion(textPortion)
            elif type == 'SoftPageBreak':
                pass
            elif type == 'Frame':
                # logging.debug("found a Frame (ignored, parsed later)")
                pass
            else:
                logging.warning("unknown text portion type '%s'", type)

    def processTextTable(self, table):
        for name in table.getCellNames():
            cell = table.getCellByName(name)
            self.processText(cell)

    def processText(self, text):
        enum = text.createEnumeration()
        while (enum.hasMoreElements()):
            paragraph = enum.nextElement()
            if paragraph.supportsService("com.sun.star.text.TextTable"):
                logging.debug("processing text element (table)")
                # this is a table "paragraph"
                self.processTextTable(paragraph)
            else:
                logging.debug("processing text element [%s]", paragraph.getString())
                # this is a text paragraph
                self.processTextParagraph(paragraph)

    def processTableShape(self, shape):
        model = shape.Model
        rows = model.RowCount
        columns = model.ColumnCount
        logging.debug("TableShape columns=%d & rows=%d", columns, rows)
        for row in range(rows):
            for column in range(columns):
                logging.debug("TableShape cell(col=%d,row=%d)", column, row)
                cell = model.getCellByPosition(column, row)
                self.processText(cell.Text)

    def processShape(self, shape):
        type = shape.getShapeType()
        if type == "com.sun.star.drawing.TextShape":
            self.processText(shape)
        elif type == "com.sun.star.drawing.GroupShape":
            for index in range(shape.getCount()):
                self.processShape(shape.getByIndex(index))
        elif type == "FrameShape":
            pass
        elif type == "com.sun.star.drawing.LineShape":
            pass
        #elif type == "com.sun.star.drawing.RectangleShape":
        #    pass
        elif type == "com.sun.star.drawing.CustomShape":
            self.processText(shape)
        elif type == "com.sun.star.drawing.TableShape":
            self.processTableShape(shape)
        elif type == "com.sun.star.presentation.TitleTextShape":
            self.processText(shape)
        elif type == "com.sun.star.presentation.SubtitleShape":
            self.processText(shape)
        elif type == "com.sun.star.presentation.OutlinerShape":
            self.processText(shape)
        else:
            logging.warning("unknown shape type '%s' for object named '%s'",
                                                            type, shape.Name)

    def processPageStyle(self, pageStyle):
        logging.debug("processing page style '%s'", pageStyle.Name)
        if pageStyle.HeaderIsOn:
            if pageStyle.HeaderText:
                self.processText(pageStyle.HeaderText)
            if pageStyle.HeaderTextLeft:
                self.processText(pageStyle.HeaderTextLeft)
            if pageStyle.HeaderTextRight:
                self.processText(pageStyle.HeaderTextRight)
        if pageStyle.FooterIsOn:
            if pageStyle.FooterText:
                self.processText(pageStyle.FooterText)
            if pageStyle.FooterTextLeft:
                self.processText(pageStyle.FooterTextLeft)
            if pageStyle.FooterTextRight:
                self.processText(pageStyle.FooterTextRight)

    def processTextDocument(self, doc):
        # convert text body
        text = doc.Text
        self.processText(text)
        # convert text frames
        frames = doc.getTextFrames()
        for index in range(frames.getCount()):
            frame = frames.getByIndex(index)
            self.processText(frame)
        # convert text shapes (in draw pages)
        drawPages = doc.getDrawPage()
        for index in range(drawPages.getCount()):
            drawPage = drawPages.getByIndex(index)
            self.processShape(drawPage)
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
            logging.debug("found page style '%s'", pageStyle.Name)
            if pageStyle.isInUse():
                self.processPageStyle(pageStyle)

    def processSheet(self, sheet):
        cursor = sheet.createCursor()
        cursor.gotoEndOfUsedArea(False)
        cursor.gotoStartOfUsedArea(True)
        rangeAddress = cursor.getRangeAddress()
        rows = rangeAddress.EndRow - rangeAddress.StartRow + 1
        columns = rangeAddress.EndColumn - rangeAddress.StartColumn + 1
        logging.debug("Sheet columns=%d & rows=%d", columns, rows)
        for row in range(rows):
            for column in range(columns):
                logging.debug("Sheet cell(col=%d,row=%d)", column, row)
                cell = cursor.getCellByPosition(column, row)
                self.processText(cell.Text)

    def processSpreadsheetDocument(self, doc):
        # disable automatic-calculation during process
        autoCalc = doc.isAutomaticCalculationEnabled()
        if autoCalc: doc.enableAutomaticCalculation(False)
        # process all sheets
        enum = doc.getSheets().createEnumeration()
        while (enum.hasMoreElements()):
            sheet = enum.nextElement()
            self.processSheet(sheet)
        # re-enable automatic-calculation if required
        if autoCalc: doc.enableAutomaticCalculation(True)

    def processDrawPresentationDocument(self, doc):
        # process all pages
        drawPages = doc.getDrawPages()
        for index in range(drawPages.getCount()):
            drawPage = drawPages.getByIndex(index)
            # convert page body
            logging.debug("converting draw page '%s'", drawPage.Name)
            for index in range(drawPage.getCount()):
                draw = drawPage.getByIndex(index)
                self.processShape(draw)
            # FIXME: should process text in drawPage.getNotesPage() too

            # FIXME: should detect if title has already been converted
            #        (by testing if it's valid Vietnamese word? argl...)
            # convert page name
            try:
                drawPage.setName(self.textConverter.convertString(
                            drawPage.Name,
                            self.textPortionConverter.mostUsedEncoding()))
            except:
                logging.info("unable to convert draw page name")
                pass # don't fail on this, since it's not that important

    def processDocument(self, doc):
        self._reset_stats()
        # XXX: check if it really works
        #doc.RecordChanges = False

        if doc.supportsService("com.sun.star.text.GenericTextDocument"):
            logging.info("this is a text document")
            self.processTextDocument(doc)
        elif doc.supportsService("com.sun.star.sheet.SpreadsheetDocument"):
            logging.info("this is a spreadsheet document")
            self.processSpreadsheetDocument(doc)
        elif doc.supportsService("com.sun.star.presentation.PresentationDocument"):
            logging.info("this is a presentation document")
            self.processDrawPresentationDocument(doc)
        elif doc.supportsService("com.sun.star.drawing.GenericDrawingDocument"):
            logging.info("this is a drawing document")
            self.processDrawPresentationDocument(doc)
        else:
            logging.warning("unknown document type")

        # convert document title
        info = doc.getDocumentInfo()
        # FIXME: should detect if title has already been converted
        #        (by testing if it's valid Vietnamese word? argl...)
        try:
            info.Title = self.textConverter.convertString(info.Title,
                            self.textPortionConverter.mostUsedEncoding())
        except:
            logging.info("unable to convert document title")
            pass # don't fail on this, since it's not that important

        # XXX: check if it really works
        #doc.RecordChanges = True

