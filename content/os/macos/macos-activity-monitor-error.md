---
title: "[Solution] macOS Activity Monitor Error -- Activity Monitor Not Showing Processes"
description: "Fix macOS Activity Monitor error when Activity Monitor does not show processes or crashes. Resolve Activity Monitor issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Activity Monitor Error -- Activity Monitor Not Showing Processes

Activity Monitor is the macOS system monitor that shows CPU, memory, disk, and network usage. When it fails, you cannot diagnose performance issues or identify resource-hungry processes.

## Common Causes
- Activity Monitor preferences are corrupted
- Process information database is not accessible
- macOS security settings are blocking process enumeration
- Activity Monitor app is corrupted
- System is under extreme load preventing data collection

## How to Fix
1. Force quit and reopen Activity Monitor
2. Delete Activity Monitor preferences
3. Reinstall Activity Monitor from macOS recovery
4. Use terminal commands as an alternative (top, ps)
5. Restart the Mac to clear system state

```bash
# Alternative to Activity Monitor using terminal
top -o cpu -l 1 -n 20
ps aux --sort=-%cpu | head -20

# Delete Activity Monitor preferences
defaults delete com.apple.ActivityMonitor
```

## Examples

```bash
# Check process CPU usage from terminal
ps aux --sort=-%cpu | head -10

# Check memory usage
ps aux --sort=-%mem | head -10
```

This error is common when the Activity Monitor preferences are corrupted, when the system is under extreme load, or when the app itself needs to be reinstalled.
