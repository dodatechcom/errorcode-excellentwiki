---
title: "systemd-resolved Error"
description: "systemd-resolved DNS resolution service fails to resolve domain names."
tools: ["systemd"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# systemd-resolved Error

A systemd-resolved error occurs when the DNS resolution service fails to resolve domain names. This affects all DNS queries on the system.

## Common Causes

- DNS server unreachable
- Configuration file errors
- DNSSEC validation failures
- Upstream DNS server issues

## How to Fix

### Check DNS Status

```bash
systemctl status systemd-resolved
resolvectl status
```

### Check DNS Resolution

```bash
resolvectl query example.com
resolvectl statistics
```

### Fix DNS Configuration

```ini
# /etc/systemd/resolved.conf
[Resolve]
DNS=8.8.8.8 8.8.4.4
FallbackDNS=1.1.1.1 1.0.0.1
Domains=~.
DNSSEC=allow-downgrade
DNSOverTLS=opportunistic
```

### Restart resolved

```bash
sudo systemctl restart systemd-resolved
```

### Fix /etc/resolv.conf

```bash
# Ensure resolv.conf points to systemd-resolved
sudo ln -sf /run/systemd/resolve/stub-resolv.conf /etc/resolv.conf
```

### Check for DNS Issues

```bash
resolvectl query example.com
# If fails, check upstream DNS
dig @8.8.8.8 example.com
```

### Flush DNS Cache

```bash
resolvectl flush-caches
```

## Examples

```bash
resolvectl query example.com
example.com: resolve call failed: No such file or directory

# Fix: check DNS configuration
resolvectl status
```

## Related Errors

- [Network Error]({{< relref "/tools/systemd/systemd-network-error" >}}) — network interface error
- [Unit Start Failed]({{< relref "/tools/systemd/systemd-unit-error" >}}) — service start failure
