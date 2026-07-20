---
title: "[Solution] Redis List Index Out of Range Error"
description: "How to fix Redis list index out of range errors"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Index exceeds list length
- List is empty
- Using positive index on a short list

## Fix

Check list length:

```bash
redis-cli LLEN mylist
```

Use negative indices to access from end:

```bash
redis-cli LINDEX mylist -1  # Last element
```

Safely access with index check:

```bash
length=$(redis-cli LLEN mylist)
if [ "$index" -lt "$length" ]; then
  redis-cli LINDEX mylist $index
fi
```

## Examples

```bash
# Check list length
redis-cli LLEN mylist

# Access last element
redis-cli LINDEX mylist -1

# Get range of elements
redis-cli LRANGE mylist 0 10
```
