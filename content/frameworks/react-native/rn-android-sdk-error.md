---
title: "Android SDK - not found error"
description: "React Native build fails because the Android SDK is not installed or ANDROID_HOME is not configured"
frameworks: ["react-native"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

The Android SDK not found error occurs when React Native cannot locate the Android SDK during the build process. This is typically caused by a missing SDK installation or incorrect environment variables.

## Common Causes

- `ANDROID_HOME` or `ANDROID_SDK_ROOT` not set in environment
- Android SDK not installed on the system
- Required build tools or platform versions not installed
- SDK path contains spaces or special characters
- Multiple SDK versions causing path conflicts

## How to Fix

1. Set `ANDROID_HOME` in your shell configuration:

```bash
# ~/.bashrc or ~/.zshrc
export ANDROID_HOME=$HOME/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/emulator
export PATH=$PATH:$ANDROID_HOME/platform-tools
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/tools/bin
```

2. Install required SDK components:

```bash
sdkmanager "platform-tools" "platforms;android-34" "build-tools;34.0.0"
```

3. Verify the SDK is properly installed:

```bash
echo $ANDROID_HOME
ls $ANDROID_HOME/platforms
sdkmanager --list
```

4. Update `local.properties` with the correct SDK path:

```properties
# android/local.properties
sdk.dir=/Users/yourname/Library/Android/sdk
```

5. Check with `flutter doctor -v` or React Native setup:

```bash
npx react-native doctor
```

## Examples

```bash
$ npx react-native run-android
error: SDK location not found. Define location with ANDROID_SDK_ROOT env variable or sdk.dir path in local.properties.
```

```bash
# Fix: set SDK path
echo "sdk.dir=$HOME/Library/Android/sdk" > android/local.properties
```

## Related Errors

- [Build error]({{< relref "/frameworks/react-native/rn-build-error-v2" >}})
- [CocoaPods error]({{< relref "/frameworks/react-native/rn-ios-cocoapods-error" >}})
