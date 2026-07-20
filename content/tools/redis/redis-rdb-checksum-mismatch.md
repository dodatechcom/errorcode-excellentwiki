---
title: "[Solution] Redis RDB Checksum Mismatch Error"
description: "How to fix Redis RDB checksum mismatch when loading a corrupted RDB file"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- RDB file corrupted during write
- Disk sector failure
- File truncated during server crash
- Filesystem corruption

## Fix

Check RDB file integrity:

```bash
redis-check-rdb /var/lib/redis/dump.rdb
```

Attempt repair:

```bash
redis-check-rdb --fix /var/lib/redis/dump.rdb
```

If unfixable, remove the RDB and restart:

```bash
sudo mv /var/lib/redis/dump.rdb /var/lib/redis/dump.rdb.bak
sudo systemctl restart redis
```

Enable AOF for additional safety:

```bash
redis-cli CONFIG SET appendonly yes
```

## Examples

```bash
# Verify RDB checksum
redis-check-rdb /var/lib/redis/dump.rdb

# Check RDB file size
ls -lh /var/lib/redis/dump.rdb

# Monitor RDB save
redis-cli INFO persistence | grep rdb_last_bgsave_status
```
