---
title: "[Solution] Code Signing Error: Hardened Runtime Required"
description: "Fix hardened runtime errors for macOS app notarization and signing."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Code Signing Error: Hardened Runtime Required

Apple requires hardened runtime for macOS apps submitted outside the App Store. Notarization fails without this setting enabled.

## Common Causes
- Hardened Runtime not enabled in build settings
- App uses JIT compilation which requires exceptions
- App loads unsigned libraries at runtime
- Missing entitlements for hardened runtime exceptions

## How to Fix
1. Enable Hardened Runtime in build settings
2. Add specific entitlements for JIT or unsigned loading
3. Sign all embedded frameworks properly
4. Submit for notarization after enabling hardened runtime

```swift
// Enable in Build Settings:
// Enable Hardened Runtime = YES

// Common hardened runtime entitlements:
// com.apple.security.cs.allow-jit
// com.apple.security.cs.allow-unsigned-executable-memory
// com.apple.security.cs.disable-library-validation
```

## Examples
```swift
// Example: Entitlements for hardened runtime
// <?xml version="1.0" encoding="UTF-8"?>
// <dict>
//     <key>com.apple.security.cs.allow-jit</key>
//     <true/>
//     <key>com.apple.security.cs.allow-unsigned-executable-memory</key>
//     <true/>
// </dict>

// Verify hardened runtime:
// $ codesign -d --entitlements - YourApp.app | \
//   grep -A2 "hardened"
```
