---
title: "[Solution] Linux: hostname-resolution-error -- hostname resolution failure"
description: "Fix Linux hostname resolution errors. Local hostname cannot be resolved on system."
os: ["linux"]
error-types: ["network-error"]
severities: ["error"]
---

# Linux: Hostname Resolution Error

Hostname resolution errors prevent the system from resolving its own hostname.

## Common Causes

- /etc/hosts missing entry for hostname
- mDNS not resolving .local hostnames
- DNS search domain not configured
- Hostname does not match any /etc/hosts entry
- nsswitch.conf not including mdns

## How to Fix

### 1. Check Hostname Resolution

```bash
hostname
hostname -f
getent hosts $(hostname)
cat /etc/hosts
```

### 2. Fix /etc/hosts

```bash
echo "127.0.1.1 $(hostname) $(hostname -s)" | sudo tee -a /etc/hosts
```

### 3. Fix nsswitch.conf

```bash
grep hosts /etc/nsswitch.conf
# Should include: hosts: files mdns4_minimal [NOTFOUND=return] dns
```

## Examples

```bash
$ hostname -f
hostname: Name or service not known
$ getent hosts myserver
# No output - not in /etc/hosts
$ echo "127.0.1.1 myserver" | sudo tee -a /etc/hosts
$ hostname -f
myserver
```
