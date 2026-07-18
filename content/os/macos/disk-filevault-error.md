---
title: "[Solution] macOS Disk FileVault Error — FileVault Decryption Failed"
description: "Fix macOS FileVault error: FileVault decryption failed, cannot unlock FileVault-encrypted disk at startup, recovery key not working."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 141
---

# Disk FileVault Error — FileVault Decryption Failed

Fix macOS FileVault error: FileVault decryption failed, cannot unlock FileVault-encrypted disk at startup, recovery key not working.

## Common Causes

- FileVault recovery key not properly stored or corrupted
- Keychain item storing FileVault credentials deleted
- FileVault encryption keys corrupted by disk error
- Multiple FileVault recovery attempts triggering security lockout

## How to Fix

### 1. Check FileVault Status and Recovery Key

```bash
sudo fdesetup status
sudo fdesetup validaterecovery
```

### 2. Use Recovery Key to Unlock Disk

```bash
# At FileVault login screen, click recovery key option
# Enter your 24-character FileVault recovery key
```

### 3. Reset FileVault from Recovery

```bash
# Recovery → Utilities → Terminal
sudo fdesetup disable
sudo fdesetup enable
```

### 4. Contact Apple Support for Recovery

```bash
# Visit https://support.apple.com/contact
# Use Apple ID to recover FileVault access if possible
```

## Common Scenarios

This error commonly occurs when:

- FileVault recovery key not accepted when unlocking disk at startup
- Cannot decrypt FileVault volume even with correct recovery key
- FileVault password not working after macOS update
- FileVault shows 'decryption failed' in System Settings

## Prevent It

- Store FileVault recovery key in a safe physical location
- Keep Apple ID credentials accessible for FileVault recovery
- Back up data regularly in case FileVault recovery is needed
- Test FileVault recovery key periodically to ensure it works
