---
title: "[Solution] macOS Disk FileVault Recovery — Lost Recovery Key Issues"
description: "Fix macOS FileVault recovery key issues: lost recovery key, cannot unlock disk, keychain not storing recovery key properly."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 142
---

# Disk FileVault Recovery — Lost Recovery Key Issues

Fix macOS FileVault recovery key issues: lost recovery key, cannot unlock disk, keychain not storing recovery key properly.

## Common Causes

- FileVault recovery key not saved during initial encryption
- Recovery key stored in keychain but keychain corrupted
- Institutional recovery key no longer available
- Apple ID FileVault recovery not configured

## How to Fix

### 1. Check for Recovery Key in Keychain

```bash
security find-generic-password -s 'FileVault' ~/Library/Keychains/login.keychain-db
security dump-keychain -d login
```

### 2. Use Institutional Recovery Key

```bash
# Enter institutional recovery key at FileVault unlock screen
```

### 3. Reset FileVault with Apple ID Recovery

```bash
# System Settings → Apple ID → iCloud → Turn on 'Use Apple ID for FileVault'
```

### 4. Contact Apple for Recovery

```bash
# Visit Apple Support with proof of purchase
# Apple can provide recovery assistance for FileVault-encrypted Macs
```

## Common Scenarios

This error commonly occurs when:

- Recovery key cannot be found in keychain or physical location
- FileVault locked out with no available recovery method
- Institutional key no longer works after server migration
- Apple ID FileVault recovery option not available

## Prevent It

- Always save FileVault recovery key in multiple safe locations
- Enable Apple ID FileVault recovery as a backup recovery method
- Store institutional recovery key securely outside the Mac
- Test FileVault recovery procedures before emergency situations
