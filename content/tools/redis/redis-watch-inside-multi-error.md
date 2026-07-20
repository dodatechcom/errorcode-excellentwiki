---
title: "[Solution] Redis WATCH Inside MULTI Error"
description: "How to fix Redis WATCH inside MULTI error when WATCH is used inside a transaction"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Common Causes

- WATCH command used after MULTI
- Client library error in transaction handling

## How to Fix

Use WATCH before MULTI:

```bash
# Correct order
redis-cli WATCH mykey
redis-cli MULTI
redis-cli SET mykey newvalue
redis-cli EXEC
```

For multiple keys:

```bash
redis-cli WATCH key1 key2
redis-cli MULTI
redis-cli SET key1 value1
redis-cli SET key2 value2
redis-cli EXEC
```

## Examples

```bash
# Wrong: WATCH inside MULTI
redis-cli MULTI
redis-cli WATCH mykey
# ERR WATCH inside MULTI

# Correct: WATCH before MULTI
redis-cli WATCH mykey
redis-cli MULTI
redis-cli SET mykey newvalue
redis-cli EXEC
```
