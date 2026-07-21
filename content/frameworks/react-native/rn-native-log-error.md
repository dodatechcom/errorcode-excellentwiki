---
title: "[Solution] React Native Native Log Not Appearing in Xcode/Logcat"
description: "react-native native code logging using NSLog or Log.d does not appear in Xcode console or Android logcat output"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The native log error occurs when developers add logging in native module implementations but the logs do not appear in Xcode (iOS) or Logcat (Android). This usually stems from log level filtering, incorrect log tags, or running in release mode where logs are stripped.

## Common Causes

- Android: Log.d() tag is too short or filtered out by logcat filter
- iOS: NSLog output is not visible in Xcode console when running from Metro
- Release builds strip all native logs via compiler flags
- Logs emitted before the native module initializes the logging system
- Using fprintf or printf instead of platform logging APIs
- Android ProGuard strips Log calls in release builds

## How to Fix

1. Android: Use Log.d with a unique tag:

```java
import android.util.Log;
private static final String TAG = "MyNativeModule";
Log.d(TAG, "This will appear in logcat");

// Filter by tag:
// adb logcat -s MyNativeModule:V
```

2. iOS: Use os_log for modern logging:

```objectivec
@import os.log;
os_log_info(OS_LOG_DEFAULT, "Native module initialized");
```

3. Disable log stripping for debug builds:

```gradle
// android/app/build.gradle
android {
  buildTypes {
    debug {
      debuggable true
      minifyEnabled false
    }
  }
}
```

## Examples

```bash
# Android: run logcat with app's PID filter
adb logcat --pid=$(adb shell pidof -s com.myapp) -v time

# iOS: run from Xcode and select "OS_ACTIVITY_MODE=debug"
export OS_ACTIVITY_MODE=debug
npx react-native run-ios
```

## Related Errors

- [Native Module Error]({{< relref "/frameworks/react-native/rn-native-module-error-rn" >}})
