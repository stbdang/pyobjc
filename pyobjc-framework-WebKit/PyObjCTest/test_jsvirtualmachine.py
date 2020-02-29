import JavaScriptCore
import objc
from PyObjCTools.TestSupport import *


class TestJSVirtualMachine(TestCase):
    @onlyOn64Bit
    @min_os_level("10.9")
    def test_classes(self):
        self.assertHasAttr(JavaScriptCore, "JSVirtualMachine")


if __name__ == "__main__":
    main()
