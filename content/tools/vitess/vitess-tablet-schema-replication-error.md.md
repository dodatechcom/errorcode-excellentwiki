---
title: "Vitess Tablet Schema Replication Error"
description: "Tablet schema replication failure"
tools:
  - vitess
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Tablet schema replication is failing.

## Common Causes
- Schema mismatch
- Table structure changed
- DDL statement failed

## How to Fix
```bash
# Check schema
vtctlclient GetSchema mykeyspace/0

# Reload schema
vtctlclient ReloadSchema mykeyspace/0
```

## Examples
```bash
# Check schema diff
vtctlclient SchemaDiff mykeyspace/0 mykeyspace/1
# Apply schema change
vtctlclient ApplySchema --sql "ALTER TABLE mytable ADD COLUMN newcol INT" mykeyspace
```

