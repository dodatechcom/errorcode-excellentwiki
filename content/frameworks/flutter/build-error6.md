---
title: "Flutter build error"
description: "Flutter build fails during compilation, linking, or resource processing"
frameworks: ["flutter"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when the Flutter build process fails, typically during Gradle (Android) or Xcode (iOS) compilation. This may be caused by dependency conflicts, missing SDK components, or plugin incompatibilities.

## Common Causes

- Plugin version incompatibility with current Flutter SDK
- Gradle or Xcode project configuration issues
- Missing Android SDK build tools or iOS deployment target
- Outdated `pubspec.lock` with conflicting dependencies

## How to Fix

1. Run flutter doctor to diagnose issues:

```bash
flutter doctor -v
```

2. Clean and rebuild:

```bash
flutter clean
flutter pub get
flutter build apk --debug
```

3. Update Flutter and Dart SDK:

```bash
flutter upgrade
flutter pub upgrade
```

4. Fix Android Gradle issues:

```gradle
// android/app/build.gradle
android {
    compileSdkVersion 34
    defaultConfig {
        minSdkVersion 21
        targetSdkVersion 34
    }
}
```

## Examples

```text
 FAILURE: Build failed with an exception.
 * What went wrong:
 Execution failed for task ':app:compileFlutterBuildDebug'.
 > Could not determine the dependencies of task ':app:compileFlutterBuildDebug'.
```

```text
Error: Gradle task assembleDebug failed with exit code 1
```

## Related Errors

- [setState after dispose]({{< relref "/frameworks/flutter/widget-error" >}})
