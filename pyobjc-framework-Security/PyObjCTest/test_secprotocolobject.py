import Security
from PyObjCTools.TestSupport import *


class TestSecProtocolObject(TestCase):
    def test_functions(self):
        self.assertFalse(hasattr(Security, "sec_retain"))
        self.assertFalse(hasattr(Security, "sec_release"))


if __name__ == "__main__":
    main()
