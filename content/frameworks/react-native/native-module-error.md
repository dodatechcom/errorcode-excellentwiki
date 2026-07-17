---
title: "NativeModule: X is null"
description: "React Native throws this error when a native module is not properly linked or initialized"
frameworks: ["react-native"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The "NativeModule: X is null" error indicates that a native module you are trying to use has not been properly linked to your React Native project. The JavaScript bridge cannot communicate with the native code.

## Common Causes

- Native module not linked after installation
- Missing native dependency in iOS Podfile or Android build.gradle
- Running on a device without rebuilding native code
- Module requires manual linking steps

## How to Fix

**Reinstall pods (iOS):**

```bash
cd ios && pod install && cd ..
```

**Run react-native link (for older projects):**

```bash
npx react-native link
```

**Rebuild the native code:**

```bash
npx react-native run-ios
# or
npx react-native run-android
```

## Examples

```javascript
// This error occurs when calling native methods:
import { NativeModules } from 'react-native';

// If MyNativeModule is not linked, this throws "NativeModule is null"
const { MyNativeModule } = NativeModules;
MyNativeModule.doSomething();
```

## Related Errors

- [Red Box Error]({{< relref "/frameworks/react-native/red-box-error" >}})
