import sys

from PyObjCTools.TestSupport import *

if sys.maxsize >= 2 ** 32:
    import GameplayKit

    class TestGKStrategist(TestCase):
        def testProtocols(self):
            objc.protocolNamed("GKStrategist")


if __name__ == "__main__":
    main()
