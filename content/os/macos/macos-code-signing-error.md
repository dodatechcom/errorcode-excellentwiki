---
title: "[Solution] macOS Code Signing Error"
description: "Fix code signing errors on Mac when building, archiving, or distributing apps. Resolve 'code signing failed' and identity issues."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# macOS Code Signing Error Fix

Code signing errors occur when Xcode or `codesign` cannot properly sign an app binary. This prevents distribution and notarization. Common messages include "Code signing failed" or "No identity found for signing."

## What This Error Means

Code signing ensures the app hasn't been tampered with and identifies the developer. Errors can occur due to missing certificates, expired provisioning profiles, or incorrect signing configurations.

## Common Causes

- Developer ID certificate expired or revoked
- Provisioning profile doesn't match the app's bundle ID
- Missing entitlements (e.g., hardened runtime)
- Keychain not unlocked
- Multiple signing identities conflicting

## How to Fix

### 1. Verify signing identity

```bash
# List available signing identities
security find-identity -v -p codesigning

# Check certificate expiration
security find-certificate -c "Developer ID Application" -p | openssl x509 -noout -dates
```

### 2. Sign manually with explicit identity

```bash
# Sign the app
codesign --force --sign "Developer ID Application: Your Name (TEAMID)" \
    --options runtime --entitlements entitlements.plist MyApp.app

# Verify the signature
codesign --verify --deep --strict MyApp.app
```

### 3. Fix keychain access

```bash
# Ensure the signing certificate is in the login keychain
security list-keychains

# Unlock the keychain
security unlock-keychain -p "your-password" ~/Library/Keychains/login.keychain-db
```

### 4. Check provisioning profile

```bash
# List installed provisioning profiles
ls ~/Library/MobileDevice/Provisioning\ Profiles/

# Check profile details
security cms -D -i ~/Library/MobileDevice/Provisioning\ Profiles/profile.mobileprovision
```

## Related Errors

- [Notarization Error](macos-notarization-error) — notarization submission failures
- [Xcode Error](macos-xcode-error) — Xcode build errors
- [Provisioning Error](macos-provisioning-error) — provisioning profile issues
