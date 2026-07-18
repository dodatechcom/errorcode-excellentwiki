---
title: "[Solution] macOS Disk Encryption Error — FileVault Encryption Stuck"
description: "Fix macOS disk encryption failure: FileVault encryption stuck at percentage, encryption cannot be enabled or disabled, encrypted disk locked."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 140
---

# Disk Encryption Error — FileVault Encryption Stuck

Fix macOS disk encryption failure: FileVault encryption stuck at percentage, encryption cannot be enabled or disabled, encrypted disk locked.

## Common Causes

- FileVault encryption process interrupted by system restart
- Corrupted encryption key in keychain
- Disk I/O errors preventing encryption from completing
- FileVault daemon (filevaultd) stuck or crashed

## How to Fix

### 1. Check FileVault Encryption Status

```bash
sudo fdesetup status
diskutil apfs list | grep -A 5 'Encryption'
```

### 2. Resume FileVault Encryption

```bash
# Encryption may resume automatically after restart
sudo fdesetup enable -user $(whoami)
```

### 3. Delete FileVault Keychain Entry

```bash
security delete-generic-password -s 'FileVault' ~/Library/Keychains/login.keychain-db
```

### 4. Decrypt and Re-encrypt FileVault

```bash
sudo fdesetup disable
# Wait for decryption to complete, then re-enable
```

## Common Scenarios

This error commonly occurs when:

- FileVault encryption stuck at same percentage for hours
- Cannot enable FileVault in System Settings → Privacy & Security
- FileVault decryption fails or takes extremely long
- Encryption key not found when unlocking disk at boot

## Prevent It

- Back up data before enabling FileVault encryption
- Keep sufficient battery and power connection during encryption
- Do not force restart Mac during FileVault encryption process
- Update macOS to receive FileVault encryption improvements
