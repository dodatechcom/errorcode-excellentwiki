---
title: "[Solution] Xcode Error: No Provisioning Profile Found"
description: "Fix missing provisioning profile errors in Xcode iOS builds."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Xcode Error: No Provisioning Profile Found

This error appears when Xcode cannot find a valid provisioning profile for your app. The provisioning profile maps your signing identity to your app's bundle identifier.

## Common Causes
- Automatic signing misconfigured or disabled
- Provisioning profile expired or revoked
- Bundle identifier mismatch between profile and project
- Xcode account does not have the profile available

## How to Fix
1. Enable Automatic Signing in your target's Signing & Capabilities
2. Revoke and regenerate the provisioning profile
3. Ensure bundle identifier matches exactly
4. Sign in to your Apple Developer account in Xcode preferences

```swift
// Enable automatic signing in Xcode:
// Target > Signing & Capabilities > check "Automatically manage signing"

// Or manually via command line:
// $ xcodebuild -exportArchive \
//   -archivePath MyApp.xcarchive \
//   -exportOptionsPlist ExportOptions.plist \
//   -exportPath ./build
```

## Examples
```swift
// Example: ExportOptions.plist for manual signing
// <?xml version="1.0" encoding="UTF-8"?>
// <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
//   "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
// <plist version="1.0">
// <dict>
//     <key>method</key>
//     <string>development</string>
//     <key>teamID</key>
//     <string>YOUR_TEAM_ID</string>
//     <key>provisioningProfiles</key>
//     <dict>
//         <key>com.example.myapp</key>
//         <string>MyApp Development Profile</string>
//     </dict>
// </dict>
// </plist>
```
