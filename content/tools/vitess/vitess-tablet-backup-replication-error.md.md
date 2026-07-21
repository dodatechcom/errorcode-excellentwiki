---
title: "Vitess Tablet Backup Replication Error"
description: "Tablet backup replication failure"
tools:
  - vitess
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Tablet backup replication is failing.

## Common Causes
- Backup storage unreachable
- Insufficient disk space
- Backup process crashed

## How to Fix
```bash
# Check backup status
vtctlclient Backup <tablet-alias>

# List backups
vtctlclient ListBackups mykeyspace/0
```

## Examples
```bash
# Create backup
vtctlclient Backup mykeyspace/0
# Check backup logs
tail -100 /var/log/vttablet/vttablet.log | grep backup
```

