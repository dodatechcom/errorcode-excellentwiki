---
title: "Vitess Keyspace Shard Error"
description: "Keyspace shard operation failure"
tools:
  - vitess
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Keyspace shard operation is failing.

## Common Causes
- Keyspace not found
- Shard not available
- Keyspace configuration error

## How to Fix
```bash
# Check keyspace
vtctlclient GetKeyspace mykeyspace

# Check shards
vtctlclient FindAllShardsInKeyspace mykeyspace
```

## Examples
```bash
# List all keyspace shards
vtctlclient ListShards mykeyspace
# Validate keyspace
vtctlclient ValidateKeyspace mykeyspace
```

