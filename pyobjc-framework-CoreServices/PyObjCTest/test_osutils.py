import CoreServices
from PyObjCTools.TestSupport import *


class TestOSUtils(TestCase):
    def assert_not_wrapped(self, name):
        self.assertTrue(
            not hasattr(CoreServices, name), "%r exposed in bindings" % (name,)
        )

    def test_not_wrapped(self):
        self.assert_not_wrapped("sortsBefore")
        self.assert_not_wrapped("sortsEqual")
        self.assert_not_wrapped("sortsAfter")
        self.assert_not_wrapped("dummyType")
        self.assert_not_wrapped("vType")
        self.assert_not_wrapped("ioQType")
        self.assert_not_wrapped("drvQType")
        self.assert_not_wrapped("evType")
        self.assert_not_wrapped("fsQType")
        self.assert_not_wrapped("sIQType")
        self.assert_not_wrapped("dtQType")
        self.assert_not_wrapped("nmType")
        self.assert_not_wrapped("QElem")
        self.assert_not_wrapped("QHdr")
        self.assert_not_wrapped("MachineLocation")
        self.assert_not_wrapped("IsMetric")
        self.assert_not_wrapped("Delay")
        self.assert_not_wrapped("Enqueue")
        self.assert_not_wrapped("Dequeue")
        self.assert_not_wrapped("MakeDataExecutable")
        self.assert_not_wrapped("ReadLocation")
        self.assert_not_wrapped("TickCount")
        self.assert_not_wrapped("CSCopyUserName")
        self.assert_not_wrapped("CSCopyMachineName")
        self.assert_not_wrapped("useFree")
        self.assert_not_wrapped("useATalk")
        self.assert_not_wrapped("useAsync")
        self.assert_not_wrapped("useExtClk")
        self.assert_not_wrapped("useMIDI")
        self.assert_not_wrapped("false32b")
        self.assert_not_wrapped("true32b")
        self.assert_not_wrapped("SysParmType")
        self.assert_not_wrapped("GetSysPPtr")
        self.assert_not_wrapped("NewDeferredTaskUPP")
        self.assert_not_wrapped("DisposeDeferredTaskUPP")
        self.assert_not_wrapped("InvokeDeferredTaskUPP")
        self.assert_not_wrapped("DeferredTask")
        self.assert_not_wrapped("DTInstall")
        self.assert_not_wrapped("DTUninstall")
        self.assert_not_wrapped("SetCurrentA5")
        self.assert_not_wrapped("SetA5")
        self.assert_not_wrapped("InitUtil")
        self.assert_not_wrapped("WriteParam")
        self.assert_not_wrapped("WriteLocation")
        self.assert_not_wrapped("curSysEnvVers")
        self.assert_not_wrapped("SysEnvRec")
        self.assert_not_wrapped("envMac")
        self.assert_not_wrapped("envXL")
        self.assert_not_wrapped("envMachUnknown")
        self.assert_not_wrapped("env512KE")
        self.assert_not_wrapped("envMacPlus")
        self.assert_not_wrapped("envSE")
        self.assert_not_wrapped("envMacII")
        self.assert_not_wrapped("envMacIIx")
        self.assert_not_wrapped("envMacIIcx")
        self.assert_not_wrapped("envSE30")
        self.assert_not_wrapped("envPortable")
        self.assert_not_wrapped("envMacIIci")
        self.assert_not_wrapped("envMacIIfx")
        self.assert_not_wrapped("envCPUUnknown")
        self.assert_not_wrapped("env68000")
        self.assert_not_wrapped("env68010")
        self.assert_not_wrapped("env68020")
        self.assert_not_wrapped("env68030")
        self.assert_not_wrapped("env68040")
        self.assert_not_wrapped("envUnknownKbd")
        self.assert_not_wrapped("envMacKbd")
        self.assert_not_wrapped("envMacAndPad")
        self.assert_not_wrapped("envMacPlusKbd")
        self.assert_not_wrapped("envAExtendKbd")
        self.assert_not_wrapped("envStandADBKbd")
        self.assert_not_wrapped("envPrtblADBKbd")
        self.assert_not_wrapped("envPrtblISOKbd")
        self.assert_not_wrapped("envStdISOADBKbd")
        self.assert_not_wrapped("envExtISOADBKbd")
        self.assert_not_wrapped("")


if __name__ == "__main__":
    main()
