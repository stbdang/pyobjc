import VideoToolbox
from PyObjCTools.TestSupport import *


class TestVTErrors(TestCase):
    def test_constants(self):
        self.assertEqual(VideoToolbox.kVTPropertyNotSupportedErr, -12900)
        self.assertEqual(VideoToolbox.kVTPropertyReadOnlyErr, -12901)
        self.assertEqual(VideoToolbox.kVTParameterErr, -12902)
        self.assertEqual(VideoToolbox.kVTInvalidSessionErr, -12903)
        self.assertEqual(VideoToolbox.kVTAllocationFailedErr, -12904)
        self.assertEqual(VideoToolbox.kVTPixelTransferNotSupportedErr, -12905)
        self.assertEqual(VideoToolbox.kVTCouldNotFindVideoDecoderErr, -12906)
        self.assertEqual(VideoToolbox.kVTCouldNotCreateInstanceErr, -12907)
        self.assertEqual(VideoToolbox.kVTCouldNotFindVideoEncoderErr, -12908)
        self.assertEqual(VideoToolbox.kVTVideoDecoderBadDataErr, -12909)
        self.assertEqual(VideoToolbox.kVTVideoDecoderUnsupportedDataFormatErr, -12910)
        self.assertEqual(VideoToolbox.kVTVideoDecoderMalfunctionErr, -12911)
        self.assertEqual(VideoToolbox.kVTVideoEncoderMalfunctionErr, -12912)
        self.assertEqual(VideoToolbox.kVTVideoDecoderNotAvailableNowErr, -12913)
        self.assertEqual(VideoToolbox.kVTImageRotationNotSupportedErr, -12914)
        self.assertEqual(VideoToolbox.kVTVideoEncoderNotAvailableNowErr, -12915)
        self.assertEqual(VideoToolbox.kVTFormatDescriptionChangeNotSupportedErr, -12916)
        self.assertEqual(VideoToolbox.kVTInsufficientSourceColorDataErr, -12917)
        self.assertEqual(VideoToolbox.kVTCouldNotCreateColorCorrectionDataErr, -12918)
        self.assertEqual(VideoToolbox.kVTColorSyncTransformConvertFailedErr, -12919)
        self.assertEqual(VideoToolbox.kVTVideoDecoderAuthorizationErr, -12210)
        self.assertEqual(VideoToolbox.kVTVideoEncoderAuthorizationErr, -12211)
        self.assertEqual(VideoToolbox.kVTColorCorrectionPixelTransferFailedErr, -12212)
        self.assertEqual(VideoToolbox.kVTMultiPassStorageIdentifierMismatchErr, -12213)
        self.assertEqual(VideoToolbox.kVTMultiPassStorageInvalidErr, -12214)
        self.assertEqual(VideoToolbox.kVTFrameSiloInvalidTimeStampErr, -12215)
        self.assertEqual(VideoToolbox.kVTFrameSiloInvalidTimeRangeErr, -12216)
        self.assertEqual(VideoToolbox.kVTCouldNotFindTemporalFilterErr, -12217)
        self.assertEqual(VideoToolbox.kVTPixelTransferNotPermittedErr, -12218)
        self.assertEqual(VideoToolbox.kVTColorCorrectionImageRotationFailedErr, -12219)
        self.assertEqual(VideoToolbox.kVTVideoDecoderRemovedErr, -17690)
        self.assertEqual(
            VideoToolbox.kVTDecodeFrame_EnableAsynchronousDecompression, 1 << 0
        )
        self.assertEqual(VideoToolbox.kVTDecodeFrame_DoNotOutputFrame, 1 << 1)
        self.assertEqual(VideoToolbox.kVTDecodeFrame_1xRealTimePlayback, 1 << 2)
        self.assertEqual(VideoToolbox.kVTDecodeFrame_EnableTemporalProcessing, 1 << 3)
        self.assertEqual(VideoToolbox.kVTDecodeInfo_Asynchronous, 1 << 0)
        self.assertEqual(VideoToolbox.kVTDecodeInfo_FrameDropped, 1 << 1)
        self.assertEqual(VideoToolbox.kVTDecodeInfo_ImageBufferModifiable, 1 << 2)
        self.assertEqual(VideoToolbox.kVTEncodeInfo_Asynchronous, 1 << 0)
        self.assertEqual(VideoToolbox.kVTEncodeInfo_FrameDropped, 1 << 1)


if __name__ == "__main__":
    main()
