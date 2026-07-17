---
title: "React Native build error"
description: "React Native build fails due to native code compilation errors, Gradle failures, or Xcode issues"
frameworks: ["react-native"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when the native build process (Gradle for Android, Xcode for iOS) fails during `react-native run-android` or `react-native run-ios`.

## Common Causes

- Missing Android SDK, NDK, or Xcode command line tools
- Native module incompatibility with the current RN version
- Gradle cache corruption
- CocoaPods not installed or pods not synced
- `minSdkVersion` mismatch between modules

## How to Fix

1. Clean and rebuild:

```bash
# Android
cd android && ./gradlew clean && cd ..
npx react-native run-android

# iOS
cd ios && xcodebuild clean && cd ..
cd ios && pod install
npx react-native run-ios
```

2. Check environment setup:

```bash
npx react-native doctor
```

3. Fix Gradle issues:

```bash
# Check Java version
java -version

# Fix Gradle wrapper
cd android && ./gradlew wrapper --gradle-version 8.0
```

4. Reset CocoaPods for iOS:

```bash
cd ios
pod deintegrate
pod install
cd ..
```

## Examples

```bash
# Build error — missing Android SDK
> Could not determine the dependencies of task ':app:compileDebugJavaWithJavac'.
> SDK location not found. Define location with sdk.dir in the local.properties file.
```

## Related Errors

- [Bundler error]({{< relref "/frameworks/react-native/bundler-error" >}})
- [Linking error]({{< relref "/frameworks/react-native/linking-error" >}})
