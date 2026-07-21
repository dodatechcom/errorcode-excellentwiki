---
title: "[Solution] App Store Connect Build Processing Error"
description: "Fix App Store Connect build processing failures after uploading an IPA."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# App Store Connect Build Processing Error

Build processing fails when App Store Connect cannot process the uploaded build due to metadata issues, entitlement mismatches, or invalid configuration.

## Common Causes
- Missing privacy manifest (PrivacyInfo.xcprivacy)
- Invalid entitlements in the uploaded build
- Architecture issues (missing arm64)
- Info.plist missing required keys

## How to Fix
1. Check the email from App Store Connect for specific errors
2. Ensure privacy manifest is included in the bundle
3. Verify entitlements match your provisioning profile
4. Upload a universal binary with all required architectures

```swift
// Verify your archive before upload:
// $ xcodebuild -archivePath MyApp.xcarchive -exportArchive \
//   -exportOptionsPlist ExportOptions.plist -exportPath ./build

// Check for privacy manifest:
// $ find MyApp.app -name "PrivacyInfo.xcprivacy"
```

## Examples
```swift
// PrivacyInfo.xcprivacy minimum content:
// <?xml version="1.0" encoding="UTF-8"?>
// <plist version="1.0">
// <dict>
//     <key>NSPrivacyTracking</key>
//     <false/>
//     <key>NSPrivacyTrackingDomains</key>
//     <array/>
//     <key>NSPrivacyCollectedDataTypes</key>
//     <array/>
//     <key>NSPrivacyAccessedAPITypes</key>
//     <array/>
// </dict>
// </plist>
```
