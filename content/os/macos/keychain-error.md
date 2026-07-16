---
title: "[Solution] macOS Keychain Error — An Error Has Occurred"
description: "Fix macOS Keychain 'An error has occurred' error. Reset keychain, unlock keychain access, and fix iCloud Keychain sync issues on Mac."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
tags: ["keychain", "password", "icloud-keychain", "access", "unlock"]
weight: 5
---

# Keychain Error — An Error Has Occurred

A Keychain error occurs when macOS cannot access, unlock, or modify the keychain database that stores passwords, certificates, and encryption keys. The most common message is simply "An error has occurred" with no further detail, making it frustrating to diagnose.

## Description

The keychain stores credentials for Wi-Fi networks, websites, apps, and certificates. When the keychain is corrupted, locked, or out of sync with iCloud, apps can't retrieve saved passwords.

Common error messages:

- `An error has occurred. (-25300)`
- `An error has occurred. (-67050)`
- `Keychain "login" is locked.`
- `The specified item could not be found in the keychain.`

## Common Causes

- Keychain password is out of sync with the login password
- Corrupted keychain database after macOS update
- iCloud Keychain sync conflict between devices
- Disk corruption damaging the keychain file

## How to Fix Keychain Errors

### 1. Unlock the Login Keychain

```bash
# Open Keychain Access (Spotlight → "Keychain Access")
# Select "login" keychain in the sidebar
# Right-click → "Lock Keychain" then "Unlock Keychain"
# Enter your login password
```

### 2. Reset the Keychain Password

```bash
# Open Keychain Access
# Edit → Change Keychain "login" Password
# Enter old password (your current login password)
# Enter new password (set it to your current login password)
```

### 3. Delete and Recreate the Keychain

```bash
# WARNING: This deletes all saved passwords
# Open Keychain Access
# Keychain Access → Settings → "Reset My Default Keychain"
# Enter your Mac login password to create a new keychain
```

### 4. Fix iCloud Keychain Sync Issues

```bash
# System Settings → Apple ID → iCloud → Keychain
# Toggle iCloud Keychain OFF, wait 30 seconds, toggle ON
# Restart your Mac and wait for sync to complete
```

### 5. Delete Corrupted Keychain Files

```bash
# First back up the keychain
mkdir -p ~/Library/Keychains/backup
cp -r ~/Library/Keychains/login.keychain-db ~/Library/Keychains/backup/

# Delete the corrupted keychain (will prompt to recreate)
rm ~/Library/Keychains/login.keychain-db

# Restart Mac — a new keychain will be created
```

## Examples

This error commonly occurs when:

- After resetting your Mac login password without updating the keychain password
- After a macOS major upgrade (e.g., Ventura → Sonoma) corrupts the keychain database
- When iCloud Keychain sync is stuck between multiple Apple devices
- After migrating to a new Mac with Migration Assistant

## Related Errors

- [iCloud Error](icloud-error) — iCloud sync failures affecting Keychain
- [SIP Error](sip-error) — System Integrity Protection may block keychain modifications
- [Finder Error](finder-error) — unable to access keychain-stored credentials from apps
