---
title: "[Solution] Code Signing Error: Ad Hoc Profile Not Found"
description: "Fix missing ad hoc provisioning profile errors for device distribution."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Code Signing Error: Ad Hoc Profile Not Found

Ad hoc profiles allow distribution to registered devices without the App Store. Missing profiles prevent ad hoc builds from being installed.

## Common Causes
- Ad hoc profile never created in the developer portal
- Profile expired or was revoked
- Device not registered for ad hoc distribution
- Export options reference wrong profile name

## How to Fix
1. Create an ad hoc profile in the developer portal
2. Register the target device UDID
3. Download and install the profile
4. Match the profile name in export options

```swift
// Create ad hoc profile:
// 1. Go to https://developer.apple.com/account/resources/profiles
// 2. Click "+" > Ad Hoc
// 3. Select your App ID
// 4. Select your distribution certificate
// 5. Select registered devices
// 6. Generate and download
```

## Examples
```swift
// Example: ExportOptions.plist for ad hoc
// <dict>
//     <key>method</key>
//     <string>ad-hoc</string>
//     <key>teamID</key>
//     <string>TEAMID</string>
//     <key>signingStyle</key>
//     <string>manual</string>
//     <key>provisioningProfiles</key>
//     <dict>
//         <key>com.example.myapp</key>
//         <string>MyApp Ad Hoc Profile</string>
//     </dict>
// </dict>
```
