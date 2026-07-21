---
title: "[Solution] Code Signing Error: Embedded Framework Signing Failed"
description: "Fix code signing failures for embedded frameworks in iOS apps."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Code Signing Error: Embedded Framework Signing Failed

Embedded frameworks must be code signed along with the main app. Signing failures in embedded frameworks prevent the app from being properly signed.

## Common Causes
- Framework not included in Embed Frameworks build phase
- Framework signed with wrong identity
- Framework architecture does not match main app
- Framework contains resources not properly signed

## How to Fix
1. Verify the framework is in Embed Frameworks build phase
2. Ensure Code Sign On Copy is checked for the framework
3. Use the same signing identity for all frameworks
4. Set Code Signing to "Sign to Run Locally" for pods

```swift
// In Target > Build Phases > Embed Frameworks:
// 1. Ensure all embedded frameworks are listed
// 2. Check "Code Sign On Copy" for each framework
// 3. Set "Embed" to "Do Not Embed" for system frameworks

// For CocoaPods, in Podfile:
post_install do |installer|
  installer.pods_project.targets.each do |target|
    target.build_configurations.each do |config|
      config.build_settings['CODE_SIGN_IDENTITY'] = '-'
    end
  end
end
```

## Examples
```swift
// Example: Verifying embedded framework signing
// $ codesign --verify --deep YourApp.app

// If a framework fails verification:
// $ codesign --verify --deep YourApp.app/Frameworks/SomeFramework.framework

// Fix by re-signing the framework:
// $ codesign --force --sign "iPhone Distribution: Your Team" \
//   YourApp.app/Frameworks/SomeFramework.framework
```
