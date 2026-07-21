---
title: "[Solution] macOS Time Capsule Error -- Time Capsule Not Detected or Backup Failing"
description: "Fix macOS Time Capsule error when Time Capsule is not detected or backup to Time Capsule fails. Resolve Time Capsule issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Time Capsule Error -- Time Capsule Not Detected or Backup Failing

Time Capsule was Apple's wireless backup device. While discontinued, many are still in use. When Time Capsule fails, backups may not complete or the device may not be detected.

## Common Causes
- Time Capsule is not powered on or connected to the network
- WiFi connection to Time Capsule is weak
- Time Capsule firmware is outdated
- Time Capsule hard drive is failing
- Network configuration changed and Time Capsule is unreachable

## How to Fix
1. Ensure Time Capsule is powered on and connected to the network
2. Check WiFi signal strength to the Time Capsule
3. Update Time Capsule firmware via AirPort Utility
4. Test the Time Capsule hard drive with Disk Utility
5. Reset Time Capsule if it is not responding

```bash
# Open AirPort Utility
open -a "AirPort Utility"

# Test Time Capsule connectivity
ping time-capsule-address
```

## Examples

```bash
# Check Time Capsule status in AirPort Utility
# Look for green status light and connected devices
```

This error is common when the Time Capsule hard drive is failing, when WiFi signal is too weak for reliable backup, or when the firmware is outdated and incompatible with current macOS.
