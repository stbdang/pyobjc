# This file is generated by objective.metadata
#
# Last update: Wed May 16 14:56:36 2012

import objc, sys

if sys.maxint > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
constants = '''$IMAVManagerStateChangedNotification$IMAVManagerURLToShareChangedNotification$IMCapabilityAudioConference$IMCapabilityDirectIM$IMCapabilityFileSharing$IMCapabilityFileTransfer$IMCapabilityText$IMCapabilityVideoConference$IMMyStatusChangedNotification$IMPersonAVBusyKey$IMPersonCapabilitiesKey$IMPersonEmailKey$IMPersonFirstNameKey$IMPersonIdleSinceKey$IMPersonInfoChangedNotification$IMPersonLastNameKey$IMPersonPictureDataKey$IMPersonScreenNameKey$IMPersonServiceNameKey$IMPersonStatusChangedNotification$IMPersonStatusKey$IMPersonStatusMessageKey$IMServiceStatusChangedNotification$IMStatusImagesChangedAppearanceNotification$'''
enums = '''$IMAVInactive@0$IMAVPending@4$IMAVRequested@1$IMAVRunning@5$IMAVShuttingDown@2$IMAVStartingUp@3$IMPersonStatusAvailable@4$IMPersonStatusAway@3$IMPersonStatusIdle@2$IMPersonStatusNoStatus@5$IMPersonStatusOffline@1$IMPersonStatusUnknown@0$IMServiceStatusDisconnected@1$IMServiceStatusLoggedIn@4$IMServiceStatusLoggedOut@0$IMServiceStatusLoggingIn@3$IMServiceStatusLoggingOut@2$IMVideoOptimizationDefault@0$IMVideoOptimizationReplacement@2$IMVideoOptimizationStills@1$'''
misc.update({})
functions={'IMComparePersonStatus': (sel32or64(b'iII', b'lLL'),)}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r('IMAVControl', b'isEnabled', {'retval': {'type': b'Z'}})
    r('IMAVControl', b'setEnabled:', {'arguments': {2: {'type': b'Z'}}})
    r('NSObject', b'getOpenGLBufferContext:pixelFormat:', {'arguments': {2: {'type_modifier': b'o'}, 3: {'type_modifier': b'o'}}})
    r('NSObject', b'getPixelBufferPixelFormat:', {'arguments': {2: {'type_modifier': b'o'}}})
    r('NSObject', b'renderIntoOpenGLBuffer:onScreen:forTime:', {'retval': {'type': 'Z'}, 'arguments': {2: {'type': '^{__CVBuffer=}'}, 3: {'type_modifier': b'n'}, 4: {'type': sel32or64(b'^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssLLLssss}QQ}', b'^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}'), 'type_modifier': b'n'}}})
    r('NSObject', b'renderIntoPixelBuffer:forTime:', {'retval': {'type': 'Z'}, 'arguments': {2: {'type': '^{__CVBuffer=}'}, 3: {'type': sel32or64(b'^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssLLLssss}QQ}', b'^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}'), 'type_modifier': b'n'}}})
finally:
    objc._updatingMetadata(False)
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r('NSObject', b'getOpenGLBufferContext:pixelFormat:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'^^{_CGLContextObject=}', 'type_modifier': b'o'}, 3: {'type': b'^^{_CGLPixelFormatObject=}', 'type_modifier': b'o'}}})
    r('NSObject', b'getPixelBufferPixelFormat:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'^I', 'type_modifier': b'o'}}})
    r('NSObject', b'renderIntoOpenGLBuffer:onScreen:forTime:', {'retval': {'type': 'Z'}, 'arguments': {2: {'type': '^{__CVBuffer=}'}, 3: {'type': b'^i', 'type_modifier': b'n'}, 4: {'type': sel32or64(b'^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssLLLssss}QQ}', b'^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}'), 'type_modifier': b'n'}}})
    r('NSObject', b'renderIntoPixelBuffer:forTime:', {'retval': {'type': 'Z'}, 'arguments': {2: {'type': '^{__CVBuffer=}'}, 3: {'type': sel32or64(b'^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssLLLssss}QQ}', b'^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}'), 'type_modifier': b'n'}}})
finally:
    objc._updatingMetadata(False)
protocols={'IMVideoDataSource': objc.informal_protocol('IMVideoDataSource', [objc.selector(None, 'renderIntoPixelBuffer:forTime:', sel32or64(b'Z@:^{__CVBuffer=}^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssLLLssss}QQ}', b'Z@:^{__CVBuffer=}^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}'), isRequired=False), objc.selector(None, 'getPixelBufferPixelFormat:', b'v@:^I', isRequired=False), objc.selector(None, 'getOpenGLBufferContext:pixelFormat:', b'v@:^^{_CGLContextObject=}^^{_CGLPixelFormatObject=}', isRequired=False), objc.selector(None, 'renderIntoOpenGLBuffer:onScreen:forTime:', sel32or64(b'Z@:^{__CVBuffer=}^i^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssLLLssss}QQ}', b'Z@:^{__CVBuffer=}^i^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}'), isRequired=False)])}
expressions = {}

# END OF FILE
