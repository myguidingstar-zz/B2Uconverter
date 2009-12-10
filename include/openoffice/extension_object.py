"""
B2UConverter — UNO extension for OpenOffice.org
File: include/openoffice/extension_object.py

Copyright ©2009  Ministry of Science and Technology of Vietnam
License: GNU Lesser General Public License version 2.1
Authors: Jean Christophe André <jcandre@hanoilug.org>
         Lê Quốc Thái <lqthai@hanoilug.org>
         Võ Đức Phương <vdphuong@hanoilug.org>
"""

######################################################################

def B2UConverterScript(event=False):
    """Convert all document text segments from old Vietnamese encodings and fonts to Unicode encoding and fonts."""
    return processDocument(XSCRIPTCONTEXT.getDocument())

g_exportedScripts = B2UConverterScript,

######################################################################

#from com.sun.star.awt import Rectangle
from com.sun.star.awt import WindowDescriptor
from com.sun.star.awt.WindowClass import MODALTOP
from com.sun.star.awt.VclWindowPeerAttribute import OK, DEF_OK

# Show a message box with the UNO based toolkit
def messageBox(document, message):
    #doc = XSCRIPTCONTEXT.getDocument()
    window = document.CurrentController.Frame.ContainerWindow

    aDescriptor = WindowDescriptor()
    aDescriptor.Type = MODALTOP
    aDescriptor.WindowServiceName = "infobox"
    aDescriptor.ParentIndex = -1
    aDescriptor.Parent = window
    #aDescriptor.Bounds = Rectangle()
    aDescriptor.WindowAttributes = OK

    tk = window.getToolkit()
    msgbox = tk.createWindow(aDescriptor)
    msgbox.setCaptionText("Convert to Unicode")
    msgbox.setMessageText(message)

    return msgbox.execute()

######################################################################

from com.sun.star.task import XJobExecutor
from com.sun.star.beans import PropertyValue
import tempfile

class B2UConverterJob(unohelper.Base, XJobExecutor):
    def __init__(self, context):
        self._context = context

        logging.basicConfig(level=logging.DEBUG,
            format='%(asctime)s %(levelname)s %(message)s',
            filename='/tmp/b2uconverter-ooo.log', filemode='w')
        logging.info("B2UConverter loaded (Python %s)", sys.version)

        self._cfgprov = self._context.ServiceManager.createInstanceWithContext(
            "com.sun.star.configuration.ConfigurationProvider",
            self._context)
        node = uno.createUnoStruct("com.sun.star.beans.PropertyValue")
        node.Name = "nodepath"
        node.Value = "/vn.gov.oss.openoffice.B2UConverter/General"
        self._node = node
        self._cfgnames = ("Debug", "RemoveDiacritics")

    def _readconfig(self):
        global _settings
        ConfigReader = self._cfgprov.createInstanceWithArguments(
            "com.sun.star.configuration.ConfigurationAccess",
            (self._node,))
        cfgvalues = ConfigReader.getPropertyValues(self._cfgnames)
        for i in range(len(self._cfgnames)):
            _settings[self._cfgnames[i]] = cfgvalues[i]

    def _error_message(self, error_count):
        if error_count > 1:
            message = "with %s errors" % error_count
        elif _error_count > 0:
            message = "with %s error" % error_count
        else:
            message = "without error"
        return message

    def convertDocument(self, document=None):
        global _error_count
        logging.debug("call to convertDocument (%s document)" \
                                % (document and "with" or "without"))
        if document:
            self._document = document
        else:
            desktop = self._context.ServiceManager.createInstanceWithContext(
                "com.sun.star.frame.Desktop", self._context)
            self._document = desktop.getCurrentComponent()
        self._readconfig()
        _error_count = 0
        processDocument(self._document)
        logging.info("Conversion completed (%s).",
                                        self._error_message(_error_count))

    def convertClipboard(self):
        #copy/paste from above
        self._readconfig()
        logging.debug("call to convertClipboard")
        desktop = self._context.ServiceManager.createInstanceWithContext(
            "com.sun.star.frame.Desktop", self._context)
        clipboard = self._context.ServiceManager.createInstanceWithContext(
            "com.sun.star.datatransfer.clipboard.SystemClipboard",
            self._context)
        contents = clipboard.getContents()
        logging.debug("Contents:\n%s\n%s\n%s",
            "-" * 78,
            "* " + "\n* ".join(dir(contents)),
            "=" * 78)
        flavors = contents.getTransferDataFlavors()
        logging.debug("Flavors:\n%s\n%s\n%s",
            "-" * 78,
            "* " + "\n* ".join([flavor.MimeType for flavor in flavors]),
            "=" * 78)
        mimetype = \
        'application/x-openoffice-embed-source-xml;windows_formatname="Star \
         Embed Source (XML)"'
        found_flavor = None
        for flavor in contents.getTransferDataFlavors():
            if flavor.MimeType == mimetype:
                found_flavor = flavor
                break

        # No suitable flavor found, warn user that nothing has been converted
        # if found_flavor == None:
        data = contents.getTransferData(found_flavor)
        #open('/tmp/clipboarddata', 'w').write(data.value)

        # Okay, since OO.o APIs only accept an URL, we have to make a temp file
        # in order to use it.
        tempFile = tempfile.NamedTemporaryFile()
        tempURL = unohelper.systemPathToFileUrl(tempFile.name)

        # Open it hiddenly
        hidden = PropertyValue()
        hidden.Name = "Hidden"
        hidden.Value = True
        document = desktop.loadComponentFromURL(tempURL, "_blank", 0,
                (hidden,))

        # Let process it, note that this doen't work yet as the font names
        # don't get preserved -> no font information -> can't guess the
        # encoding :(
        processDocument(document)
        document.store()

        # Ok, now to put it back in the clipboard
        dispatcher =
        self._context.ServiceManager.createInstanceWithContext( \
                "com.sun.star.frame.DispatchHelper",
                self._context)
        frame = document.getCurrentController().getFrame()
        # Note that while hidden has nothing to do here, OO.o will throw a
        # tantrum if it is not there :|
        dispatcher.executeDispatch(frame, ".uno:SelectAll", "", 0, (hidden,))
        dispatcher.executeDispatch(frame, ".uno:Copy", "", 0, (hidden,))

    def convertSelection(self):
        self.convertClipboard()

    def trigger(self, args):
        global _error_count
        _error_count = 0
        logging.debug("Trigger arguments: %s", args)
        try:
            if args == 'document':
                self.convertDocument()
            elif args == 'clipboard':
                self.convertClipboard()
            elif args == 'selection':
                self.convertSelection()
            else:
                raise ValueError, "Invalid trigger call (programming error)."
            messageBox(self._document, "Unicode conversion completed (%s)." \
                                        % self._error_message(_error_count))
        except:
            logging.exception("Exception during conversion:")
            err = traceback.format_exc()
            messageBox(self._document, "Unicode conversion failed:\n" + err)


g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationHelper.addImplementation( \
    B2UConverterJob, "vn.gov.oss.openoffice.B2UConverterJob", \
    ("com.sun.star.task.Job",),)
