import Security
from PyObjCTools.TestSupport import *


class Testcssmdli(TestCase):
    def test_unsuppported(self):
        self.assertFalse(hasattr(Security, "CSSM_SPI_DL_FUNCS"))


if __name__ == "__main__":
    main()
