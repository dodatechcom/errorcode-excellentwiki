---
title: "[Solution] Provisioning Profile Not Found for Bundle Identifier"
description: "Fix missing provisioning profile errors for your app bundle identifier."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Provisioning Profile Not Found for Bundle Identifier

This error occurs when Xcode cannot find a provisioning profile matching your app's bundle identifier. The profile may not be installed or may not exist in the portal.

## Common Causes
- Provisioning profile was never created for this bundle ID
- Profile deleted from developer portal
- Xcode cache does not include the profile
- Free developer account limits on profiles

## How to Fix
1. Create a new provisioning profile in the developer portal
2. Download and install it by double-clicking
3. Refresh Xcode's profile list via Preferences > Accounts
4. For automatic signing, let Xcode create it automatically

```swift
// Create profile in developer portal:
// 1. Go to https://developer.apple.com/account/resources/profiles
// 2. Click "+" to create new profile
// 3. Select iOS App Development
// 4. Select your app's bundle identifier
// 5. Select your certificate
// 6. Download and install
```

## Examples
```swift
// Example: Listing installed profiles
// $ ls ~/Library/MobileDevice/Provisioning\ Profiles/

// Or use fastlane to manage:
// $ fastlane sigh

// For automatic signing, ensure:
// Target > Signing & Capabilities > Automtically manage signing = YES
```
