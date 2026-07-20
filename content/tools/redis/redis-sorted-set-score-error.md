---
title: "[Solution] Redis Sorted Set Score Error"
description: "How to fix Redis sorted set score-related errors"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Score is not a valid floating point number
- Trying to increment score on a member that does not exist
- NAN or INF values in score

## Fix

Verify member exists before incrementing:

```bash
redis-cli ZSCORE myzset member
```

Add member with score:

```bash
redis-cli ZADD myzset 1.0 member
```

Increment score:

```bash
redis-cli ZINCRBY myzset 1.0 member
```

## Examples

```bash
# Check member score
redis-cli ZSCORE myzset player1

# Get rank
redis-cli ZRANK myzset player1

# Increment score
redis-cli ZINCRBY myzset 10 player1
```
