---
title: "SSH Max Auth Tries Exceeded"
description: "SSH connection dropped after too many authentication attempts"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# SSH Max Auth Tries Exceeded

SSH connection dropped after too many authentication attempts

## Common Causes

- Client trying too many SSH keys before finding correct one
- Default MaxAuthTries (6) reached
- GSSAPIAuthentication failing before public key tried
- Multiple identities loaded in agent

## How to Fix

1. Check setting: `sshd -T | grep maxauthtries`
2. Increase in sshd_config: `MaxAuthTries 10`
3. Use IdentitiesOnly: `ssh -o IdentitiesOnly=yes user@host`
4. Specify key explicitly: `ssh -i /path/to/key user@host`

## Examples

```bash
# Check current MaxAuthTries
sudo sshd -T | grep maxauthtries

# Use specific identity file
ssh -i ~/.ssh/id_ed25519 user@host

# Try only specified identities
ssh -o IdentitiesOnly=yes user@host
```
