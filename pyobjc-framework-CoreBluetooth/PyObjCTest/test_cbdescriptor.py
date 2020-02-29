import sys

import CoreBluetooth
from PyObjCTools.TestSupport import *


class TestCBAdvertisementData(TestCase):
    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(CoreBluetooth.CBDescriptor, objc.objc_class)
        self.assertIsInstance(CoreBluetooth.CBMutableDescriptor, objc.objc_class)


if __name__ == "__main__":
    main()
