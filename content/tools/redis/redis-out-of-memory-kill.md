---
title: "[Solution] Redis Out of Memory Process Kill"
description: "How to handle Redis being killed by the Linux OOM killer"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Redis using too much system memory
- OOM killer targeting Redis process
- Overcommit memory disabled

## Fix

Check OOM killer logs:

```bash
dmesg | grep -i oom
journalctl -k | grep -i oom
```

Protect Redis from OOM killer:

```bash
echo -17 > /proc/$(pidof redis-server)/oom_adj
```

Set overcommit memory:

```bash
sudo sysctl vm.overcommit_memory=1
```

Limit Redis memory:

```bash
redis-cli CONFIG SET maxmemory 3gb
redis-cli CONFIG SET maxmemory-policy allkeys-lru
```

## Examples

```bash
# Check Redis RSS memory
redis-cli INFO memory | grep used_memory_rss_human

# Set memory limit
redis-cli CONFIG SET maxmemory 4gb

# Monitor process memory
ps aux | grep redis-server
```
