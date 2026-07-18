---
title: "[Solution] macOS App Notification Error — Notifications Not Showing"
description: "Fix macOS app notification error: notifications not showing for app, notification badge stuck, notification settings lost."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 210
---

# App Notification Error — Notifications Not Showing

Fix macOS app notification error: notifications not showing for app, notification badge stuck, notification settings lost.

## Common Causes

- App notification permissions disabled at system level
- Focus mode blocking notifications from specific app
- Notification settings corrupted after macOS update
- App not properly registered with Notification Center

## How to Fix

### 1. Check App Notification Settings

```bash
# System Settings → Notifications → Find app → Allow Notifications ON
# Verify alert style, sound, and badge settings
```

### 2. Reset Notification Preferences

```bash
defaults delete com.apple.notificationcenterui
rm -rf ~/Library/Caches/com.apple.notificationcenter*
sudo shutdown -r now
```

### 3. Restart Notification Center

```bash
killall notificationcenterd
killall usernoted
```

### 4. Test Notification

```bash
osascript -e 'display notification "Test" with title "Notification Test"'
```

## Common Scenarios

This error commonly occurs when:

- App notifications stopped appearing after macOS update
- Notification badge shows wrong number for app
- Notification sounds not playing for specific app
- Notification Center shows old notifications but not new ones

## Prevent It

- Review notification settings for each app after macOS updates
- Restart notification center daemon if notifications stop appearing
- Keep macOS updated for Notification Center compatibility
- Check Focus mode settings if notifications from specific apps are blocked
