---
title: "[Solution] Xcode Error: SDK Not Compatible"
description: "Fix Xcode SDK compatibility errors for iOS development."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Xcode Error: SDK Not Compatible

SDK not compatible errors occur when your project targets an SDK version that does not match the Xcode or deployment target configuration.

## Common Causes
- Xcode version too old for the project SDK setting
- Deployment target set lower than supported SDK
- Mismatched SDK paths in build settings
- Command-line tools pointing to wrong SDK

## How to Fix
1. Update Xcode to the latest compatible version
2. Set deployment target to a supported value
3. Verify SDK path in Build Settings matches installed SDK
4. Reset the SDK selection by clearing DerivedData

```swift
// Check which SDKs are installed:
// $ xcrun --show-sdk-path
// $ xcrun --show-sdk-version

// In your project, ensure deployment target is valid:
// Build Settings > Deployment Target
// iOS: 13.0 or later (for modern APIs)
// macOS: 10.15 or later
```

## Examples
```swift
// Example: Verifying SDK compatibility
// Check available SDKs:
// $ xcodebuild -showsdks

// Example output:
// iOS SDKs:
//   iOS 17.0                    -sdk iphoneos17.0
// iOS Simulator SDKs:
//   Simulator - iOS 17.0        -sdk iphonesimulator17.0

// Ensure your project's SDKROOT matches one of these
// Build Settings > SDKROOT > iphoneos
```
