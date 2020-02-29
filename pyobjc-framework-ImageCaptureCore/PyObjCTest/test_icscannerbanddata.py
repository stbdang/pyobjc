from ImageCaptureCore import *
from PyObjCTools.TestSupport import *


class TestICScannerBandData(TestCase):
    @min_os_level("10.7")
    def testMethods(self):
        self.assertResultIsBOOL(ICScannerBandData.isBigEndian)


if __name__ == "__main__":
    main()
