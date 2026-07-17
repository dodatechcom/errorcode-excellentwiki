---
title: "[Solution] Xcode Simulator Failed to Boot on Mac"
description: "Fix Xcode simulator errors when iOS Simulator fails to boot, gets stuck on Apple logo, or crashes on launch."
platforms: ["macos"]
severities: ["error"]
error-types: ["system-error"]
weight: 5
---

# Xcode Simulator Failed to Boot on Mac

The iOS Simulator fails to boot, shows a black screen, gets stuck on the Apple logo, or crashes immediately after launch.

## What This Error Means

The Xcode Simulator relies on a virtualization framework to emulate iOS devices. A boot failure means the simulator runtime cannot initialize the virtual device, often due to corrupted runtime state, insufficient resources, or conflicts with macOS security settings.

## Common Causes

- Corrupted simulator runtime or device state
- Insufficient disk space or memory
- Conflicting macOS security settings (SIP, Gatekeeper)
- Outdated simulator runtime mismatched with Xcode version
- Corrupted device support files
- Multiple Xcode versions installed

## How to Fix

### Reset Simulator

```bash
# Shutdown all simulators
xcrun simctl shutdown all

# Erase all simulator data
xcrun simctl erase all

# Delete specific device
xcrun simctl delete <device-udid>
```

### Delete DerivedData and Simulator Caches

```bash
rm -rf ~/Library/Developer/Xcode/DerivedData
rm -rf ~/Library/Developer/CoreSimulator/Caches
rm -rf ~/Library/Developer/CoreSimulator/Devices
```

### Reinstall Simulator Runtimes

```bash
# List installed runtimes
xcrun simctl runtime list

# Download missing runtime
xcodebuild -downloadPlatform iOS
```

### Check System Resources

```bash
# Check disk space
df -h

# Check memory pressure
memory_pressure

# Check for conflicting processes
ps aux | grep -i simulator
```

### Reset CoreSimulator Service

```bash
sudo killall -9 com.apple.CoreSimulator.CoreSimulatorService
```

## Related Errors

- [Xcode Build Error]({{< relref "/os/macos/macos-xcode-error-v2" >}}) — Build failures
- [Xcode Archive Error]({{< relref "/os/macos/macos-xcode-archive-error" >}}) — Archive issues
- [Swift Package Error]({{< relref "/os/macos/macos-swift-package-error-v2" >}}) — SPM dependency issues
