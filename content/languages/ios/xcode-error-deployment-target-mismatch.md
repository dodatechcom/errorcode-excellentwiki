---
title: "[Solution] Xcode Error: Deployment Target Mismatch"
description: "Fix iOS deployment target mismatch errors between targets and frameworks."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Xcode Error: Deployment Target Mismatch

Deployment target mismatch errors occur when frameworks or dependencies require a higher deployment target than your project specifies.

## Common Causes
- Framework requires iOS 15 but project targets iOS 13
- CocoaPods dependencies have different minimum deployment targets
- SwiftUI features used with deployment target too low
- Xcode warning about deployment target lower than SDK

## How to Fix
1. Raise your project's deployment target to the highest required version
2. Check each dependency's minimum deployment target
3. Use @available annotations for newer API usage
4. Update the IPHONEOS_DEPLOYMENT_TARGET in Build Settings

```swift
// Check minimum deployment targets for dependencies:
// $ pod ipc spec SomePod | grep platform

// In your Podfile, set a global deployment target:
platform :ios, '16.0'

// Or check each dependency:
pod 'SomePod', :git => 'url', :branch => 'main'
// Check the podspec for platform requirements
```

## Examples
```swift
// Example: Using @available for newer APIs
@available(iOS 16.0, *)
func useNewAPI() {
    let config = UISheetPresentationController.Detent.medium()
}

// Guard availability at runtime:
if #available(iOS 16.0, *) {
    useNewAPI()
} else {
    // Fallback for older iOS
    presentLegacySheet()
}
```
