---
title: "[Solution] macOS Firmware Password Error -- Cannot Change Firmware Password"
description: "Fix macOS firmware password error when unable to change or remove the firmware password on Mac. Resolve firmware lock issues."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Firmware Password Error -- Cannot Change Firmware Password

The firmware password prevents unauthorized users from booting from external drives or Recovery Mode. When you forget or need to change this password, the Mac becomes very difficult to service or troubleshoot.

## Common Causes
- Firmware password was set and the original password is forgotten
- Firmware password was set by an employer or IT department
- Attempting to change the password with incorrect credentials
- Apple Silicon Macs use a different mechanism via Startup Security Utility

## How to Fix
1. On Apple Silicon Macs, boot into Recovery Mode and use Startup Security Utility
2. On Intel Macs with T2 chip, boot into Recovery and use Firmware Password Utility
3. On older Intel Macs without T2, contact Apple Support with proof of purchase
4. Apple can remove firmware passwords with proof of ownership at an Apple Store

```bash
# On Intel Macs with T2:
# Boot into Recovery Mode (Command+R)
# From the menu bar: Utilities > Firmware Password Utility
# Select 'Turn Off Firmware Password' and enter the current password
```

## Examples

```bash
# On Apple Silicon Macs:
# 1. Shut down the Mac
# 2. Press and hold the power button until 'Loading startup options' appears
# 3. Click Options > Continue
# 4. Open Startup Security Utility from the Utilities menu
# 5. Select the startup disk and change the firmware password
```

This error is common when purchasing a used Mac that was enrolled in a corporate MDM program, or when setting up a Mac for a child and later needing to adjust security settings.
