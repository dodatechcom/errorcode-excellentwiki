---
title: "[Solution] macOS Diagnostics Error -- Apple Diagnostics Failed or Not Available"
description: "Fix macOS diagnostics error when Apple Diagnostics fails to run or reports hardware issues. Resolve diagnostic issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Diagnostics Error -- Apple Diagnostics Failed or Not Available

Apple Diagnostics (formerly Apple Hardware Test) checks your Mac for hardware issues. When it fails to run or reports errors, it may indicate a hardware problem or a firmware issue.

## Common Causes
- Diagnostics partition is corrupted or missing
- Internet connection is required but unavailable for online diagnostics
- Hardware failure is preventing diagnostics from running
- Firmware issue is blocking the diagnostic tool
- Mac model does not support the diagnostic version

## How to Fix
1. Ensure the Mac is connected to the internet (required for newer Macs)
2. Hold D during startup (Intel) or hold power button and follow prompts (Apple Silicon)
3. If diagnostics partition is missing, use an Apple diagnostic tool from another Mac
4. Try running diagnostics from Internet Recovery
5. Contact Apple Support if diagnostics cannot run

```bash
# Run Apple Diagnostics
# Intel Macs: Shut down, then hold D during startup
# Apple Silicon: Shut down, hold power button, follow prompts to diagnostics

# Check if diagnostics partition exists
diskutil list | grep -i "diagnostics"
```

## Examples

```bash
# View diagnostic error codes
# Error codes like PPF, PPT, PPR indicate specific hardware issues
```

This error is common when the diagnostics partition is missing, when the Mac requires internet for online diagnostics, or when a hardware failure prevents the diagnostic tool from running.
