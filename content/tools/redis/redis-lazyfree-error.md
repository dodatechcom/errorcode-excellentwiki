---
title: "[Solution] Redis Lazy Free Configuration Error"
description: "How to fix Redis lazy free configuration errors for asynchronous key deletion"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Lazy free not enabled causing blocking deletes
- DEL on large keys blocking server
- Memory not reclaimed after deletion

## Fix

Check lazy free settings:

```bash
redis-cli CONFIG GET lazyfree-lazy-expire
redis-cli CONFIG SET lazyfree-lazy-expire yes
redis-cli CONFIG SET lazyfree-lazy-server-del yes
redis-cli CONFIG SET lazyfree-lazy-user-del yes
```

Use UNLINK instead of DEL:

```bash
redis-cli UNLINK mykey
```

Enable lazy free for all operations:

```bash
redis-cli CONFIG SET lazyfree-lazy-expire yes
redis-cli CONFIG SET lazyfree-lazy-server-del yes
redis-cli CONFIG SET lazyfree-lazy-user-flush yes
```

## Examples

```bash
# Check lazy free settings
redis-cli CONFIG GET lazyfree-*

# Use UNLINK
redis-cli UNLINK largekey

# Monitor memory after delete
redis-cli INFO memory | grep used_memory_human
```
