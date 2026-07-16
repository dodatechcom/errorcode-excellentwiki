---
title: "Native module bridge error"
description: "React Native throws an error when the JS bridge cannot communicate with a native module"
frameworks: ["react-native"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["bridge", "native", "module", "communication", "jsi"]
weight: 5
---

This error occurs when the JavaScript bridge cannot establish communication with a native module on iOS or Android. The native code may not be linked, compiled, or the bridge may be in a broken state.

## Common Causes

- Native module not properly linked in the build
- Old bridge architecture incompatibility with new React Native versions
- Native module was removed but JS code still references it
- React Native version mismatch between JS and native code

## How to Fix

1. Rebuild the native project after installing native modules:

```bash
npx react-native run-ios
npx react-native run-android
```

2. Clean the build cache for iOS:

```bash
cd ios && rm -rf build Pods && pod install && cd ..
```

3. Clean Android build:

```bash
cd android && ./gradlew clean && cd ..
npx react-native run-android
```

4. Verify the module is properly linked:

```bash
# For older React Native
npx react-native link
```

## Examples

```javascript
import { NativeModules } from 'react-native';

const { MyNativeModule } = NativeModules;
MyNativeModule.init(); // Error: module is null or undefined
```

```text
TypeError: Cannot read property 'init' of undefined
NativeModule: MyNativeModule is null
```

## Related Errors

- [Red Box Error]({{< relref "/frameworks/react-native/red-box-error" >}})
