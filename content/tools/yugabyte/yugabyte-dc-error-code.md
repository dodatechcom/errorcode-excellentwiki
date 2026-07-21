---
title: "YugabyteDB DC Error Code"
description: "DC error with specific code"
tools:
  - yugabyte
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
DC configuration returning specific error code.

## Common Causes
- DC placement misconfigured
- Cross-DC replication failed
- Network latency

## How to Fix
```bash
# Check DC placement
yb-admin get_placement_info

# Modify DC config
yb-admin modify_table_placement_info
```

## Examples
```bash
# Check tablet placement
yb-admin list_tablets | grep dc
# Verify DC config
yb-admin get_placement_info --master_addresses localhost:7100
```

