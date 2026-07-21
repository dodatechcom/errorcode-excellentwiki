---
title: "YugabyteDB Placement Error Code"
description: "Placement error with specific code"
tools:
  - yugabyte
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Placement returning specific error code.

## Common Causes
- Zone/region unavailable
- Placement group misconfigured
- Load balancer issue

## How to Fix
```bash
# Check placement info
yb-admin get_placement_info

# Modify placement
yb-admin modify_table_placement_info
```

## Examples
```bash
# Check tablet placement
yb-admin list_tablets | grep zone
# Verify placement constraints
yb-admin get_placement_info --master_addresses localhost:7100
```

