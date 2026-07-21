---
title: "[Solution] Code Signing Error: Code Signature Invalid"
description: "Fix invalid code signature errors in Xcode builds and submissions."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Code Signing Error: Code Signature Invalid

Invalid code signature errors occur when the generated code signature does not meet Apple's requirements. This can happen during build, archive, or submission.

## Common Causes
- Signed bundle was modified after signing
- Missing or corrupted code signature resources
- Framework not properly code signed
- Hardened runtime not enabled for notarization

## How to Fix
1. Clean the build folder and rebuild
2. Ensure all frameworks are code signed
3. Enable hardened runtime for macOS apps
4. Re-sign the app with proper entitlements

```swift
// Verify code signature:
// $ codesign --verify --deep --strict YourApp.app

// Check entitlements:
// $ codesign -d --entitlements - YourApp.app

// Re-sign if needed:
// $ codesign --force --sign "iPhone Developer: Your Name" YourApp.app
```

## Examples
```swift
// Example: Deep verification of app signature
// $ codesign --verify --deep --strict --verbose=4 YourApp.app

// Look for:
// valid on disk
// satisfies its Designated Requirement
// timestamp is valid

// If errors appear, re-sign:
// $ codesign --force --sign "iPhone Distribution: Team" YourApp.app
```
