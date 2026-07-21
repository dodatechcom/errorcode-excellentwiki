---
title: "[Solution] Xcode Error: Toolchain Not Found"
description: "Fix missing toolchain errors when switching Swift toolchains in Xcode."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Xcode Error: Toolchain Not Found

This error occurs when Xcode cannot find the selected Swift toolchain. This is common when installing or switching between multiple toolchain versions.

## Common Causes
- Toolchain not installed or was removed
- Xcode references a toolchain that no longer exists
- Toolchain installation path changed after Xcode update
- Multiple Xcode installations with conflicting toolchains

## How to Fix
1. Verify the toolchain is installed at the expected path
2. Reinstall the toolchain if it was deleted
3. Switch back to the default Xcode toolchain
4. Update Xcode to the latest version for the latest toolchain

```swift
// Check available toolchains:
// $ xcrun --toolchain default -- swift --version

// List installed toolchains:
// $ ls /Library/Developer/Toolchains/

// Switch to default toolchain:
// Xcode > Toolchains > select "Xcode Default"

// Or use the current toolchain:
// $ xcrun --toolchain com.apple.dt.toolchain.Swift_5_0 swift --version
```

## Examples
```swift
// Example: Installing a Swift toolchain
// Download from swift.org/download
// Install to /Library/Developer/Toolchains/

// Verify installation:
// $ ls /Library/Developer/Toolchains/
// swift-5.10-RELEASE.xctoolchain

// Use specific toolchain:
// $ TOOLCHAINS=com.apple.dt.toolchain.Swift_5_10 swift build
```
