import QTKit
from PyObjCTools.TestSupport import *


class TestQTMetadaItem(TestCase):
    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(QTKit.QTMetadataFormatQuickTimeUserData, unicode)
        self.assertIsInstance(QTKit.QTMetadataFormatQuickTimeMetadata, unicode)
        self.assertIsInstance(QTKit.QTMetadataFormatiTunesMetadata, unicode)
        self.assertIsInstance(QTKit.QTMetadataFormatID3Metadata, unicode)
        self.assertIsInstance(QTKit.QTMetadataKeySpaceCommon, unicode)
        self.assertIsInstance(QTKit.QTMetadataKeySpaceQuickTimeUserData, unicode)
        self.assertIsInstance(QTKit.QTMetadataKeySpaceQuickTimeMetadata, unicode)
        self.assertIsInstance(QTKit.QTMetadataKeySpaceiTunes, unicode)
        self.assertIsInstance(QTKit.QTMetadataKeySpaceID3, unicode)
        self.assertIsInstance(QTKit.QTMetadataCommonKeyTitle, unicode)
        self.assertIsInstance(QTKit.QTMetadataCommonKeyCreator, unicode)
        self.assertIsInstance(QTKit.QTMetadataCommonKeySubject, unicode)
        self.assertIsInstance(QTKit.QTMetadataCommonKeyDescription, unicode)
        self.assertIsInstance(QTKit.QTMetadataCommonKeyPublisher, unicode)
        self.assertIsInstance(QTKit.QTMetadataCommonKeyContributor, unicode)
        self.assertIsInstance(QTKit.QTMetadataCommonKeyCreationDate, unicode)
        self.assertIsInstance(QTKit.QTMetadataCommonKeyLastModifiedDate, unicode)
        self.assertIsInstance(QTKit.QTMetadataCommonKeyType, unicode)
        self.assertIsInstance(QTKit.QTMetadataCommonKeyFormat, unicode)
        self.assertIsInstance(QTKit.QTMetadataCommonKeyIdentifier, unicode)
        self.assertIsInstance(QTKit.QTMetadataCommonKeySource, unicode)
        self.assertIsInstance(QTKit.QTMetadataCommonKeyLanguage, unicode)
        self.assertIsInstance(QTKit.QTMetadataCommonKeyRelation, unicode)
        self.assertIsInstance(QTKit.QTMetadataCommonKeyLocation, unicode)
        self.assertIsInstance(QTKit.QTMetadataCommonKeyCopyrights, unicode)
        self.assertIsInstance(QTKit.QTMetadataCommonKeyAlbumName, unicode)
        self.assertIsInstance(QTKit.QTMetadataCommonKeyAuthor, unicode)
        self.assertIsInstance(QTKit.QTMetadataCommonKeyArtist, unicode)
        self.assertIsInstance(QTKit.QTMetadataCommonKeyArtwork, unicode)
        self.assertIsInstance(QTKit.QTMetadataCommonKeyMake, unicode)
        self.assertIsInstance(QTKit.QTMetadataCommonKeyModel, unicode)
        self.assertIsInstance(QTKit.QTMetadataCommonKeySoftware, unicode)
        self.assertIsInstance(QTKit.QTMetadataCommonKeyComment, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeyAlbum, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeyArranger, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeyArtist, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeyAuthor, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeyChapter, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeyComment, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeyComposer, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeyCopyright, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeyCreationDate, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeyDescription, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeyDirector, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeyDisclaimer, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeyEncodedBy, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeyFullName, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeyGenre, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeyHostComputer, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeyInformation, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeyKeywords, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeyMake, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeyModel, unicode)
        self.assertIsInstance(
            QTKit.QTMetadataQuickTimeUserDataKeyOriginalArtist, unicode
        )
        self.assertIsInstance(
            QTKit.QTMetadataQuickTimeUserDataKeyOriginalFormat, unicode
        )
        self.assertIsInstance(
            QTKit.QTMetadataQuickTimeUserDataKeyOriginalSource, unicode
        )
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeyPerformers, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeyProducer, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeyPublisher, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeyProduct, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeySoftware, unicode)
        self.assertIsInstance(
            QTKit.QTMetadataQuickTimeUserDataKeySpecialPlaybackRequirements, unicode
        )
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeyTrack, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeyWarning, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeyWriter, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeyURLLink, unicode)
        self.assertIsInstance(
            QTKit.QTMetadataQuickTimeUserDataKeyLocationISO6709, unicode
        )
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeyTrackName, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeUserDataKeyCredits, unicode)
        self.assertIsInstance(
            QTKit.QTMetadataQuickTimeUserDataKeyPhonogramRights, unicode
        )
        self.assertIsInstance(QTKit.QTMetadataISOUserDataKeyCopyright, unicode)
        self.assertIsInstance(QTKit.QTMetadata3GPUserDataKeyCopyright, unicode)
        self.assertIsInstance(QTKit.QTMetadata3GPUserDataKeyAuthor, unicode)
        self.assertIsInstance(QTKit.QTMetadata3GPUserDataKeyPerformer, unicode)
        self.assertIsInstance(QTKit.QTMetadata3GPUserDataKeyGenre, unicode)
        self.assertIsInstance(QTKit.QTMetadata3GPUserDataKeyRecordingYear, unicode)
        self.assertIsInstance(QTKit.QTMetadata3GPUserDataKeyLocation, unicode)
        self.assertIsInstance(QTKit.QTMetadata3GPUserDataKeyTitle, unicode)
        self.assertIsInstance(QTKit.QTMetadata3GPUserDataKeyDescription, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeMetadataKeyAuthor, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeMetadataKeyComment, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeMetadataKeyCopyright, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeMetadataKeyCreationDate, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeMetadataKeyDirector, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeMetadataKeyDisplayName, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeMetadataKeyInformation, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeMetadataKeyKeywords, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeMetadataKeyProducer, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeMetadataKeyPublisher, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeMetadataKeyAlbum, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeMetadataKeyArtist, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeMetadataKeyArtwork, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeMetadataKeyDescription, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeMetadataKeySoftware, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeMetadataKeyYear, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeMetadataKeyGenre, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeMetadataKeyiXML, unicode)
        self.assertIsInstance(
            QTKit.QTMetadataQuickTimeMetadataKeyLocationISO6709, unicode
        )
        self.assertIsInstance(QTKit.QTMetadataQuickTimeMetadataKeyMake, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeMetadataKeyModel, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeMetadataKeyArranger, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeMetadataKeyEncodedBy, unicode)
        self.assertIsInstance(
            QTKit.QTMetadataQuickTimeMetadataKeyOriginalArtist, unicode
        )
        self.assertIsInstance(QTKit.QTMetadataQuickTimeMetadataKeyPerformer, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeMetadataKeyComposer, unicode)
        self.assertIsInstance(QTKit.QTMetadataQuickTimeMetadataKeyCredits, unicode)
        self.assertIsInstance(
            QTKit.QTMetadataQuickTimeMetadataKeyPhonogramRights, unicode
        )
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyAlbum, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyArtist, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyUserComment, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyCoverArt, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyCopyright, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyReleaseDate, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyEncodedBy, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyPredefinedGenre, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyUserGenre, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeySongName, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyTrackSubTitle, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyEncodingTool, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyComposer, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyAlbumArtist, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyAccountKind, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyAppleID, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyArtistID, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeySongID, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyDiscCompilation, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyDiscNumber, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyGenreID, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyGrouping, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyPlaylistID, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyContentRating, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyBeatsPerMin, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyTrackNumber, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyArtDirector, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyArranger, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyAuthor, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyLyrics, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyAcknowledgement, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyConductor, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyDescription, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyDirector, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyEQ, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyLinerNotes, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyRecordCompany, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyOriginalArtist, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyPhonogramRights, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyProducer, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyPerformer, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyPublisher, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeySoundEngineer, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeySoloist, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyCredits, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyThanks, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyOnlineExtras, unicode)
        self.assertIsInstance(QTKit.QTMetadataiTunesMetadataKeyExecProducer, unicode)

    @expectedFailure
    @min_os_level("10.7")
    def testConstants10_7_missing(self):
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyAudioEncryption, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyAttachedPicture, unicode)
        self.assertIsInstance(
            QTKit.QTMetadataID3MetadataKeyAudioSeekPointIndex, unicode
        )
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyComments, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyCommerical, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyEncryption, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyEqualization, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyEqualization2, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyEventTimingCodes, unicode)
        self.assertIsInstance(
            QTKit.QTMetadataID3MetadataKeyGeneralEncapsulatedObject, unicode
        )
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyGroupIdentifier, unicode)
        self.assertIsInstance(
            QTKit.QTMetadataID3MetadataKeyInvolvedPeopleList_v23, unicode
        )
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyLink, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyMusicCDIdentifier, unicode)
        self.assertIsInstance(
            QTKit.QTMetadataID3MetadataKeyMPEGLocationLookupTable, unicode
        )
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyOwnership, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyPrivate, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyPlayCounter, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyPopularimeter, unicode)
        self.assertIsInstance(
            QTKit.QTMetadataID3MetadataKeyPositionSynchronization, unicode
        )
        self.assertIsInstance(
            QTKit.QTMetadataID3MetadataKeyRecommendedBufferSize, unicode
        )
        self.assertIsInstance(
            QTKit.QTMetadataID3MetadataKeyRelativeVolumeAdjustment, unicode
        )
        self.assertIsInstance(
            QTKit.QTMetadataID3MetadataKeyRelativeVolumeAdjustment2, unicode
        )
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyReverb, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeySeek, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeySignature, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeySynchronizedLyric, unicode)
        self.assertIsInstance(
            QTKit.QTMetadataID3MetadataKeySynchronizedTempoCodes, unicode
        )
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyAlbumTitle, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyBeatsPerMinute, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyComposer, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyContentType, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyCopyright, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyDate, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyEncodingTime, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyPlaylistDelay, unicode)
        self.assertIsInstance(
            QTKit.QTMetadataID3MetadataKeyOriginalReleaseTime, unicode
        )
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyRecordingTime, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyReleaseTime, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyTaggingTime, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyEncodedBy, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyLyricist, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyFileType, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyTime, unicode)
        self.assertIsInstance(
            QTKit.QTMetadataID3MetadataKeyInvolvedPeopleList_v24, unicode
        )
        self.assertIsInstance(
            QTKit.QTMetadataID3MetadataKeyContentGroupDescription, unicode
        )
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyTitleDescription, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeySubTitle, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyInitialKey, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyLanguage, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyLength, unicode)
        self.assertIsInstance(
            QTKit.QTMetadataID3MetadataKeyMusicianCreditsList, unicode
        )
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyMediaType, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyMood, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyOriginalAlbumTitle, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyOriginalFilename, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyOriginalLyricist, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyOriginalArtist, unicode)
        self.assertIsInstance(
            QTKit.QTMetadataID3MetadataKeyOriginalReleaseYear, unicode
        )
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyFileOwner, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyLeadPerformer, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyBand, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyConductor, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyModifiedBy, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyPartOfASet, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyProducedNotice, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyPublisher, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyTrackNumber, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyRecordingDates, unicode)
        self.assertIsInstance(
            QTKit.QTMetadataID3MetadataKeyInternetRadioStationName, unicode
        )
        self.assertIsInstance(
            QTKit.QTMetadataID3MetadataKeyInternetRadioStationOwner, unicode
        )
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeySize, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyAlbumSortOrder, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyPerformerSortOrder, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyTitleSortOrder, unicode)
        self.assertIsInstance(
            QTKit.QTMetadataID3MetadataKeyInternationalStandardRecordingCode, unicode
        )
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyEncodedWith, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeySetSubtitle, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyYear, unicode)
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyUserText, unicode)
        self.assertIsInstance(
            QTKit.QTMetadataID3MetadataKeyUniqueFileIdentifier, unicode
        )
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyTermsOfUse, unicode)
        self.assertIsInstance(
            QTKit.QTMetadataID3MetadataKeyUnsynchronizedLyric, unicode
        )
        self.assertIsInstance(
            QTKit.QTMetadataID3MetadataKeyCommercialInformation, unicode
        )
        self.assertIsInstance(
            QTKit.QTMetadataID3MetadataKeyCopyrightInformation, unicode
        )
        self.assertIsInstance(
            QTKit.QTMetadataID3MetadataKeyOfficialAudioFileWebpage, unicode
        )
        self.assertIsInstance(
            QTKit.QTMetadataID3MetadataKeyOfficialArtistWebpage, unicode
        )
        self.assertIsInstance(
            QTKit.QTMetadataID3MetadataKeyOfficialAudioSourceWebpage, unicode
        )
        self.assertIsInstance(
            QTKit.QTMetadataID3MetadataKeyOfficialInternetRadioStationHomepage, unicode
        )
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyPayment, unicode)
        self.assertIsInstance(
            QTKit.QTMetadataID3MetadataKeyOfficialPublisherWebpage, unicode
        )
        self.assertIsInstance(QTKit.QTMetadataID3MetadataKeyUserURL, unicode)


if __name__ == "__main__":
    main()
