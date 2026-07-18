---
title: "[Solution] macOS Disk SSD Error — SSD Not Detected or TRIM Not Working"
description: "Fix macOS SSD error: SSD not detected, TRIM not working, SSD health warnings in System Information, slow SSD performance."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 149
---

# Disk SSD Error — SSD Not Detected or TRIM Not Working

Fix macOS SSD error: SSD not detected, TRIM not working, SSD health warnings in System Information, slow SSD performance.

## Common Causes

- SSD firmware incompatibility with macOS TRIM implementation
- Third-party SSD lacking Apple TRIM support
- SSD controller failure preventing detection
- SATA/NVMe connection issue causing intermittent SSD detection

## How to Fix

### 1. Check SSD Health and TRIM Status

```bash
system_profiler SPNVMeDataType
system_profiler SPStorageDataType | grep TRIM
sudo trimforce status
```

### 2. Enable TRIM for Third-Party SSDs

```bash
# WARNING: Enable only for compatible third-party SSDs
sudo trimforce enable
```

### 3. Update SSD Firmware

```bash
system_profiler SPNVMeDataType | grep Firmware
# Visit SSD manufacturer website for firmware updates
```

### 4. Check SSD Connection

```bash
system_profiler SPNVMeDataType
system_profiler SPThunderboltDataType
```

## Common Scenarios

This error commonly occurs when:

- SSD not showing up in Disk Utility after macOS update
- TRIM not enabled for third-party SSD in System Information
- SSD performance degrades significantly over time
- SSD health warning appears in System Information

## Prevent It

- Keep SSD firmware updated to latest version from manufacturer
- Enable TRIM only for SSDs that support it properly
- Monitor SSD health using System Information or third-party tools
- Back up data regularly as SSDs can fail without warning
