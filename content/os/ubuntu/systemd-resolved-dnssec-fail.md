---
title: "Systemd-Resolved DNSSEC Validation Failure"
description: "DNSSEC signature validation fails causing DNS resolution errors"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Systemd-Resolved DNSSEC Validation Failure

DNSSEC signature validation fails causing DNS resolution errors

## Common Causes

- DNSSEC validation enabled but upstream DNS does not support it
- System clock incorrect causing timestamp validation failure
- DS record not propagated for domain
- DNSSEC key rotation incomplete

## How to Fix

1. Check DNSSEC status: `resolvectl status`
2. Test specific domain: `resolvectl query example.com`
3. Disable DNSSEC: `DNSSEC=no` in /etc/systemd/resolved.conf
4. Verify system clock: `timedatectl`

## Examples

```bash
# Check DNSSEC status
resolvectl status | grep DNSSEC

# Test DNS resolution for a domain
resolvectl query example.com

# Disable DNSSEC if causing issues
sudo sed -i 's/#DNSSEC=.*/DNSSEC=no/' /etc/systemd/resolved.conf
sudo systemctl restart systemd-resolved
```
