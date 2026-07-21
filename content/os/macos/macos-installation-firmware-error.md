---
title: "[Solution] macOS Installation Firmware Error -- Firmware Update Failed"
description: "Fix macOS firmware update error during installation when firmware update fails on Mac. Resolve firmware error preventing macOS install."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Installation Firmware Error -- Firmware Update Failed

Some macOS updates include firmware updates for the Mac's BridgeOS (T2 chip), SMC, or Apple Silicon Boot ROM. When the firmware update fails, the installation cannot complete.

## Common Causes
- Mac is not connected to a power source during firmware update
- Battery is critically low on a MacBook
- Third-party hardware modifications blocking firmware validation
- T2 chip or Apple Silicon secure boot policy conflicts
- Corrupted firmware image from a partial download

## How to Fix
1. Ensure the Mac is connected to AC power -- do not run on battery
2. If the Mac is stuck in firmware recovery, connect via USB-C to a host Mac
3. On Apple Silicon Macs, DFU restore using Apple Configurator
4. On T2 Macs, use Apple Configurator 2 to restore firmware
5. Contact Apple Support if the firmware restore fails

```bash
# Check current firmware version
system_profiler SPHardwareDataType | grep -i "Boot\|Firmware"
```

## Examples

```bash
# For Apple Silicon Macs in DFU mode:
# 1. Connect the Mac to another Mac via USB-C
# 2. Open Apple Configurator 2 on the host Mac
# 3. Select the DFU Mac and choose Actions > Restore
```

This error is most common when updating a MacBook on battery power, when the Mac has been modified with third-party components, or when the power cable is accidentally disconnected during the update.
