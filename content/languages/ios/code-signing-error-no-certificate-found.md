---
title: "[Solution] Code Signing Error: No Certificate Found"
description: "Fix missing code signing certificate errors in Xcode."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Code Signing Error: No Certificate Found

This error occurs when Xcode cannot find a valid signing certificate. The certificate may not be installed, or it may have been revoked.

## Common Causes
- Certificate not installed in Keychain Access
- Certificate was revoked by Apple
- Keychain does not include the certificate's private key
- Certificate expired

## How to Fix
1. Open Keychain Access and verify the certificate exists
2. Download a new certificate from the developer portal
3. Ensure the private key is associated with the certificate
4. Check certificate expiration in Keychain Access

```swift
// List installed certificates:
// $ security find-identity -v -p codesigning

// Check certificate expiry:
// $ security find-certificate -c "iPhone Developer" -p | \
//   openssl x509 -noout -dates

// Install certificate from portal:
// Download .cer file > double-click to install in Keychain
```

## Examples
```swift
// Example: Verifying certificate installation
// 1. Open Keychain Access
// 2. Select "login" keychain
// 3. Search for "iPhone" or "Apple Development"
// 4. Verify certificate is present and not expired
// 5. Ensure the private key is nested under the certificate
```
