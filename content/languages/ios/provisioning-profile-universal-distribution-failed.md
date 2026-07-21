---
title: "[Solution] Provisioning Profile Universal Distribution Failed"
description: "Fix universal distribution provisioning profile errors in Xcode."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Provisioning Profile Universal Distribution Failed

Universal distribution profiles allow installation on both development and distribution devices. Configuration errors can prevent proper distribution.

## Common Causes
- Profile configured as development only
- Distribution certificate not included in profile
- Profile type does not match export method
- Missing App Store Connect configuration

## How to Fix
1. Verify the profile type matches your export method
2. Include both development and distribution certificates
3. Configure the profile for universal distribution in the portal
4. Update export options to match the profile type

```swift
// For universal distribution:
// 1. Create a profile with both dev and dist certificates
// 2. In ExportOptions.plist:
// <key>method</key>
// <string>development</string>
// (for testing on registered devices)

// For App Store:
// <key>method</key>
// <string>app-store</string>
```

## Examples
```swift
// Example: Verifying profile includes distribution
// $ security cms -D -i profile.mobileprovision | \
//   plutil -extract DeveloperCertificates -o - - | \
//   plutil -convert xml1 -

// Look for multiple certificates:
// - iPhone Developer: ... (development)
// - iPhone Distribution: ... (distribution)
// Both should be present for universal profiles
```
