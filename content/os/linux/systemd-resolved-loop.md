---
title: "[Solution] Linux: systemd-resolved-loop -- DNS resolution loop"
description: "Fix Linux systemd-resolved loop errors. DNS queries looping through systemd-resolved service."
os: ["linux"]
error-types: ["systemd-error"]
severities: ["error"]
---

# Linux: Systemd-Resolved Loop

Systemd-resolved loop occurs when DNS queries loop back through resolved, causing failures.

## Common Causes

- /etc/resolv.conf pointing to 127.0.0.53 in a loop
- Multiple DNS resolvers referencing each other
- Broken symlink from /etc/resolv.conf to resolved stub
- NetworkManager misconfiguration overriding DNS
- VPN client pushing conflicting DNS servers

## How to Fix

### 1. Check Current DNS Config

```bash
resolvectl status
cat /etc/resolv.conf
ls -la /etc/resolv.conf
```

### 2. Fix DNS Configuration

```bash
sudo resolvectl flush-caches
sudo systemctl restart systemd-resolved
```

### 3. Set Direct DNS

```bash
sudo tee /etc/systemd/resolved.conf << EOF
[Resolve]
DNS=8.8.8.8 8.8.4.4
FallbackDNS=1.1.1.1
EOF
sudo systemctl restart systemd-resolved
```

## Examples

```bash
$ resolvectl status
Global
         Protocols: +LLMNR +mDNS -DNSOverTLS DNSSEC=no/unsupported
$ cat /etc/resolv.conf
nameserver 127.0.0.53
$ dig example.com
;; connection timed out; no servers could be reached
```
