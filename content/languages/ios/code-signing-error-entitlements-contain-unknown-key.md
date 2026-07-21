---
title: "[Solution] Code Signing Error: Entitlements Contain Unknown Key"
description: "Fix unknown entitlement key errors during code signing in Xcode."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Code Signing Error: Entitlements Contain Unknown Key

Unknown entitlement keys in your entitlements file cause signing failures. These keys may be outdated, misspelled, or from a different platform.

## Common Causes
- Copied entitlements from macOS project to iOS
- Misspelled entitlement key
- Entitlement key from older iOS version
- Custom entitlement from a specific framework

## How to Fix
1. Remove unknown entitlement keys from the .entitlements file
2. Verify each key against Apple's entitlements reference
3. Only include entitlements you actually use
4. Use Xcode's Signing & Capabilities to add entitlements properly

```swift
// Use Xcode to manage entitlements:
// Target > Signing & Capabilities > + Capability
// This adds the correct entitlement keys automatically

// Common iOS entitlement keys:
// - com.apple.developer.icloud-container-identifiers
// - com.apple.developer.aps-environment
// - com.apple.security.application-groups
// - keychain-access-groups
```

## Examples
```swift
// Example: Validating entitlements file
// Remove all unknown keys by starting fresh:
// 1. Delete existing .entitlements file
// 2. Add capabilities via Signing & Capabilities
// 3. Xcode creates correct entitlements file

// Or manually verify each key:
// $ plutil -lint YourApp.entitlements
```
