---
title: "[Solution] macOS Provisioning Profile Error"
description: "Fix provisioning profile errors on Mac when Xcode shows 'No matching provisioning profile found' or profile-related build failures."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["provisioning", "profile", "xcode", "development", "distribution"]
weight: 5
---

# macOS Provisioning Profile Error Fix

Provisioning profile errors occur when Xcode cannot find or use a valid provisioning profile for your app. Common messages include "No matching provisioning profile found" or "Provisioning profile has expired."

## What This Error Means

A provisioning profile links your signing certificate to specific app IDs and device UDIDs. Xcode needs a valid profile to sign and install apps on devices. Errors indicate a mismatch between the profile, certificate, and app configuration.

## Common Causes

- Provisioning profile expired
- Bundle ID doesn't match the profile's app ID
- Certificate not included in the profile
- Profile was regenerated but Xcode cache is stale
- Automatic signing configuration issues

## How to Fix

### 1. Regenerate provisioning profiles

```bash
# In Xcode: Preferences → Accounts → Select team → Manage Certificates
# Or via command line:
xcodebuild -exportArchive -archivePath MyApp.xcarchive \
    -exportPath ./output -exportOptionsPlist ExportOptions.plist
```

### 2. Delete stale profiles and let Xcode regenerate

```bash
# Remove old profiles
rm -rf ~/Library/MobileDevice/Provisioning\ Profiles/*

# In Xcode: Enable "Automatically manage signing"
# Xcode will regenerate all needed profiles
```

### 3. Match bundle ID to profile

```bash
# Check your app's bundle ID
defaults read MyApp.app/Contents/Info.plist CFBundleIdentifier

# Ensure it matches the provisioning profile's app ID
# Profiles with "*" are wildcard and accept any bundle ID
```

### 4. Force Xcode to refresh profiles

```bash
# Download all profiles from Apple Developer Portal
xcrun provisioning-profile list

# Clean build folder
xcodebuild clean
```

## Related Errors

- [Code Signing Error](macos-code-signing-error) — code signing failures
- [Xcode Error](macos-xcode-error) — Xcode build errors
- [Xcode Archive Error](macos-xcode-archive) — archive failures
