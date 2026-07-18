---
title: "[Solution] macOS WindowServer Error — Display Server Crashes"
description: "Fix macOS WindowServer crash or high CPU: display server consumes excessive memory causing UI lag or system crash."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 109
---

# WindowServer Error — Display Server Crashes

Fix macOS WindowServer crash or high CPU: display server consumes excessive memory causing UI lag or system crash.

## Common Causes

- Too many open windows or graphical elements exhausting GPU memory
- Corrupted WindowServer preferences or cache files
- Third-party app with heavy overlay or screen recording causing overload
- External display with high resolution consuming additional GPU resources

## How to Fix

### 1. Check WindowServer Resource Usage

```bash
top -l 1 -o mem -n 10 | grep WindowServer
sudo powermetrics --samplers gpu_power -n 1 -i 2000
ls -lt /Library/Logs/DiagnosticReports/WindowServer* | head -5
```

### 2. Close Windows and Reduce Visual Load

```bash
# System Settings → Accessibility → Display → Reduce Transparency
# System Settings → Accessibility → Display → Reduce Motion
```

### 3. Reset WindowServer Preferences

```bash
rm -f ~/Library/Preferences/ByHost/com.apple.windowserver.*.plist
rm -f ~/Library/Preferences/com.apple.display.plist
sudo shutdown -r now
```

### 4. Identify and Remove Problematic Apps

```bash
ps aux | grep -i 'screen\|record\|overlay'
# Quit screen recording or streaming apps temporarily
```

## Common Scenarios

This error commonly occurs when:

- WindowServer uses 8GB+ RAM when many browser tabs are open
- UI becomes sluggish with visual artifacts after extended uptime
- WindowServer crash report generated when disconnecting external display
- High WindowServer CPU coincides with screen sharing or recording

## Prevent It

- Limit the number of simultaneously open windows and tabs
- Disable transparency and motion effects for better performance
- Close screen sharing and recording apps when not in use
- Restart Mac weekly to clear accumulated WindowServer memory
