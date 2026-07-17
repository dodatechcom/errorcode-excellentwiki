---
title: "[Solution] macOS Kernel Panic — GPU Error"
description: "Fix macOS kernel panic caused by GPU errors. Diagnose graphics card failures, eGPU issues, and resolve GPU-related kernel panics."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["kernel-panic", "gpu", "graphics", "egpu", "metal", "crash"]
weight: 5
---

# Kernel Panic — GPU Error on macOS

A GPU-related kernel panic occurs when the graphics subsystem encounters an unrecoverable error. This is common with external GPUs (eGPUs), failing discrete GPUs, or corrupt graphics drivers.

## What This Error Means

The macOS kernel panic log will reference GPU-related components such as `AMD`, `NVIDIA`, `IntelGPU`, or `AGDC` (Apple Graphics Device Control). The panic may occur during boot, under heavy graphics load, or when connecting/disconnecting an eGPU.

## Common Causes

- Failing or overheating discrete GPU (common in 2011-2013 MacBook Pros)
- Incompatible or faulty eGPU connected via Thunderbolt
- Corrupt GPU driver or kext
- macOS update breaking GPU compatibility
- VRAM failure on the GPU

## How to Fix

### 1. Disconnect eGPU if applicable

```bash
# Safely eject the eGPU before disconnecting
# If system is panicked, force shutdown by holding power button
# Disconnect the Thunderbolt cable
# Boot without eGPU and test stability
```

### 2. Check GPU panic logs

```bash
# Search for GPU-related panics
grep -i "gpu\|amd\|nvidia\|intel\|agdc\|accelerator" /Library/Logs/DiagnosticReports/KernelPanics/*.panic

# Check GPU temperature
sudo powermetrics --samplers gpu_power -i 2000 -n 5
```

### 3. Reset NVRAM

```bash
# Shut down Mac
# Turn on and immediately hold Option+Command+P+R for 20 seconds
# This resets GPU-related NVRAM settings
```

### 4. Disable automatic GPU switching (MacBook Pro)

```bash
# Open System Preferences → Battery → Battery
# Uncheck "Automatic graphics switching"
# This forces the discrete GPU to always be active, avoiding switch-related panics
```

### 5. Use safe mode to isolate

```bash
# Intel Mac: Hold Shift during startup
# Apple Silicon: Hold power button → Select startup disk → Hold Shift → Continue in Safe Mode
# Safe mode loads minimal GPU drivers and disables third-party kexts
```

## Related Errors

- [Kernel Panic](kernel-panic) — general kernel panic troubleshooting
- [Metal Error](metal-error) — Metal API graphics framework errors
- [Kernel Panic: RAM](macos-kernel-panic-ram) — memory-related kernel panics
