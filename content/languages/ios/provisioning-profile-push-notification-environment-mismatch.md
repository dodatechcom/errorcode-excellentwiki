---
title: "[Solution] Provisioning Profile Push Notification Environment Mismatch"
description: "Fix push notification provisioning profile environment errors in Xcode."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Provisioning Profile Push Notification Environment Mismatch

Push notification entitlements require the correct environment (development or production). Using the wrong environment causes notification delivery failures.

## Common Causes
- Development profile used for App Store build
- Production profile used for debug builds
- APNS certificate environment mismatch
- Entitlements file has wrong aps-environment value

## How to Fix
1. Use development profile for Debug builds
2. Use App Store profile for Release/Archive builds
3. Verify aps-environment in entitlements matches profile
4. Generate separate APNS certificates for dev and production

```swift
// In your .entitlements file:
// Debug: aps-environment = development
// Release: aps-environment = production

// Or use conditional compilation:
#if DEBUG
let apsEnvironment = "development"
#else
let apsEnvironment = "production"
#endif
```

## Examples
```swift
// Example: Configuring push notification environment
// 1. Check current entitlement:
// $ /usr/libexec/PlistBuddy -c "Print aps-environment" YourApp.entitlements

// 2. For App Store, it should be "production"
// 3. For development, it should be "development"

// 4. Create separate schemes:
// Debug scheme > Build Settings > Code Sign Entitlements
// Release scheme > Build Settings > Code Sign Entitlements
```
