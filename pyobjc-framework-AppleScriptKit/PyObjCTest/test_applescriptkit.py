"""
Some simple tests to check that the framework is properly wrapped.
"""
import AppleScriptKit
import objc
from PyObjCTools.TestSupport import *


class TestAppleScriptKit(TestCase):
    def testClasses(self):
        self.assertHasAttr(AppleScriptKit, "ASKPluginObject")
        self.assertIsInstance(AppleScriptKit.ASKPluginObject, objc.objc_class)


if __name__ == "__main__":
    main()
