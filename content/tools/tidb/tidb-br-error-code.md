---
title: "TiDB BR Error Code"
description: "BR error with specific code"
tools:
  - tidb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
BR returning specific error code.

## Common Causes
- Backup storage unreachable
- Version incompatibility
- Insufficient privileges

## How to Fix
```bash
# Check BR logs
br backup full --pd pd:2379 --storage s3://bucket/path --log-file br.log

# Check error details
cat br.log | grep -i error
```

## Examples
```bash
# Verbose backup
br backup db --db mydb --pd pd:2379 --storage local:///backup --log-file br.log
# Check backup metadata
br validate backup --storage s3://bucket/path
```

