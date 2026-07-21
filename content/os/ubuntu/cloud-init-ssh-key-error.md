---
title: "Cloud-Init SSH Key Injection Error"
description: "Cloud-init fails to inject SSH keys into VM"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Cloud-Init SSH Key Injection Error

Cloud-init fails to inject SSH keys into VM

## Common Causes

- SSH key format invalid (not OpenSSH format)
- Cloud-init metadata missing SSH keys
- ~/.ssh directory permissions too open
- authorized_keys file not writable

## How to Fix

1. Check keys: `cloud-init query -k`
2. Verify SSH key: `ssh-keygen -l -f /path/to/key`
3. Check authorized_keys: `ls -la ~/.ssh/authorized_keys`
4. View logs: `grep -i ssh /var/log/cloud-init.log`

## Examples

```bash
# Check cloud-init SSH key data
cloud-init query --format json | jq '.ssh_keys'

# Check authorized_keys
ls -la ~/.ssh/
cat ~/.ssh/authorized_keys

# View cloud-init SSH logs
grep -i ssh /var/log/cloud-init.log
```
