import CoreServices
from PyObjCTools.TestSupport import *


class TestDateTimeUtils(TestCase):
    def assert_not_wrapped(self, name):
        self.assertTrue(
            not hasattr(CoreServices, name), "%r exposed in bindings" % (name,)
        )

    def test_not_wrapped(self):
        self.assert_not_wrapped("toggleUndefined")
        self.assert_not_wrapped("toggleOK")
        self.assert_not_wrapped("toggleBadField")
        self.assert_not_wrapped("toggleBadDelta")
        self.assert_not_wrapped("toggleBadChar")
        self.assert_not_wrapped("toggleUnknown")
        self.assert_not_wrapped("toggleBadNum")
        self.assert_not_wrapped("toggleOutOfRange")
        self.assert_not_wrapped("toggleErr3")
        self.assert_not_wrapped("toggleErr4")
        self.assert_not_wrapped("toggleErr5")
        self.assert_not_wrapped("smallDateBit")
        self.assert_not_wrapped("togChar12HourBit")
        self.assert_not_wrapped("togCharZCycleBit")
        self.assert_not_wrapped("togDelta12HourBit")
        self.assert_not_wrapped("genCdevRangeBit")
        self.assert_not_wrapped("validDateFields")
        self.assert_not_wrapped("maxDateField")
        self.assert_not_wrapped("eraMask")
        self.assert_not_wrapped("yearMask")
        self.assert_not_wrapped("monthMask")
        self.assert_not_wrapped("dayMask")
        self.assert_not_wrapped("hourMask")
        self.assert_not_wrapped("minuteMask")
        self.assert_not_wrapped("secondMask")
        self.assert_not_wrapped("dayOfWeekMask")
        self.assert_not_wrapped("dayOfYearMask")
        self.assert_not_wrapped("weekOfYearMask")
        self.assert_not_wrapped("pmMask")
        self.assert_not_wrapped("dateStdMask")
        self.assert_not_wrapped("eraField")
        self.assert_not_wrapped("yearField")
        self.assert_not_wrapped("monthField")
        self.assert_not_wrapped("dayField")
        self.assert_not_wrapped("hourField")
        self.assert_not_wrapped("minuteField")
        self.assert_not_wrapped("secondField")
        self.assert_not_wrapped("dayOfWeekField")
        self.assert_not_wrapped("dayOfYearField")
        self.assert_not_wrapped("weekOfYearField")
        self.assert_not_wrapped("pmField")
        self.assert_not_wrapped("res1Field")
        self.assert_not_wrapped("res2Field")
        self.assert_not_wrapped("res3Field")
        self.assert_not_wrapped("shortDate")
        self.assert_not_wrapped("longDate")
        self.assert_not_wrapped("abbrevDate")
        self.assert_not_wrapped("fatalDateTime")
        self.assert_not_wrapped("longDateFound")
        self.assert_not_wrapped("leftOverChars")
        self.assert_not_wrapped("sepNotIntlSep")
        self.assert_not_wrapped("fieldOrderNotIntl")
        self.assert_not_wrapped("extraneousStrings")
        self.assert_not_wrapped("tooManySeps")
        self.assert_not_wrapped("sepNotConsistent")
        self.assert_not_wrapped("tokenErr")
        self.assert_not_wrapped("cantReadUtilities")
        self.assert_not_wrapped("dateTimeNotFound")
        self.assert_not_wrapped("dateTimeInvalid")
        self.assert_not_wrapped("DateCacheRecord")
        self.assert_not_wrapped("DateTimeRec")
        self.assert_not_wrapped("LongDateCvt")
        self.assert_not_wrapped("LongDateRec")
        self.assert_not_wrapped("TogglePB")
        self.assert_not_wrapped("UCConvertUTCDateTimeToCFAbsoluteTime")
        self.assert_not_wrapped("UCConvertSecondsToCFAbsoluteTime")
        self.assert_not_wrapped("UCConvertLongDateTimeToCFAbsoluteTime")
        self.assert_not_wrapped("UCConvertCFAbsoluteTimeToUTCDateTime")
        self.assert_not_wrapped("UCConvertCFAbsoluteTimeToSeconds")
        self.assert_not_wrapped("UCConvertCFAbsoluteTimeToLongDateTime")
        self.assert_not_wrapped("DateString")
        self.assert_not_wrapped("TimeString")
        self.assert_not_wrapped("LongDateString")
        self.assert_not_wrapped("LongTimeString")
        self.assert_not_wrapped("InitDateCache")
        self.assert_not_wrapped("StringToDate")
        self.assert_not_wrapped("StringToTime")
        self.assert_not_wrapped("LongDateToSeconds")
        self.assert_not_wrapped("LongSecondsToDate")
        self.assert_not_wrapped("ToggleDate")
        self.assert_not_wrapped("ValidDate")
        self.assert_not_wrapped("ReadDateTime")
        self.assert_not_wrapped("GetDateTime")
        self.assert_not_wrapped("SetDateTime")
        self.assert_not_wrapped("SetTime")
        self.assert_not_wrapped("GetTime")
        self.assert_not_wrapped("DateToSeconds")
        self.assert_not_wrapped("SecondsToDate")
        self.assert_not_wrapped("DateString")
        self.assert_not_wrapped("TimeString")
        self.assert_not_wrapped("LongDateString")
        self.assert_not_wrapped("LongTimeString")
        self.assert_not_wrapped("String2Date")
        self.assert_not_wrapped("String2Time")
        self.assert_not_wrapped("LongDate2Secs")
        self.assert_not_wrapped("LongSecs2Date")
        self.assert_not_wrapped("Date2Secs")
        self.assert_not_wrapped("Secs2Date")


if __name__ == "__main__":
    main()
