---
title: "Vitess Tablet Replication Error"
description: "Tablet replication failure"
tools:
  - vitess
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Tablet replication is failing.

## Common Causes
- Replication lag
- Binlog position stale
- Replica crashed

## How to Fix
```bash
# Check replication status
vtctlclient ReplicationStatus <tablet-alias>

# Stop and restart replication
vtctlclient StopSlave <tablet-alias>
vtctlclient StartSlave <tablet-alias>
```

## Examples
```bash
# Check replication lag
vtctlclient ReplicationStatus <tablet-alias> | grep lag
# Reset replication
vtctlclient ResetReplication <tablet-alias>
```

