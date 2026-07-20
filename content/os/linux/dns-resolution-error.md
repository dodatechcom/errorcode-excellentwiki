---
title: "[Solution] Linux: dns-resolution-error — DNS resolution failure"
description: "Fix Linux dns-resolution-error errors. DNS resolution failure with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["network"]
weight: 8
---
# Linux: DNS Resolution Error

DNS resolution errors occur when a hostname cannot be translated to an IP address, preventing network connections.

## Common Causes

- DNS server not configured or incorrect in /etc/resolv.conf
- DNS server unreachable or not responding
- NetworkManager or systemd-resolved not managing DNS correctly
- DNSSEC validation failure or DNS over HTTPS issues
- User error in hostname spelling

## How to Fix

### 1. Test DNS Resolution

```bash
nslookup google.com
dig google.com
host google.com
```

### 2. Check DNS Configuration

```bash
cat /etc/resolv.conf
systemd-resolve --status
networkctl status
```

### 3. Test with Different DNS Server

```bash
# Query Google DNS directly
dig @8.8.8.8 google.com

# Query Cloudflare DNS
dig @1.1.1.1 google.com
```

### 4. Restart DNS Resolution

```bash
sudo systemctl restart systemd-resolved
# Or if using NetworkManager
sudo systemctl restart NetworkManager
```

### 5. Check /etc/hosts

```bash
cat /etc/hosts
# Ensure no incorrect entries
```

## Examples

```bash
$ ping google.com
ping: google.com: Temporary failure in name resolution

$ cat /etc/resolv.conf
# This file is managed by systemd-resolved
nameserver 127.0.0.53
options edns0 trust-ad
search .

$ nslookup google.com
;; connection timed out; no servers could be reached

$ sudo systemctl restart systemd-resolved
$ ping google.com
# Now resolves
```
