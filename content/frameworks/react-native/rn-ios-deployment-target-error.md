---
title: "[Solution] React Native iOS Deployment Target Mismatch"
description: "react-native iOS CocoaPods fails with minimum deployment target mismatch between React Native, native libraries, and Xcode project settings"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The iOS deployment target error occurs when the minimum deployment target in the Podfile or Xcode project is not compatible with React Native's required target. React Native 0.71+ requires iOS 12.0, while individual native libraries may target iOS 13.0 or later.

## Common Causes

- Project target set to iOS 11 but React Native requires iOS 12
- One library declares iOS 13.0 minimum but most of the app expects iOS 12
- Podfile platform line missing or lower than meant for dependencies
- Xcode project.plist and Podfile have different deployment targets
- Flutter or React Native interop with wrong iOS target

## How to Fix

1. Set the correct minimum deployment target in the Podfile:

```ruby
# ios/Podfile
platform :ios, '13.0'
```

2. Align target in Xcode project:

```bash
# You can set it via a post_install hook
post_install do |installer|
  installer.pods_project.build_configurations.each do |config|
    config.build_settings['IPHONEOS_DEPLOYMENT_TARGET'] = '13.0'
  end
end
```

3. Check all individual library targets in Pods project:

```bash
# Run this to see current deployment targets
xcodebuild -project MyApp.xcodeproj -list
```

## Examples

```bash
# Error: iOS deployment target '11.0' does not support automated dylib detection
# Fix:
# In ios/Podfile:
platform :ios, '13.0'
# And then run:
cd ios && pod install
```

## Related Errors

- [iOS Build Failed]({{< relref "/frameworks/react-native/rn-ios-build-failed" >}})
