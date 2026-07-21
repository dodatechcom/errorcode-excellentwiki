---
title: "[Solution] Linux: systemd-resolved-dnssec-error -- DNSSEC validation failure"
description: "Fix Linux systemd-resolved DNSSEC errors. DNSSEC validation failure in resolved service."
os: ["linux"]
error-types: ["systemd-error"]
severities: ["error"]
---

# Linux: Systemd-Resolved DNSSEC Error

DNSSEC validation failures in systemd-resolved cause domain resolution to fail for signed zones.

## Common Causes

- DNSSEC validation enabled but upstream does not support it
- System clock wrong causing signature validation failure
- Trust anchor expired or missing
- Forwarded domain stripping DNSSEC RRSIG records
- Broken DNSSEC chain from authoritative server

## How to Fix

### 1. Check DNSSEC Status

```bash
resolvectl status
resolvectl query example.com
resolvectl dnssec
```

### 2. Disable or Fix DNSSEC

```bash
resolvectl dnssec no
sudo tee /etc/systemd/resolved.conf << EOF
[Resolve]
DNSSEC=allow-downgrade
EOF
sudo systemctl restart systemd-resolved
```

### 3. Fix System Clock

```bash
sudo timedatectl set-ntp true
chronyc tracking 2>/dev/null
timedatectl status
```

## Examples

```bash
$ resolvectl query example.com
example.com: resolve call failed: DNSSEC validation failed: no signatures
$ resolvectl dnssec
DNSSEC setting: yes
```
