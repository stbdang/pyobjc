import objc
import StoreKit
from PyObjCTools.TestSupport import *


class TestProtocols(TestCase):
    def test_formal_protocols(self):
        self.assertIsInstance(
            objc.protocolNamed("SKPaymentTransactionObserver"), objc.formal_protocol
        )
        self.assertIsInstance(
            objc.protocolNamed("SKProductsRequestDelegate"), objc.formal_protocol
        )
        self.assertIsInstance(
            objc.protocolNamed("SKRequestDelegate"), objc.formal_protocol
        )


if __name__ == "__main__":
    main()
