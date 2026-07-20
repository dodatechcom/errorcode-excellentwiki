---
title: "[Solution] Redis DISCARD Without MULTI Error"
description: "How to fix Redis DISCARD without MULTI error"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Common Causes

- Client sends DISCARD without starting a transaction with MULTI
- Connection state issue

## Fix

Start transaction first:

```bash
redis-cli MULTI
redis-cli SET key1 value1
redis-cli DISCARD
```

Check if in transaction mode:

```bash
redis-cli DISCARD
# ERR DISCARD without MULTI
```

## Examples

```bash
# Correct usage
redis-cli MULTI
OK
redis-cli SET key1 value1
QUEUED
redis-cli DISCARD
OK

# Wrong usage
redis-cli DISCARD
# ERR DISCARD without MULTI
```
