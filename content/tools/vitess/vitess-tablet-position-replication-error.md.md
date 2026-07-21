---
title: "Vitess Tablet Position Replication Error"
description: "Tablet position replication failure"
tools:
  - vitess
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Tablet position replication is failing.

## Common Causes
- Binlog position stale
- Replication lag
- Position corruption

## How to Fix
```bash
# Check replication position
vtctlclient MasterPosition mykeyspace/0

# Reset replication position
vtctlclient ResetReplication <tablet-alias>
```

## Examples
```bash
# Check master position
vtctlclient MasterPosition mykeyspace/0
# Check slave lag
vtctlclient ReplicationStatus <tablet-alias>
```

