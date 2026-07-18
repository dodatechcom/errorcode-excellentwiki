---
title: "[Solution] macOS Stage Manager Error — Window Management Not Working"
description: "Fix macOS Stage Manager issues: windows not organizing properly, app thumbnails missing, stage groups broken, cannot focus apps."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 126
---

# Stage Manager Error — Window Management Not Working

Fix macOS Stage Manager issues: windows not organizing properly, app thumbnails missing, stage groups broken, cannot focus apps.

## Common Causes

- Stage Manager feature disabled in System Settings
- Corrupted window manager preferences or cache
- Stage Manager conflicting with multiple display configuration
- App not compatible with Stage Manager window management

## How to Fix

### 1. Enable and Configure Stage Manager

```bash
defaults read com.apple.WindowManager
# System Settings → Desktop & Dock → Stage Manager → Toggle ON
```

### 2. Reset Stage Manager Preferences

```bash
defaults delete com.apple.WindowManager
defaults write com.apple.dock ResetLaunchPad -bool true; killall Dock
sudo shutdown -r now
```

### 3. Fix Multiple Display Issues

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
 
D
i
s
p
l
a
y
s
 
→
 
A
d
v
a
n
c
e
d
 
→
 
S
e
t
 
t
o
 
e
x
t
e
n
d
e
d
 
m
o
d
e
```

### 4. Reset Window Management State

```bash
rm -f ~/Library/Preferences/com.apple.WindowManager.plist
killall Dock
```

## Common Scenarios

This error commonly occurs when:

- Stage Manager groups show wrong apps in thumbnail view
- Windows not automatically organizing when Stage Manager is enabled
- Stage Manager stops working after connecting external display
- Clicking stage group does not bring apps to foreground

## Prevent It

- Keep macOS updated for Stage Manager bug fixes and improvements
- Avoid force-quitting apps which can corrupt window manager state
- Restart Mac if Stage Manager groups become unresponsive
- Configure Stage Manager display settings for multi-monitor setups
