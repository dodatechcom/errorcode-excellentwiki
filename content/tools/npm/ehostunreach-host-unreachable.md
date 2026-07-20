---
title: "[Solution] npm install EHOSTUNREACH Host Unreachable"
description: "Fix EHOSTUNREACH host unreachable errors during npm install by resolving network routing and DNS configuration issues."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install EHOSTUNREACH Host Unreachable

This guide helps you diagnose and resolve npm install EHOSTUNREACH Host Unreachable errors encountered when running npm commands.

## Common Causes

- Network route to the npm registry host is unavailable
- DNS resolution pointing to an unreachable IP address
- VPN or network interface misconfiguration blocking access

## How to Fix

### Check Network Routing

```bash
traceroute registry.npmjs.org
```

### Flush DNS Cache

```bash
sudo dscacheutil -flushcache && sudo killall -HUP mDNSResponder
```

### Use a Different DNS Server

```bash
npm config set registry https://registry.npmjs.org
```

## Examples

```bash
# VPN blocking registry access
npm install typescript
# Fix: Disconnect VPN or use alternative DNS
dig registry.npmjs.org
npm config set registry https://registry.npmmirror.com

# No route to host error
npm install react-scripts
# Fix: Check routing table
netstat -rn

```

## Related Errors

- [Connection Refused]({{< relref "/tools/npm/econnrefused-connection-refused" >}}) -- connection refused
- [DNS Error]({{< relref "/tools/npm/enotfound-dns-error" >}}) -- DNS resolution failed
