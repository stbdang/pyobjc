import sys

import objc
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import GameCenter

    class TestGKEventListener(TestCase):
        @min_os_level("10.10")
        def testProtocols(self):
            objc.protocolNamed("GKChallengeListener")


if __name__ == "__main__":
    main()
