#!
# -*- coding: utf_8 -*-
import uno
import unohelper

# interfaces
from com.sun.star.lang import XServiceInfo
from com.sun.star.awt import XContainerWindowEventHandler
# listeners
#from com.sun.star.awt import XActionListener

# action listener
#class MyActionListener(unohelper.Base, XActionListener):
#    def __init__(self, cast, dialog):
#        self.cast = cast
#        self.dialog = dialog
#    def disposing(self, eventObject):
#        pass
#    def actionPerformed(self, actionEvent):
#        cmd = str(actionEvent.ActionCommand)
#        if cmd == "clic":
#            self.dialog.getControl("RemoveSoftHyphen").State =
#                (1 - self.dialog.getControl("RemoveSoftHyphen").State)
#        return

# main class
class DialogHandler(unohelper.Base, XServiceInfo, XContainerWindowEventHandler):
    def __init__(self, ctx):
        self.ctx = ctx;
        self.cp = self.ctx.ServiceManager.createInstanceWithContext( 
            "com.sun.star.configuration.ConfigurationProvider",
            self.ctx)
        node = uno.createUnoStruct("com.sun.star.beans.PropertyValue")
        node.Name = "nodepath"
        node.Value = "/org.hanoilug.openoffice.OvniConv/General"
        self.node = node
        self.cfg_names = ("Debug", "KeepVietnameseFonts", \
                                "RemoveDiacritics", "RemoveSoftHyphen")
        return

    # XContainerWindowEventHandler
    def callHandlerMethod(self, window, eventObject, method):
        if method == "external_event":
            try:
                self.handleExternalEvent(window, eventObject)
            except:
                pass
        return True

    # XContainerWindowEventHandler
    def getSupportedMethodNames(self):
        return ("external_event",)

    def supportsService(self, name):
        return False

    def getImplementationName(self):
        return "org.hanoilug.openoffice.OvniConv.DialogHandler"

    def getSupportedServiceNames(self):
        return ()

    def handleExternalEvent(self, window, eventName):
        if eventName == "ok":
            self.saveData(window)
        elif eventName == "back":
            self.loadData(window, "back")
        elif eventName == "initialize":
            self.loadData(window, "initialize")
        return True

    # load and set the data
    def loadData(self, window, ev):
        name = window.getModel().Name
        if name != "GeneralDialog":
            return
        settings = self.configreader()
        if not settings:
            return
        for name in ("Debug", "KeepVietnameseFonts", \
                                "RemoveDiacritics", "RemoveSoftHyphen"):
            window.getControl(name).setState(int(settings[name]))
#        if ev == "initialize":
#            listener = MyActionListener(self, window)
#            remove_soft_hyphen = window.getControl("RemoveSoftHyphen")
#            remove_soft_hyphen.ActionCommand = "clic"
#            remove_soft_hyphen.addActionListener(listener)
        return

    # making the save data
    def saveData(self,window):
        name = window.getModel().Name
        if name != "GeneralDialog":
            return
        settings = []
        for name in ("Debug", "KeepVietnameseFonts", \
                                "RemoveDiacritics", "RemoveSoftHyphen"):
            settings.append(bool(window.getControl(name).State))
        self.configwriter(tuple(settings))
        return

    # read configuration
    def configreader(self):
        settings = {}
        try:
            ConfigReader = self.cp.createInstanceWithArguments( 
                "com.sun.star.configuration.ConfigurationAccess",
                (self.node,))
            cfg_values = ConfigReader.getPropertyValues(self.cfg_names)
            for i in range(len(self.cfg_names)):
                settings[self.cfg_names[i]] = cfg_values[i]
        except:
            raise
        return settings

    # write configuration, cfg_values: tuple
    # keep the order of the values
    def configwriter(self, cfg_values):
        try:
            ConfigWriter = self.cp.createInstanceWithArguments( 
                "com.sun.star.configuration.ConfigurationUpdateAccess",
                (self.node,))
            ConfigWriter.setPropertyValues(self.cfg_names, cfg_values)
            ConfigWriter.commitChanges()
        except:
            raise

# uno implementation
g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationHelper.addImplementation( \
    DialogHandler, "org.hanoilug.openoffice.OvniConv.DialogHandler", \
    ("org.hanoilug.openoffice.OvniConv.DialogHandler",),)
