# -*- coding: utf_8 -*-
"""
B2UConverter — UNO extension for OpenOffice.org

Copyright ©2009  Ministry of Science and Technology of Vietnam
License: GNU Lesser General Public License version 2.1
Authors: Jean Christophe André <jcandre@hanoilug.org>
         Lê Quốc Thái <lqthai@hanoilug.org>
         Võ Đức Phương <vdphuong@hanoilug.org>
"""

import uno
import unohelper

# interfaces
from com.sun.star.lang import XServiceInfo
from com.sun.star.awt import XContainerWindowEventHandler

_uninitialized = True

# main class
class DialogHandler(unohelper.Base, XServiceInfo, XContainerWindowEventHandler):
    def __init__(self, ctx):
        self.ctx = ctx;
        self.cp = self.ctx.ServiceManager.createInstanceWithContext( 
            "com.sun.star.configuration.ConfigurationProvider",
            self.ctx)
        node = uno.createUnoStruct("com.sun.star.beans.PropertyValue")
        node.Name = "nodepath"
        node.Value = "/vn.gov.oss.openoffice.B2UConverter/General"
        self.node = node
        self.cfg_names = ("Debug", "RemoveDiacritics", "VNIHacks")
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
        return "vn.gov.oss.openoffice.B2UConverter.DialogHandler"

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
        for name in ("Debug", "RemoveDiacritics", "VNIHacks"):
            window.getControl(name).setState(int(settings[name]))
        return

    # making the save data
    def saveData(self,window):
        name = window.getModel().Name
        if name != "GeneralDialog":
            return
        settings = []
        for name in ("Debug", "RemoveDiacritics", "VNIHacks"):
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
        except:
            print "DEBUG: configreader exception"
            raise
        for i in range(len(self.cfg_names)):
            settings[self.cfg_names[i]] = cfg_values[i]
        # special case for RemoveDiacritics: always False at start
        global _uninitialized
        if _uninitialized:
            _uninitialized = False
            settings['RemoveDiacritics'] = False
            self.configwriter(tuple(settings.values()))
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
            print "DEBUG: configwriter exception"
            raise

# uno implementation
g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationHelper.addImplementation( \
    DialogHandler, "vn.gov.oss.openoffice.B2UConverter.DialogHandler", \
    ("vn.gov.oss.openoffice.B2UConverter.DialogHandler",),)
