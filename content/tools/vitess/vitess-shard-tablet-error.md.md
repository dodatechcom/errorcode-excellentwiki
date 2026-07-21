---
title: "Vitess Shard Tablet Error"
description: "Shard tablet operation failure"
tools:
  - vitess
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Shard tablet operation is failing.

## Common Causes
- Shard tablet not found
- Shard tablet type error
- Shard tablet health issue

## How to Fix
```bash
# Check shard tablets
vtctlclient ListTablets | grep mykeyspace/0

# Check shard status
vtctlclient GetShard mykeyspace/0
```

## Examples
```bash
# Check shard tablets
vtctlclient ListShards mykeyspace
# Verify shard routing
vtctlclient ValidateKeyspace mykeyspace
```

