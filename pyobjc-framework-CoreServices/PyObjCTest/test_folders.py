import CoreServices
from PyObjCTools.TestSupport import *


class TestFolders(TestCase):
    def assert_not_wrapped(self, name):
        self.assertTrue(
            not hasattr(CoreServices, name), "%r exposed in bindings" % (name,)
        )

    def test_not_wrapped(self):
        self.assert_not_wrapped("kOnSystemDisk")
        self.assert_not_wrapped("kOnAppropriateDisk")
        self.assert_not_wrapped("kSystemDomain")
        self.assert_not_wrapped("kLocalDomain")
        self.assert_not_wrapped("kNetworkDomain")
        self.assert_not_wrapped("kUserDomain")
        self.assert_not_wrapped("kClassicDomain")
        self.assert_not_wrapped("kFolderManagerLastDomain")
        self.assert_not_wrapped("kLastDomainConstant")
        self.assert_not_wrapped("kCreateFolder")
        self.assert_not_wrapped("kDontCreateFolder")
        self.assert_not_wrapped("FindFolder")
        self.assert_not_wrapped("ReleaseFolder")
        self.assert_not_wrapped("FSFindFolder")
        self.assert_not_wrapped("kDesktopFolderType")
        self.assert_not_wrapped("kTrashFolderType")
        self.assert_not_wrapped("kWhereToEmptyTrashFolderType")
        self.assert_not_wrapped("kFontsFolderType")
        self.assert_not_wrapped("kPreferencesFolderType")
        self.assert_not_wrapped("kSystemPreferencesFolderType")
        self.assert_not_wrapped("kTemporaryFolderType")
        self.assert_not_wrapped("kChewableItemsFolderType")
        self.assert_not_wrapped("kTemporaryItemsInCacheDataFolderType")
        self.assert_not_wrapped("kApplicationsFolderType")
        self.assert_not_wrapped("kVolumeRootFolderType")
        self.assert_not_wrapped("kDomainTopLevelFolderType")
        self.assert_not_wrapped("kDomainLibraryFolderType")
        self.assert_not_wrapped("kUsersFolderType")
        self.assert_not_wrapped("kCurrentUserFolderType")
        self.assert_not_wrapped("kSharedUserDataFolderType")
        self.assert_not_wrapped("kDocumentsFolderType")
        self.assert_not_wrapped("kPictureDocumentsFolderType")
        self.assert_not_wrapped("kMovieDocumentsFolderType")
        self.assert_not_wrapped("kMusicDocumentsFolderType")
        self.assert_not_wrapped("kInternetSitesFolderType")
        self.assert_not_wrapped("kPublicFolderType")
        self.assert_not_wrapped("kDropBoxFolderType")
        self.assert_not_wrapped("kSharedLibrariesFolderType")
        self.assert_not_wrapped("kVoicesFolderType")
        self.assert_not_wrapped("kUtilitiesFolderType")
        self.assert_not_wrapped("kThemesFolderType")
        self.assert_not_wrapped("kFavoritesFolderType")
        self.assert_not_wrapped("kInternetSearchSitesFolderType")
        self.assert_not_wrapped("kInstallerLogsFolderType")
        self.assert_not_wrapped("kScriptsFolderType")
        self.assert_not_wrapped("kFolderActionsFolderType")
        self.assert_not_wrapped("kSpeakableItemsFolderType")
        self.assert_not_wrapped("kKeychainFolderType")
        self.assert_not_wrapped("kColorSyncFolderType")
        self.assert_not_wrapped("kColorSyncCMMFolderType")
        self.assert_not_wrapped("kColorSyncScriptingFolderType")
        self.assert_not_wrapped("kPrintersFolderType")
        self.assert_not_wrapped("kSpeechFolderType")
        self.assert_not_wrapped("kCarbonLibraryFolderType")
        self.assert_not_wrapped("kDocumentationFolderType")
        self.assert_not_wrapped("kISSDownloadsFolderType")
        self.assert_not_wrapped("kUserSpecificTmpFolderType")
        self.assert_not_wrapped("kCachedDataFolderType")
        self.assert_not_wrapped("kFrameworksFolderType")
        self.assert_not_wrapped("kPrivateFrameworksFolderType")
        self.assert_not_wrapped("kClassicDesktopFolderType")
        self.assert_not_wrapped("kSystemSoundsFolderType")
        self.assert_not_wrapped("kComponentsFolderType")
        self.assert_not_wrapped("kQuickTimeComponentsFolderType")
        self.assert_not_wrapped("kCoreServicesFolderType")
        self.assert_not_wrapped("kAudioSupportFolderType")
        self.assert_not_wrapped("kAudioPresetsFolderType")
        self.assert_not_wrapped("kAudioSoundsFolderType")
        self.assert_not_wrapped("kAudioSoundBanksFolderType")
        self.assert_not_wrapped("kAudioAlertSoundsFolderType")
        self.assert_not_wrapped("kAudioPlugInsFolderType")
        self.assert_not_wrapped("kAudioComponentsFolderType")
        self.assert_not_wrapped("kKernelExtensionsFolderType")
        self.assert_not_wrapped("kDirectoryServicesFolderType")
        self.assert_not_wrapped("kDirectoryServicesPlugInsFolderType")
        self.assert_not_wrapped("kInstallerReceiptsFolderType")
        self.assert_not_wrapped("kFileSystemSupportFolderType")
        self.assert_not_wrapped("kAppleShareSupportFolderType")
        self.assert_not_wrapped("kAppleShareAuthenticationFolderType")
        self.assert_not_wrapped("kMIDIDriversFolderType")
        self.assert_not_wrapped("kKeyboardLayoutsFolderType")
        self.assert_not_wrapped("kIndexFilesFolderType")
        self.assert_not_wrapped("kFindByContentIndexesFolderType")
        self.assert_not_wrapped("kManagedItemsFolderType")
        self.assert_not_wrapped("kBootTimeStartupItemsFolderType")
        self.assert_not_wrapped("kAutomatorWorkflowsFolderType")
        self.assert_not_wrapped("kAutosaveInformationFolderType")
        self.assert_not_wrapped("kSpotlightSavedSearchesFolderType")
        self.assert_not_wrapped("kSpotlightImportersFolderType")
        self.assert_not_wrapped("kSpotlightMetadataCacheFolderType")
        self.assert_not_wrapped("kInputManagersFolderType")
        self.assert_not_wrapped("kInputMethodsFolderType")
        self.assert_not_wrapped("kLibraryAssistantsFolderType")
        self.assert_not_wrapped("kAudioDigidesignFolderType")
        self.assert_not_wrapped("kAudioVSTFolderType")
        self.assert_not_wrapped("kColorPickersFolderType")
        self.assert_not_wrapped("kCompositionsFolderType")
        self.assert_not_wrapped("kFontCollectionsFolderType")
        self.assert_not_wrapped("kiMovieFolderType")
        self.assert_not_wrapped("kiMoviePlugInsFolderType")
        self.assert_not_wrapped("kiMovieSoundEffectsFolderType")
        self.assert_not_wrapped("kDownloadsFolderType")
        self.assert_not_wrapped("kColorSyncProfilesFolderType")
        self.assert_not_wrapped("kApplicationSupportFolderType")
        self.assert_not_wrapped("kTextEncodingsFolderType")
        self.assert_not_wrapped("kPrinterDescriptionFolderType")
        self.assert_not_wrapped("kPrinterDriverFolderType")
        self.assert_not_wrapped("kScriptingAdditionsFolderType")
        self.assert_not_wrapped("kClassicPreferencesFolderType")
        self.assert_not_wrapped("kQuickLookFolderType")
        self.assert_not_wrapped("kServicesFolderType")
        self.assert_not_wrapped("kSystemFolderType")
        self.assert_not_wrapped("kSystemDesktopFolderType")
        self.assert_not_wrapped("kSystemTrashFolderType")
        self.assert_not_wrapped("kPrintMonitorDocsFolderType")
        self.assert_not_wrapped("kALMModulesFolderType")
        self.assert_not_wrapped("kALMPreferencesFolderType")
        self.assert_not_wrapped("kALMLocationsFolderType")
        self.assert_not_wrapped("kAppleExtrasFolderType")
        self.assert_not_wrapped("kContextualMenuItemsFolderType")
        self.assert_not_wrapped("kMacOSReadMesFolderType")
        self.assert_not_wrapped("kStartupFolderType")
        self.assert_not_wrapped("kShutdownFolderType")
        self.assert_not_wrapped("kAppleMenuFolderType")
        self.assert_not_wrapped("kControlPanelFolderType")
        self.assert_not_wrapped("kSystemControlPanelFolderType")
        self.assert_not_wrapped("kExtensionFolderType")
        self.assert_not_wrapped("kExtensionDisabledFolderType")
        self.assert_not_wrapped("kControlPanelDisabledFolderType")
        self.assert_not_wrapped("kSystemExtensionDisabledFolderType")
        self.assert_not_wrapped("kStartupItemsDisabledFolderType")
        self.assert_not_wrapped("kShutdownItemsDisabledFolderType")
        self.assert_not_wrapped("kAssistantsFolderType")
        self.assert_not_wrapped("kStationeryFolderType")
        self.assert_not_wrapped("kOpenDocFolderType")
        self.assert_not_wrapped("kOpenDocShellPlugInsFolderType")
        self.assert_not_wrapped("kEditorsFolderType")
        self.assert_not_wrapped("kOpenDocEditorsFolderType")
        self.assert_not_wrapped("kOpenDocLibrariesFolderType")
        self.assert_not_wrapped("kGenEditorsFolderType")
        self.assert_not_wrapped("kHelpFolderType")
        self.assert_not_wrapped("kInternetPlugInFolderType")
        self.assert_not_wrapped("kModemScriptsFolderType")
        self.assert_not_wrapped("kControlStripModulesFolderType")
        self.assert_not_wrapped("kInternetFolderType")
        self.assert_not_wrapped("kAppearanceFolderType")
        self.assert_not_wrapped("kSoundSetsFolderType")
        self.assert_not_wrapped("kDesktopPicturesFolderType")
        self.assert_not_wrapped("kFindSupportFolderType")
        self.assert_not_wrapped("kRecentApplicationsFolderType")
        self.assert_not_wrapped("kRecentDocumentsFolderType")
        self.assert_not_wrapped("kRecentServersFolderType")
        self.assert_not_wrapped("kLauncherItemsFolderType")
        self.assert_not_wrapped("kQuickTimeExtensionsFolderType")
        self.assert_not_wrapped("kDisplayExtensionsFolderType")
        self.assert_not_wrapped("kMultiprocessingFolderType")
        self.assert_not_wrapped("kPrintingPlugInsFolderType")
        self.assert_not_wrapped("kAppleshareAutomountServerAliasesFolderType")
        self.assert_not_wrapped("kVolumeSettingsFolderType")
        self.assert_not_wrapped("kPreMacOS91ApplicationsFolderType")
        self.assert_not_wrapped("kPreMacOS91InstallerLogsFolderType")
        self.assert_not_wrapped("kPreMacOS91AssistantsFolderType")
        self.assert_not_wrapped("kPreMacOS91UtilitiesFolderType")
        self.assert_not_wrapped("kPreMacOS91AppleExtrasFolderType")
        self.assert_not_wrapped("kPreMacOS91MacOSReadMesFolderType")
        self.assert_not_wrapped("kPreMacOS91InternetFolderType")
        self.assert_not_wrapped("kPreMacOS91AutomountedServersFolderType")
        self.assert_not_wrapped("kPreMacOS91StationeryFolderType")
        self.assert_not_wrapped("kLocalesFolderType")
        self.assert_not_wrapped("kFindByContentPluginsFolderType")
        self.assert_not_wrapped("kFindByContentFolderType")
        self.assert_not_wrapped("kMagicTemporaryItemsFolderType")
        self.assert_not_wrapped("kTemporaryItemsInUserDomainFolderType")
        self.assert_not_wrapped("kCurrentUserRemoteFolderLocation")
        self.assert_not_wrapped("kCurrentUserRemoteFolderType")
        self.assert_not_wrapped("kDeveloperDocsFolderType")
        self.assert_not_wrapped("kDeveloperHelpFolderType")
        self.assert_not_wrapped("kDeveloperFolderType")
        self.assert_not_wrapped("kDeveloperApplicationsFolderType")
        self.assert_not_wrapped("kCreateFolderAtBoot")
        self.assert_not_wrapped("kCreateFolderAtBootBit")
        self.assert_not_wrapped("kFolderCreatedInvisible")
        self.assert_not_wrapped("kFolderCreatedInvisibleBit")
        self.assert_not_wrapped("kFolderCreatedNameLocked")
        self.assert_not_wrapped("kFolderCreatedNameLockedBit")
        self.assert_not_wrapped("kFolderCreatedAdminPrivs")
        self.assert_not_wrapped("kFolderCreatedAdminPrivsBit")
        self.assert_not_wrapped("kFolderInUserFolder")
        self.assert_not_wrapped("kFolderInUserFolderBit")
        self.assert_not_wrapped("kFolderTrackedByAlias")
        self.assert_not_wrapped("kFolderTrackedByAliasBit")
        self.assert_not_wrapped("kFolderInRemoteUserFolderIfAvailable")
        self.assert_not_wrapped("kFolderInRemoteUserFolderIfAvailableBit")
        self.assert_not_wrapped("kFolderNeverMatchedInIdentifyFolder")
        self.assert_not_wrapped("kFolderNeverMatchedInIdentifyFolderBit")
        self.assert_not_wrapped("kFolderMustStayOnSameVolume")
        self.assert_not_wrapped("kFolderMustStayOnSameVolumeBit")
        self.assert_not_wrapped(
            "kFolderManagerFolderInMacOS9FolderIfMacOSXIsInstalledMask"
        )
        self.assert_not_wrapped(
            "kFolderManagerFolderInMacOS9FolderIfMacOSXIsInstalledBit"
        )
        self.assert_not_wrapped("kFolderInLocalOrRemoteUserFolder")
        self.assert_not_wrapped("kFolderManagerNotCreatedOnRemoteVolumesBit")
        self.assert_not_wrapped("kFolderManagerNotCreatedOnRemoteVolumesMask")
        self.assert_not_wrapped("kFolderManagerNewlyCreatedFolderIsLocalizedBit")
        self.assert_not_wrapped(
            "kFolderManagerNewlyCreatedFolderShouldHaveDotLocalizedCreatedWithinMask"
        )
        self.assert_not_wrapped("kRelativeFolder")
        self.assert_not_wrapped("kRedirectedRelativeFolder")
        self.assert_not_wrapped("kSpecialFolder")
        self.assert_not_wrapped("kBlessedFolder")
        self.assert_not_wrapped("kRootFolder")
        self.assert_not_wrapped("kCurrentUserFolderLocation")
        self.assert_not_wrapped("kDictionariesFolderType")
        self.assert_not_wrapped("kLogsFolderType")
        self.assert_not_wrapped("kPreferencePanesFolderType")
        self.assert_not_wrapped("kWidgetsFolderType")
        self.assert_not_wrapped("kScreenSaversFolderType")
        self.assert_not_wrapped("FolderDesc")
        self.assert_not_wrapped("FolderRouting")
        self.assert_not_wrapped("AddFolderDescriptor")
        self.assert_not_wrapped("GetFolderTypes")
        self.assert_not_wrapped("RemoveFolderDescriptor")
        self.assert_not_wrapped("GetFolderNameUnicode")
        self.assert_not_wrapped("InvalidateFolderDescriptorCache")
        self.assert_not_wrapped("IdentifyFolder")
        self.assert_not_wrapped("FSDetermineIfRefIsEnclosedByFolder")
        self.assert_not_wrapped("DetermineIfPathIsEnclosedByFolder")
        self.assert_not_wrapped("FindFolderExtended")
        self.assert_not_wrapped("FSFindFolderExtended")
        self.assert_not_wrapped("GetFolderDescriptor")
        self.assert_not_wrapped("GetFolderName")
        self.assert_not_wrapped("AddFolderRouting")
        self.assert_not_wrapped("RemoveFolderRouting")
        self.assert_not_wrapped("FindFolderRouting")
        self.assert_not_wrapped("GetFolderRoutings")
        self.assert_not_wrapped("FSpDetermineIfSpecIsEnclosedByFolder")
        self.assert_not_wrapped("NewFolderManagerNotificationUPP")
        self.assert_not_wrapped("DisposeFolderManagerNotificationUPP")
        self.assert_not_wrapped("InvokeFolderManagerNotificationUPP")
        self.assert_not_wrapped("FolderManagerRegisterNotificationProc")
        self.assert_not_wrapped("FolderManagerUnregisterNotificationProc")
        self.assert_not_wrapped("FolderManagerRegisterCallNotificationProcs")


if __name__ == "__main__":
    main()
