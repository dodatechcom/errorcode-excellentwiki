---
title: "[Solution] Flutter Podfile Error — CocoaPods, pod install, deployment target, arm64"
description: "Fix Flutter iOS build errors from CocoaPods configuration, pod install failures, minimum deployment target, and arm64 architecture."
languages: ["dart"]
error-types: ["compile-time-error"]
severities: ["error"]
weight: 206
---

Podfile errors occur when CocoaPods installation fails, deployment target is too low, or arm64 architecture is not configured correctly.

## Common Causes

1. `pod install` failing due to version conflicts.
2. Minimum deployment target below Flutter's requirement.
3. `arm64` architecture not included for device builds.
4. `Podfile.lock` being out of sync with `pubspec.yaml`.
5. Missing platform declaration in `Podfile`.

## How to Fix It

**Solution 1: Configure Podfile correctly**

```ruby
# ios/Podfile

platform :ios, '13.0'  # Flutter requires iOS 13.0+

# Fix for CocoaPods on Apple Silicon
# arch x86_64 arm64

target 'Runner' do
  use_frameworks!
  use_modular_headers!

  flutter_install_all_ios_pods File.dirname(File.realpath(__FILE__))
end

post_install do |installer|
  installer.pods_project.targets.each do |target|
    flutter_additional_ios_build_settings(target)
  end
end
```

**Solution 2: Run pod install**

```bash
cd ios

# Remove old pods
rm -rf Pods/
rm -f Podfile.lock

# Reinstall
pod install

cd ..
```

**Solution 3: Handle deployment target**

```ruby
# ios/Podfile
platform :ios, '13.0'

post_install do |installer|
  installer.pods_project.targets.each do |target|
    target.build_configurations.each do |config|
      config.build_settings['IPHONEOS_DEPLOYMENT_TARGET'] = '13.0'
    end
  end
end
```

**Solution 4: Fix arm64 architecture issues**

```ruby
# ios/Podfile
post_install do |installer|
  installer.pods_project.targets.each do |target|
    target.build_configurations.each do |config|
      config.build_settings['EXCLUDED_ARCHS[sdk=iphonesimulator*]'] = 'arm64 i386'
    end
  end
end
```

**Solution 5: Handle CocoaPods repo issues**

```bash
# Reset CocoaPods repo
pod repo update

# If that fails, remove and re-add
pod repo remove trunk
pod repo add-cdn trunk https://cdn.cocoapods.org/

# Clean pod cache
pod cache clean --all

# Then reinstall
cd ios && pod install && cd ..
```

## Examples

Flutter's minimum iOS deployment target is 13.0. For Apple Silicon Macs, ensure the simulator destination includes arm64 architecture.

## Related Errors

- [Flutter Build Gradle Error](/languages/dart/flutter-build-gradle-error/)
- [Flutter Package Name Error](/languages/dart/flutter-package-name-error/)
- [Flutter Firebase Core Error](/languages/dart/flutter-firebase-core-error/)
