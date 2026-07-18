---
title: "[Solution] macOS Beachball Cursor Error — Spinning Rainbow Wheel"
description: "Fix macOS spinning beachball cursor: rainbow wheel appears over apps, apps become unresponsive, system slows down significantly."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 101
---

# Beachball Cursor Error — Spinning Rainbow Wheel

Fix macOS spinning beachball cursor: rainbow wheel appears over apps, apps become unresponsive, system slows down significantly.

## Common Causes

- App consuming excessive CPU or memory resources
- Low available RAM causing heavy swap usage and disk thrashing
- Slow or failing storage drive causing I/O bottlenecks
- Network-dependent app waiting on slow server response

## How to Fix

### 1. Identify Resource-Heavy Processes

```bash
top -l 1 -o cpu -n 10
memory_pressure
df -h /
```

### 2. Kill Unresponsive Apps

```bash
killall -9 'App Name'
# Press Command+Option+Escape for Force Quit window
```

### 3. Free Up Disk Space and RAM

```bash
df -h /
sudo rm -rf ~/Library/Caches/*
rm -rf ~/Library/Caches/com.apple.Safari
sudo shutdown -r now
```

### 4. Optimize System Performance

```bash
# System Settings → Accessibility → Display → Reduce Motion
# System Settings → General → Login Items → Remove unneeded apps
```

## Common Scenarios

This error commonly occurs when:

- Beachball appears when switching between apps with many tabs
- System becomes sluggish with beachball during Time Machine backup
- Safari shows persistent beachball on media-heavy websites
- Beachball occurs in Finder when copying large files to external drive

## Prevent It

- Close unused apps and browser tabs to conserve RAM and CPU
- Keep at least 15% of startup disk free for swap and caches
- Upgrade to SSD if Mac still uses mechanical hard drive
- Monitor Activity Monitor regularly to catch resource hogs early
