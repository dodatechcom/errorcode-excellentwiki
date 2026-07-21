---
title: "[Solution] Provisioning Profile App ID Does Not Match"
description: "Fix App ID mismatches between provisioning profile and project."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Provisioning Profile App ID Does Not Match

The App ID in the provisioning profile must match your project's bundle identifier exactly. Mismatches prevent successful code signing.

## Common Causes
- App ID was modified after profile creation
- Wildcard App ID used where explicit App ID required
- Bundle identifier changed in project but not in portal
- iCloud or push notifications require explicit App ID

## How to Fix
1. Verify the App ID in the developer portal matches your bundle ID
2. Create a new explicit App ID if needed
3. Regenerate the provisioning profile with the correct App ID
4. For capabilities requiring explicit App ID, use exact bundle ID

```swift
// Explicit App IDs are required for:
// - iCloud
// - Push Notifications
// - App Groups
// - Keychain Sharing

// Wildcard App IDs (com.example.*) cannot use these features
// Use explicit App ID: com.example.myapp
```

## Examples
```swift
// Example: App ID configuration in developer portal
// 1. Go to https://developer.apple.com/account/resources/identifiers
// 2. Create new App ID or edit existing
// 3. Set Bundle ID to exact match: com.example.myapp
// 4. Enable required capabilities (iCloud, Push, etc.)
// 5. Regenerate provisioning profile for this App ID
```
