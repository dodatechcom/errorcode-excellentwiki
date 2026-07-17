---
title: "Flutter build - Gradle build error"
description: "Flutter Android build fails with Gradle build errors caused by configuration issues or dependency conflicts"
frameworks: ["flutter"]
error-types: ["build-error"]
severities: ["error"]
tags: ["flutter", "gradle", "android", "build", "dependency", "kotlin"]
weight: 5
---

A Flutter Gradle build error occurs when the Android build system fails to compile your app. This is one of the most common issues when building Flutter apps for Android and can be caused by Gradle version conflicts, dependency issues, or SDK configuration problems.

## Common Causes

- Gradle version incompatible with Flutter SDK
- Android SDK or build tools version mismatch
- Kotlin or Java version conflicts between dependencies
- Gradle daemon cache corruption
- Missing Android license agreements

## How to Fix

1. Clean the Flutter build and Gradle cache:

```bash
flutter clean
cd android && ./gradlew clean
cd ..
flutter pub get
```

2. Check Flutter doctor for Android SDK issues:

```bash
flutter doctor -v
```

3. Update Gradle wrapper in `android/gradle/wrapper/gradle-wrapper.properties`:

```properties
distributionUrl=https\://services.gradle.org/distributions/gradle-8.3-all.zip
```

4. Align Kotlin version in `android/build.gradle`:

```gradle
buildscript {
  ext.kotlin_version = '1.9.0'
  dependencies {
    classpath 'com.android.tools.build:gradle:8.1.0'
    classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:$kotlin_version"
  }
}
```

5. Accept all Android licenses:

```bash
flutter doctor --android-licenses
```

6. Run the build with stack trace for debugging:

```bash
cd android && ./gradlew assembleDebug --stacktrace
```

## Examples

```bash
$ flutter build apk
Running Gradle task 'assembleRelease'...
FAILURE: Build failed with an exception.
* What went wrong:
Could not determine the dependencies of task ':app:compileReleaseJavaWithJavac'.
> Could not resolve all dependencies for configuration ':app:releaseRuntimeClasspath'.
```

```bash
# Fix: update Gradle and rebuild
cd android
sed -i 's/gradle-7.5/gradle-8.3/' gradle/wrapper/gradle-wrapper.properties
./gradlew clean
cd ..
flutter build apk
```

## Related Errors

- [iOS build error]({{< relref "/frameworks/flutter/ios-build-error" >}})
- [Pub error]({{< relref "/frameworks/flutter/flutter-pub-error-v2" >}})
