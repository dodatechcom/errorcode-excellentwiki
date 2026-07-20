---
title: "[Solution] npm install ENOTFOUND DNS Error"
description: "Handle ENOTFOUND DNS errors in npm install by fixing DNS resolution, nameserver configuration, and network connectivity."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install ENOTFOUND DNS Error

This guide helps you diagnose and resolve npm install ENOTFOUND DNS Error errors encountered when running npm commands.

## Common Causes

- DNS server cannot resolve the npm registry hostname
- Local DNS cache contains stale or incorrect records
- Nameserver configuration is incorrect or unreachable

## How to Fix

### Verify DNS Resolution

```bash
nslookup registry.npmjs.org
```

### Switch to Public DNS Servers

```bash
sudo bash -c 'echo "nameserver 8.8.8.8" > /etc/resolv.conf'
```

### Flush DNS Cache

```bash
sudo systemd-resolve --flush-caches
```

## Examples

```bash
# DNS failure on corporate network
npm install vue
# Fix: Use Google DNS
dig registry.npmjs.org

# Stale DNS cache
npm install next
# Fix: Flush DNS cache
sudo systemd-resolve --flush-caches
npm install next

```

## Related Errors

- [Connection Refused]({{< relref "/tools/npm/econnrefused-connection-refused" >}}) -- connection refused
- [Host Unreachable]({{< relref "/tools/npm/ehostunreach-host-unreachable" >}}) -- host unreachable
