---
title: "[Solution] macOS Calendar Error -- Calendar Events Not Syncing"
description: "Fix macOS Calendar error when calendar events are not syncing or displaying correctly. Resolve Calendar app issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Calendar Error -- Calendar Events Not Syncing

The Calendar app on macOS syncs events from iCloud, Google, Exchange, and other calendar services. When sync fails, events may be missing, duplicated, or showing incorrect times.

## Common Causes
- Calendar account credentials are expired or incorrect
- iCloud calendar sync is disabled
- Calendar database is corrupted
- Time zone settings are incorrect causing event misalignment
- Calendar subscription URL is invalid or expired

## How to Fix
1. Verify the calendar account credentials in System Preferences
2. Ensure iCloud calendar sync is enabled
3. Delete and re-add the calendar account
4. Check time zone settings in System Preferences > Date & Time
5. Refresh calendar subscriptions

```bash
# Check Calendar database
ls -la ~/Library/Application\ Support/Calendar/

# View Calendar errors
log show --predicate 'process == "Calendar"' --last 10m
```

## Examples

```bash
# Check time zone settings
systemsetup -gettimezone

# Set time zone automatically
systemsetup -setusingnetworktime on
```

This error is common after an account password change, when the time zone is incorrect causing event misalignment, or when the Calendar database is corrupted.
