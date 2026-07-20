---
title: "[Solution] Redis Busy Writing Error"
description: "How to fix Redis busy writing error when the server is blocked by a long-running write operation"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Slow RDB save or AOF rewrite blocking other commands
- Large dataset being persisted to disk
- Fork operation for background saves

## Fix

Disable RDB saves temporarily:

```bash
redis-cli CONFIG SET save ""
```

Check RDB background save status:

```bash
redis-cli LASTSAVE
```

Kill a blocking BGSAVE:

```bash
redis-cli CLIENT KILL TYPE NORMAL LADDR <addr>
```

Switch to AOF persistence:

```bash
redis-cli CONFIG SET appendonly yes
```

## Examples

```bash
# Trigger background save
redis-cli BGSAVE

# Check if background operation is running
redis-cli INFO persistence | grep rdb_bgsave_in_progress

# Monitor disk I/O
iostat -x 1
```
