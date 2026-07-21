---
title: "[Solution] macOS Hardened Runtime Error -- App Cannot Run With Hardened Runtime"
description: "Fix macOS hardened runtime error when an app fails with hardened runtime restrictions. Resolve hardened runtime issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Hardened Runtime Error -- App Cannot Run With Hardened Runtime

Hardened runtime is a macOS security feature that restricts certain operations like JIT compilation, unsigned library loading, and unrestricted filesystem access. Apps may crash when they try to perform restricted operations.

## Common Causes
- App uses JIT compilation without the jit entitlement
- App loads unsigned dynamic libraries
- App accesses user files without the files-user-selected entitlement
- App uses dlopen to load libraries at runtime
- App requires specific exceptions for features

## How to Fix
1. Add the specific entitlements needed for your app's features
2. Sign all dynamic libraries with the same certificate
3. Use NSOpenPanel for file access instead of direct paths
4. Enable specific exceptions in the entitlements file
5. Test with the hardened runtime evaluate tool

```bash
# Check hardened runtime status
codesign -d --entitlements - /Applications/MyApp.app

# Sign with hardened runtime
codesign --force --sign "Developer ID Application: Name" --options runtime /Applications/MyApp.app
```

## Examples

```bash
# Evaluate hardened runtime restrictions
com.apple.security.app-sandbox --evaluate
```

This error is common when apps use JIT compilation for JavaScript engines, when dynamically loading libraries without signing them, or when accessing user files without the proper entitlements.
