---
title: "[Solution] macOS Error Codes — Carbon, Cocoa & POSIX Fixes"
description: "Find solutions for macOS error codes. Fix FNFErr (-43), ioErr (-36), and paramErr (-50) with step-by-step solutions."
platforms: ["macos"]
---

macOS error codes come from several overlapping frameworks — Carbon, Cocoa, CoreServices, and the POSIX layer. Below are the most frequently encountered codes with fixes you can apply immediately.

## Error Codes

| Error | Description | Fix |
|-------|-------------|-----|
| [Error -36 (ioErr)](/os/macos/-36/) | Input/output error — disk read failure or filesystem corruption | Run Disk Utility First Aid, check cables, and verify the disk with `diskutil verifyVolume` |
| [Error -43 (FNFErr)](/os/macos/-43/) | File not found — the requested file or alias cannot be located | Check the file path, resolve broken aliases, and verify the file exists in Finder |
| [Error -50 (paramErr)](/os/macos/-50/) | Parameter error — invalid argument passed to an API or command | Verify command arguments, check for null values, and review API documentation |

## Quick Diagnosis

Run these commands on macOS to gather error context:

```bash
# Read the system log for recent errors
log show --predicate 'eventMessage contains "error"' --last 1h

# Check Keychain access
security list-keychains

# Run diagnostics
diagnose
```
