---
title: "PAM Module Missing Error"
description: "PAM authentication fails because required module is not installed"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# PAM Module Missing Error

PAM authentication fails because required module is not installed

## Common Causes

- PAM module package not installed
- Module path incorrect in PAM configuration
- Module name misspelled in auth config
- 32-bit module on 64-bit system

## How to Fix

1. Check PAM config: `cat /etc/pam.d/<service>`
2. Find module: `find /lib/security/ /lib/security64/ -name '*.so' | grep <module>`
3. Install missing package: `apt-cache search pam-<module>`
4. Verify module architecture: `file /lib/security/<module>.so`

## Examples

```bash
# Check PAM configuration for sshd
cat /etc/pam.d/sshd

# Find available PAM modules
find /lib/security/ -name '*.so' | grep pam_unix

# Install missing PAM module
sudo apt-get install libpam-modules
```
