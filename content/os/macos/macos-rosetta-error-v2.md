---
title: "[Solution] Rosetta 2 Translation Failed Error on Mac"
description: "Fix Rosetta 2 errors on Apple Silicon Macs when Intel apps fail to translate, crash, or refuse to run."
platforms: ["macos"]
severities: ["error"]
error-types: ["system-error"]
tags: ["rosetta", "apple-silicon", "intel", "translation", "compatibility", "macos"]
weight: 5
---

# Rosetta 2 Translation Failed Error on Mac

Intel apps fail to run on Apple Silicon with "Rosetta translation failed", "Unable to launch", or apps crash immediately after opening.

## What This Error Means

Rosetta 2 translates Intel (x86_64) instructions to Apple Silicon (ARM64) at install time or runtime. Translation failures occur when apps use incompatible instructions, rely on Intel-specific hardware features, or have copy protection that blocks translation.

## Common Causes

- App uses Intel-specific kernel extensions (kexts)
- App relies on unsupported CPU instructions
- DRM/copy protection incompatible with Rosetta
- Corrupted app installation
- Rosetta 2 not installed
- App uses 32-bit code (not supported)

## How to Fix

### Install Rosetta 2

```bash
# Install Rosetta 2 if not already installed
softwareupdate --install-rosetta

# Or trigger installation by running an Intel app
```

### Check App Architecture

```bash
# Check if app is Universal or Intel
file /Applications/AppName.app/Contents/MacOS/AppName

# Check with otool
otool -L /Applications/AppName.app/Contents/MacOS/AppName

# List all apps and their architecture
find /Applications -name "*.app" -exec sh -c 'echo "$(file "$1/Contents/MacOS/"* | head -1): $1"' _ {} \;
```

### Force Rosetta Translation

```bash
# Force an app to run under Rosetta
# Right-click app > Get Info > "Open using Rosetta"

# Or via command line:
arch -x86_64 /Applications/AppName.app/Contents/MacOS/AppName

# Check current arch
uname -m
```

### Fix Corrupted Installation

```bash
# Delete and reinstall the app
rm -rf /Applications/AppName.app
# Download fresh copy from developer

# Clear Rosetta cache
rm -rf ~/Library/Caches/com.apple.Rosetta*
```

### Check for Native Version

```bash
# Search for Apple Silicon native version
# Visit developer website for ARM64 build
# Or check App Store for Universal version
```

### Debug Translation Issues

```bash
# Run with Rosetta logging
ROSETTA_LOGGING=1 /Applications/AppName.app/Contents/MacOS/AppName

# Check Console.app for Rosetta errors
log show --predicate 'process == "Rosetta"' --last 1h
```

## Related Errors

- [Apple Silicon Error]({{< relref "/os/macos/macos-m1-error-v2" >}}) — Rosetta not installed
- [Xcode Build Error]({{< relref "/os/macos/macos-xcode-error-v2" >}}) — Build issues
- [Gatekeeper Error]({{< relref "/os/macos/macos-gatekeeper-error-v2" >}}) — App security
