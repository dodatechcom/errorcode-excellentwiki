---
title: "[Solution] React Native Flipper Missing Plugin Error"
description: "react-native Flipper desktop app not showing expected plugins like LayoutInspector or NetworkPlugin for React Native debugging sessions"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The missing plugin error in Flipper occurs when a desired plugin does not appear in the Flipper desktop client despite the native plugin being registered. This usually stems from version mismatches between the Flipper client and the Flipper SDK built into the app.

## Common Causes

- Flipper desktop app is older than the Flipper SDK version in the app
- Plugin name registration mismatch between JS and native code
- FlipperKitLayoutPlugin not linked in Podfile for iOS
- Android Flipper initialization uses a version that skips certain plugins
- App compiled in release mode where Flipper is stripped

## How to Fix

1. Update Flipper desktop to the latest version:

```bash
brew upgrade flipper
# or download from https://fbflipper.com/
```

2. Ensure all plugins are linked in iOS Podfile:

```ruby
# ios/Podfile
use_flipper!({ 'Flipper' => '0.201.0' })
```

3. For Android, verify the Flipper initialization in MainApplication.java:

```java
SoLoader.init(this, false);
ReactNativeFlipper.initializeFlipper(this, reactNativeHost);
```

## Examples

```bash
# Flipper shows no plugins installed
# Fix: reset Flipper client cache
rm -rf ~/.flipper/
```

## Related Errors

- [Flipper Version Mismatch]({{< relref "/frameworks/react-native/rn-flipper-version-mismatch" >}})
