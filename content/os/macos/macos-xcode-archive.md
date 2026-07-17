---
title: "[Solution] Xcode Archive Error on macOS"
description: "Fix Xcode archive errors when archiving for distribution. Resolve 'archive failed' and export issues in Xcode."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["xcode", "archive", "distribution", "app-store", "export"]
weight: 5
---

# Xcode Archive Error Fix

Archive errors occur when trying to create a build archive for App Store or enterprise distribution. Xcode shows "Archive Failed" in the organizer with specific error details.

## What This Error Means

Archiving bundles the app for distribution, including code signing, asset compilation, and IPA generation. Failures at this stage prevent app submission to the App Store.

## Common Causes

- Provisioning profile mismatch for archive configuration
- Code signing identity not found
- Bitcode compilation errors
- Missing required architectures
- Stale build products in the archive

## How to Fix

### 1. Clean and rebuild the archive

```bash
# Clean build folder
xcodebuild clean archive -workspace MyApp.xcworkspace -scheme MyApp

# Archive again
xcodebuild archive -workspace MyApp.xcworkspace -scheme MyApp \
    -archivePath MyApp.xcarchive
```

### 2. Check archive settings

```bash
# Verify build settings for archive
xcodebuild -showBuildSettings -workspace MyApp.xcworkspace \
    -scheme MyApp -configuration Release
```

### 3. Fix export options

```bash
# Create an ExportOptions.plist for command-line export
cat > ExportOptions.plist << 'PLIST'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>method</key>
    <string>app-store</string>
    <key>teamID</key>
    <string>TEAMID</string>
</dict>
</plist>
PLIST

# Export the archive
xcodebuild -exportArchive -archivePath MyApp.xcarchive \
    -exportOptionsPlist ExportOptions.plist -exportPath ./output
```

## Related Errors

- [Xcode Error](macos-xcode-error) — general build errors
- [Code Signing Error](macos-code-signing-error) — signing failures
- [Notarization Error](macos-notarization-error) — notarization issues
