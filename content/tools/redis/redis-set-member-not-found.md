---
title: "[Solution] Redis Set Member Not Found Error"
description: "How to fix Redis errors when set member is not found"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Member was removed from the set
- Member name misspelled
- Case sensitivity issues

## Fix

Check set membership:

```bash
redis-cli SISMEMBER myset "member"
```

List all members:

```bash
redis-cli SMEMBERS myset
```

Add member if not exists:

```bash
redis-cli SADD myset "member"
```

## Examples

```bash
# Check if member exists
redis-cli SISMEMBER myset "user1"

# List all members
redis-cli SMEMBERS myset

# Count members
redis-cli SCARD myset
```
