# This file is generated by objective.metadata
#
# Last update: Sun Aug  4 16:16:31 2019

import sys

import objc

if sys.maxsize > 2 ** 32:

    def sel32or64(a, b):
        return b


else:

    def sel32or64(a, b):
        return a


misc = {}
constants = """$kSKEndTermChars@^{__CFString=}$kSKLanguageTypes@^{__CFString=}$kSKMaximumTerms@^{__CFString=}$kSKMinTermLength@^{__CFString=}$kSKProximityIndexing@^{__CFString=}$kSKStartTermChars@^{__CFString=}$kSKStopWords@^{__CFString=}$kSKSubstitutions@^{__CFString=}$kSKTermChars@^{__CFString=}$"""
enums = """$kSKDocumentStateAddPending@2$kSKDocumentStateDeletePending@3$kSKDocumentStateIndexed@1$kSKDocumentStateNotIndexed@0$kSKIndexInverted@1$kSKIndexInvertedVector@3$kSKIndexUnknown@0$kSKIndexVector@2$kSKSearchBooleanRanked@1$kSKSearchOptionDefault@0$kSKSearchOptionFindSimilar@4$kSKSearchOptionNoRelevanceScores@1$kSKSearchOptionSpaceMeansOR@2$kSKSearchPrefixRanked@3$kSKSearchRanked@0$kSKSearchRequiredRanked@2$"""
misc.update({})
functions = {
    "SKIndexGetMaximumTermID": (sel32or64(b"l^{__SKIndex=}", b"q^{__SKIndex=}"),),
    "SKDocumentGetName": (b"^{__CFString=}@",),
    "SKIndexRemoveDocument": (b"Z^{__SKIndex=}@",),
    "SKIndexCopyTermIDArrayForDocumentID": (
        sel32or64(b"^{__CFArray=}^{__SKIndex=}l", b"^{__CFArray=}^{__SKIndex=}q"),
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKSearchGetTypeID": (sel32or64(b"L", b"Q"),),
    "SKIndexDocumentIteratorCreate": (
        b"^{__SKIndexDocumentIterator=}^{__SKIndex=}@",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKDocumentGetTypeID": (sel32or64(b"L", b"Q"),),
    "SKSummaryGetParagraphSummaryInfo": (
        sel32or64(b"l^{__SKSummary=}l^l^l", b"q^{__SKSummary=}q^q^q"),
        "",
        {"arguments": {2: {"type_modifier": "o"}, 3: {"type_modifier": "o"}}},
    ),
    "SKSummaryGetParagraphCount": (
        sel32or64(b"l^{__SKSummary=}", b"q^{__SKSummary=}"),
    ),
    "SKIndexGetMaximumDocumentID": (sel32or64(b"l^{__SKIndex=}", b"q^{__SKIndex=}"),),
    "SKSearchGroupCreate": (
        b"^{__SKSearchGroup=}^{__CFArray=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKIndexFlush": (b"Z^{__SKIndex=}",),
    "SKIndexCreateWithURL": (
        b"^{__SKIndex=}^{__CFURL=}^{__CFString=}I^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKSummaryGetSentenceCount": (sel32or64(b"l^{__SKSummary=}", b"q^{__SKSummary=}"),),
    "SKIndexGetMaximumBytesBeforeFlush": (
        sel32or64(b"l^{__SKIndex=}", b"q^{__SKIndex=}"),
    ),
    "SKIndexCopyDocumentIDArrayForTermID": (
        sel32or64(b"^{__CFArray=}^{__SKIndex=}l", b"^{__CFArray=}^{__SKIndex=}q"),
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKSearchResultsCreateWithDocuments": (
        sel32or64(
            b"^{__SKSearchResults=}^{__SKSearchGroup=}^{__CFArray=}l^v^?",
            b"^{__SKSearchResults=}^{__SKSearchGroup=}^{__CFArray=}q^v^?",
        ),
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"Z"},
                        "arguments": {
                            0: {"type": b"^{__SKIndex=}"},
                            1: {"type": b"@"},
                            2: {"type": b"^v"},
                        },
                    }
                }
            },
        },
    ),
    "SKSummaryCopyParagraphAtIndex": (
        sel32or64(b"^{__CFString=}^{__SKSummary=}l", b"^{__CFString=}^{__SKSummary=}q"),
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKIndexGetDocumentID": (sel32or64(b"l^{__SKIndex=}@", b"q^{__SKIndex=}@"),),
    "SKIndexOpenWithURL": (b"^{__SKIndex=}^{__CFURL=}^{__CFString=}Z",),
    "SKIndexCreateWithMutableData": (
        b"^{__SKIndex=}^{__CFData=}^{__CFString=}I^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKIndexCopyDocumentURLsForDocumentIDs": (
        sel32or64(b"v^{__SKIndex=}l^l^^{__CFURL=}", b"v^{__SKIndex=}q^q^^{__CFURL=}"),
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                2: {"c_array_length_in_arg": 1, "type_modifier": "n"},
                3: {
                    "already_cfretained": True,
                    "c_array_length_in_arg": 1,
                    "type_modifier": "o",
                },
            },
        },
    ),
    "SKSearchResultsCreateWithQuery": (
        sel32or64(
            b"^{__SKSearchResults=}^{__SKSearchGroup=}^{__CFString=}Il^v^?",
            b"^{__SKSearchResults=}^{__SKSearchGroup=}^{__CFString=}Iq^v^?",
        ),
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                5: {
                    "callable": {
                        "retval": {"type": b"Z"},
                        "arguments": {
                            0: {"type": b"^{__SKIndex=}"},
                            1: {"type": b"@"},
                            2: {"type": b"^v"},
                        },
                    }
                }
            },
        },
    ),
    "SKIndexCompact": (b"Z^{__SKIndex=}",),
    "SKSearchGroupGetTypeID": (sel32or64(b"L", b"Q"),),
    "SKSummaryCopySentenceAtIndex": (
        sel32or64(b"^{__CFString=}^{__SKSummary=}l", b"^{__CFString=}^{__SKSummary=}q"),
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKSearchGroupCopyIndexes": (
        b"^{__CFArray=}^{__SKSearchGroup=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKLoadDefaultExtractorPlugIns": (b"v",),
    "SKIndexMoveDocument": (b"Z^{__SKIndex=}@@",),
    "SKIndexOpenWithData": (b"^{__SKIndex=}^{__CFData=}^{__CFString=}",),
    "SKIndexCopyDocumentProperties": (
        b"^{__CFDictionary=}^{__SKIndex=}@",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKIndexCopyDocumentRefsForDocumentIDs": (
        sel32or64(b"v^{__SKIndex=}l^l^@", b"v^{__SKIndex=}q^q^@"),
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                2: {"c_array_lengt_in_arg": 1, "type_modifier": "n"},
                3: {"c_array_lengt_in_arg": 1, "type_modifier": "o"},
            },
        },
    ),
    "SKIndexOpenWithMutableData": (b"^{__SKIndex=}^{__CFData=}^{__CFString=}",),
    "SKSearchResultsCopyMatchingTerms": (
        sel32or64(
            b"^{__CFArray=}^{__SKSearchResults=}l",
            b"^{__CFArray=}^{__SKSearchResults=}q",
        ),
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKDocumentGetParent": (b"@@",),
    "SKSearchResultsGetTypeID": (sel32or64(b"L", b"Q"),),
    "SKSummaryCreateWithString": (
        b"^{__SKSummary=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKIndexGetDocumentTermCount": (sel32or64(b"l^{__SKIndex=}l", b"q^{__SKIndex=}q"),),
    "SKIndexSetDocumentProperties": (b"v^{__SKIndex=}@^{__CFDictionary=}",),
    "SKSummaryGetSentenceSummaryInfo": (
        sel32or64(b"l^{__SKSummary=}l^l^l^l", b"q^{__SKSummary=}q^q^q^q"),
        "",
        {
            "arguments": {
                2: {"type_modifier": "o"},
                3: {"type_modifier": "o"},
                4: {"type_modifier": "o"},
            }
        },
    ),
    "SKDocumentCreate": (
        b"@^{__CFString=}@^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKDocumentCreateWithURL": (
        b"@^{__CFURL=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKIndexClose": (b"v^{__SKIndex=}",),
    "SKIndexGetDocumentTermFrequency": (
        sel32or64(b"l^{__SKIndex=}ll", b"q^{__SKIndex=}qq"),
    ),
    "SKIndexDocumentIteratorCopyNext": (
        b"@^{__SKIndexDocumentIterator=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKIndexRenameDocument": (b"Z^{__SKIndex=}@^{__CFString=}",),
    "SKSummaryGetTypeID": (sel32or64(b"L", b"Q"),),
    "SKDocumentGetSchemeName": (b"^{__CFString=}@",),
    "SKDocumentCopyURL": (
        b"^{__CFURL=}@",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKIndexGetTypeID": (sel32or64(b"L", b"Q"),),
    "SKSearchCancel": (b"v^{__SKSearch=}",),
    "SKIndexGetDocumentCount": (sel32or64(b"l^{__SKIndex=}", b"q^{__SKIndex=}"),),
    "SKSummaryCopySentenceSummaryString": (
        sel32or64(b"^{__CFString=}^{__SKSummary=}l", b"^{__CFString=}^{__SKSummary=}q"),
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKIndexGetTermDocumentCount": (sel32or64(b"l^{__SKIndex=}l", b"q^{__SKIndex=}q"),),
    "SKIndexGetTermIDForTermString": (
        sel32or64(b"l^{__SKIndex=}^{__CFString=}", b"q^{__SKIndex=}^{__CFString=}"),
    ),
    "SKSummaryCopyParagraphSummaryString": (
        sel32or64(b"^{__CFString=}^{__SKSummary=}l", b"^{__CFString=}^{__SKSummary=}q"),
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKIndexGetDocumentState": (b"I^{__SKIndex=}@",),
    "SKSearchCreate": (
        sel32or64(
            b"^{__SKSearch=}^{__SKIndex=}^{__CFString=}L",
            b"^{__SKSearch=}^{__SKIndex=}^{__CFString=}I",
        ),
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKIndexAddDocumentWithText": (b"Z^{__SKIndex=}@^{__CFString=}Z",),
    "SKIndexAddDocument": (b"Z^{__SKIndex=}@^{__CFString=}Z",),
    "SKIndexSetMaximumBytesBeforeFlush": (
        sel32or64(b"v^{__SKIndex=}l", b"v^{__SKIndex=}q"),
    ),
    "SKSearchFindMatches": (
        sel32or64(b"Z^{__SKSearch=}l^l^fd^l", b"Z^{__SKSearch=}q^q^fd^q"),
        "",
        {
            "arguments": {
                2: {"c_array_length_in_arg": (1, 5), "type_modifier": "o"},
                3: {"c_array_length_in_arg": (1, 5), "type_modifier": "o"},
                5: {"type_modifier": "o"},
            }
        },
    ),
    "SKIndexCopyTermStringForTermID": (
        sel32or64(b"^{__CFString=}^{__SKIndex=}l", b"^{__CFString=}^{__SKIndex=}q"),
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKIndexGetAnalysisProperties": (b"^{__CFDictionary=}^{__SKIndex=}",),
    "SKSearchResultsGetCount": (
        sel32or64(b"l^{__SKSearchResults=}", b"q^{__SKSearchResults=}"),
    ),
    "SKSearchResultsGetInfoInRange": (
        sel32or64(
            b"l^{__SKSearchResults=}{_CFRange=ll}^@^^{__SKIndex=}^f",
            b"q^{__SKSearchResults=}{_CFRange=qq}^@^^{__SKIndex=}^f",
        ),
        "",
        {
            "arguments": {
                2: {
                    "c_array_length_in_arg": 1,
                    "c_array_length_in_result": True,
                    "type_modifier": "o",
                },
                3: {
                    "c_array_length_in_arg": 1,
                    "c_array_length_in_result": True,
                    "type_modifier": "o",
                },
                4: {
                    "c_array_length_in_arg": 1,
                    "c_array_length_in_result": True,
                    "type_modifier": "o",
                },
            }
        },
    ),
    "SKIndexCopyDocumentForDocumentID": (
        sel32or64(b"@^{__SKIndex=}l", b"@^{__SKIndex=}q"),
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKIndexCopyInfoForDocumentIDs": (
        sel32or64(
            b"v^{__SKIndex=}l^l^^{__CFString=}^l", b"v^{__SKIndex=}q^q^^{__CFString=}^q"
        ),
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                2: {"c_array_length_in_arg": 1, "type_modifier": "n"},
                3: {
                    "already_cfretained": True,
                    "c_array_length_in_arg": 1,
                    "type_modifier": "o",
                },
                4: {"c_array_length_in_arg": 1, "type_modifier": "o"},
            },
        },
    ),
    "SKIndexGetIndexType": (b"I^{__SKIndex=}",),
    "SKIndexDocumentIteratorGetTypeID": (sel32or64(b"L", b"Q"),),
}
cftypes = [
    (
        "SKIndexDocumentIteratorRef",
        b"^{__SKIndexDocumentIterator=}",
        "SKIndexDocumentIteratorGetTypeID",
        None,
    ),
    ("SKIndexRef", b"^{__SKIndex=}", "SKIndexGetTypeID", None),
    ("SKSearchGroupRef", b"^{__SKSearchGroup=}", "SKSearchGroupGetTypeID", None),
    ("SKSearchRef", b"^{__SKSearch=}", "SKSearchGetTypeID", None),
    ("SKSearchResultsRef", b"^{__SKSearchResults=}", "SKSearchResultsGetTypeID", None),
    ("SKSummaryRef", b"^{__SKSummary=}", "SKSummaryGetTypeID", None),
    ("SKDocumentRef", b"@", "SKDocumentGetTypeID", None),
]
expressions = {}

# END OF FILE
