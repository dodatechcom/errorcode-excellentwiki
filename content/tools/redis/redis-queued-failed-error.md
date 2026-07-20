---
title: "[Solution] Redis QUEUED Command Failed Error"
description: "How to fix Redis command queuing failure inside a transaction"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Command syntax error in queued command
- Wrong number of arguments for a queued command
- Command not supported inside MULTI

## Fix

Verify commands before queuing:

```bash
redis-cli MULTI
redis-cli SET key1 value1
# Check for syntax errors
redis-cli EXEC
```

Non-queueable commands in MULTI:

```bash
# These commands cannot be queued
redis-cli MULTI
redis-cli MULTI  # will fail
redis-cli EXEC
```

## Examples

```bash
# Correct transaction
redis-cli MULTI
OK
redis-cli SET key1 value1
QUEUED
redis-cli SET key2 value2
QUEUED
redis-cli EXEC

# Command with error (will fail at EXEC)
redis-cli MULTI
redis-cli SET key1 value1
QUEUED
redis-cli INCR key1  # OK if key1 is string
redis-cli EXEC
```
