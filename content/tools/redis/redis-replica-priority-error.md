---
title: "[Solution] Redis Replica Priority Error"
description: "How to fix Redis replica-priority configuration errors during failover"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Replica-priority set to 0 (ineligible for promotion)
- All replicas have priority 0
- Sentinel cannot find a suitable replica to promote

## Fix

Check replica priority:

```bash
redis-cli CONFIG GET replica-priority
```

Set correct priority:

```bash
# Primary replica (higher priority = less likely to be promoted first)
redis-cli CONFIG SET replica-priority 100

# Replica that should never be promoted
redis-cli CONFIG SET replica-priority 0
```

## Examples

```bash
# Check priority
redis-cli CONFIG GET replica-priority

# Set priority for sentinel failover
redis-cli CONFIG SET replica-priority 50

# Check Sentinel view
redis-cli -p 26379 SENTINEL replicas mymaster | grep priority
```
