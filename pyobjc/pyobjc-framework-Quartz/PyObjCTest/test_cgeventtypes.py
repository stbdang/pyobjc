
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGEventTypes (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CGEventRef)
        self.failUnlessIsCFType(CGEventSourceRef)

    def testConstants(self):
        self.failUnlessEqual(kCGMouseButtonLeft, 0)
        self.failUnlessEqual(kCGMouseButtonRight, 1)
        self.failUnlessEqual(kCGMouseButtonCenter, 2)
        self.failUnlessEqual(kCGScrollEventUnitPixel, 0)
        self.failUnlessEqual(kCGScrollEventUnitLine, 1)
        self.failUnlessEqual(kCGEventFlagMaskAlphaShift, 0x00010000)
        self.failUnlessEqual(kCGEventFlagMaskShift, 0x00020000)
        self.failUnlessEqual(kCGEventFlagMaskControl, 0x00040000)
        self.failUnlessEqual(kCGEventFlagMaskAlternate, 0x00080000)
        self.failUnlessEqual(kCGEventFlagMaskCommand, 0x00100000)
        self.failUnlessEqual(kCGEventFlagMaskHelp, 0x00400000)
        self.failUnlessEqual(kCGEventFlagMaskSecondaryFn, 0x00800000)
        self.failUnlessEqual(kCGEventFlagMaskNumericPad, 0x00200000)
        self.failUnlessEqual(kCGEventFlagMaskNonCoalesced, 0x00000100)
        self.failUnlessEqual(kCGEventNull, 0)
        self.failUnlessEqual(kCGEventLeftMouseDown, 1)
        self.failUnlessEqual(kCGEventLeftMouseUp, 2)
        self.failUnlessEqual(kCGEventRightMouseDown, 3)
        self.failUnlessEqual(kCGEventRightMouseUp, 4)
        self.failUnlessEqual(kCGEventMouseMoved, 5)
        self.failUnlessEqual(kCGEventLeftMouseDragged, 6)
        self.failUnlessEqual(kCGEventRightMouseDragged, 7)
        self.failUnlessEqual(kCGEventKeyDown, 10)
        self.failUnlessEqual(kCGEventKeyUp, 11)
        self.failUnlessEqual(kCGEventFlagsChanged, 12)
        self.failUnlessEqual(kCGEventScrollWheel, 22)
        self.failUnlessEqual(kCGEventTabletPointer, 23)
        self.failUnlessEqual(kCGEventTabletProximity, 24)
        self.failUnlessEqual(kCGEventOtherMouseDown, 25)
        self.failUnlessEqual(kCGEventOtherMouseUp, 26)
        self.failUnlessEqual(kCGEventOtherMouseDragged, 27)
        self.failUnlessEqual(kCGEventTapDisabledByTimeout, cast_int(0xFFFFFFFE))
        self.failUnlessEqual(kCGEventTapDisabledByUserInput, cast_int(0xFFFFFFFF))
        self.failUnlessEqual(kCGMouseEventNumber, 0)
        self.failUnlessEqual(kCGMouseEventClickState, 1)
        self.failUnlessEqual(kCGMouseEventPressure, 2)
        self.failUnlessEqual(kCGMouseEventButtonNumber, 3)
        self.failUnlessEqual(kCGMouseEventDeltaX, 4)
        self.failUnlessEqual(kCGMouseEventDeltaY, 5)
        self.failUnlessEqual(kCGMouseEventInstantMouser, 6)
        self.failUnlessEqual(kCGMouseEventSubtype, 7)
        self.failUnlessEqual(kCGKeyboardEventKeycode, 9)
        self.failUnlessEqual(kCGKeyboardEventKeyboardType, 10)
        self.failUnlessEqual(kCGScrollWheelEventDeltaAxis1, 11)
        self.failUnlessEqual(kCGScrollWheelEventDeltaAxis2, 12)
        self.failUnlessEqual(kCGScrollWheelEventDeltaAxis3, 13)
        self.failUnlessEqual(kCGScrollWheelEventFixedPtDeltaAxis1, 93)
        self.failUnlessEqual(kCGScrollWheelEventFixedPtDeltaAxis2, 94)
        self.failUnlessEqual(kCGScrollWheelEventFixedPtDeltaAxis3, 95)
        self.failUnlessEqual(kCGScrollWheelEventPointDeltaAxis1, 96)
        self.failUnlessEqual(kCGScrollWheelEventPointDeltaAxis2, 97)
        self.failUnlessEqual(kCGScrollWheelEventPointDeltaAxis3, 98)
        self.failUnlessEqual(kCGScrollWheelEventInstantMouser, 14)
        self.failUnlessEqual(kCGTabletEventPointX, 15)
        self.failUnlessEqual(kCGTabletEventPointY, 16)
        self.failUnlessEqual(kCGTabletEventPointZ, 17)
        self.failUnlessEqual(kCGTabletEventPointButtons, 18)
        self.failUnlessEqual(kCGTabletEventPointPressure, 19)
        self.failUnlessEqual(kCGTabletEventTiltX, 20)
        self.failUnlessEqual(kCGTabletEventTiltY, 21)
        self.failUnlessEqual(kCGTabletEventRotation, 22)
        self.failUnlessEqual(kCGTabletEventTangentialPressure, 23)
        self.failUnlessEqual(kCGTabletEventDeviceID, 24)
        self.failUnlessEqual(kCGTabletEventVendor1, 25)
        self.failUnlessEqual(kCGTabletEventVendor2, 26)
        self.failUnlessEqual(kCGTabletEventVendor3, 27)
        self.failUnlessEqual(kCGTabletProximityEventVendorID, 28)
        self.failUnlessEqual(kCGTabletProximityEventTabletID, 29)
        self.failUnlessEqual(kCGTabletProximityEventPointerID, 30)
        self.failUnlessEqual(kCGTabletProximityEventDeviceID, 31)
        self.failUnlessEqual(kCGTabletProximityEventSystemTabletID, 32)
        self.failUnlessEqual(kCGTabletProximityEventVendorPointerType, 33)
        self.failUnlessEqual(kCGTabletProximityEventVendorPointerSerialNumber, 34)
        self.failUnlessEqual(kCGTabletProximityEventVendorUniqueID, 35)
        self.failUnlessEqual(kCGTabletProximityEventCapabilityMask, 36)
        self.failUnlessEqual(kCGTabletProximityEventPointerType, 37)
        self.failUnlessEqual(kCGTabletProximityEventEnterProximity, 38)
        self.failUnlessEqual(kCGEventTargetProcessSerialNumber, 39)
        self.failUnlessEqual(kCGEventTargetUnixProcessID, 40)
        self.failUnlessEqual(kCGEventSourceUnixProcessID, 41)
        self.failUnlessEqual(kCGEventSourceUserData, 42)
        self.failUnlessEqual(kCGEventSourceUserID, 43)
        self.failUnlessEqual(kCGEventSourceGroupID, 44)
        self.failUnlessEqual(kCGEventSourceStateID, 45)
        self.failUnlessEqual(kCGScrollWheelEventIsContinuous, 88)
        self.failUnlessEqual(kCGEventMouseSubtypeDefault, 0)
        self.failUnlessEqual(kCGEventMouseSubtypeTabletPoint, 1)
        self.failUnlessEqual(kCGEventMouseSubtypeTabletProximity, 2)
        self.failUnlessEqual(kCGHIDEventTap, 0)
        self.failUnlessEqual(kCGSessionEventTap, 1)
        self.failUnlessEqual(kCGAnnotatedSessionEventTap, 2)
        self.failUnlessEqual(kCGHeadInsertEventTap, 0)
        self.failUnlessEqual(kCGTailAppendEventTap, 1)
        self.failUnlessEqual(kCGEventTapOptionDefault, 0x00000000)
        self.failUnlessEqual(kCGEventTapOptionListenOnly, 0x00000001)

        self.failUnlessEqual(kCGNotifyEventTapAdded, "com.apple.coregraphics.eventTapAdded")
        self.failUnlessEqual(kCGNotifyEventTapRemoved, "com.apple.coregraphics.eventTapRemoved")

        self.failUnlessEqual(kCGEventSourceStatePrivate, -1)
        self.failUnlessEqual(kCGEventSourceStateCombinedSessionState, 0)
        self.failUnlessEqual(kCGEventSourceStateHIDSystemState, 1)
        self.failUnlessEqual(kCGAnyInputEventType, 0xffffffff)

    def testStructs(self):
        v = CGEventTapInformation()
        self.failUnless(hasattr(v, 'eventTapID'))
        self.failUnless(hasattr(v, 'tapPoint'))
        self.failUnless(hasattr(v, 'options'))
        self.failUnless(hasattr(v, 'eventsOfInterest'))
        self.failUnless(hasattr(v, 'tappingProcess'))
        self.failUnless(hasattr(v, 'processBeingTapped'))
        self.failUnless(hasattr(v, 'enabled'))
        self.failUnless(hasattr(v, 'minUsecLatency'))
        self.failUnless(hasattr(v, 'avgUsecLatency'))
        self.failUnless(hasattr(v, 'maxUsecLatency'))

    def testMissing(self):
        self.fail("CGEventMaskBit")


if __name__ == "__main__":
    main()