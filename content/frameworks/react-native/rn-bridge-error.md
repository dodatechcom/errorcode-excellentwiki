---
title: "Native Bridge - module method error"
description: "React Native bridge fails to invoke a native module method, causing method not found or argument mismatch errors"
frameworks: ["react-native"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

The Native Bridge module method error occurs when JavaScript tries to call a method on a native module that does not exist, has incorrect arguments, or was not properly registered. This is a common issue when bridging between JS and native code.

## Common Causes

- Method name mismatch between JS and native code
- Wrong number of arguments passed to the native method
- Native module not registered in the app's module registry
- Method exposed only to iOS but called on Android (or vice versa)
- Native module method signature changed without updating JS

## How to Fix

1. Verify method names match exactly between JS and native:

```objc
// iOS: MyModule.m
RCT_EXPORT_METHOD(getData:(NSString *)key
                  resolver:(RCTPromiseResolveBlock)resolve
                  rejecter:(RCTPromiseRejectBlock)reject)
```

```javascript
// JS: must match exactly
NativeModules.MyModule.getData('key');
```

2. Check argument types match the native implementation:

```javascript
// If native expects NSString, pass string not number
NativeModules.MyModule.saveData(String(id), String(value));
```

3. Ensure the module is registered:

```objc
// iOS: MyModule.m
@implementation MyModule

RCT_EXPORT_MODULE()

// ...
@end
```

```java
// Android: MyModule.java
@Override
public Map<String, Object> getConstants() {
  return Map.of("METHOD_NAME", "value");
}
```

4. Add null checks for native module availability:

```javascript
import { NativeModules } from 'react-native';

const { MyModule } = NativeModules;

if (MyModule) {
  MyModule.getData('key');
} else {
  console.warn('Native module not available on this platform');
}
```

## Examples

```javascript
// Error: NativeModule'Camera' method 'takePhoto' was not found
NativeModules.Camera.takePhoto();
// Camera module exists but method is named 'capturePhoto'

// Fix: use correct method name
NativeModules.Camera.capturePhoto();
```

## Related Errors

- [Linking error]({{< relref "/frameworks/react-native/rn-linking-error" >}})
- [RedBox error]({{< relref "/frameworks/react-native/rn-redbox-error-v2" >}})
