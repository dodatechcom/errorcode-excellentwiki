---
title: "[Solution] Provisioning Profile iOS Distribution Failed"
description: "Fix iOS distribution provisioning profile errors for App Store."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Provisioning Profile iOS Distribution Failed

Distribution profile errors occur when trying to export an archive for App Store or TestFlight submission. The profile must be a distribution profile, not development.

## Common Causes
- Development profile used instead of distribution
- Distribution certificate missing from keychain
- Profile does not match the archive's bundle identifier
- Export options specify wrong signing method

## How to Fix
1. Create an App Store distribution profile in the portal
2. Ensure the distribution certificate is installed
3. Match the profile's bundle ID with your archive
4. Set the correct method in export options

```swift
// In ExportOptions.plist:
// <key>method</key>
// <string>app-store</string>

// Available methods:
// "app-store" — App Store distribution
// "ad-hoc" — Ad hoc distribution
// "enterprise" — Enterprise distribution
// "development" — Development distribution
```

## Examples
```swift
// Example: Creating distribution profile
// 1. Go to https://developer.apple.com/account/resources/profiles
// 2. Click "+" > App Store Connect
// 3. Select your App ID
// 4. Select your distribution certificate
// 5. Generate and download

// Verify profile type:
// $ security cms -D -i distribution.mobileprovision | \
//   grep -A1 "ProvisionedDevices"
// If present, it's a development profile (wrong for App Store)
```
