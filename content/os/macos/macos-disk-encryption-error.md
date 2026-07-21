---
title: "[Solution] macOS Disk Encryption Error -- FileVault Encryption Failed"
description: "Fix macOS disk encryption error when FileVault encryption or decryption fails. Resolve encryption issues on Mac startup disk."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Disk Encryption Error -- FileVault Encryption Failed

FileVault full-disk encryption protects your data by encrypting the entire startup volume. When encryption or decryption fails, you may see progress stuck, errors, or the disk may become inaccessible.

## Common Causes
- Disk has bad sectors preventing encryption of certain blocks
- Power loss during encryption interrupted the process
- FileVault recovery key is not escrowed correctly
- APFS container corruption is blocking encryption operations
- T2 chip or Apple Silicon Secure Enclave issue

## How to Fix
1. Check FileVault status and encryption progress
2. Ensure the Mac is connected to power during encryption
3. Try pausing and resuming the encryption process
4. Boot into Recovery Mode and check disk health
5. If encryption is stuck, you may need to erase and start over

```bash
# Check FileVault status
fdesetup status

# Check encryption progress
diskutil apfs list | grep -A 5 "FileVault"
```

## Examples

```bash
# Enable FileVault from terminal
sudo fdesetup enable

# Check encryption conversion status
diskutil apfs list | grep "Conversion"
```

This error is common when the disk has bad sectors, when the Mac loses power during encryption, or when the Secure Enclave on T2/Apple Silicon Macs has an issue.
