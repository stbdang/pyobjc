import sys


if sys.maxsize >= 2 ** 32:
    from PyObjCTools.TestSupport import TestCase
    import Vision

    class TestVNGenerateObjectnessBasedSaliencyImageRequest(TestCase):
        def test_constants(self):
            self.assertEqual(
                Vision.VNGenerateObjectnessBasedSaliencyImageRequestRevision1, 1
            )
