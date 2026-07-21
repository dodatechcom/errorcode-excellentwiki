---
title: "[Solution] Code Signing Error: Provisioning Profile Does Not Match"
description: "Fix provisioning profile mismatch errors during code signing."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Code Signing Error: Provisioning Profile Does Not Match

This error means the provisioning profile does not match the certificate, bundle identifier, or entitlements required for signing.

## Common Causes
- Profile generated with a different certificate
- Bundle identifier changed after profile creation
- Profile does not include required entitlements
- Profile type does not match the build configuration

## How to Fix
1. Regenerate the provisioning profile with current settings
2. Ensure the bundle ID matches exactly
3. Include all required capabilities in the profile
4. Use automatic signing to keep profiles in sync

```swift
// Compare profile details with your project:
// 1. Certificate: Must match installed cert
// 2. Bundle ID: Must match project's CFBundleIdentifier
// 3. Entitlements: Must include all capabilities

// Check profile details:
// $ security cms -D -i embedded.mobileprovision | plutil - -
```

## Examples
```swift
// Example: Quick profile verification
// $ security cms -D -i embedded.mobileprovision | \
//   grep -E "(Name|AppIDName|application-identifier)"

// Output:
// AppIDName = MyApp Development
// application-identifier = ABCDE12345.com.example.myapp
```
