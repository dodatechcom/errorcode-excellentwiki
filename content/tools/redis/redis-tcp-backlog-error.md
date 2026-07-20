---
title: "[Solution] Redis TCP Backlog Error"
description: "How to fix Redis TCP backlog overflow errors"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- TCP backlog queue full during connection spikes
- Operating system tcp backlog limit exceeded
- High connection rate overwhelming backlog

## Fix

Check current backlog:

```bash
redis-cli CONFIG GET tcp-backlog
```

Increase TCP backlog:

```bash
redis-cli CONFIG SET tcp-backlog 1024
```

Make permanent in redis.conf:

```bash
sudo sed -i 's/^tcp-backlog 511/tcp-backlog 2048/' /etc/redis/redis.conf
```

Check system limits:

```bash
sysctl net.core.somaxconn
```

Increase system backlog:

```bash
sudo sysctl net.core.somaxconn=4096
```

## Examples

```bash
# Check TCP backlog
redis-cli CONFIG GET tcp-backlog

# Check system max connections
cat /proc/sys/net/core/somaxconn

# Monitor connection rate
redis-cli INFO clients | grep connected_clients
```
