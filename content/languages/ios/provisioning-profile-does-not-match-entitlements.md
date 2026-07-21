---
title: "[Solution] Provisioning Profile Does Not Match Entitlements"
description: "Fix entitlements and provisioning profile mismatch errors in Xcode."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Provisioning Profile Does Not Match Entitlements

This error appears when your app's entitlements file references capabilities not included in the provisioning profile. The profile must contain all entitlements your app uses.

## Common Causes
- Added new capability without regenerating profile
- iCloud entitlements require specific container IDs
- App Groups not configured in the portal
- Push notification environment (development vs production) mismatch

## How to Fix
1. Add the missing capability in the developer portal
2. Regenerate the provisioning profile
3. Download and install the new profile
4. Verify entitlements match in Xcode's Signing & Capabilities

```swift
// Check your entitlements file:
// YourApp.entitlements contains:
// - com.apple.security.application-groups
// - com.apple.developer.icloud-container-identifiers
// - aps-environment

// Each entitlement must be enabled in the portal
// and included in the provisioning profile
```

## Examples
```swift
// Example: Comparing entitlements with profile
// Extract profile entitlements:
// $ security cms -D -i embedded.mobileprovision | \
//   plutil -extract Entitlements -o - - | \
//   plutil -convert xml1 -

// Compare with your .entitlements file
// They should match for all keys
```
