---
title: "[Solution] Redis Sentinel Monitor Duplicate Error"
description: "How to fix Sentinel duplicate monitor errors when trying to add duplicate monitoring"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Sentinel already monitoring the specified master
- Configuration file contains duplicate MONITOR directives
- Multiple Sentinel instances with overlapping configs

## Fix

Check current monitoring:

```bash
redis-cli -p 26379 SENTINEL masters | grep name
```

Remove duplicate MONITOR from sentinel.conf:

```bash
sudo sed -i '/^sentinel monitor/d' /etc/redis/sentinel.conf
```

Reload Sentinel:

```bash
sudo systemctl restart redis-sentinel
```

## Examples

```bash
# List all monitored masters
redis-cli -p 26379 SENTINEL masters

# Check specific master
redis-cli -p 26379 SENTINEL get-master-addr-by-name mymaster

# View Sentinel config
grep monitor /etc/redis/sentinel.conf
```
