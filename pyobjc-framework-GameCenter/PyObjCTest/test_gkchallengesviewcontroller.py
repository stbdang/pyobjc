import sys

import objc
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import GameCenter

    class TestGKChallengesViewController(TestCase):
        @expectedFailure
        @min_os_level("10.8")
        def testClasses10_8(self):
            self.assertIsInstance(
                GameCenter.GKChallengesViewController, objc.objc_class
            )

        @min_os_level("10.8")
        def testProtocols10_8(self):
            objc.protocolNamed("GKChallengesViewControllerDelegate")


if __name__ == "__main__":
    main()
