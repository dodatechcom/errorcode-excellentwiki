---
title: "[Solution] macOS Kernel Panic — System Restarts Unexpectedly"
description: "Fix macOS kernel panic: system restarts unexpectedly with panic log, black screen, or power cycling. Diagnose RAM, disk, and extension issues."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 90
---

# Kernel Panic — System Restarts Unexpectedly

Fix macOS kernel panic: system restarts unexpectedly with panic log, black screen, or power cycling.

## Common Causes

- Faulty RAM or memory module causing data corruption
- Corrupted kernel extension (kext) from third-party software
- Faulty storage drive with bad sectors or failing NAND
- Incompatible macOS update or beta version installed

## How to Fix

### 1. Run Apple Diagnostics

```bash
# Restart and hold D during startup (Intel) or use startup options (Apple Silicon)
system_profiler SPHardwareDataType | head -20
sudo powermetrics --samplers cpu_power -n 1 -i 2000
```

### 2. Check Panic Logs

```bash
log show --predicate 'eventMessage contains "panic"' --last 1h
ls -lt /Library/Logs/DiagnosticReports/kernel* | head -5
cat $(ls -t /Library/Logs/DiagnosticReports/kernel* | head -1)
```

### 3. Boot Safe Mode and Remove Kexts

```bash
# Intel: Restart and hold Shift
kextstat | grep -v com.apple
sudo kextunload /Library/Extensions/problematic.kext
```

### 4. Reset NVRAM and Reinstall macOS

```bash
# Intel: Hold Option+Command+P+R for 20s
sudo shutdown -r now
```

## Common Scenarios

This error commonly occurs when:

- Mac restarts randomly during intensive tasks like video editing
- Panic log mentions a specific kext or driver causing the crash
- Kernel panic started after installing macOS update or new RAM
- Mac crashes during boot showing black screen before login

## Prevent It

- Run Apple Diagnostics periodically to check RAM and hardware health
- Avoid installing untrusted kernel extensions from unknown developers
- Keep macOS updated and avoid beta versions on production machines
- Back up data regularly with Time Machine before major changes
