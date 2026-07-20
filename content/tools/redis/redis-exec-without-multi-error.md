---
title: "[Solution] Redis EXEC Without MULTI Error"
description: "How to fix Redis EXEC without MULTI error when EXEC is called without starting a transaction"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Common Causes

- Client sends EXEC without prior MULTI command
- Connection state lost between MULTI and EXEC
- Client library bug

## How to Fix

Always start transaction with MULTI:

```bash
redis-cli MULTI
redis-cli SET key1 value1
redis-cli SET key2 value2
redis-cli EXEC
```

Check if in transaction mode:

```bash
redis-cli EXEC
# If not in MULTI, returns: ERR EXEC without MULTI
```

Use pipeline instead of transaction:

```python
pipe = r.pipeline()
pipe.set('key1', 'value1')
pipe.set('key2', 'value2')
pipe.execute()
```

## Examples

```bash
# Correct transaction
redis-cli MULTI
OK
redis-cli SET a 1
QUEUED
redis-cli SET b 2
QUEUED
redis-cli EXEC
1) OK
2) OK

# Wrong - EXEC without MULTI
redis-cli EXEC
# ERR EXEC without MULTI
```
