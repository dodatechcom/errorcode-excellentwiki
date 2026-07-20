---
title: "[Solution] Redis EXECABORT Transaction Discarded Error"
description: "How to fix Redis EXECABORT error when transaction is automatically discarded"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- WATCHed key modified during transaction
- Server rejecting transaction due to memory
- Command syntax error inside MULTI block

## Fix

Check what commands were queued:

```bash
redis-cli MULTI
redis-cli SET key1 value1
redis-cli EXEC
```

Retry without WATCH if not needed:

```bash
redis-cli MULTI
redis-cli SET key1 value1
redis-cli EXEC
```

Use UNWATCH to cancel:

```bash
redis-cli WATCH mykey
redis-cli UNWATCH
```

## Examples

```bash
# Simple transaction without WATCH
redis-cli MULTI
redis-cli SET name "John"
redis-cli SET age "30"
redis-cli EXEC

# Cancel WATCH if not needed
redis-cli WATCH mykey
redis-cli UNWATCH
```
