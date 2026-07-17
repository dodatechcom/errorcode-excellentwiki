---
title: "iOS build - CocoaPods error"
description: "Flutter iOS build fails with CocoaPods errors due to pod installation or version conflicts"
frameworks: ["flutter"]
error-types: ["build-error"]
severities: ["error"]
tags: ["flutter", "ios", "cocoapods", "pod", "xcode", "build"]
weight: 5
---

A CocoaPods error during Flutter iOS build occurs when `pod install` fails or when the iOS build cannot resolve pod dependencies. This is one of the most common issues when building Flutter apps for iOS.

## Common Causes

- CocoaPods not installed or outdated
- Podfile.lock conflicts after updating Flutter or dependencies
- Missing or corrupted Pods directory
- Ruby version incompatibility with CocoaPods
- Xcode version mismatch

## How to Fix

1. Update CocoaPods:

```bash
sudo gem install cocoapods
pod repo update
```

2. Clean and reinstall pods:

```bash
cd ios
rm -rf Pods Podfile.lock
pod install
cd ..
```

3. Verify CocoaPods installation:

```bash
pod --version
pod repo list
```

4. Run flutter clean before iOS build:

```bash
flutter clean
flutter pub get
cd ios && pod install
cd ..
flutter build ios --no-codesign
```

5. Fix Ruby version issues with rbenv:

```bash
rbenv install 3.1.0
rbenv local 3.1.0
pod install
```

6. Check for iOS deployment target conflicts:

```ruby
# ios/Podfile
platform :ios, '13.0'
```

## Examples

```bash
$ flutter build ios
Running pod install...
[!] Unable to determine Swift version for the following pods:
- 'Flutter' does not specify a Swift version.

# Fix: update Podfile
post_install do |installer|
  installer.pods_project.targets.each do |target|
    target.build_configurations.each do |config|
      config.build_settings['IPHONEOS_DEPLOYMENT_TARGET'] = '13.0'
    end
  end
end
```

## Related Errors

- [Android build error]({{< relref "/frameworks/flutter/flutter-android-build-error" >}})
- [Build error]({{< relref "/frameworks/flutter/flutter-build-error-v2" >}})
