---
title: "[Solution] macOS App Login Item Error — App Not Starting at Login"
description: "Fix macOS login item error: app not starting at login, cannot add or remove login items, login items missing, startup delay."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 209
---

# App Login Item Error — App Not Starting at Login

Fix macOS login item error: app not starting at login, cannot add or remove login items, login items missing, startup delay.

## Common Causes

- Login item corrupted or improperly configured
- Launch agent plist file missing executable reference
- macOS blocking login items for security reasons
- Login item conflicting with other startup processes

## How to Fix

### 1. Check Login Items

```bash
# System Settings → General → Login Items → Review list
# osascript -e 'tell application "System Events" to get name of every login item'
```

### 2. Add App as Login Item

```bash
# System Settings → General → Login Items → Add app via + button
```

### 3. Remove Problematic Login Items

```bash
# System Settings → General → Login Items → Select item → Remove via - button
```

### 4. Check Launch Agents

```bash
ls ~/Library/LaunchAgents/
ls /Library/LaunchAgents/
# Verify plist files point to valid executables
```

## Common Scenarios

This error commonly occurs when:

- App should start at login but doesn't appear in startup
- Login items list shows app but it doesn't launch at startup
- Cannot add app to login items in System Settings
- Too many login items causing slow startup

## Prevent It

- Manage login items through System Settings → General → Login Items
- Remove unnecessary login items to speed up Mac startup
- Verify launch agent plist files point to valid executables
- Restart Mac to verify login items work after making changes
