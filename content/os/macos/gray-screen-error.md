---
title: "[Solution] macOS Gray Screen Error — Gray Background at Startup"
description: "Fix macOS gray screen: display shows gray background with Apple logo or spinner but system does not boot to login window."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 106
---

# Gray Screen Error — Gray Background at Startup

Fix macOS gray screen: display shows gray background with Apple logo or spinner but system does not boot to login window.

## Common Causes

- Corrupted system files preventing macOS from completing boot
- Startup disk errors blocking OS from loading fully
- Third-party extension blocking boot sequence completion
- FileVault encryption key issue preventing disk unlock

## How to Fix

### 1. Boot into Recovery and Run First Aid

```bash
diskutil verifyVolume disk0s1
# Recovery → Disk Utility → First Aid
```

### 2. Reinstall macOS Without Erasing Data

```bash
# Recovery → Select Reinstall macOS → Follow prompts
```

### 3. Boot in Verbose Mode to Diagnose

```bash
# Restart and hold Command+V for text output
# Look for errors or hung processes
```

### 4. Reset NVRAM and Check Startup Disk

```bash
# Hold Option+Command+P+R for 20s
bless --mount /Volumes/Macintosh\ HD --setBoot
```

## Common Scenarios

This error commonly occurs when:

- Gray screen appears with Apple logo but progress bar never completes
- Gray screen occurred after FileVault was enabled or updated
- Gray screen with spinning gear but never reaches login
- Gray screen started after installing third-party extension

## Prevent It

- Always verify disk health with First Aid before major system changes
- Avoid untrusted system extensions that modify boot process
- Keep a bootable macOS USB installer for emergency recovery
- Ensure FileVault is fully encrypted before restarting or updating
