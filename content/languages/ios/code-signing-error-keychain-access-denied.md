---
title: "[Solution] Code Signing Error: Keychain Access Denied"
description: "Fix keychain access denied errors during Xcode code signing."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Code Signing Error: Keychain Access Denied

Keychain access errors prevent codesign from reading the private key needed for signing. This is common in CI/CD environments.

## Common Causes
- Keychain is locked during build
- Private key access not granted to codesign
- CI environment keychain not properly configured
- Keychain ACL does not include the signing identity

## How to Fix
1. Unlock the keychain before signing
2. Grant codesign access to the private key
3. For CI, use a custom keychain with proper settings
4. Set keychain timeout to allow long builds

```swift
// Unlock keychain for CI builds:
// $ security unlock-keychain -p "password" ~/Library/Keychains/login.keychain-db

// Set keychain timeout:
// $ security set-keychain-settings -t 3600 ~/Library/Keychains/login.keychain-db

// Add keychain to search list:
// $ security list-keychains -d user -s login.keychain-db
```

## Examples
```swift
// Example: CI keychain setup script
#!/bin/bash
KEYCHAIN_NAME="build.keychain"
KEYCHAIN_PASSWORD="password"

# Create keychain
security create-keychain -p "$KEYCHAIN_PASSWORD" "$KEYCHAIN_NAME"
security set-keychain-settings -lut 21600 "$KEYCHAIN_NAME"
security unlock-keychain -p "$KEYCHAIN_PASSWORD" "$KEYCHAIN_NAME"

# Import certificate
security import cert.p12 -k "$KEYCHAIN_NAME" -P "cert-password" -T /usr/bin/codesign

# Set keychain search list
security list-keychains -d user -s "$KEYCHAIN_NAME" login.keychain-db
```
