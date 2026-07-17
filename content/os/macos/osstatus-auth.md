---
title: "[Solution] macOS OSStatus Authentication Errors (-25293, -25291)"
description: "Fix macOS OSStatus authentication errors -25293 and -25291. Causes and solutions for Keychain and Security framework auth failures."
platforms: ["macos"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["osstatus", "authentication", "-25293", "-25291", "keychain", "security"]
weight: 5
---

# macOS OSStatus Authentication Errors (-25293, -25291)

OSStatus authentication errors are Security framework codes indicating failures in credential verification, Keychain access, or identity validation. These codes commonly appear in applications using Touch ID, certificate-based auth, or Keychain.

## What This Error Means

- `-25293 (errSecAuthFailed)` — Authentication failed. The user could not be authenticated for the requested operation.
- `-25291 (errSecNotAvailable)` — Keychain is not available. The security database cannot be accessed.

Both indicate failures in the Security framework's authentication pipeline, often triggered by incorrect credentials, locked Keychain, or certificate issues.

## Common Causes

- User entered incorrect password or credentials
- Keychain is locked (auto-lock or manual lock)
- Missing or expired certificates for certificate-based authentication
- Security entitlements missing from the application

## How to Fix

### Verify Keychain Access

```bash
# Check Keychain status
security default-keychain

# List keychains
security list-keychains

# Unlock default keychain
security unlock-keychain -p "yourpassword" ~/Library/Keychains/login.keychain-db
```

### Reset Keychain if Corrupted

```bash
# Backup keychain
cp ~/Library/Keychains/login.keychain-db ~/Library/Keychains/login.keychain-db.bak

# Delete and recreate
security delete-keychain ~/Library/Keychains/login.keychain-db
```

### Check Certificate Validity

```bash
# List certificates
security find-identity -v -p codesigning

# Verify certificate expiry
openssl x509 -in certificate.pem -noout -dates
```

### Add Keychain Access Entitlements

```xml
<key>keychain-access-groups</key>
<array>
    <string>$(AppIdentifierPrefix)com.yourcompany.yourapp</string>
</array>
```

## Related Errors

- [Core Foundation Errors]({{< relref "/os/macos/core-foundation" >}}) — Foundation-level errors that may cascade from auth failures
- [CloudKit Errors]({{< relref "/os/macos/cloudkit-error" >}}) — CloudKit authentication failures
- [Launch Services Errors (-10810, -10811)]({{< relref "/os/macos/launch-services-error" >}}) — App launch failures that may involve entitlements
