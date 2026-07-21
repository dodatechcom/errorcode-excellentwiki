---
title: "ZFS Encryption Key Error"
description: "ZFS encrypted dataset cannot be unlocked or key is lost"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# ZFS Encryption Key Error

ZFS encrypted dataset cannot be unlocked or key is lost

## Common Causes

- Encryption key file missing or corrupted
- Key not loaded into ZFS keyring
- Wrong passphrase entered for passphrase-based encryption
- Key location changed (file vs prompt)

## How to Fix

1. Check encryption: `zfs get encryption,keystore <dataset>`
2. Load key: `zfs load-key <dataset>`
3. Check key status: `zfs get keylocation <dataset>`
4. Verify key file exists at specified location

## Examples

```bash
# Check encryption status
zfs get encryption,keystore,passphrase tank/secure

# Load encryption key
sudo zfs load-key tank/secure

# Mount encrypted dataset
sudo zfs mount tank/secure
```
