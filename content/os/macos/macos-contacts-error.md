---
title: "[Solution] macOS Contacts Error -- Contacts App Not Syncing or Crashing"
description: "Fix macOS Contacts error when the Contacts app crashes, shows duplicate entries, or fails to sync. Resolve Contacts issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Contacts Error -- Contacts App Not Syncing or Crashing

The Contacts app on macOS stores and syncs your contact information. Errors can include duplicate contacts, sync failures with iCloud, or the app crashing when opened.

## Common Causes
- Contacts database is corrupted
- iCloud sync is conflicting with local contacts
- vCard import created duplicate or malformed entries
- Contact groups are pointing to deleted accounts
- Spotlight indexing is interfering with Contacts database

## How to Fix
1. Rebuild the Contacts database from the Contacts app
2. Sign out of iCloud and back in to resync contacts
3. Export contacts, delete all, and re-import from the backup
4. Check for duplicate entries and merge them
5. Delete the Contacts cache and let it rebuild

```bash
# Check Contacts database
ls -la ~/Library/Application\ Support/AddressBook/

# Delete Contacts cache
rm -rf ~/Library/Application\ Support/AddressBook/AddressBook-v22.*
```

## Examples

```bash
# View Contacts errors in logs
log show --predicate 'process == "Contacts"' --last 10m
```

This error is common after importing a large number of vCards, when iCloud sync creates duplicate entries, or when the Contacts database becomes corrupted.
