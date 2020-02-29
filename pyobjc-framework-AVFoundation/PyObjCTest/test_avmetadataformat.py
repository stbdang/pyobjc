import AVFoundation
from PyObjCTools.TestSupport import *


class TestAVMetadataFormat(TestCase):
    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(AVFoundation.AVMetadataKeySpaceCommon, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyTitle, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyCreator, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeySubject, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyDescription, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyPublisher, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyContributor, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyCreationDate, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyLastModifiedDate, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyType, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyFormat, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyIdentifier, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeySource, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyLanguage, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyRelation, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyLocation, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyCopyrights, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyAlbumName, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyAuthor, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyArtist, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyArtwork, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyMake, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyModel, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeySoftware, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataFormatQuickTimeUserData, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataKeySpaceQuickTimeUserData, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeUserDataKeyAlbum, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyArranger, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyArtist, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyAuthor, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyChapter, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyComment, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyComposer, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyCopyright, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyCreationDate, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyDescription, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyDirector, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyDisclaimer, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyEncodedBy, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyFullName, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeUserDataKeyGenre, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyHostComputer, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyInformation, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyKeywords, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeUserDataKeyMake, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeUserDataKeyModel, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyOriginalArtist, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyOriginalFormat, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyOriginalSource, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyPerformers, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyProducer, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyPublisher, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyProduct, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeySoftware, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeySpecialPlaybackRequirements,
            unicode,
        )
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeUserDataKeyTrack, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyWarning, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyWriter, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyURLLink, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyLocationISO6709, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyTrackName, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyCredits, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyPhonogramRights, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataISOUserDataKeyCopyright, unicode)
        self.assertIsInstance(AVFoundation.AVMetadata3GPUserDataKeyCopyright, unicode)
        self.assertIsInstance(AVFoundation.AVMetadata3GPUserDataKeyAuthor, unicode)
        self.assertIsInstance(AVFoundation.AVMetadata3GPUserDataKeyPerformer, unicode)
        self.assertIsInstance(AVFoundation.AVMetadata3GPUserDataKeyGenre, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadata3GPUserDataKeyRecordingYear, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadata3GPUserDataKeyLocation, unicode)
        self.assertIsInstance(AVFoundation.AVMetadata3GPUserDataKeyTitle, unicode)
        self.assertIsInstance(AVFoundation.AVMetadata3GPUserDataKeyDescription, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataFormatQuickTimeMetadata, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataKeySpaceQuickTimeMetadata, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyAuthor, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyComment, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyCopyright, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyCreationDate, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyDirector, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyDisplayName, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyInformation, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyKeywords, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyProducer, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyPublisher, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeMetadataKeyAlbum, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyArtist, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyArtwork, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyDescription, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeySoftware, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeMetadataKeyYear, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeMetadataKeyGenre, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeMetadataKeyiXML, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyLocationISO6709, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeMetadataKeyMake, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeMetadataKeyModel, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyArranger, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyEncodedBy, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyOriginalArtist, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyPerformer, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyComposer, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyCredits, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyPhonogramRights, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyCameraIdentifier, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyCameraFrameReadoutTime, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeMetadataKeyTitle, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyCollectionUser, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyRatingUser, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyLocationName, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyLocationBody, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyLocationNote, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyLocationRole, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyLocationDate, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyDirectionFacing, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyDirectionMotion, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataFormatiTunesMetadata, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataKeySpaceiTunes, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyAlbum, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyArtist, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyUserComment, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyCoverArt, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyCopyright, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyReleaseDate, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyEncodedBy, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyPredefinedGenre, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyUserGenre, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeySongName, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyTrackSubTitle, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyEncodingTool, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyComposer, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyAlbumArtist, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyAccountKind, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyAppleID, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyArtistID, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeySongID, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyDiscCompilation, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyDiscNumber, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyGenreID, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyGrouping, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyPlaylistID, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyContentRating, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyBeatsPerMin, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyTrackNumber, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyArtDirector, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyArranger, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyAuthor, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyLyrics, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyAcknowledgement, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyConductor, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyDescription, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyDirector, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyEQ, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyLinerNotes, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyRecordCompany, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyOriginalArtist, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyPhonogramRights, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyProducer, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyPerformer, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyPublisher, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeySoundEngineer, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeySoloist, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyCredits, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyThanks, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyOnlineExtras, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyExecProducer, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataFormatID3Metadata, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataKeySpaceID3, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyAudioEncryption, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyAttachedPicture, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyAudioSeekPointIndex, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyComments, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyCommerical, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyEncryption, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyEqualization, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyEqualization2, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyEventTimingCodes, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyGeneralEncapsulatedObject, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyGroupIdentifier, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyInvolvedPeopleList_v23, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyLink, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyMusicCDIdentifier, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyMPEGLocationLookupTable, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyOwnership, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyPrivate, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyPlayCounter, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyPopularimeter, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyPositionSynchronization, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyRecommendedBufferSize, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyRelativeVolumeAdjustment, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyRelativeVolumeAdjustment2, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyReverb, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeySeek, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeySignature, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeySynchronizedLyric, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeySynchronizedTempoCodes, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyAlbumTitle, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyBeatsPerMinute, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyComposer, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyContentType, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyCopyright, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyDate, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyEncodingTime, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyPlaylistDelay, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyOriginalReleaseTime, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyRecordingTime, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyReleaseTime, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyTaggingTime, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyEncodedBy, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyLyricist, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyFileType, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyTime, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyInvolvedPeopleList_v24, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyContentGroupDescription, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyTitleDescription, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeySubTitle, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyInitialKey, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyLanguage, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyLength, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyMusicianCreditsList, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyMediaType, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyMood, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyOriginalAlbumTitle, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyOriginalFilename, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyOriginalLyricist, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyOriginalArtist, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyOriginalReleaseYear, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyFileOwner, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyLeadPerformer, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyBand, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyConductor, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyModifiedBy, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyPartOfASet, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyProducedNotice, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyPublisher, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyTrackNumber, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyRecordingDates, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyInternetRadioStationName, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyInternetRadioStationOwner, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeySize, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyAlbumSortOrder, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyPerformerSortOrder, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyTitleSortOrder, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyInternationalStandardRecordingCode,
            unicode,
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyEncodedWith, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeySetSubtitle, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyYear, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyUserText, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyUniqueFileIdentifier, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyTermsOfUse, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyUnsynchronizedLyric, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyCommercialInformation, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyCopyrightInformation, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyOfficialAudioFileWebpage, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyOfficialArtistWebpage, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyOfficialAudioSourceWebpage, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyOfficialInternetRadioStationHomepage,
            unicode,
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyPayment, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyOfficialPublisherWebpage, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyUserURL, unicode)

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyTaggedCharacteristic, unicode
        )

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(AVFoundation.AVMetadataFormatISOUserData, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataKeySpaceISOUserData, unicode)
        self.assertIsInstance(AVFoundation.AVMetadata3GPUserDataKeyCollection, unicode)
        self.assertIsInstance(AVFoundation.AVMetadata3GPUserDataKeyUserRating, unicode)
        self.assertIsInstance(AVFoundation.AVMetadata3GPUserDataKeyThumbnail, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadata3GPUserDataKeyAlbumAndTrack, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadata3GPUserDataKeyKeywordList, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadata3GPUserDataKeyMediaClassification, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadata3GPUserDataKeyMediaRating, unicode)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(
            AVFoundation.AVMetadataISOUserDataKeyTaggedCharacteristic, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataKeySpaceIcy, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataIcyMetadataKeyStreamTitle, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataIcyMetadataKeyStreamURL, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataFormatHLSMetadata, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataExtraAttributeValueURIKey, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataExtraAttributeBaseURIKey, unicode)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyContentIdentifier, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyCommercial, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataExtraAttributeInfoKey, unicode)

    @min_os_level("10.11.3")
    def testConstants10_11_3(self):
        self.assertIsInstance(AVFoundation.AVMetadataKeySpaceHLSDateRange, unicode)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(AVFoundation.AVMetadataISOUserDataKeyDate, unicode)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(AVFoundation.AVMetadataKeySpaceAudioFile, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataFormatUnknown, unicode)


if __name__ == "__main__":
    main()
