---
title: "[Solution] macOS App Uninstall Error — Cannot Delete App"
description: "Fix macOS app uninstall failure: cannot delete app, app leftover files, app still running after moving to trash, uninstall incomplete."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 208
---

# App Uninstall Error — Cannot Delete App

Fix macOS app uninstall failure: cannot delete app, app leftover files, app still running after moving to trash, uninstall incomplete.

## Common Causes

- App still running in background preventing deletion
- App installed with installer leaving background processes
- System integrity protection preventing app removal
- App has launch agents or daemons still active

## How to Fix

### 1. Force Quit and Delete App

```bash
killall -9 'App Name'
# Move app to Trash: drag to Trash or Command+Delete
```

### 2. Remove App Leftover Files

```bash
rm -rf ~/Library/Preferences/com.developer.appname*
rm -rf ~/Library/Caches/com.developer.appname*
rm -rf ~/Library/Application\ Support/AppName
```

### 3. Check for Background Processes

```bash
ps aux | grep -i 'appname'
# Kill any remaining background processes
```

### 4. Remove Login Items and Launch Agents

```bash
# System Settings → General → Login Items → Remove app
# Remove from ~/Library/LaunchAgents/ if present
```

## Common Scenarios

This error commonly occurs when:

- App bounces in Trash and refuses to be deleted
- Moving app to Trash says 'app is in use' even when closed
- Uninstalling app leaves preference files and caches behind
- App uninstaller fails to remove all components

## Prevent It

- Force quit app completely before moving to Trash
- Use Activity Monitor to find and kill background processes
- Clean up leftover files in Library folders after uninstalling
- Use app's built-in uninstaller if available for complete removal
