---
title: "[Solution] macOS Installation Crash -- Installer Crashes During Installation"
description: "Fix macOS installation crash when the installer application crashes during install. Resolve Mac OS install crashing mid-process."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Installation Crash -- Installer Crashes During Installation

The macOS installer may crash during the installation process, showing an error like 'macOS Installer quit unexpectedly' or simply disappearing.

## Common Causes
- Insufficient disk space causing the installer to fail
- Corrupted installer package from a bad download
- Third-party software interfering with the installation process
- Memory pressure causing the installer to be killed by the system
- FileVault encryption locking files the installer needs to modify

## How to Fix
1. Check disk space and free up at least 25 GB on the startup volume
2. Re-download the macOS installer from the App Store
3. Boot into Safe Mode before running the installer
4. Check the crash report in Console.app to identify the cause
5. Use a full installer from App Store instead of Software Update

```bash
# Check installer crash reports
ls -lt ~/Library/Logs/DiagnosticReports/ | grep -i install

# Clear the Software Update cache
sudo rm -rf /Library/Updates/*
```

## Examples

```bash
# View the crash report for details
# The crash report will indicate the faulting module and exception type
```

This error commonly occurs when the startup volume is nearly full, when a third-party antivirus intercepts the installer, or when the Mac is low on RAM and the installer is killed by the memory pressure.
