---
title: "[Solution] Linux: systemd-resolved-cache-error -- stale DNS cache"
description: "Fix Linux systemd-resolved cache errors. Resolved serving stale DNS answers from cache."
os: ["linux"]
error-types: ["systemd-error"]
severities: ["warning"]
---

# Linux: Systemd-Resolved Cache Error

Resolved cache errors cause stale DNS answers to be served, preventing fresh resolution.

## Common Causes

- Negative cache entry TTL too long
- DNS cache not flushed after upstream changes
- Cache corruption causing SERVFAIL responses
- LLMNR or mDNS cache conflicts
- Cache size limit causing eviction of valid entries

## How to Fix

### 1. Flush Cache

```bash
sudo resolvectl flush-caches
resolvectl statistics
```

### 2. Check Cache Stats

```bash
resolvectl statistics
resolvectl query example.com
resolvectl cache
```

### 3. Restart Resolved

```bash
sudo systemctl restart systemd-resolved
sudo resolvectl flush-caches
resolvectl query example.com
```

## Examples

```bash
$ resolvectl statistics
Current Cache Size: 523
Cache Miss: 1204
Cache Hit: 8932
$ resolvectl flush-caches
$ resolvectl statistics
Current Cache Size: 0
```
