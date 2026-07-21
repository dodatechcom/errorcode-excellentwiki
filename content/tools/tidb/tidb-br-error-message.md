---
title: "TiDB BR Error Message"
description: "BR detailed error message"
tools:
  - tidb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
BR showing detailed error message.

## Common Causes
- Backup storage error
- Network timeout
- Version mismatch

## How to Fix
```bash
# Check BR error details
br backup full --pd pd:2379 --storage s3://bucket/path --log-file br.log 2>&1 | tail -50

# Check error type
cat br.log | grep -i 'error\|fail'
```

## Examples
```bash
# Verbose error output
br backup db --db mydb --pd pd:2379 --storage local:///backup --log-file br.log --log-level debug
# Check error stack
br validate backup --storage s3://bucket/path 2>&1 | grep -A5 'Error'
```

