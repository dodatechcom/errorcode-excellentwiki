---
title: "[Solution] macOS App Translation Error -- App Translation Not Available"
description: "Fix macOS app translation error when an app cannot be translated to run on Mac. Resolve app translation issues on Apple Silicon Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS App Translation Error -- App Translation Not Available

When running iOS or iPad apps on Apple Silicon Macs, translation errors can prevent the app from launching or running correctly.

## Common Causes
- App requires APIs not available in the Mac translation layer
- App uses hardware features not present on Mac
- App's Info.plist does not support the target platform
- App was built for an architecture not supported by translation
- Translation cache is corrupted

## How to Fix
1. Check if the app supports Mac in the App Store
2. Clear the translation cache
3. Reinstall the app from the App Store
4. Contact the developer for Mac compatibility updates
5. Try running the app in Rosetta 2 mode

```bash
# Clear translation cache
rm -rf ~/Library/Caches/com.apple.applettranslation*

# Check app platform support
mdls -name kMDItemSupportedPlatforms /Applications/MyApp.app
```

## Examples

```bash
# Check app bundle for platform support
defaults read /Applications/MyApp.app/Contents/Info.plist UIRequiredDeviceCapabilities
```

This error is common when the app uses iOS-only APIs, when the translation cache is corrupted, or when the app was not configured for Mac support in App Store Connect.
