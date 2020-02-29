import DiscRecordingUI
from PyObjCTools.TestSupport import *


class TestDiscRecordingUIResources(TestCase):
    def testConstants(self):
        self.assertIsInstance(DiscRecordingUI.DRBurnIcon, unicode)
        self.assertIsInstance(DiscRecordingUI.DREraseIcon, unicode)


if __name__ == "__main__":
    main()
