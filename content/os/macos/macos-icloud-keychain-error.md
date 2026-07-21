---
title: "[Solution] macOS iCloud Keychain Error -- iCloud Keychain Not Syncing"
description: "Fix macOS iCloud Keychain error when iCloud Keychain passwords are not syncing between devices. Resolve iCloud Keychain sync issues."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS iCloud Keychain Error -- iCloud Keychain Not Syncing

iCloud Keychain syncs your saved passwords, Wi-Fi passwords, and payment card numbers across all your Apple devices. When sync fails, passwords saved on one device do not appear on others.

## Common Causes
- iCloud Keychain is not enabled on one or more devices
- Two-factor authentication is not enabled for the Apple ID
- iCloud account needs to be re-authenticated
- Keychain escrow record is corrupted
- Network connectivity prevents sync

## How to Fix
1. Ensure iCloud Keychain is enabled on all devices
2. Enable two-factor authentication for the Apple ID
3. Sign out of iCloud and sign back in on all devices
4. Check Apple's iCloud system status page
5. Reset iCloud Keychain if sync is consistently failing

```bash
# Check iCloud Keychain status
security show-keychain-info ~/Library/Keychains/iCloud.keychain-db

# Check iCloud account status
defaults read MobileMeAccounts
```

## Examples

```bash
# View iCloud Keychain sync logs
log show --predicate 'process == "keychain-sync"' --last 10m
```

This error is common when two-factor authentication is not enabled, when one device has iCloud Keychain disabled, or when the iCloud Keychain escrow record becomes corrupted.
