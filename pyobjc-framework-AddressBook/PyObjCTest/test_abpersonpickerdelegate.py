from AddressBook import *
from PyObjCTools.TestSupport import *


class TestABPersonPickerDelegate(TestCase):
    @min_sdk_level("10.9")
    def test_protocols(self):
        objc.protocolNamed("ABPersonPickerDelegate")


if __name__ == "__main__":
    main()
