---
title: "[Solution] Xcode Simulator Error on macOS"
description: "Fix Xcode Simulator errors including simulator not launching, app crashes on simulator, or 'Unable to install' simulator errors."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Xcode Simulator Error Fix

Simulator errors include the simulator not launching, apps crashing immediately on launch, "Unable to install" messages, or the simulator stuck on a black screen.

## What This Error Means

The iOS/tvOS/watchOS Simulator runs a virtualized version of the OS. Errors can occur due to corrupt simulator data, incompatible runtime versions, or Xcode cache issues.

## Common Causes

- Corrupt simulator runtime or data
- Xcode and simulator runtime version mismatch
- Insufficient disk space for simulator data
- Stale simulator device data
- macOS security software blocking simulator processes

## How to Fix

### 1. Reset the simulator

```bash
# In Xcode: Open Simulator → File → Reset Content and Settings

# Or delete simulator data manually:
rm -rf ~/Library/Developer/CoreSimulator/Devices/*
xcrun simctl delete all
```

### 2. Install the correct simulator runtime

```bash
# List available runtimes
xcrun simctl list runtimes

# Download missing runtimes via Xcode → Settings → Platforms
# Or install via command line:
xcodebuild -downloadPlatform iOS
```

### 3. Clean simulator caches

```bash
# Kill all simulator processes
killall -9 com.apple.CoreSimulator.CoreSimulatorService

# Remove simulator cache
rm -rf ~/Library/Developer/CoreSimulator/Caches/
```

### 4. Check simulator status

```bash
# List all simulators
xcrun simctl list devices

# Boot a specific simulator
xcrun simctl boot "iPhone 15"

# Check simulator log
xcrun simctl spawn booted log show --predicate 'process == "SpringBoard"'
```

## Related Errors

- [Xcode Error](macos-xcode-error) — general Xcode build errors
- [Swift Package Error](macos-swift-package-error) — SPM dependency issues
- [Xcode Archive Error](macos-xcode-archive) — archive failures
