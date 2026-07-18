---
title: "[Solution] Linux: systemd-resolved-error — DNS resolution failed via systemd-resolved"
description: "Fix Linux systemd-resolved-error errors. DNS resolution failed via systemd-resolved with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["network-error"]
weight: 12
---

# Linux: systemd-resolved-error — DNS resolution failed via systemd-resolved

Fix Linux systemd-resolved-error errors. This guide covers common causes, step-by-step fixes, real-world scenarios, and prevention tips.

## Common Causes

- Service not running
- Wrong DNS servers
- Stub resolver not linked
- Upstream DNS unreachable

## How to Fix

### 1. Check Status
```bash
resolvectl status
systemctl status systemd-resolved
```

### 2. Configure DNS
```bash
sudo mkdir -p /etc/systemd/resolved.conf.d
sudo tee /etc/systemd/resolved.conf.d/dns.conf << EOF
[Resolve]
DNS=8.8.8.8 8.8.4.4
FallbackDNS=1.1.1.1
EOF
```

### 3. Link Stub Resolver
```bash
sudo ln -sf /run/systemd/resolve/stub-resolv.conf /etc/resolv.conf
```

### 4. Flush Cache
```bash
sudo resolvectl flush-caches
```

## Common Scenarios

- DNS SERVFAIL or timeout
- resolv.conf not pointing to 127.0.0.53
- DNS works with IP only

## Prevent It

- Keep resolv.conf symlinked
- Configure multiple DNS servers
- Monitor with resolvectl
