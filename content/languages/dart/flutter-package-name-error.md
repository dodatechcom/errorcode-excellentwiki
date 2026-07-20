---
title: "[Solution] Flutter Package Name Error — mismatch, AndroidManifest, Info.plist"
description: "Fix Flutter package name mismatch errors from AndroidManifest.xml, Info.plist, and build configuration conflicts."
languages: ["dart"]
error-types: ["compile-time-error"]
severities: ["error"]
weight: 204
---

Package name errors occur when the application ID does not match across configuration files, or when renaming the package without updating all references.

## Common Causes

1. Android `applicationId` not matching `AndroidManifest.xml` package name.
2. iOS `PRODUCT_BUNDLE_IDENTIFIER` not matching `Info.plist` bundle ID.
3. Firebase `google-services.json` having a different package name.
4. Renaming package without running `flutter pub get`.
5. Deep link scheme not matching the package name.

## How to Fix It

**Solution 1: Check Android package name**

```xml
<!-- android/app/build.gradle -->
android {
    defaultConfig {
        applicationId "com.example.myapp"  <!-- Must match -->
    }
}

<!-- android/app/src/main/AndroidManifest.xml -->
<manifest package="com.example.myapp">  <!-- Must match -->
```

**Solution 2: Check iOS bundle identifier**

```xml
<!-- ios/Runner/Info.plist -->
<key>CFBundleIdentifier</key>
<string>com.example.myapp</string>

<!-- ios/Runner.xcodeproj/project.pbxproj -->
PRODUCT_BUNDLE_IDENTIFIER = com.example.myapp;  <!-- Must match -->
```

**Solution 3: Rename package using CLI**

```bash
# Android
# Manually update android/app/build.gradle applicationId
# Manually update android/app/src/main/AndroidManifest.xml package

# iOS
# Update ios/Runner.xcodeproj with new bundle identifier
```

**Solution 4: Verify Firebase configuration matches**

```dart
// android/app/google-services.json must have:
// "package_name": "com.example.myapp"

// ios/Runner/GoogleService-Info.plist must have:
// BUNDLE_ID: com.example.myapp
```

**Solution 5: Check pubspec.yaml name**

```yaml
# pubspec.yaml
name: my_app  # This is the Dart package name, not the app ID
description: My Flutter application

# The application ID is set in build.gradle (Android) and Xcode (iOS)
```

## Examples

The Dart package name in `pubspec.yaml` is separate from the Android `applicationId` and iOS `bundleIdentifier`. All three must be consistent for push notifications and deep linking to work.

## Related Errors

- [Flutter Build Gradle Error](/languages/dart/flutter-build-gradle-error/)
- [Flutter Podfile Error](/languages/dart/flutter-podfile-error/)
- [Flutter Firebase Core Error](/languages/dart/flutter-firebase-core-error/)
