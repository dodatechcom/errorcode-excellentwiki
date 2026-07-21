---
title: "[Solution] Code Signing Error: Watch App Extension Signing"
description: "Fix code signing errors for Apple Watch app extensions."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Code Signing Error: Watch App Extension Signing

Watch app extensions have specific signing requirements including paired bundle identifiers and entitlement sharing with the main iOS app.

## Common Causes
- Watch extension bundle ID does not follow naming convention
- Extension not properly linked to the iOS app
- Entitlements mismatch between iOS and watchOS targets
- Different teams used for iOS and watchOS targets

## How to Fix
1. Use the same team for both iOS and watchOS targets
2. Ensure bundle IDs follow the pattern: com.app.main.watchkitapp
3. Share entitlements between the targets
4. Include the watch extension in the Embed Watch Content build phase

```swift
// Bundle ID naming convention:
// iOS app: com.example.myapp
// WatchKit app: com.example.myapp.watchkitapp
// Watch extension: com.example.myapp.watchkitapp.extension

// All must use the same development team
```

## Examples
```swift
// Example: Verifying watch app signing
// $ codesign --verify --deep YourApp.app/Watch/YourWatch.app

// If watch extension signing fails:
// $ codesign --force --sign "iPhone Distribution: Your Team" \
//   YourApp.app/Watch/YourWatch.app/PlugIns/YourWatchExtension.appex
```
