---
title: "Android build - Gradle error"
description: "Flutter Android build fails with Gradle errors due to configuration, dependency, or SDK issues"
frameworks: ["flutter"]
error-types: ["build-error"]
severities: ["error"]
tags: ["flutter", "android", "gradle", "build", "sdk", "kotlin"]
weight: 5
---

A Flutter Android Gradle error occurs when the Gradle build system encounters problems during the Android compilation phase. This is distinct from general Flutter build errors and specifically relates to the Android build pipeline.

## Common Causes

- Gradle wrapper version outdated
- Android build tools version mismatch
- Kotlin version incompatible with Flutter
- Memory issues during Gradle execution
- Android Gradle plugin version conflict

## How to Fix

1. Update the Gradle wrapper version:

```properties
# android/gradle/wrapper/gradle-wrapper.properties
distributionUrl=https\://services.gradle.org/distributions/gradle-8.3-all.zip
```

2. Update Android Gradle plugin in `android/build.gradle`:

```gradle
buildscript {
  ext {
    compileSdkVersion = 34
    targetSdkVersion = 34
  }
  dependencies {
    classpath 'com.android.tools.build:gradle:8.1.0'
  }
}
```

3. Set Java 17 for Gradle:

```bash
export JAVA_HOME=$(/usr/libexec/java_home -v 17 2>/dev/null || echo /usr/lib/jvm/java-17)
```

4. Increase Gradle memory in `android/gradle.properties`:

```properties
org.gradle.jvmargs=-Xmx8G -XX:MaxMetaspaceSize=4G -XX:+HeapDumpOnOutOfMemoryError
org.gradle.parallel=true
org.gradle.caching=true
```

5. Clean and rebuild:

```bash
flutter clean
cd android && ./gradlew clean
cd ..
flutter build apk --debug
```

6. Check Gradle daemon status:

```bash
cd android && ./gradlew --stop
./gradlew assembleDebug --no-daemon
```

## Examples

```bash
$ flutter build apk
What went wrong:
Execution failed for task ':app:checkDebugAarMetadata'.
> A failure occurred while executing com.android.build.gradle.internal.tasks.CheckAarMetadataWorkAction
> The minCompileSdk (33) specified in a dependency's AAR metadata is greater than this module's compileSdk (32).
```

```bash
# Fix: update compileSdkVersion in android/build.gradle
ext {
  compileSdkVersion = 34
}
```

## Related Errors

- [iOS build error]({{< relref "/frameworks/flutter/flutter-ios-build-error" >}})
- [Build error]({{< relref "/frameworks/flutter/flutter-build-error-v2" >}})
