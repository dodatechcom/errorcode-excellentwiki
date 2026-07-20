---
title: "[Solution] Redis Replica Read Only Error"
description: "How to fix Redis replica read-only errors when trying to write to a replica"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Replica configured with replica-read-only yes
- Application writing to replica instead of master

## Fix

Check read-only setting:

```bash
redis-cli CONFIG GET replica-read-only
```

Disable read-only (not recommended):

```bash
redis-cli CONFIG SET replica-read-only no
```

Route writes to master:

```bash
redis-cli -h master-host -p 6379 SET key value
```

## Examples

```bash
# Check if replica is read-only
redis-cli CONFIG GET replica-read-only

# Write to master
redis-cli -h master-host SET key value

# Read from replica
redis-cli -h replica-host GET key
```
