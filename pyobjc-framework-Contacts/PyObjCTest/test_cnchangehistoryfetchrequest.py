import sys

import objc
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import Contacts

    class TestCNChangeHistoryFetchRequest(TestCase):
        @min_os_level("10.15")
        def testProtocols(self):
            objc.protocolNamed("CNKeyDescriptor")

        @min_os_level("10.15")
        def test_methods(self):
            self.assertResultIsBOOL(
                Contacts.CNChangeHistoryFetchRequest.shouldUnifyResults
            )
            self.assertArgIsBOOL(
                Contacts.CNChangeHistoryFetchRequest.setShouldUnifyResults_, 0
            )

            self.assertResultIsBOOL(Contacts.CNChangeHistoryFetchRequest.mutableObjects)
            self.assertArgIsBOOL(
                Contacts.CNChangeHistoryFetchRequest.setMutableObjects_, 0
            )

            self.assertResultIsBOOL(
                Contacts.CNChangeHistoryFetchRequest.includeGroupChanges
            )
            self.assertArgIsBOOL(
                Contacts.CNChangeHistoryFetchRequest.setIncludeGroupChanges_, 0
            )


if __name__ == "__main__":
    main()
