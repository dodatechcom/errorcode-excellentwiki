---
title: "[Solution] Redis Cluster Resharding Error"
description: "How to fix Redis cluster resharding failures when moving slots between nodes"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Target node cannot accept slots (insufficient memory)
- Source node cannot migrate keys
- Network timeout during migration
- Slot already being migrated

## Fix

Check resharding status:

```bash
redis-cli CLUSTER NODES | grep migrating
```

Complete or abort resharding:

```bash
# Complete migration by setting slot to target node
redis-cli CLUSTER SETSLOT 5000 STABLE
```

Check cluster health:

```bash
redis-cli --cluster check 127.0.0.1:7001
```

Use interactive reshard:

```bash
redis-cli --cluster reshard 127.0.0.1:7001
```

## Examples

```bash
# Check migrating slots
redis-cli CLUSTER NODES | grep -i migrating

# Check cluster balance
redis-cli CLUSTER SLOTS | grep -c "127.0.0.1:7001"

# Repair cluster
redis-cli --cluster fix 127.0.0.1:7001
```
