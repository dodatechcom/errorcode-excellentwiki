---
title: "[Solution] macOS Login Item Error -- App Cannot Be Added to Login Items"
description: "Fix macOS login item error when apps cannot be added to or removed from login items. Resolve login items issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Login Item Error -- App Cannot Be Added to Login Items

Login items are apps that start automatically when you log in. When you cannot add or remove login items, the app may not launch at startup or unwanted apps may keep launching.

## Common Causes
- Login Items preferences file is corrupted
- App is using a Launch Agent instead of Login Items
- System Integrity Protection is blocking the modification
- MDM profile is restricting login item changes
- macOS Ventura+ moved login items to a new settings location

## How to Fix
1. Check System Settings > General > Login Items (macOS Ventura+)
2. For older macOS, check System Preferences > Users & Groups > Login Items
3. Delete the corrupted login items preferences file
4. Remove Launch Agents that are adding login items
5. Use terminal to manage login items

```bash
# List login items
osascript -e 'tell application "System Events" to get the name of every login item'

# Remove a login item
osascript -e 'tell application "System Events" to delete login item "AppName"'

# Check Launch Agents
ls -la ~/Library/LaunchAgents/
ls -la /Library/LaunchAgents/
```

## Examples

```bash
# Check Launch Daemons
ls -la /Library/LaunchDaemons/ | grep -v com.apple
```

This error is common when the login items preferences file is corrupted, when apps use Launch Agents instead of the standard Login Items mechanism, or when MDM profiles restrict login item changes.
