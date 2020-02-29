from AppKit import *
from Foundation import *
from PyObjCTools import AppHelper
from ServiceTest import *


def main():
    # NSLog(u"main()")
    serviceProvider = ServiceTest.alloc().init()
    # NSLog(u"serviceProvider = %s", serviceProvider)
    NSRegisterServicesProvider(serviceProvider, "PyObjCSimpleService")
    # NSLog(u"registered as PyObjCSimpleService")
    AppHelper.runConsoleEventLoop()


if __name__ == "__main__":
    main()
