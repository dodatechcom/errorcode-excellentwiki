---
title: "[Solution] macOS Messages Error -- iMessage Not Sending or Receiving"
description: "Fix macOS Messages error when iMessage or SMS messages fail to send or receive. Resolve Messages app issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Messages Error -- iMessage Not Sending or Receiving

The Messages app on macOS handles iMessage and SMS conversations. Errors can include messages failing to send, not receiving messages, or the app showing 'Waiting for activation.'

## Common Causes
- Apple ID is not signed in or the session has expired
- iMessage is not enabled in Messages preferences
- Network connectivity issues
- Apple ID has been locked or disabled
- Time zone settings are incorrect causing message ordering issues

## How to Fix
1. Sign out of iMessage and sign back in
2. Ensure iMessage is enabled in Messages > Preferences > iMessage
3. Check internet connection
4. Contact Apple Support if the Apple ID is locked
5. Reset the Messages database

```bash
# Check Messages database
ls -la ~/Library/Messages/

# View Messages errors
log show --predicate 'process == "Messages"' --last 10m
```

## Examples

```bash
# Check iMessage registration status
# Messages > Preferences > iMessage > Settings
```

This error is common after changing an Apple ID password, when the network connection is unstable, or when the Messages database is corrupted.
