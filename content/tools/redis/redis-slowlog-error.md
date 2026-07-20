---
title: "[Solution] Redis Slowlog Configuration Error"
description: "How to fix Redis slowlog configuration and retention issues"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Slowlog-max-len too small (losing entries)
- Slowlog-log-slower-than set too high
- Slowlog consuming too much memory

## Fix

Check slowlog configuration:

```bash
redis-cli CONFIG GET slowlog-log-slower-than
redis-cli CONFIG GET slowlog-max-len
```

Adjust slowlog settings:

```bash
# Log queries slower than 10ms
redis-cli CONFIG SET slowlog-log-slower-than 10000

# Keep last 1000 entries
redis-cli CONFIG SET slowlog-max-len 1000
```

View slow log:

```bash
redis-cli SLOWLOG GET 10
redis-cli SLOWLOG LEN
```

## Examples

```bash
# Check slowlog entries
redis-cli SLOWLOG GET 5

# Reset slowlog
redis-cli SLOWLOG RESET

# Check slowlog length
redis-cli SLOWLOG LEN
```
