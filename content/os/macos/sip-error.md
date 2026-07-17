---
title: "[Solution] macOS SIP Error — System Integrity Protection: Operation Not Permitted"
description: "Fix macOS System Integrity Protection (SIP) 'operation not permitted' error. Understand SIP restrictions, when to disable it, and safe workarounds."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 5
---

# System Integrity Protection — Operation Not Permitted

A SIP error occurs when you try to modify protected system files or directories and macOS blocks the operation with "Operation not permitted." System Integrity Protection (SIP / rootless) prevents even the root user from altering critical system components.

## Description

SIP restricts access to:

- `/System` and `/usr` (except `/usr/local`)
- `/bin` and `/sbin`
- Applications pre-installed with macOS
- Kernel extensions and system-level configurations

Common error messages:

- `Operation not permitted`
- `You can't modify this because it is required by macOS.`
- `could not modify partition map` (when SIP blocks disk changes)

## Common Causes

- Attempting to modify system files (e.g., `/System/Library/`)
- Installing kexts without disabling SIP first
- Running scripts that need to write to protected paths
- Trying to change boot configuration without proper SIP exemption

## How to Fix SIP Errors

### 1. Check SIP Status

```bash
csrutil status
# Output: "System Integrity Protection status: enabled."
# or "disabled"
```

### 2. Disable SIP Temporarily (Recovery Mode Required)

```bash
# Shut down Mac
# Boot into Recovery Mode (Intel: Cmd+R, Apple Silicon: hold power button)
# Open Terminal from Utilities menu
csrutil disable

# Restart Mac
# SIP is now disabled until you re-enable it
```

### 3. Re-enable SIP After Making Changes

```bash
# Boot into Recovery Mode
# Open Terminal
csrutil enable

# Restart Mac
# Verify
csrutil status
```

### 4. Use Specific SIP Exemptions (macOS 11+)

```bash
# Boot into Recovery Mode
# Allow specific kexts without fully disabling SIP
csrutil enable --without kext

# Allow filesystem protections to be modified
csrutil enable --without fs

# Check available options
csrutil status
```

### 5. Work Around SIP Instead of Disabling It

```bash
# Instead of modifying /System, create local overrides:
sudo ln -s /path/to/custom/binary /usr/local/bin/binary-name

# Or use /Library instead of /System/Library for custom extensions
sudo cp my-extension.kext /Library/Extensions/

# For kernel debugging, use --without debug
# Boot into Recovery → csrutil enable --without debug
```

## Examples

This error commonly occurs when:

- Trying to delete `/System/Library/CoreServices/Siri.app` to "remove Siri"
- Installing Hackintosh kernel extensions (kexts)
- Attempting to modify the boot picker or startup disk configuration
- Running system cleanup tools that target protected directories

## Related Errors

- [Gatekeeper Error](gatekeeper-error) — blocks unsigned apps (related security feature)
- [Kernel Panic](kernel-panic) — modifying SIP-protected files may cause panics
- [Disk Utility Error](disk-utility-error) — SIP blocks certain disk operations
