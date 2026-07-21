---
title: "Vitess Tablet Restore Error"
description: "Tablet restore operation failure"
tools:
  - vitess
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Tablet restore operation is failing.

## Common Causes
- Backup not found
- Restore target keyspace not empty
- Storage backend error

## How to Fix
```bash
# Check backup availability
vtctlclient ListBackups mykeyspace/0

# Cancel restore
vtctlclient Restore mykeyspace/0 --cancel
```

## Examples
```bash
# Start restore
vtctlclient Restore mykeyspace/0 --backup_timestamp 2024-01-01T00:00:00Z
# Check restore status
vtctlclient GetShard mykeyspace/0
```

