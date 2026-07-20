---
title: "[Solution] Redis Swap File Full Error"
description: "How to fix Redis swap file or swap space exhaustion errors"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- System swap space exhausted
- Redis using swap due to insufficient physical memory
- Disk full preventing swap file growth

## Fix

Check swap usage:

```bash
free -h
swapon --show
```

Reduce Redis memory footprint:

```bash
redis-cli MEMORY PURGE
redis-cli CONFIG SET maxmemory 1gb
```

Add more swap space:

```bash
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

Disable swap for Redis:

```bash
sudo swapoff /swapfile
sudo sysctl vm.swappiness=10
```

## Examples

```bash
# Check if Redis is swapping
redis-cli INFO memory | grep used_memory_rss_human

# Monitor swap usage
watch -n 2 'free -h'

# Disable swap temporarily
sudo swapoff -a
```
