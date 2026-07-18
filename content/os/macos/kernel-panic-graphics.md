---
title: "[Solution] macOS Kernel Panic Graphics — GPU Driver Crash"
description: "Fix macOS kernel panic from GPU: black screen, flickering, graphics driver panic in system logs. Check GPU health and display drivers."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 92
---

# Kernel Panic Graphics — GPU Driver Crash

Fix macOS kernel panic from GPU: black screen, flickering, graphics driver panic in system logs.

## Common Causes

- Failing or overheating GPU (especially on older MacBook Pros)
- Corrupted graphics drivers from macOS update
- External GPU (eGPU) compatibility or Thunderbolt issue
- GPU demanding more power than system can supply under load

## How to Fix

### 1. Check GPU Health and Temperature

```bash
sudo powermetrics --samplers gpu_power -n 5 -i 1000
system_profiler SPDisplaysDataType
log show --predicate 'eventMessage contains "GPU"' --last 1h | grep panic
```

### 2. Disable Automatic Graphics Switching

```bash
# System Settings → Battery → Options → Disable auto graphics switching
sudo shutdown -r now
```

### 3. Reset GPU Driver and NVRAM

```bash
# Restart and hold Option+Command+P+R for 20s
# Boot Safe Mode to use basic graphics driver
```

### 4. Check External GPU or Disconnect eGPU

```bash
system_profiler SPDisplaysDataType | grep -A 5 'eGPU'
# Disconnect eGPU and test with built-in GPU
```

## Common Scenarios

This error commonly occurs when:

- Kernel panic occurs during GPU-intensive tasks like video rendering
- Panic log references AppleIntelFramebuffer or AMDRadeon kext
- System crashes when connecting external display to MacBook
- GPU panic started after macOS update affecting display drivers

## Prevent It

- Keep GPU drivers updated through macOS software updates
- Ensure adequate ventilation for MacBook Pro during heavy GPU use
- Use only Apple-approved eGPU enclosures with compatible GPUs
- Monitor GPU temperature during intensive workloads
