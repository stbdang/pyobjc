import CoreServices
from PyObjCTools.TestSupport import *


class TestAIFF(TestCase):
    def assert_not_wrapped(self, name):
        self.assertTrue(
            not hasattr(CoreServices, name), "%r exposed in bindings" % (name,)
        )

    def test_not_wrapped(self):
        self.assert_not_wrapped("kAVLPreOrder")
        self.assert_not_wrapped("kAVLInOrder")
        self.assert_not_wrapped("kAVLPostOrder")
        self.assert_not_wrapped("kLeftToRight")
        self.assert_not_wrapped("kRightToLeft")
        self.assert_not_wrapped("kAVLIsTree")
        self.assert_not_wrapped("kAVLIsLeftBranch")
        self.assert_not_wrapped("kAVLIsRightBranch")
        self.assert_not_wrapped("kAVLIsLeaf")
        self.assert_not_wrapped("kAVLNullNode")
        self.assert_not_wrapped("errItemAlreadyInTree")
        self.assert_not_wrapped("errNotValidTree")
        self.assert_not_wrapped("errItemNotFoundInTree")
        self.assert_not_wrapped("errCanNotInsertWhileWalkProcInProgress")
        self.assert_not_wrapped("errTreeIsLocked")
        self.assert_not_wrapped("AVLTreeStruct")
        self.assert_not_wrapped("NewAVLCompareItemsUPP")
        self.assert_not_wrapped("NewAVLItemSizeUPP")
        self.assert_not_wrapped("NewAVLDisposeItemUPP")
        self.assert_not_wrapped("NewAVLWalkUPP")
        self.assert_not_wrapped("DisposeAVLCompareItemsUPP")
        self.assert_not_wrapped("DisposeAVLItemSizeUPP")
        self.assert_not_wrapped("DisposeAVLDisposeItemUPP")
        self.assert_not_wrapped("DisposeAVLWalkUPP")
        self.assert_not_wrapped("InvokeAVLCompareItemsUPP")
        self.assert_not_wrapped("InvokeAVLItemSizeUPP")
        self.assert_not_wrapped("InvokeAVLDisposeItemUPP")
        self.assert_not_wrapped("InvokeAVLWalkUPP")
        self.assert_not_wrapped("NewAVLCompareItemsUPP")
        self.assert_not_wrapped("NewAVLItemSizeUPP")
        self.assert_not_wrapped("NewAVLDisposeItemUPP")
        self.assert_not_wrapped("NewAVLWalkUPP")
        self.assert_not_wrapped("DisposeAVLCompareItemsUPP")
        self.assert_not_wrapped("DisposeAVLItemSizeUPP")
        self.assert_not_wrapped("DisposeAVLDisposeItemUPP")
        self.assert_not_wrapped("DisposeAVLWalkUPP")
        self.assert_not_wrapped("InvokeAVLCompareItemsUPP")
        self.assert_not_wrapped("InvokeAVLItemSizeUPP")
        self.assert_not_wrapped("InvokeAVLDisposeItemUPP")
        self.assert_not_wrapped("InvokeAVLWalkUPP")
        self.assert_not_wrapped("AVLInit")
        self.assert_not_wrapped("AVLDispose")
        self.assert_not_wrapped("AVLWalk")
        self.assert_not_wrapped("AVLCount")
        self.assert_not_wrapped("AVLGetIndItem")
        self.assert_not_wrapped("AVLInsert")
        self.assert_not_wrapped("AVLRemove")
        self.assert_not_wrapped("AVLFind")
        self.assert_not_wrapped("AVLGetRefcon")


if __name__ == "__main__":
    main()
