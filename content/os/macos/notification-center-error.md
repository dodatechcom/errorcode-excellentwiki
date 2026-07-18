---
title: "[Solution] macOS Notification Center Error — Notifications Not Showing"
description: "Fix macOS Notification Center not showing: notifications missing, Notification Center widget not loading, no alerts appearing."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 128
---

# Notification Center Error — Notifications Not Showing

Fix macOS Notification Center not showing: notifications missing, Notification Center widget not loading, no alerts appearing.

## Common Causes

- Notification Center daemon (notificationcenterd) crashed or stuck
- Focus mode blocking notifications from appearing in Notification Center
- Corrupted notification database or cache files
- App notification permissions disabled at system level

## How to Fix

### 1. Check Notification Center Status

```bash
ps aux | grep notificationcenterd
log show --predicate 'process == "notificationcenterd"' --last 1h | head -20
```

### 2. Restart Notification Center Daemon

```bash
killall notificationcenterd
killall usernoted
osascript -e 'display notification "Test" with title "Notification Test"'
```

### 3. Fix Notification Preferences

```bash
defaults delete com.apple.notificationcenterui
rm -rf ~/Library/Preferences/com.apple.notificationcenterui.plist
sudo shutdown -r now
```

### 4. Verify App Notification Permissions

```bash
#
 
S
y
s
t
e
m
 
S
e
t
t
i
n
g
s
 
→
 
N
o
t
i
f
i
c
a
t
i
o
n
s
 
→
 
F
i
n
d
 
a
p
p
 
→
 
A
l
l
o
w
 
N
o
t
i
f
i
c
a
t
i
o
n
s
 
O
N
```

## Common Scenarios

This error commonly occurs when:

- Notification Center sidebar shows no notifications from any app
- New notifications appear briefly then disappear from screen
- Notification Center widgets show loading spinner indefinitely
- Notifications work for some apps but not others

## Prevent It

- Keep macOS updated to receive Notification Center stability fixes
- Review notification settings for each app after major macOS updates
- Restart Mac periodically to prevent notification daemon memory leaks
- Check Focus mode settings if notifications suddenly stop appearing
