---
title: "[Solution] macOS Hardware Test Error -- Apple Hardware Test Failed or Unavailable"
description: "Fix macOS hardware test error when Apple Hardware Test fails to run or reports errors. Resolve hardware test issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Hardware Test Error -- Apple Hardware Test Failed or Unavailable

Apple Hardware Test (now Apple Diagnostics) checks your Mac for hardware problems. When it fails to run, you cannot diagnose hardware issues like faulty RAM or a failing drive.

## Common Causes
- Diagnostics partition is missing or corrupted
- Internet connection is required but unavailable
- Hardware failure is preventing the test from running
- Mac model requires online diagnostics
- Firmware issue is blocking the diagnostic tool

## How to Fix
1. Ensure the Mac is connected to the internet for online diagnostics
2. Hold D during startup (Intel) to run diagnostics
3. On Apple Silicon, hold power button and follow prompts to diagnostics
4. Use an external diagnostic tool if the built-in one fails
5. Contact Apple Support for hardware service

```bash
# Run Apple Diagnostics
# Intel Macs: Shut down, then hold D during startup
# Apple Silicon: Shut down, hold power button, follow prompts

# Check diagnostics partition
diskutil list | grep -i "diagnostics"
```

## Examples

```bash
# View diagnostic error codes
# Common codes: PPF (fans), PPT (temperature), PPR (processor)
```

This error is common when the diagnostics partition is missing, when the Mac requires internet for online diagnostics, or when a hardware failure prevents the test from running.
