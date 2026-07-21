---
title: "Repository Signing Key Expired"
description: "APT repository GPG key has expired and packages cannot be verified"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Repository Signing Key Expired

APT repository GPG key has expired and packages cannot be verified

## Common Causes

- Repository key has not been refreshed
- Key expiration date passed
- Third-party repository stopped updating their key
- System clock incorrect causing false expiration

## How to Fix

1. Check key expiry: `apt-key list`
2. Download new key from repository
3. Check system clock: `date`
4. Remove and re-add repository with fresh key

## Examples

```bash
# Check GPG key expiry dates
apt-key list 2>/dev/null | grep -A2 -B2 'expired\|exp'

# Update system clock
sudo timedatectl set-ntp true

# Re-add repository key
curl -fsSL https://repo.example.com/key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/repo.gpg
```
