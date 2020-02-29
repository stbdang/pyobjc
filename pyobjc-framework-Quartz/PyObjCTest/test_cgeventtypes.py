import sys

from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *


class TestCGEventTypes(TestCase):
    def testTypes(self):
        self.assertIsCFType(CGEventRef)
        self.assertIsCFType(CGEventSourceRef)

    def testConstants(self):
        self.assertEqual(kCGMomentumScrollPhaseNone, 0)
        self.assertEqual(kCGMomentumScrollPhaseBegin, 1)
        self.assertEqual(kCGMomentumScrollPhaseContinue, 2)
        self.assertEqual(kCGMomentumScrollPhaseEnd, 3)

        self.assertEqual(kCGScrollPhaseBegan, 1)
        self.assertEqual(kCGScrollPhaseChanged, 2)
        self.assertEqual(kCGScrollPhaseEnded, 4)
        self.assertEqual(kCGScrollPhaseCancelled, 8)
        self.assertEqual(kCGScrollPhaseMayBegin, 128)

        self.assertEqual(kCGGesturePhaseNone, 0)
        self.assertEqual(kCGGesturePhaseBegan, 1)
        self.assertEqual(kCGGesturePhaseChanged, 2)
        self.assertEqual(kCGGesturePhaseEnded, 4)
        self.assertEqual(kCGGesturePhaseCancelled, 8)
        self.assertEqual(kCGGesturePhaseMayBegin, 128)

        self.assertEqual(kCGMouseButtonLeft, 0)
        self.assertEqual(kCGMouseButtonRight, 1)
        self.assertEqual(kCGMouseButtonCenter, 2)

        self.assertEqual(kCGScrollEventUnitPixel, 0)
        self.assertEqual(kCGScrollEventUnitLine, 1)

        self.assertEqual(kCGEventFlagMaskAlphaShift, 0x00010000)
        self.assertEqual(kCGEventFlagMaskShift, 0x00020000)
        self.assertEqual(kCGEventFlagMaskControl, 0x00040000)
        self.assertEqual(kCGEventFlagMaskAlternate, 0x00080000)
        self.assertEqual(kCGEventFlagMaskCommand, 0x00100000)
        self.assertEqual(kCGEventFlagMaskHelp, 0x00400000)
        self.assertEqual(kCGEventFlagMaskSecondaryFn, 0x00800000)
        self.assertEqual(kCGEventFlagMaskNumericPad, 0x00200000)
        self.assertEqual(kCGEventFlagMaskNonCoalesced, 0x00000100)

        self.assertEqual(kCGEventNull, 0)
        self.assertEqual(kCGEventLeftMouseDown, 1)
        self.assertEqual(kCGEventLeftMouseUp, 2)
        self.assertEqual(kCGEventRightMouseDown, 3)
        self.assertEqual(kCGEventRightMouseUp, 4)
        self.assertEqual(kCGEventMouseMoved, 5)
        self.assertEqual(kCGEventLeftMouseDragged, 6)
        self.assertEqual(kCGEventRightMouseDragged, 7)
        self.assertEqual(kCGEventKeyDown, 10)
        self.assertEqual(kCGEventKeyUp, 11)
        self.assertEqual(kCGEventFlagsChanged, 12)
        self.assertEqual(kCGEventScrollWheel, 22)
        self.assertEqual(kCGEventTabletPointer, 23)
        self.assertEqual(kCGEventTabletProximity, 24)
        self.assertEqual(kCGEventOtherMouseDown, 25)
        self.assertEqual(kCGEventOtherMouseUp, 26)
        self.assertEqual(kCGEventOtherMouseDragged, 27)
        self.assertEqual(kCGEventTapDisabledByTimeout, 0xFFFFFFFE)
        self.assertEqual(kCGEventTapDisabledByUserInput, 0xFFFFFFFF)

        self.assertEqual(kCGMouseEventNumber, 0)
        self.assertEqual(kCGMouseEventClickState, 1)
        self.assertEqual(kCGMouseEventPressure, 2)
        self.assertEqual(kCGMouseEventButtonNumber, 3)
        self.assertEqual(kCGMouseEventDeltaX, 4)
        self.assertEqual(kCGMouseEventDeltaY, 5)
        self.assertEqual(kCGMouseEventInstantMouser, 6)
        self.assertEqual(kCGMouseEventSubtype, 7)
        self.assertEqual(kCGKeyboardEventAutorepeat, 8)
        self.assertEqual(kCGKeyboardEventKeycode, 9)
        self.assertEqual(kCGKeyboardEventKeyboardType, 10)
        self.assertEqual(kCGScrollWheelEventDeltaAxis1, 11)
        self.assertEqual(kCGScrollWheelEventDeltaAxis2, 12)
        self.assertEqual(kCGScrollWheelEventDeltaAxis3, 13)
        self.assertEqual(kCGScrollWheelEventFixedPtDeltaAxis1, 93)
        self.assertEqual(kCGScrollWheelEventFixedPtDeltaAxis2, 94)
        self.assertEqual(kCGScrollWheelEventFixedPtDeltaAxis3, 95)
        self.assertEqual(kCGScrollWheelEventPointDeltaAxis1, 96)
        self.assertEqual(kCGScrollWheelEventPointDeltaAxis2, 97)
        self.assertEqual(kCGScrollWheelEventPointDeltaAxis3, 98)
        self.assertEqual(kCGScrollWheelEventScrollPhase, 99)
        self.assertEqual(kCGScrollWheelEventScrollCount, 100)
        self.assertEqual(kCGScrollWheelEventMomentumPhase, 123)
        self.assertEqual(kCGScrollWheelEventInstantMouser, 14)
        self.assertEqual(kCGTabletEventPointX, 15)
        self.assertEqual(kCGTabletEventPointY, 16)
        self.assertEqual(kCGTabletEventPointZ, 17)
        self.assertEqual(kCGTabletEventPointButtons, 18)
        self.assertEqual(kCGTabletEventPointPressure, 19)
        self.assertEqual(kCGTabletEventTiltX, 20)
        self.assertEqual(kCGTabletEventTiltY, 21)
        self.assertEqual(kCGTabletEventRotation, 22)
        self.assertEqual(kCGTabletEventTangentialPressure, 23)
        self.assertEqual(kCGTabletEventDeviceID, 24)
        self.assertEqual(kCGTabletEventVendor1, 25)
        self.assertEqual(kCGTabletEventVendor2, 26)
        self.assertEqual(kCGTabletEventVendor3, 27)
        self.assertEqual(kCGTabletProximityEventVendorID, 28)
        self.assertEqual(kCGTabletProximityEventTabletID, 29)
        self.assertEqual(kCGTabletProximityEventPointerID, 30)
        self.assertEqual(kCGTabletProximityEventDeviceID, 31)
        self.assertEqual(kCGTabletProximityEventSystemTabletID, 32)
        self.assertEqual(kCGTabletProximityEventVendorPointerType, 33)
        self.assertEqual(kCGTabletProximityEventVendorPointerSerialNumber, 34)
        self.assertEqual(kCGTabletProximityEventVendorUniqueID, 35)
        self.assertEqual(kCGTabletProximityEventCapabilityMask, 36)
        self.assertEqual(kCGTabletProximityEventPointerType, 37)
        self.assertEqual(kCGTabletProximityEventEnterProximity, 38)
        self.assertEqual(kCGEventTargetProcessSerialNumber, 39)
        self.assertEqual(kCGEventTargetUnixProcessID, 40)
        self.assertEqual(kCGEventSourceUnixProcessID, 41)
        self.assertEqual(kCGEventSourceUserData, 42)
        self.assertEqual(kCGEventSourceUserID, 43)
        self.assertEqual(kCGEventSourceGroupID, 44)
        self.assertEqual(kCGEventSourceStateID, 45)
        self.assertEqual(kCGScrollWheelEventIsContinuous, 88)
        self.assertEqual(kCGMouseEventWindowUnderMousePointer, 91)
        self.assertEqual(kCGMouseEventWindowUnderMousePointerThatCanHandleThisEvent, 92)
        self.assertEqual(kCGEventUnacceleratedPointerMovementX, 170)
        self.assertEqual(kCGEventUnacceleratedPointerMovementY, 171)

        self.assertEqual(kCGEventMouseSubtypeDefault, 0)
        self.assertEqual(kCGEventMouseSubtypeTabletPoint, 1)
        self.assertEqual(kCGEventMouseSubtypeTabletProximity, 2)

        self.assertEqual(kCGHIDEventTap, 0)
        self.assertEqual(kCGSessionEventTap, 1)
        self.assertEqual(kCGAnnotatedSessionEventTap, 2)

        self.assertEqual(kCGHeadInsertEventTap, 0)
        self.assertEqual(kCGTailAppendEventTap, 1)

        self.assertEqual(kCGEventTapOptionDefault, 0x00000000)
        self.assertEqual(kCGEventTapOptionListenOnly, 0x00000001)

        self.assertEqual(
            kCGNotifyEventTapAdded, b"com.apple.coregraphics.eventTapAdded"
        )
        self.assertEqual(
            kCGNotifyEventTapRemoved, b"com.apple.coregraphics.eventTapRemoved"
        )

        self.assertEqual(kCGEventSourceStatePrivate, -1)
        self.assertEqual(kCGEventSourceStateCombinedSessionState, 0)
        self.assertEqual(kCGEventSourceStateHIDSystemState, 1)

        self.assertEqual(kCGAnyInputEventType, 0xFFFFFFFF)
        if sys.maxsize > 2 ** 32:
            self.assertEqual(kCGEventMaskForAllEvents, 0xFFFFFFFFFFFFFFFF)
        else:
            self.assertEqual(kCGEventMaskForAllEvents, 0xFFFFFFFF)

    def testStructs(self):
        v = CGEventTapInformation()
        self.assertTrue(hasattr(v, "eventTapID"))
        self.assertTrue(hasattr(v, "tapPoint"))
        self.assertTrue(hasattr(v, "options"))
        self.assertTrue(hasattr(v, "eventsOfInterest"))
        self.assertTrue(hasattr(v, "tappingProcess"))
        self.assertTrue(hasattr(v, "processBeingTapped"))
        self.assertTrue(hasattr(v, "enabled"))
        self.assertTrue(hasattr(v, "minUsecLatency"))
        self.assertTrue(hasattr(v, "avgUsecLatency"))
        self.assertTrue(hasattr(v, "maxUsecLatency"))

    def testInline(self):
        self.assertEqual(CGEventMaskBit(10), 1 << 10)


if __name__ == "__main__":
    main()
