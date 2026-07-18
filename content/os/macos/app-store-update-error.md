---
title: "[Solution] macOS App Store Update Error — Updates Not Appearing"
description: "Fix macOS App Store update failure: updates not appearing, update stuck downloading, App Store update error message."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 192
---

# App Store Update Error — Updates Not Appearing

Fix macOS App Store update failure: updates not appearing, update stuck downloading, App Store update error message.

## Common Causes

- App Store not checking for updates correctly
- Update server connection issue
- App Store update cache not refreshing
- macOS update notification system not triggering

## How to Fix

### 1. Check for Updates Manually

```bash
softwareupdate -l
# Or open App Store → Updates tab
```

### 2. Force App Store to Refresh

```bash
# App Store → Store → Reload Page (Command+R)
rm -rf ~/Library/Caches/com.apple.appstore
killall 'App Store'
```

### 3. Reset App Store Update Preferences

```bash
defaults delete com.apple.appstore
defaults write com.apple.appstore ShowUpdateStatusBar -bool true
killall 'App Store'
```

### 4. Install Updates via Terminal

```bash
softwareupdate -i -a
# This installs all available updates bypassing App Store UI
```

## Common Scenarios

This error commonly occurs when:

- App Store shows no updates available but apps are outdated
- Update download starts but never completes
- App Store update tab shows loading spinner indefinitely
- App Store says updates available but won't install

## Prevent It

- Check for updates via terminal if App Store UI fails
- Clear App Store cache to force update list refresh
- Keep macOS updated to maintain App Store update compatibility
- Use 'softwareupdate' command as backup for App Store updates
