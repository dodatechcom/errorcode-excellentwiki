---
title: "Vitess Tablet Replication Query Error"
description: "Tablet replication query failure"
tools:
  - vitess
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Tablet replication query is failing.

## Common Causes
- Query syntax error
- Table not found
- Permission denied

## How to Fix
```bash
# Check query logs
vtctlclient Query <tablet> "SHOW TABLES"

# Validate query
vtctlclient Explain mykeyspace/0 "SELECT * FROM mytable"
```

## Examples
```bash
# Execute query directly
vtctlclient ExecuteFetch "SELECT 1" <tablet-alias>
# Check query stats
vtctlclient GetQueryStats <tablet-alias>
```

