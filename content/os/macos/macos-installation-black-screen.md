---
title: "[Solution] macOS Installation Black Screen -- Screen Goes Dark During Install"
description: "Fix macOS installation black screen when the display goes dark during the install process. Resolve Mac install black screen."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Installation Black Screen -- Screen Goes Dark During Install

A black screen during macOS installation indicates the display output has stopped while the system continues processing in the background.

## Common Causes
- GPU driver is being replaced and the display driver is unloaded
- External monitor connection is lost during the resolution change
- eGPU is disconnected during the installation
- Display brightness is set to zero
- Corrupted display drivers from a previous installation

## How to Fix
1. Shine a flashlight on the screen -- if you see a faint image, it is a brightness issue
2. Try pressing brightness up keys (F1 or F2)
3. Connect an external display to see if the system is running
4. Reset NVRAM and restart the installation
5. Boot into Recovery Mode and run First Aid on the startup volume

```bash
# Reset NVRAM to restore display settings
# Shut down, power on, hold Option+Command+P+R for 20 seconds
```

## Examples

```bash
# From Recovery terminal, check if the system is running
log show --predicate 'process == "kernel"' --last 5m
```

This error is common on Macs with external GPUs, when using a DisplayPort or HDMI adapter, or when the installer changes the display resolution to one unsupported by the connected monitor.
