---
title: "[Solution] macOS Sleep Wake Error -- Mac Does Not Wake From Sleep"
description: "Fix macOS sleep wake error when Mac does not wake from sleep or crashes when waking. Resolve sleep wake issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Sleep Wake Error -- Mac Does Not Wake From Sleep

Sleep wake errors occur when the Mac fails to resume from sleep mode. The screen may stay black, the keyboard may not respond, or the Mac may restart after waking.

## Common Causes
- External device is preventing the Mac from sleeping properly
- SMC settings are corrupted
- macOS sleep settings are misconfigured
- Third-party app is holding a sleep assertion
- Hardware issue with the display or power button

## How to Fix
1. Press any key or the power button to try waking the Mac
2. Force shutdown and restart if the Mac is unresponsive
3. Reset SMC on Intel Macs
4. Check for apps holding sleep assertions
5. Adjust Energy Saver settings

```bash
# Check sleep assertions
pmset -g assertions

# Check current power settings
pmset -g

# Reset SMC (Intel Macs with T2)
# Shut down, hold left Shift+Control+Option+Power for 10 seconds
```

## Examples

```bash
# Monitor sleep/wake events
log show --predicate 'eventMessage contains "sleep" or eventMessage contains "wake"' --last 30m
```

This error is common when external USB devices prevent sleep, when the SMC needs a reset, or when a third-party app holds a sleep assertion.
