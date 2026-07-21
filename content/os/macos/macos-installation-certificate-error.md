---
title: "[Solution] macOS Installation Certificate Error -- Certificate Validation Failed"
description: "Fix macOS installation certificate error when installer certificate validation fails. Resolve certificate errors during Mac OS installation."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Installation Certificate Error -- Certificate Validation Failed

Certificate errors during installation occur when macOS cannot validate the Apple-signed certificates embedded in the installer.

## Common Causes
- System clock is incorrect, causing certificate date validation to fail
- Root certificate store is outdated or corrupted
- Network MITM proxy is intercepting Apple certificate validation
- Installer was modified and the embedded certificate chain is broken

## How to Fix
1. Correct your system date and time before running the installer
2. Use automatic date and time settings in System Preferences
3. Re-download the installer to ensure an unmodified copy
4. Ensure no MITM proxy is intercepting the download

```bash
# Sync system clock with Apple time servers
sudo sntp -sS time.apple.com

# Check current date
date
```

## Examples

```bash
# Verify the installer code signature
codesign --verify --verbose /Applications/Install\ macOS\ Sequoia.app
```

This error is common when the system clock drifts on old Macs, when running macOS on a VM with incorrect time sync, or when a corporate proxy is inspecting HTTPS traffic destined for Apple.
