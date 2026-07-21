---
title: "[Solution] Code Signing Error: Cannot Sign with Apple ID"
description: "Fix Apple ID code signing errors in Xcode for personal development."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Code Signing Error: Cannot Sign with Apple ID

Personal Apple ID signing requires a free Apple Developer account. Certain features and distribution methods are not available with free accounts.

## Common Causes
- Apple ID not verified for development
- Attempting to distribute with free account
- Device limit reached for free accounts
- Certificates expired for free developer account

## How to Fix
1. Verify your Apple ID in Xcode preferences
2. Register devices before building
3. Limit to 3 devices per platform for free accounts
4. Consider a paid Apple Developer account for full features

```swift
// Verify Apple ID in Xcode:
// Xcode > Settings > Accounts > Select your Apple ID

// For free accounts, you can:
// - Build and run on registered devices (max 3)
// - Use development provisioning profiles
// - Cannot submit to App Store or TestFlight
```

## Examples
```swift
// Example: Free account limitations
// Free Apple Developer account allows:
// - Building for simulator (unlimited)
// - Building for registered devices (max 3 iOS, 3 macOS)
// - Development provisioning profiles
// - Cannot create distribution profiles

// Paid account ($99/year) allows:
// - App Store submission
// - TestFlight beta testing
// - Up to 100 devices per platform
```
