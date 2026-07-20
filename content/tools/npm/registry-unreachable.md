---
title: "[Solution] npm ping Registry Unreachable"
description: "Fix npm ping registry unreachable errors by testing network connectivity, checking DNS resolution, and verifying registry server status."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm ping Registry Unreachable

This guide helps you diagnose and resolve npm ping Registry Unreachable errors encountered when running npm commands.

## Common Causes

- npm registry server is down or unreachable
- Network firewall is blocking outgoing connections
- DNS resolution is failing for registry.npmjs.org

## How to Fix

### Test Registry Connectivity

```bash
curl -I https://registry.npmjs.org
```

### Check DNS Resolution

```bash
nslookup registry.npmjs.org
```

### Try Alternative Registry

```bash
npm config set registry https://registry.npmmirror.com
```

## Examples

```bash
# Registry server down
npm ping
# Fix: Check status and use mirror
curl https://status.npmjs.org
npm config set registry https://registry.npmmirror.com

# Firewall blocking connection
npm ping
# Fix: Check firewall rules
sudo iptables -L

```

## Related Errors

- [ETIMEDOUT Timeout]({{< relref "/tools/npm/etimedout-timeout" >}}) -- request timeout
- [DNS Error]({{< relref "/tools/npm/enotfound-dns-error" >}}) -- DNS resolution failed
