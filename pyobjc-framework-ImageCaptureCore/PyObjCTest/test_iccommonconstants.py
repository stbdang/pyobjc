from ImageCaptureCore import *
from PyObjCTools.TestSupport import *


class TestICCameraDevice(TestCase):
    def testConstants(self):
        self.assertEqual(ICEXIFOrientation1, 1)
        self.assertEqual(ICEXIFOrientation2, 2)
        self.assertEqual(ICEXIFOrientation3, 3)
        self.assertEqual(ICEXIFOrientation4, 4)
        self.assertEqual(ICEXIFOrientation5, 5)
        self.assertEqual(ICEXIFOrientation6, 6)
        self.assertEqual(ICEXIFOrientation7, 7)
        self.assertEqual(ICEXIFOrientation8, 8)

        self.assertEqual(ICReturnSuccess, 0)
        self.assertEqual(ICReturnInvalidParam, -9922)
        self.assertEqual(ICReturnCommunicationTimedOut, -9923)
        self.assertEqual(ICReturnScanOperationCanceled, -9924)
        self.assertEqual(ICReturnScannerInUseByLocalUser, -9925)
        self.assertEqual(ICReturnScannerInUseByRemoteUser, -9926)
        self.assertEqual(ICReturnDeviceFailedToOpenSession, -9927)
        self.assertEqual(ICReturnDeviceFailedToCloseSession, -9928)
        self.assertEqual(ICReturnScannerFailedToSelectFunctionalUnit, -9929)
        self.assertEqual(ICReturnScannerFailedToCompleteOverviewScan, -9930)
        self.assertEqual(ICReturnScannerFailedToCompleteScan, -9931)
        self.assertEqual(ICReturnReceivedUnsolicitedScannerStatusInfo, -9932)
        self.assertEqual(ICReturnReceivedUnsolicitedScannerErrorInfo, -9933)
        self.assertEqual(ICReturnDownloadFailed, -9934)
        self.assertEqual(ICReturnUploadFailed, -9935)
        self.assertEqual(ICReturnFailedToCompletePassThroughCommand, -9936)
        self.assertEqual(ICReturnDownloadCanceled, -9937)
        self.assertEqual(ICReturnFailedToEnabeTethering, -9938)
        self.assertEqual(ICReturnFailedToDisabeTethering, -9939)
        self.assertEqual(ICReturnFailedToCompleteSendMessageRequest, -9940)
        self.assertEqual(ICReturnDeleteFilesFailed, -9941)
        self.assertEqual(ICReturnDeleteFilesCanceled, -9942)
        self.assertEqual(ICReturnDeviceIsPasscodeLocked, -9943)
        self.assertEqual(ICReturnDeviceFailedToTakePicture, -9944)
        self.assertEqual(ICReturnDeviceSoftwareNotInstalled, -9945)
        self.assertEqual(ICReturnDeviceSoftwareIsBeingInstalled, -9946)
        self.assertEqual(ICReturnDeviceSoftwareInstallationCompleted, -9947)
        self.assertEqual(ICReturnDeviceSoftwareInstallationCanceled, -9948)
        self.assertEqual(ICReturnDeviceSoftwareInstallationFailed, -9949)
        self.assertEqual(ICReturnDeviceSoftwareNotAvailable, -9950)
        self.assertEqual(ICReturnDeviceCouldNotPair, -9951)
        self.assertEqual(ICReturnDeviceCouldNotUnpair, -9952)
        self.assertEqual(ICReturnDeviceNeedsCredentials, -9953)
        self.assertEqual(ICReturnDeviceIsBusyEnumerating, -9954)
        self.assertEqual(ICReturnDeviceCommandGeneralFailure, -9955)

        self.assertEqual(ICReturnCodeThumbnailOffset, -21000)
        self.assertEqual(ICReturnCodeMetadataOffset, -21050)
        self.assertEqual(ICReturnCodeDownloadOffset, -21100)
        self.assertEqual(ICReturnCodeDeleteOffset, -21150)
        self.assertEqual(ICReturnCodeExFATOffset, -21200)
        self.assertEqual(ICReturnCodePTPOffset, -21250)
        self.assertEqual(ICReturnCodeSystemOffset, -21300)
        self.assertEqual(ICReturnCodeDeviceOffset, -21350)
        self.assertEqual(ICReturnCodeDeviceConnection, -21400)
        self.assertEqual(ICReturnCodeObjectOffset, -21450)
        self.assertEqual(ICReturnDeviceFailedToCompleteTransfer, -9956)
        self.assertEqual(ICReturnDeviceFailedToSendData, -9957)
        self.assertEqual(ICReturnSessionNotOpened, -9958)
        self.assertEqual(ICReturnThumbnailNotAvailable, ICReturnCodeThumbnailOffset)

        self.assertEqual(ICReturnErrorDeviceEjected, ICReturnCodeSystemOffset)
        self.assertEqual(ICReturnConnectionDriverExited, ICReturnCodeDeviceOffset)
        self.assertEqual(ICReturnMultiErrorDictionary, -30000)

        self.assertEqual(ICLegacyReturnCodeCommunicationErr, -9900)
        self.assertEqual(ICLegacyReturnCodeDeviceNotFoundErr, -9901)
        self.assertEqual(ICLegacyReturnCodeDeviceNotOpenErr, -9902)
        self.assertEqual(ICLegacyReturnCodeFileCorruptedErr, -9903)
        self.assertEqual(ICLegacyReturnCodeIOPendingErr, -9904)
        self.assertEqual(ICLegacyReturnCodeInvalidObjectErr, -9905)
        self.assertEqual(ICLegacyReturnCodeInvalidPropertyErr, -9906)
        self.assertEqual(ICLegacyReturnCodeIndexOutOfRangeErr, -9907)
        self.assertEqual(ICLegacyReturnCodePropertyTypeNotFoundErr, -9908)
        self.assertEqual(ICLegacyReturnCodeCannotYieldDevice, -9909)
        self.assertEqual(ICLegacyReturnCodeDataTypeNotFoundErr, -9910)
        self.assertEqual(ICLegacyReturnCodeDeviceMemoryAllocationErr, -9911)
        self.assertEqual(ICLegacyReturnCodeDeviceInternalErr, -9912)
        self.assertEqual(ICLegacyReturnCodeDeviceInvalidParamErr, -9913)
        self.assertEqual(ICLegacyReturnCodeDeviceAlreadyOpenErr, -9914)
        self.assertEqual(ICLegacyReturnCodeDeviceLocationIDNotFoundErr, -9915)
        self.assertEqual(ICLegacyReturnCodeDeviceGUIDNotFoundErr, -9916)
        self.assertEqual(ICLegacyReturnCodeDeviceIOServicePathNotFoundErr, -9917)
        self.assertEqual(ICLegacyReturnCodeDeviceUnsupportedErr, -9918)
        self.assertEqual(ICLegacyReturnCodeFrameworkInternalErr, -9919)
        self.assertEqual(ICLegacyReturnCodeExtensionInternalErr, -9920)
        self.assertEqual(ICLegacyReturnCodeInvalidSessionErr, -9921)

        self.assertEqual(ICReturnSuccess, 0)
        self.assertEqual(ICReturnInvalidParam, -9922)
        self.assertEqual(ICReturnCommunicationTimedOut, -9923)
        self.assertEqual(ICReturnScanOperationCanceled, -9924)
        self.assertEqual(ICReturnScannerInUseByLocalUser, -9925)
        self.assertEqual(ICReturnScannerInUseByRemoteUser, -9926)
        self.assertEqual(ICReturnDeviceFailedToOpenSession, -9927)
        self.assertEqual(ICReturnDeviceFailedToCloseSession, -9928)
        self.assertEqual(ICReturnScannerFailedToSelectFunctionalUnit, -9929)
        self.assertEqual(ICReturnScannerFailedToCompleteOverviewScan, -9930)
        self.assertEqual(ICReturnScannerFailedToCompleteScan, -9931)
        self.assertEqual(ICReturnReceivedUnsolicitedScannerStatusInfo, -9932)
        self.assertEqual(ICReturnReceivedUnsolicitedScannerErrorInfo, -9933)
        self.assertEqual(ICReturnDownloadFailed, -9934)
        self.assertEqual(ICReturnUploadFailed, -9935)
        self.assertEqual(ICReturnFailedToCompletePassThroughCommand, -9936)
        self.assertEqual(ICReturnDownloadCanceled, -9937)
        self.assertEqual(ICReturnFailedToEnabeTethering, -9938)
        self.assertEqual(ICReturnFailedToDisabeTethering, -9939)
        self.assertEqual(ICReturnFailedToCompleteSendMessageRequest, -9940)
        self.assertEqual(ICReturnDeleteFilesFailed, -9941)
        self.assertEqual(ICReturnDeleteFilesCanceled, -9942)
        self.assertEqual(ICReturnDeviceFailedToTakePicture, -9944)
        self.assertEqual(ICReturnDeviceSoftwareNotInstalled, -9945)
        self.assertEqual(ICReturnDeviceSoftwareIsBeingInstalled, -9946)
        self.assertEqual(ICReturnDeviceSoftwareInstallationCompleted, -9947)
        self.assertEqual(ICReturnDeviceSoftwareInstallationCanceled, -9948)
        self.assertEqual(ICReturnDeviceSoftwareInstallationFailed, -9949)
        self.assertEqual(ICReturnDeviceSoftwareNotAvailable, -9950)
        self.assertEqual(ICReturnDeviceCouldNotPair, -9951)
        self.assertEqual(ICReturnDeviceCouldNotUnpair, -9952)
        self.assertEqual(ICReturnDeviceNeedsCredentials, -9953)
        self.assertEqual(ICReturnDeviceIsBusyEnumerating, -9954)
        self.assertEqual(ICReturnDeviceCommandGeneralFailure, -9955)
        self.assertEqual(ICReturnDeviceFailedToCompleteTransfer, -9956)
        self.assertEqual(ICReturnDeviceFailedToSendData, -9957)
        self.assertEqual(ICReturnSessionNotOpened, -9958)
        self.assertEqual(ICReturnExFATVolumeInvalid, 21200)
        self.assertEqual(ICReturnMultiErrorDictionary, -30000)
        self.assertEqual(ICReturnDownloadPathInvalid, ICReturnCodeDownloadOffset)
        self.assertEqual(ICReturnCodeObjectDoesNotExist, ICReturnCodeObjectOffset)

        self.assertEqual(ICReturnThumbnailNotAvailable, -21000)
        self.assertEqual(ICReturnThumbnailAlreadyFetching, -20999)
        self.assertEqual(ICReturnThumbnailCanceled, -20098)
        self.assertEqual(ICReturnThumbnailInvalid, -20097)

        self.assertEqual(ICReturnMetadataNotAvailable, -20150)
        self.assertEqual(ICReturnMetadataAlreadyFetching, -20149)
        self.assertEqual(ICReturnMetadataCanceled, -20148)
        self.assertEqual(ICReturnMetadataInvalid, -20147)

        self.assertEqual(ICReturnConnectionDriverExited, -21350)
        self.assertEqual(ICReturnConnectionClosedSessionSuddenly, -21349)
        self.assertEqual(ICReturnConnectionEjectedSuddenly, -21348)
        self.assertEqual(ICReturnConnectionSessionAlreadyOpen, -21347)
        self.assertEqual(ICReturnConnectionEjectFailed, -21346)
        self.assertEqual(ICReturnConnectionFailedToOpen, -21345)
        self.assertEqual(ICReturnConnectionFailedToOpenDevice, -21344)
        self.assertEqual(ICReturnPTPFailedToSendCommand, -21250)
        self.assertEqual(ICReturnPTPNotAuthorizedToSendCommand, -21249)

        self.assertEqual(ICReturnDownloadPathInvalid, -21100)
        self.assertEqual(ICReturnDownloadFileWritable, -21099)

        self.assertEqual(ICLegacyReturnCodeCommunicationErr, -9900)
        self.assertEqual(ICLegacyReturnCodeDeviceNotFoundErr, -9901)
        self.assertEqual(ICLegacyReturnCodeDeviceNotOpenErr, -9902)
        self.assertEqual(ICLegacyReturnCodeFileCorruptedErr, -9903)
        self.assertEqual(ICLegacyReturnCodeIOPendingErr, -9904)
        self.assertEqual(ICLegacyReturnCodeInvalidObjectErr, -9905)
        self.assertEqual(ICLegacyReturnCodeInvalidPropertyErr, -9906)
        self.assertEqual(ICLegacyReturnCodeIndexOutOfRangeErr, -9907)
        self.assertEqual(ICLegacyReturnCodePropertyTypeNotFoundErr, -9908)
        self.assertEqual(ICLegacyReturnCodeCannotYieldDevice, -9909)
        self.assertEqual(ICLegacyReturnCodeDataTypeNotFoundErr, -9910)
        self.assertEqual(ICLegacyReturnCodeDeviceMemoryAllocationErr, -9911)
        self.assertEqual(ICLegacyReturnCodeDeviceInternalErr, -9912)
        self.assertEqual(ICLegacyReturnCodeDeviceInvalidParamErr, -9913)
        self.assertEqual(ICLegacyReturnCodeDeviceAlreadyOpenErr, -9914)
        self.assertEqual(ICLegacyReturnCodeDeviceLocationIDNotFoundErr, -9915)
        self.assertEqual(ICLegacyReturnCodeDeviceGUIDNotFoundErr, -9916)
        self.assertEqual(ICLegacyReturnCodeDeviceIOServicePathNotFoundErr, -9917)
        self.assertEqual(ICLegacyReturnCodeDeviceUnsupportedErr, -9918)
        self.assertEqual(ICLegacyReturnCodeFrameworkInternalErr, -9919)
        self.assertEqual(ICLegacyReturnCodeExtensionInternalErr, -9920)
        self.assertEqual(ICLegacyReturnCodeInvalidSessionErr, -9921)

        self.assertEqual(ICReturnSuccess, 0)
        self.assertEqual(ICReturnInvalidParam, -9922)
        self.assertEqual(ICReturnCommunicationTimedOut, -9923)
        self.assertEqual(ICReturnScanOperationCanceled, -9924)
        self.assertEqual(ICReturnScannerInUseByLocalUser, -9925)
        self.assertEqual(ICReturnScannerInUseByRemoteUser, -9926)
        self.assertEqual(ICReturnDeviceFailedToOpenSession, -9927)
        self.assertEqual(ICReturnDeviceFailedToCloseSession, -9928)
        self.assertEqual(ICReturnScannerFailedToSelectFunctionalUnit, -9929)
        self.assertEqual(ICReturnScannerFailedToCompleteOverviewScan, -9930)
        self.assertEqual(ICReturnScannerFailedToCompleteScan, -9931)
        self.assertEqual(ICReturnReceivedUnsolicitedScannerStatusInfo, -9932)
        self.assertEqual(ICReturnReceivedUnsolicitedScannerErrorInfo, -9933)
        self.assertEqual(ICReturnDownloadFailed, -9934)
        self.assertEqual(ICReturnUploadFailed, -9935)
        self.assertEqual(ICReturnFailedToCompletePassThroughCommand, -9936)
        self.assertEqual(ICReturnDownloadCanceled, -9937)
        self.assertEqual(ICReturnFailedToEnabeTethering, -9938)
        self.assertEqual(ICReturnFailedToDisabeTethering, -9939)
        self.assertEqual(ICReturnFailedToCompleteSendMessageRequest, -9940)
        self.assertEqual(ICReturnDeleteFilesFailed, -9941)
        self.assertEqual(ICReturnDeleteFilesCanceled, -9942)
        self.assertEqual(ICReturnDeviceIsPasscodeLocked, -9943)
        self.assertEqual(ICReturnDeviceFailedToTakePicture, -9944)
        self.assertEqual(ICReturnDeviceSoftwareNotInstalled, -9945)
        self.assertEqual(ICReturnDeviceSoftwareIsBeingInstalled, -9946)
        self.assertEqual(ICReturnDeviceSoftwareInstallationCompleted, -9947)
        self.assertEqual(ICReturnDeviceSoftwareInstallationCanceled, -9948)
        self.assertEqual(ICReturnDeviceSoftwareInstallationFailed, -9949)
        self.assertEqual(ICReturnDeviceSoftwareNotAvailable, -9950)
        self.assertEqual(ICReturnDeviceCouldNotPair, -9951)
        self.assertEqual(ICReturnDeviceCouldNotUnpair, -9952)
        self.assertEqual(ICReturnDeviceNeedsCredentials, -9953)
        self.assertEqual(ICReturnDeviceIsBusyEnumerating, -9954)
        self.assertEqual(ICReturnDeviceCommandGeneralFailure, -9955)
        self.assertEqual(ICReturnDeviceFailedToCompleteTransfer, -9956)
        self.assertEqual(ICReturnDeviceFailedToSendData, -9957)
        self.assertEqual(ICReturnSessionNotOpened, -9958)
        self.assertEqual(ICReturnExFATVolumeInvalid, 21200)
        self.assertEqual(ICReturnMultiErrorDictionary, -30000)

        self.assertEqual(ICReturnCodeObjectDoesNotExist, -21450)
        self.assertEqual(ICReturnCodeObjectDataOffsetInvalid, -21449)
        self.assertEqual(ICReturnCodeObjectCouldNotBeRead, -21448)
        self.assertEqual(ICReturnCodeObjectDataEmpty, -21447)
        self.assertEqual(ICReturnCodeObjectDataRequestTooLarge, -21446)

        self.assertEqual(
            ICReturnFailedToEnableTethering, ICReturnFailedToEnabeTethering
        )
        self.assertEqual(
            ICReturnFailedToDisableTethering, ICReturnFailedToDisabeTethering
        )


if __name__ == "__main__":
    main()
