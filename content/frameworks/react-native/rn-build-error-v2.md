---
title: "Android build - duplicate class error"
description: "React Native Android build fails with duplicate class error caused by conflicting dependencies or library versions"
frameworks: ["react-native"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

The "duplicate class" error occurs during Android builds when two or more libraries provide the same Java/Kotlin class. This typically happens when dependencies include overlapping transitive dependencies or when a library is included both directly and transitively.

## Common Causes

- Two versions of the same library included as dependencies
- Library bundled as both a Maven dependency and a local `.jar`/`.aar`
- React Native and third-party libraries both pulling in the same support library
- Missing `packagingOptions` in `build.gradle`

## How to Fix

1. Exclude duplicate classes in `android/app/build.gradle`:

```gradle
android {
  packagingOptions {
    exclude 'META-INF/LICENSE'
    exclude 'META-INF/NOTICE'
    pickFirst '**/libjsc.so'
    pickFirst '**/libc++_shared.so'
  }
}
```

2. Use `implementation` instead of `compile` and add exclusions:

```gradle
dependencies {
  implementation('com.example:library:1.0') {
    exclude group: 'com.google.guava', module: 'guava'
  }
}
```

3. Check for duplicate dependencies:

```bash
cd android && ./gradlew app:dependencies --configuration releaseRuntimeClasspath | grep -i duplicate
```

4. Force a single version resolution in `android/build.gradle`:

```gradle
subprojects {
  configurations.all {
    resolutionStrategy {
      force 'com.google.guava:guava:31.1-jre'
    }
  }
}
```

5. Clean and rebuild:

```bash
cd android && ./gradlew clean
cd .. && npx react-native run-android
```

## Examples

```bash
# Build output
> Task :app:mergeDexBuilderRelease FAILED
FAILURE: Build failed with an exception.
* What went wrong:
Execution failed for task ':app:mergeDexBuilderRelease'.
> A failure occurred while executing com.android.build.gradle.internal.tasks.DexMergingTaskDelegate
> There was a failure while executing work items
> Duplicate class com.google.gson.Gson found in modules gson-2.8.6.jar and gson-2.10.jar
```

## Related Errors

- [iOS CocoaPods error]({{< relref "/frameworks/react-native/rn-ios-cocoapods-error" >}})
- [Hermes error]({{< relref "/frameworks/react-native/rn-hermes-error" >}})
