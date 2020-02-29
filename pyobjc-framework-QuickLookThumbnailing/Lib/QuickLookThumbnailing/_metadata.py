# This file is generated by objective.metadata
#
# Last update: Sun Aug  4 09:43:31 2019

import sys

import objc

if sys.maxsize > 2 ** 32:

    def sel32or64(a, b):
        return b


else:

    def sel32or64(a, b):
        return a


misc = {}
constants = """$QLThumbnailErrorDomain$"""
enums = """$QLThumbnailErrorGenerationFailed@0$QLThumbnailErrorNoCachedThumbnail@2$QLThumbnailErrorNoCloudThumbnail@3$QLThumbnailErrorRequestCancelled@5$QLThumbnailErrorRequestInvalid@4$QLThumbnailErrorSavingToURLFailed@1$QLThumbnailGenerationRequestRepresentationTypeAll@18446744073709551615$QLThumbnailGenerationRequestRepresentationTypeIcon@1$QLThumbnailGenerationRequestRepresentationTypeLowQualityThumbnail@2$QLThumbnailGenerationRequestRepresentationTypeThumbnail@4$QLThumbnailRepresentationTypeIcon@0$QLThumbnailRepresentationTypeLowQualityThumbnail@1$QLThumbnailRepresentationTypeThumbnail@2$"""
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b"QLThumbnailGenerationRequest", b"iconMode", {"retval": {"type": b"Z"}})
    r(
        b"QLThumbnailGenerationRequest",
        b"setIconMode:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"QLThumbnailGenerator",
        b"generateBestRepresentationForRequest:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"QLThumbnailGenerator",
        b"generateRepresentationsForRequest:updateHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"Q"},
                            3: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"QLThumbnailGenerator",
        b"saveBestRepresentationForRequest:toFileAtURL:withContentType:completionHandler:",
        {
            "arguments": {
                5: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"QLThumbnailProvider",
        b"provideThumbnailForFileRequest:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"QLThumbnailReply",
        b"replyWithContextSize:currentContextDrawingBlock:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"Z"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                }
            }
        },
    )
    r(
        b"QLThumbnailReply",
        b"replyWithContextSize:drawingBlock:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"Z"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"^{CGContext=}"},
                        },
                    }
                }
            }
        },
    )
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
