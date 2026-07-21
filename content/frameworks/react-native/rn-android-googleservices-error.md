---
title: "[Solution] React Native Android Google Services Error"
description: "react-native Google Services plugin fails during Android build with missing google-services.json or mismatched com.google.gms version in React Native apps"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The Google Services error surfaces during the Android build when the google-services.json file is missing or the Google Services plugin version does not match the Firebase library versions declared in the project.

## Common Causes

- google-services.json file not placed in android/app/ directory
- google-services.json is from the wrong Firebase project
- Mismatch between com.google.gms plugin version and com.google.firebase versions
- google-services.json contains invalid or corrupted JSON
- Multiple google-services.json files in the project causing conflict

## How to Fix

1. Verify google-services.json location:

```bash
ls android/app/google-services.json
```

2. Download the correct google-services.json from Firebase Console:

```bash
curl -o android/app/google-services.json "https://your-project.firebaseio.com/.../google-services.json"
```

3. Ensure consistent version in android/build.gradle:

```gradle
// android/build.gradle
dependencies {
  classpath('com.google.gms:google-services:4.4.2')
  classpath('com.google.firebase:firebase-crashlytics-gradle:3.0.2')
}
```

## Examples

```bash
# Error output during Gradle build
# "File google-services.json is missing."

# Fix:
cp ~/Downloads/google-services.json android/app/google-services.json
```

## Related Errors

- [Android Build Failed]({{< relref "/frameworks/react-native/rn-android-build-failed" >}})
