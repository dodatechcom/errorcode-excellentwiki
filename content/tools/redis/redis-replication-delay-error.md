---
title: "[Solution] Redis Replication Delay Error"
description: "How to fix Redis replication delay and lag issues"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Common Causes

- High write throughput on master
- Network latency between master and replica
- Replica disk I/O bottleneck
- Replication backlog too small

## How to Fix

Check replication lag:

```bash
redis-cli INFO replication | grep master_repl_offset
redis-cli INFO replication | grep slave_repl_offset
```

Increase replication backlog:

```bash
redis-cli CONFIG SET repl-backlog-size 256mb
```

Check network latency:

```bash
redis-cli --latency -h master-host
```

Monitor replica offset:

```bash
watch -n 1 'redis-cli INFO replication | grep -E "master_repl_offset|slave_repl_offset"'
```

## Examples

```bash
# Check replication status
redis-cli INFO replication

# Increase backlog
redis-cli CONFIG SET repl-backlog-size 256mb

# Check replica ping
redis-cli INFO replication | grep master_last_io_seconds_ago
```
