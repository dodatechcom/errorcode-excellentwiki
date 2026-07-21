---
title: "[Solution] macOS Contacts Permission Error -- App Cannot Access Contacts"
description: "Fix macOS contacts permission error when an app cannot access your contacts. Resolve contacts permission issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Contacts Permission Error -- App Cannot Access Contacts

Apps need contacts permission to read or modify your address book. When permission is not granted, apps like Mail, Messages, and third-party apps cannot access contact information.

## Common Causes
- Contacts permission was not granted in System Preferences
- App was updated and needs permission re-granted
- TCC database is corrupted
- Contacts database is corrupted
- MDM profile is restricting contacts access

## How to Fix
1. Open System Preferences > Privacy & Security > Contacts
2. Add the app to the allowed list
3. Check that the Contacts app can open and display contacts
4. Reset contacts permissions and re-grant them
5. Rebuild the Contacts database if corrupted

```bash
# Check contacts permissions
sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db "SELECT client FROM access WHERE service='kTCCServiceAddressBook';"

# Reset contacts permissions
tccutil reset AddressBook
```

## Examples

```bash
# Check Contacts database
ls -la ~/Library/Application\ Support/AddressBook/
```

This error is common after updating an app when permissions need to be re-granted, when the TCC database is corrupted, or when the Contacts database is corrupted.
