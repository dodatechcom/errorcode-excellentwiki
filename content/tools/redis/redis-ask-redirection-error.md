---
title: "[Solution] Redis ASK Redirection Error"
description: "How to fix Redis ASK redirection error during slot migration"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Common Causes

- Slot is being migrated to another node
- Client sending commands to wrong node during migration
- Client not handling ASK redirection correctly

## How to Fix

Handle ASK redirection in client:

```bash
# The client should:
# 1. Send ASKING command to the target node
# 2. Then retry the command on the target node
```

Check migration status:

```bash
redis-cli CLUSTER NODES | grep migrating
```

Wait for migration to complete:

```bash
redis-cli CLUSTER INFO | grep cluster_slots_assigned
```

## Examples

```bash
# Check slot migration
redis-cli CLUSTER NODES | grep -E "importing|migrating"

# Manually set slot
redis-cli CLUSTER SETSLOT 5000 NODE <node-id>

# Check cluster slots
redis-cli CLUSTER SLOTS
```
