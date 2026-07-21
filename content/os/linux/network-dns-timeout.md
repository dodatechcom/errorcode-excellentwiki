---
title: "[Solution] Linux: network-dns-timeout -- DNS resolution timeout"
description: "Fix Linux network DNS timeout errors. DNS resolution timing out preventing name resolution."
os: ["linux"]
error-types: ["network-error"]
severities: ["error"]
---

# Linux: Network DNS Timeout

DNS timeout occurs when DNS queries fail to receive a response in time.

## Common Causes

- DNS server unreachable due to network issues
- Firewall blocking UDP port 53 or TCP port 53
- DNS server overloaded or misconfigured
- ISP DNS server experiencing outages
- Excessive DNSSEC validation delays

## How to Fix

### 1. Test DNS Resolution

```bash
dig example.com @8.8.8.8
nslookup example.com
```

### 2. Check DNS Configuration

```bash
cat /etc/resolv.conf
resolvectl status 2>/dev/null
```

### 3. Switch DNS Servers

```bash
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
sudo systemctl restart systemd-resolved 2>/dev/null
```

## Examples

```bash
$ dig example.com @8.8.8.8
;; connection timed out; no servers could be reached
$ ping -c 3 8.8.8.8
3 packets transmitted, 3 received, 0% packet loss
```
