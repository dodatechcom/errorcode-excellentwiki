---
title: "[Solution] React Native iOS Bitcode Error"
description: "react-native iOS build fails with bitcode error when submitting to App Store or building for release: missing bitcode in React Native native dependency"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The iOS bitcode error occurs during archives or App Store Connect upload when a native dependency library within the React Native app is not built with bitcode enabled. Since Xcode 14, bitcode is deprecated but still required for certain React Native native library builds.

## Common Causes

- A CocoaPod or static library is compiled without bitcode flags
- React Native version predates Xcode 14 and uses incompatible bitcode settings
- Podfile.lock pulls a binary pod that lacks bitcode slice
- Third-party native SDK that uses a bitcode-enabled build from an older Xcode
- Using dynamic libraries with incompatible bitcode setting (YES vs NO)

## How to Fix

1. Enable bitcode for all pods and the project:

```ruby
# Podfile
post_install do |installer|
  installer.pods_project.targets.each do |target|
    target.build_configurations.each do |config|
      config.build_settings['ENABLE_BITCODE'] = 'YES'
    end
  end
end
```

2. Or disable bitcode entirely if no library requires it:

```ruby
# ios/YourApp.xcodeproj/project.pbxproj
# In the Build Settings for both project and targets, set:
# ENABLE_BITCODE = NO;
```

3. Use XCFrameworks if bitcode is problematic:

```bash
# Check if bitcode is in your release binary
otool -l MyApp | grep LLVM
```

## Examples

```bash
# Error: ITMS-90683: Missing Info.plink - bitcode not found
# Fix: recompile the missing library with bitcode
cd node_modules/some-native-module/ios && xcodebuild -workspace SOME.xcworkspace -scheme SOME -derivedDataPath build -configuration Release ENABLE_BITCODE=YES
```

## Related Errors

- [iOS Cocoapods Error]({{< relref "/frameworks/react-native/rn-ios-cocoapods-error" >}})
