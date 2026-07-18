---
title: "[Solution] macOS Spinning Wheel Error — Wait Cursor Freezes System"
description: "Fix macOS spinning wait cursor: rainbow wheel appears over apps, system slows or freezes, requires waiting or force quitting."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 102
---

# Spinning Wheel Error — Wait Cursor Freezes System

Fix macOS spinning wait cursor: rainbow wheel appears over apps, system slows or freezes, requires waiting or force quitting.

## Common Causes

- Application performing long-running operation on main thread
- Insufficient free memory causing system to page to disk
- Background process consuming CPU and starving foreground apps
- Corrupted application cache or preference causing infinite loop

## How to Fix

### 1. Monitor System Activity

```bash
ps aux --sort=-%cpu | head -15
vm_stat | head -10
```

### 2. Force Quit Frozen Applications

```bash
killall -9 'Safari'
osascript -e 'tell application "System Events" to get name of every process whose background only is false'
```

### 3. Clear System Caches

```bash
rm -rf ~/Library/Caches/*
sudo rm -rf /Library/Caches/*
sudo atsutil databases -remove
sudo shutdown -r now
```

### 4. Optimize Performance Settings

```bash
# System Settings → Accessibility → Display → Reduce Motion
# Close unnecessary login items in System Settings → General
```

## Common Scenarios

This error commonly occurs when:

- Spinning wheel appears when scrolling through large PDF documents
- System shows spinning wheel when switching virtual desktops
- Wheel cursor appears when opening large image files
- Spinning wheel occurs system-wide after Mac running for days

## Prevent It

- Restart Mac at least once a week to clear accumulated caches
- Limit the number of simultaneously open applications
- Keep sufficient free disk space for virtual memory operations
- Use Activity Monitor to identify slow background processes
