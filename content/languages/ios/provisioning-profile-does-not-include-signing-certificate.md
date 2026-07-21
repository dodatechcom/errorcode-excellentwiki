---
title: "[Solution] Provisioning Profile Does Not Include Signing Certificate"
description: "Fix provisioning profile certificate mismatch errors in Xcode."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Provisioning Profile Does Not Include Signing Certificate

This error means the provisioning profile you are using does not contain the signing certificate installed in your keychain. The profile and certificate must be paired.

## Common Causes
- Profile generated with a different certificate
- Certificate was regenerated and old profile not updated
- Distribution certificate replaced but profile not re-generated
- Team member changed roles and certificates differ

## How to Fix
1. Regenerate the provisioning profile with the current certificate
2. Download and install the new profile from the developer portal
3. For automatic signing, let Xcode regenerate the profile
4. Revoke old certificates if they are no longer needed

```swift
// To regenerate a provisioning profile:
// 1. Go to developer.apple.com/account/resources/profiles
// 2. Click Edit on the existing profile
// 3. Re-select the current certificate
// 4. Download the updated profile

// For automatic signing in Xcode:
// Target > Signing & Capabilities > check "Automatically manage signing"
// Xcode will regenerate profiles as needed
```

## Examples
```swift
// Example: Verifying profile-certificate match
// List installed certificates:
// $ security find-identity -v -p codesigning

// Extract profile certificate info:
// $ security cms -D -i embedded.mobileprovision | grep -A2 "Developer"

// Compare the two outputs to verify they match
```
