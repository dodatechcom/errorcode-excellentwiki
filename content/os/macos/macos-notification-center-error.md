---
title: "[Solution] macOS Notification Center Error -- Notifications Not Appearing"
description: "Fix macOS Notification Center error when notifications are not showing or Notification Center is not working. Resolve notification issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Notification Center Error -- Notifications Not Appearing

Notification Center displays alerts, banners, and widgets on macOS. When it fails, notifications may not appear, the widget panel may be empty, or Do Not Disturb may be stuck.

## Common Causes
- Notification Center preferences are corrupted
- Do Not Disturb or Focus mode is enabled
- App notification permissions are disabled
- Notification Center daemon has crashed
- Corrupted user account state

## How to Fix
1. Check Do Not Disturb and Focus mode settings
2. Verify notification permissions for the app in System Preferences
3. Restart Notification Center from terminal
4. Delete Notification Center preferences
5. Restart the Mac to reset all notification services

```bash
# Restart Notification Center
killall NotificationCenter

# Delete Notification Center preferences
defaults delete com.apple.notificationcenterui

# Check notification settings
defaults read com.apple.notificationcenterui
```

## Examples

```bash
# View Notification Center errors
log show --predicate 'process == "NotificationCenter"' --last 10m
```

This error is common when Do Not Disturb is accidentally enabled, when the Notification Center preferences are corrupted, or when the notification daemon crashes.
