---
title: "[Solution] macOS Notification Permission Error -- App Cannot Send Notifications"
description: "Fix macOS notification permission error when an app cannot send notifications. Resolve notification permission issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Notification Permission Error -- App Cannot Send Notifications

Apps need notification permission to display alerts, banners, and badges. When permission is not granted, the app cannot notify you of events.

## Common Causes
- Notification permission was not granted in System Preferences
- App was updated and needs permission re-granted
- TCC database is corrupted
- Do Not Disturb or Focus mode is blocking notifications
- Notification settings for the app are disabled

## How to Fix
1. Open System Preferences > Notifications & Focus
2. Find the app and enable notifications
3. Ensure Do Not Disturb is not blocking the app
4. Reset notification permissions and re-grant them
5. Restart the app after changing notification settings

```bash
# Check notification permissions
defaults read com.apple.notificationcenterui

# Reset notification permissions
tccutil reset Notifications
```

## Examples

```bash
# View notification center settings
defaults read com.apple.ncprefs
```

This error is common when notification permissions are not granted, when Do Not Disturb is blocking the app, or when the notification settings for the app are disabled.
