---
title: "[Solution] React Native Firebase Crashlytics Error"
description: "react-native Firebase Crashlytics fails to initialize or report crashes on Android and iOS due to missing dependencies or version misalignment in React Native apps"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The Crashlytics initialization or reporting error in React Native occurs when the native Crashlytics SDK cannot bind to the Firebase project or the React Native Firebase module is not correctly wired in the native build.

## Common Causes

- Crashlytics plugin not applied in android/app/build.gradle
- Missing google-services.json in android/app
- dSYM upload failure on iOS App Store submissions
- Firebase and Crashlytics versions mismatch
- Running on an emulator without Google Play Services

## How to Fix

1. Ensure Crashlytics plugin is applied at the bottom of android/app/build.gradle:

```gradle
// android/app/build.gradle
apply plugin: 'com.google.firebase.crashlytics'
```

2. Initialize in App.js before any import that depends on crash reporting:

```javascript
import crashlytics from '@react-native-firebase/crashlytics';

crashlytics().setCrashlyticsCollectionEnabled(true);
```

3. Upload dSYMs for iOS manually if Bitcode is enabled:

```bash
cd ios && Pods/FirebaseCrashlytics/upload-symbols -gsp GoogleService-Info.plist -p ios App.dSYMs
```

## Examples

```javascript
// Error: Crashlytics not initialized
try {
  crashlytics().log('Custom message');
} catch (e) {
  console.warn('Crashlytics unavailable:', e.message);
}

// Fix: check initialized before use
if (crashlytics().isCrashlyticsCollectionEnalbed) {
  crashlytics().log('Initialized and ready');
}
```

## Related Errors

- [Build Error]({{< relref "/frameworks/react-native/rn-build-error" >}})
