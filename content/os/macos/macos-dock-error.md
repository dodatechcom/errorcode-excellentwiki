---
title: "[Solution] macOS Dock Error -- Dock Not Showing or Crashing"
description: "Fix macOS Dock error when the Dock disappears, crashes, or icons are missing. Resolve Dock issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Dock Error -- Dock Not Showing or Crashing

The Dock is the application launcher and switcher at the bottom (or side) of the screen. When it crashes, it may disappear entirely, show blank spaces, or fail to respond to clicks.

## Common Causes
- Dock preference files are corrupted
- A Dock customization app is interfering
- Dock process crashed due to a corrupted icon cache
- Multiple displays are causing Dock rendering issues
- macOS update changed Dock behavior

## How to Fix
1. Force quit and restart the Dock process
2. Delete Dock preference files and restart
3. Remove third-party Dock customization apps
4. Reset the Dock to its default layout
5. Restart the Mac to clear all Dock-related caches

```bash
# Restart the Dock
killall Dock

# Delete Dock preferences (resets to default)
defaults delete com.apple.dock

# Restart to apply changes
killall Dock
```

## Examples

```bash
# Check Dock crash reports
ls -lt ~/Library/Logs/DiagnosticReports/ | grep -i Dock

# View Dock process status
ps aux | grep -i Dock
```

This error is common after installing a Dock customization app, after a macOS update changes Dock behavior, or when a corrupted icon causes the Dock to crash on restart.
