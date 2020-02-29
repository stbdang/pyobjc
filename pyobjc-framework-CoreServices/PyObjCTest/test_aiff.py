import CoreServices
from PyObjCTools.TestSupport import *


class TestAIFF(TestCase):
    def assert_not_wrapped(self, name):
        self.assertTrue(
            not hasattr(CoreServices, name), "%r exposed in bindings" % (name,)
        )

    def test_not_wrapped(self):
        self.assert_not_wrapped("AIFFID")
        self.assert_not_wrapped("AIFCID")
        self.assert_not_wrapped("FormatVersionID")
        self.assert_not_wrapped("CommonID")
        self.assert_not_wrapped("FORMID")
        self.assert_not_wrapped("SoundDataID")
        self.assert_not_wrapped("MarkerID")
        self.assert_not_wrapped("InstrumentID")
        self.assert_not_wrapped("MIDIDataID")
        self.assert_not_wrapped("AudioRecordingID")
        self.assert_not_wrapped("ApplicationSpecificID")
        self.assert_not_wrapped("CommentID")
        self.assert_not_wrapped("NameID")
        self.assert_not_wrapped("AuthorID")
        self.assert_not_wrapped("CopyrightID")
        self.assert_not_wrapped("AnnotationID")
        self.assert_not_wrapped("NoLooping")
        self.assert_not_wrapped("ForwardLooping")
        self.assert_not_wrapped("ForwardBackwardLooping")
        self.assert_not_wrapped("AIFCVersion1")
        self.assert_not_wrapped("NoneName")
        self.assert_not_wrapped("ACE2to1Name")
        self.assert_not_wrapped("ACE8to3Name")
        self.assert_not_wrapped("MACE3to1Name")
        self.assert_not_wrapped("MACE6to1Name")
        self.assert_not_wrapped("NoneType")
        self.assert_not_wrapped("ACE2Type")
        self.assert_not_wrapped("ACE8Type")
        self.assert_not_wrapped("MACE3Type")
        self.assert_not_wrapped("MACE6Type")
        self.assert_not_wrapped("ChunkHeader")
        self.assert_not_wrapped("ContainerChunk")
        self.assert_not_wrapped("FormatVersionChunk")
        self.assert_not_wrapped("CommonChunk")
        self.assert_not_wrapped("ExtCommonChunk")
        self.assert_not_wrapped("SoundDataChunk")
        self.assert_not_wrapped("Marker")
        self.assert_not_wrapped("MarkerChunk")
        self.assert_not_wrapped("AIFFLoop")
        self.assert_not_wrapped("InstrumentChunk")
        self.assert_not_wrapped("MIDIDataChunk")
        self.assert_not_wrapped("AudioRecordingChunk")
        self.assert_not_wrapped("ApplicationSpecificChunk")
        self.assert_not_wrapped("Comment")
        self.assert_not_wrapped("CommentsChunk")
        self.assert_not_wrapped("TextChunk")


if __name__ == "__main__":
    main()
