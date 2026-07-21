---
title: "[Solution] macOS Installation Error 3 -- Installer Cannot Verify Integrity"
description: "Fix macOS installation error 3 when the installer cannot verify its integrity. Resolve Mac OS install integrity check failure."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Installation Error 3 -- Installer Cannot Verify Integrity

Error code 3 indicates the macOS installer failed its integrity check. The installer package hash does not match the expected value.

## Common Causes
- Download was corrupted or incomplete from the App Store
- Installer was modified after downloading (patched or cracked)
- Filesystem errors corrupted the installer file on disk
- Antivirus software modified the installer during scanning
- Disk bad sectors where the installer is stored

## How to Fix
1. Delete the corrupted installer and re-download from App Store
2. Run Disk Utility First Aid to check for disk errors
3. Temporarily disable antivirus software during the download
4. Use terminal to download the installer directly from Apple servers
5. Download to a different location

```bash
# Remove the corrupted installer
rm -rf /Applications/Install\ macOS\ Sequoia.app

# Re-download from terminal
softwareupdate --fetch-full-installer --full-installer-version 14.5
```

## Examples

```bash
# Verify the installer after download
codesign --verify --verbose /Applications/Install\ macOS\ Sequoia.app
```

This error is common when antivirus software modifies the installer during download, when the download is interrupted by network issues, or when the disk has bad sectors where the file is stored.
