---
title: "[Solution] macOS Shutdown Error -- Mac Fails to Shut Down Completely"
description: "Fix macOS shutdown error when Mac does not shut down or gets stuck during shutdown. Resolve shutdown issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Shutdown Error -- Mac Fails to Shut Down Completely

When macOS fails to shut down, the screen may go black but the Mac remains powered on, or the shutdown progress bar stalls indefinitely.

## Common Causes
- A background process is not responding to the shutdown signal
- App is holding a file lock preventing shutdown
- FileVault is completing encryption/decryption
- Sleep/wake settings are conflicting with shutdown
- Hardware issue with the power button or logic board

## How to Fix
1. Force shutdown by holding the power button for 10 seconds
2. Check Activity Monitor for unresponsive processes
3. Quit all applications before shutting down
4. Check for apps holding file locks with lsof
5. Reset SMC if the power button is not responding

```bash
# Check for processes preventing shutdown
lsof +D / | grep -i "txt\|DEL"

# Force shutdown from terminal (use with caution)
sudo shutdown -h now
```

## Examples

```bash
# Check shutdown logs
log show --predicate 'eventMessage contains "shutdown"' --last 10m
```

This error is common when a background process does not respond to shutdown signals, when FileVault is completing encryption, or when the power button hardware is failing.
