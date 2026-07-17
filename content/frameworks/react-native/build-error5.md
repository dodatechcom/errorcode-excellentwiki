---
title: "Gradle/Xcode build error"
description: "React Native project fails to compile due to native build tool errors on Android or iOS"
frameworks: ["react-native"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when the native build process fails during Android Gradle build or Xcode compilation. This typically happens after installing a new native module or upgrading React Native.

## Common Causes

- Gradle cache corruption or version mismatch
- Xcode derived data needs cleaning
- Native module dependency conflicts
- Incompatible SDK versions between modules

## How to Fix

1. Clean Android build:

```bash
cd android
./gradlew clean
cd ..
npx react-native run-android
```

2. Clean iOS build:

```bash
cd ios
pod deintegrate
pod install
rm -rf ~/Library/Developer/Xcode/DerivedData
cd ..
npx react-native run-ios
```

3. Update podfile.lock (iOS):

```bash
cd ios
pod install --repo-update
cd ..
```

4. Fix dependency conflicts in Android:

```bash
cd android
./gradlew app:dependencies
# Check for version conflicts and update build.gradle
```

## Examples

```text
Execution failed for task ':app:compileDebugJavaWithJavac'.
> Compilation failed; see the compiler error output for details.
```

```text
error: ld: library not found for -lRNGestureHandler
clang: error: linker command failed with exit code 1
```

## Related Errors

- [Network request failed]({{< relref "/frameworks/react-native/network-error5" >}})
