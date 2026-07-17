---
title: "iOS CocoaPods - pod install error"
description: "React Native iOS build fails during CocoaPods pod installation due to dependency conflicts or missing pods"
frameworks: ["react-native"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

A CocoaPods error in React Native occurs when `pod install` fails to resolve or install iOS dependencies. This can happen due to version conflicts, corrupted pod cache, or configuration issues in the Podfile.

## Common Causes

- Podfile or Podfile.lock contains conflicting versions
- Corrupted CocoaPods cache
- Xcode command line tools not updated
- Missing or incorrect platform declaration in Podfile
- CocoaPods version incompatibility

## How to Fix

1. Update CocoaPods and reinstall pods:

```bash
sudo gem install cocoapods
cd ios && rm -rf Pods Podfile.lock
pod install
```

2. Update pod repo for latest versions:

```bash
pod repo update
pod install
```

3. Verify platform in Podfile:

```ruby
platform :ios, '13.4'

target 'YourApp' do
  use_frameworks! :linkage => :static
  # ... pods
end
```

4. Clean derived data and pods:

```bash
cd ios && rm -rf Pods build
rm -rf ~/Library/Developer/Xcode/DerivedData/*
pod install
```

5. Check for architecture issues on Apple Silicon:

```bash
arch -x86_64 pod install
```

6. Verify Xcode command line tools:

```bash
xcode-select --install
sudo xcode-select --switch /Applications/Xcode.app
```

## Examples

```bash
$ pod install
[!] Unable to find a target named `YourAppTests`, did find `YourApp`.
```

```bash
# Fix: clean everything
cd ios
rm -rf Pods Podfile.lock
pod deintegrate
pod install
```

## Related Errors

- [Android SDK error]({{< relref "/frameworks/react-native/rn-android-sdk-error" >}})
- [Build error]({{< relref "/frameworks/react-native/rn-build-error-v2" >}})
