---
title: "[Solution] Xcode Error: XCFramework Not Compatible"
description: "Fix XCFramework compatibility errors when integrating binary frameworks."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Xcode Error: XCFramework Not Compatible

XCFramework errors occur when a binary framework is not compatible with the target platform or architecture. The XCFramework may not include a slice for your target.

## Common Causes
- XCFramework missing iOS simulator slice
- Framework built for arm64 only (no x86_64 for older simulators)
- XCFramework built with different Xcode version
- Architecture slice corrupted or incomplete

## How to Fix
1. Verify XCFramework contents with xcodebuild -list
2. Ensure the framework includes slices for your target platform
3. Rebuild the XCFramework with the correct build settings
4. Check that all required architectures are present

```swift
// Check XCFramework contents:
// $ xcodebuild -create-xcframework -list

// Or inspect the framework directory:
// $ ls -R MyFramework.xcframework/
// ios-arm64/
// ios-arm64_x86_64-simulator/

// If missing simulator slice, rebuild with:
// $ xcodebuild archive -scheme MyFramework \
//   -sdk iphonesimulator -archivePath ./simulator.xcarchive
// $ xcodebuild archive -scheme MyFramework \
//   -sdk iphoneos -archivePath ./device.xcarchive
// $ xcodebuild -create-xcframework \
//   -archive ./device.xcarchive -framework MyFramework.framework \
//   -archive ./simulator.xcarchive -framework MyFramework.framework \
//   -output MyFramework.xcframework
```

## Examples
```swift
// Example: Verifying XCFramework platform support
// $ file MyFramework.xcframework/ios-arm64/MyFramework.framework/MyFramework
// MyFramework: Mach-O 64-bit dynamically linked shared library arm64

// $ file MyFramework.xcframework/ios-arm64_x86_64-simulator/MyFramework.framework/MyFramework
// MyFramework: Mach-O 64-bit dynamically linked shared library x86_64

// If the simulator slice shows arm64, it should work with Apple Silicon Macs
```
