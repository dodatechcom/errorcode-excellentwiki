---
title: "[Solution] macOS Startup Item Error -- App Not Launching at Startup"
description: "Fix macOS startup item error when apps that should launch at startup are not starting. Resolve startup item issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Startup Item Error -- App Not Launching at Startup

Startup items are apps or services that launch automatically when macOS starts. When they fail to launch, background services like sync tools, security software, or utilities do not start.

## Common Causes
- Login item is disabled or removed from Login Items
- Launch Agent plist file is corrupted or missing
- App was updated and the Launch Agent path changed
- macOS security settings are blocking the startup item
- The app requires specific permissions to run at startup

## How to Fix
1. Check System Settings > General > Login Items (macOS Ventura+)
2. Verify the Launch Agent plist file exists and is valid
3. Reinstall the app to recreate the startup item
4. Check Console.app for startup item crash logs
5. Ensure the app has the necessary permissions

```bash
# List login items
osascript -e 'tell application "System Events" to get the name of every login item'

# Check Launch Agents
ls -la ~/Library/LaunchAgents/
ls -la /Library/LaunchAgents/

# Validate a Launch Agent plist
plutil -lint ~/Library/LaunchAgents/com.example.agent.plist
```

## Examples

```bash
# Check Launch Agent status
launchctl list | grep -i example
```

This error is common after an app update changes the Launch Agent path, when the Launch Agent plist is corrupted, or when macOS security settings block the startup item.
