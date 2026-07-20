---
title: "[Solution] Flutter Build Gradle Error — compileSdk, minSdk, ndkVersion, AGP"
description: "Fix Flutter Android build errors from compileSdkVersion, minSdkVersion, ndkVersion, AGP version, and Gradle configuration."
languages: ["dart"]
error-types: ["compile-time-error"]
severities: ["error"]
weight: 205
---

Build Gradle errors occur when SDK versions are incompatible, AGP version is outdated, or Gradle configuration conflicts with Flutter requirements.

## Common Causes

1. `compileSdkVersion` too low for required Flutter plugins.
2. `minSdkVersion` below Flutter's minimum requirement (21).
3. `ndkVersion` not specified or incompatible.
4. Android Gradle Plugin version incompatible with Gradle version.
5. `dependencies` block missing required SDK versions.

## How to Fix It

**Solution 1: Set correct SDK versions**

```groovy
// android/app/build.gradle
android {
    compileSdkVersion 34
    
    defaultConfig {
        applicationId "com.example.myapp"
        minSdkVersion 21
        targetSdkVersion 34
        versionCode 1
        versionName "1.0.0"
    }
    
    compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
}
```

**Solution 2: Set ndkVersion**

```groovy
// android/app/build.gradle
android {
    ndkVersion "25.1.8937393"  // Use Flutter's recommended version
    // or
    ndkVersion flutter.ndkVersion
}
```

**Solution 3: Update AGP and Gradle**

```groovy
// android/build.gradle
buildscript {
    ext.kotlin_version = '1.9.22'
    
    dependencies {
        classpath 'com.android.tools.build:gradle:8.1.0'
        classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:$kotlin_version"
    }
}

// android/gradle/wrapper/gradle-wrapper.properties
distributionUrl=https\://services.gradle.org/distributions/gradle-8.3-all.zip
```

**Solution 4: Handle flavor configurations**

```groovy
// android/app/build.gradle
android {
    flavorDimensions "environment"
    
    productFlavors {
        dev {
            dimension "environment"
            applicationIdSuffix ".dev"
            minSdkVersion 21
        }
        prod {
            dimension "environment"
            minSdkVersion 21
        }
    }
}
```

**Solution 5: Clean and rebuild**

```bash
# Clean build files
flutter clean

# Get dependencies
flutter pub get

# Rebuild
flutter build apk --debug

# If Gradle issues persist
cd android && ./gradlew clean && cd ..
flutter build apk
```

## Examples

Flutter requires `compileSdkVersion >= 34` and `minSdkVersion >= 21` as of 2024. Always check Flutter's release notes for current requirements.

## Related Errors

- [Flutter Podfile Error](/languages/dart/flutter-podfile-error/)
- [Flutter Package Name Error](/languages/dart/flutter-package-name-error/)
- [Flutter Firebase Core Error](/languages/dart/flutter-firebase-core-error/)
