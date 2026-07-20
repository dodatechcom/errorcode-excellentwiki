---
title: "[Solution] Redis MULTI EXEC Nested Transaction Error"
description: "How to fix Redis nested transaction errors when MULTI is called inside a transaction"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Attempting to start a new MULTI inside an active MULTI block
- Client library error

## Fix

Do not nest MULTI:

```bash
# Wrong
redis-cli MULTI
redis-cli MULTI  # ERR MULTI calls can not be nested
redis-cli EXEC

# Correct - single MULTI block
redis-cli MULTI
redis-cli SET key1 value1
redis-cli EXEC
```

Use pipelining for batching:

```python
pipe = r.pipeline(transaction=False)
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
redis-cli EXEC
1) OK

# Wrong - nested MULTI
redis-cli MULTI
redis-cli MULTI
# ERR MULTI calls can not be nested
```
