---
title: "[Solution] React Native Native Event Emitter Not Receiving Events"
description: "react-native NativeEventEmitter fails to receive events from native modules on Android and iOS, causing JavaScript listeners to never fire"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The native event emitter error occurs when the native module emits events that never reach the JavaScript listener. This typically happens because the event emitter is not correctly initialized, the event name is mismatched, or the emitter is deallocated before the event fires.

## Common Causes

- NativeEventEmitter created but the module does not support event emission
- Event name mistyped in native code (case-sensitive)
- native module is null or undefined when NativeEventEmitter is constructed
- Only one listener subscription is active but multiple are needed
- Native side sends events before the JS listener is registered
- iOS native module does not conform to RCTEventEmitter protocol

## How to Fix

1. Verify the native module has a supportedEvents method:

```objectivec
// iOS: MyModule.m
#import <React/RCTEventEmitter.h>
@interface MyModule : RCTEventEmitter <RCTBridgeModule>
@end

@implementation MyModule
RCT_EXPORT_MODULE();

- (NSArray<NSString *> *)supportedEvents {
  return @[@"onProgress"];
}
@end
```

2. Subscribe correctly in JS:

```javascript
import { NativeEventEmitter, NativeModules } from 'react-native';

const { MyModule } = NativeModules;
const eventEmitter = new NativeEventEmitter(MyModule);

useEffect(() => {
  const sub = eventEmitter.addListener('onProgress', handleProgress);
  return () => sub.remove();
}, []);
```

## Examples

```javascript
// Error: no listeners for event "onProgress"
// Fix: ensure the native module implements supportedEvents
if (!MyModule) {
  console.warn('Module not available');
}
```

## Related Errors

- [Native Bridge Error]({{< relref "/frameworks/react-native/rn-bridge-error" >}})
