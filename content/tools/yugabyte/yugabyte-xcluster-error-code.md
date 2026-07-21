---
title: "YugabyteDB XCluster Error Code"
description: "XCluster error with specific code"
tools:
  - yugabyte
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
XCluster replication returning specific error code.

## Common Causes
- Target cluster unreachable
- Replication lag too high
- Table not in replication group

## How to Fix
```bash
# Check xCluster status
yb-admin list_replication_groups

# Add table to replication
yb-admin add_table_to_replication_group
```

## Examples
```bash
# Check replication lag
yb-admin get_replication_status
# Remove from replication
yb-admin remove_table_from_replication_group
```

