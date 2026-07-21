---
title: "Vitess Tablet Replication Consistency Error"
description: "Tablet replication consistency failure"
tools:
  - vitess
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Tablet replication consistency is failing.

## Common Causes
- Replication lag
- Data inconsistency
- Network partition

## How to Fix
```bash
# Check replication status
vtctlclient ReplicationStatus <tablet-alias>

# Check data consistency
vtctlclient ValidateKeyspace mykeyspace
```

## Examples
```bash
# Check replication lag
vtctlclient ReplicationStatus <tablet-alias> | grep lag
# Verify data consistency
vtctlclient ValidateTablets mykeyspace
```

