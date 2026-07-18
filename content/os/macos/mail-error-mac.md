---
title: "[Solution] macOS Mail Error — Cannot Send or Receive Email"
description: "Fix macOS Mail app error: cannot send or receive email, Mail account offline, Mail server connection failed, Mail crashes on launch."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 186
---

# Mail Error — Cannot Send or Receive Email

Fix macOS Mail app error: cannot send or receive email, Mail account offline, Mail server connection failed, Mail crashes on launch.

## Common Causes

- Mail account credentials incorrect or expired
- Mail server settings misconfigured for IMAP/POP3
- SSL/TLS settings incompatible with mail server
- Mail app corrupted preference files preventing launch

## How to Fix

### 1. Check Mail Account Settings

```bash
# Mail → Settings → Accounts → Verify server settings
# Ensure IMAP/POP3/SMTP server addresses and ports are correct
```

### 2. Rebuild Mailbox

```bash
# Mail → Mailbox → Rebuild
# This re-indexes all emails without deleting them
```

### 3. Delete and Re-add Mail Account

```bash
# Mail → Settings → Accounts → Select account → Remove account
# Add account back with correct credentials
```

### 4. Reset Mail Preferences

```bash
defaults delete com.apple.mail
rm -rf ~/Library/Mail
# Restart Mail app (accounts will need to be reconfigured)
```

## Common Scenarios

This error commonly occurs when:

- Mail shows 'Offline' status for IMAP or POP3 account
- Cannot send emails but can receive, or vice versa
- Mail crashes immediately on launch with error
- Mail syncs very slowly or stops syncing new emails

## Prevent It

- Verify mail server settings match provider documentation
- Keep email account credentials updated and current
- Use IMAP instead of POP3 for better multi-device sync
- Rebuild Mailbox index periodically for optimal performance
