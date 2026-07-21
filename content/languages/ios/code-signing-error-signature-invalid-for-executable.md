---
title: "[Solution] Code Signing Error: Signature Invalid for Executable"
description: "Fix invalid signature errors on executable binaries in Xcode."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Code Signing Error: Signature Invalid for Executable

Executable binaries may have invalid signatures due to corruption, modification, or improper signing configuration. This prevents the app from launching or being distributed.

## Common Causes
- Binary was modified after code signing
- Sign script failed silently during build
- Architecture slices were added after signing
- Hardened runtime requirements not met

## How to Fix
1. Rebuild the project without incremental builds
2. Verify the signature with codesign tool
3. Check that no post-build scripts modify the binary
4. Ensure hardened runtime is properly configured

```swift
// Verify executable signature:
// $ codesign --verify --deep YourApp.app/YourApp

// Check for modifications:
// $ codesign -dvvv YourApp.app/YourApp

// Re-sign the entire bundle:
// $ codesign --force --sign "iPhone Distribution: Your Team" \
//   --entitlements YourApp.entitlements YourApp.app
```

## Examples
```swift
// Example: Checking signature details
// $ codesign -d --entitlements - YourApp.app

// Output shows entitlements used during signing:
// [dict]
//     [key] com.apple.security.cs.allow-jit
//     [bool] true
//     [key] com.apple.security.cs.allow-unsigned-executable-memory
//     [bool] true
```
