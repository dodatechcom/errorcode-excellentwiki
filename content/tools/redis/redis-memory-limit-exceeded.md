---
title: "[Solution] Redis Memory Limit Exceeded"
description: "How to fix Redis memory limit being exceeded across multiple databases"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Memory spread across multiple Redis databases
- Key expiration disabled or not configured
- Data accumulation over time

## Fix

Check memory per database:

```bash
for i in $(seq 0 15); do
  echo "DB $i: $(redis-cli -n $i DBSIZE)"
done
```

Set maxmemory:

```bash
redis-cli CONFIG SET maxmemory 4gb
```

Enable eviction:

```bash
redis-cli CONFIG SET maxmemory-policy allkeys-lru
```

Find and clean unused keys:

```bash
redis-cli --bigkeys
redis-cli --memkeys --samples 100
```

## Examples

```bash
# Check total keys
redis-cli INFO keyspace

# Set TTL on old keys
redis-cli SCAN 0 MATCH temp:* COUNT 100 | while read key; do
  redis-cli EXPIRE "$key" 3600
done
```
