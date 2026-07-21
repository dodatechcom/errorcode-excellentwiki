---
title: "[Solution] Code Signing Error: Private Key Not Found"
description: "Fix missing private key errors for code signing certificates."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Code Signing Error: Private Key Not Found

The private key associated with your signing certificate is missing from the keychain. Without the private key, the certificate cannot be used for signing.

## Common Causes
- Private key was deleted from keychain
- Certificate imported without its private key
- Keychain access list does not include codesign
- Private key is in a different keychain

## How to Fix
1. Verify the private key is nested under the certificate in Keychain Access
2. Export the certificate and key as .p12 from another Mac
3. Import the .p12 file into your keychain
4. Grant codesign access to the private key

```swift
// Export certificate with private key:
// Keychain Access > Certificates > right-click > Export
// Format: Personal Information Exchange (.p12)

// Import on new machine:
// Double-click the .p12 file
// Enter the export password
```

## Examples
```swift
// Example: Checking keychain for private key
// $ security find-certificate -a -c "iPhone Developer" | \
//   grep "alis"

// If no private key, export .p12 from the original machine
// and import it on the current machine
```
