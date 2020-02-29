# This file is generated by objective.metadata
#
# Last update: Sat Aug 10 16:51:58 2019

import sys

import objc

if sys.maxsize > 2 ** 32:

    def sel32or64(a, b):
        return b


else:

    def sel32or64(a, b):
        return a


misc = {}
constants = """$SNErrorDomain$"""
enums = """$SNErrorCodeInvalidFile@5$SNErrorCodeInvalidFormat@3$SNErrorCodeInvalidModel@4$SNErrorCodeOperationFailed@2$SNErrorCodeUnknownError@1$"""
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"NSObject",
        b"request:didFailWithError:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"request:didProduceResult:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"requestDidComplete:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"SNAudioFileAnalyzer",
        b"addRequest:withObserver:error:",
        {"retval": {"type": b"Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"SNAudioFileAnalyzer",
        b"analyzeWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"SNAudioFileAnalyzer",
        b"initWithURL:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"SNAudioStreamAnalyzer",
        b"addRequest:withObserver:error:",
        {"retval": {"type": b"Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"SNClassificationResult",
        b"timeRange",
        {"retval": {"type": b"{_CMTimeRange={_CMTime=qiIq}{_CMTime=qiIq}}"}},
    )
    r(
        b"SNClassifySoundRequest",
        b"initWithMLModel:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
