# This file is generated by objective.metadata
#
# Last update: Sat Aug  3 22:16:04 2019

import sys

import objc

if sys.maxsize > 2 ** 32:

    def sel32or64(a, b):
        return b


else:

    def sel32or64(a, b):
        return a


misc = {}
constants = """$LPErrorDomain$"""
enums = """$LPErrorMetadataFetchCancelled@3$LPErrorMetadataFetchFailed@2$LPErrorMetadataFetchTimedOut@4$LPErrorUnknown@1$"""
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"LPMetadataProvider",
        b"setShouldFetchSubresources:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"LPMetadataProvider", b"shouldFetchSubresources", {"retval": {"type": b"Z"}})
    r(
        b"LPMetadataProvider",
        b"startFetchingMetadataForURL:completionHandler:",
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
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
