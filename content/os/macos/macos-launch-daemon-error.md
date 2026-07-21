---
title: "[Solution] macOS Launch Daemon Error -- Launch Daemon Not Running"
description: "Fix macOS launch daemon error when system launch daemons fail to start or run. Resolve launch daemon issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Launch Daemon Error -- Launch Daemon Not Running

Launch Daemons are system-wide background processes that run as root. When they fail, critical system services like networking, printing, or security features may stop working.

## Common Causes
- Launch Daemon plist file has syntax errors
- Launch Daemon binary is missing or corrupted
- Required frameworks or libraries are not available
- Launch Daemon is conflicting with another daemon
- Permissions on the plist or binary are incorrect

## How to Fix
1. Validate the Launch Daemon plist file
2. Check that the binary exists and is accessible
3. Check system logs for Launch Daemon errors
4. Remove or disable conflicting daemons
5. Reinstall the software that provides the daemon

```bash
# List system Launch Daemons
ls -la /Library/LaunchDaemons/ | grep -v com.apple

# Validate a plist file
plutil -lint /Library/LaunchDaemons/com.example.daemon.plist

# Check daemon status
launchctl list | grep -i example
```

## Examples

```bash
# Check launchd system logs
log show --predicate 'process == "launchd"' --last 10m
```

This error is common when a third-party Launch Daemon plist has syntax errors, when the daemon binary is missing, or when a macOS update changes the Launch Daemon API.
