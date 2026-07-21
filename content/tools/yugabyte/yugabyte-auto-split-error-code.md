---
title: "YugabyteDB Auto Split Error Code"
description: "Auto split error with specific code"
tools:
  - yugabyte
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Auto split returning specific error code.

## Common Causes
- Split threshold not met
- Split in progress
- Insufficient resources

## How to Fix
```bash
# Check auto-split settings
curl http://localhost:9000/conf | grep auto_split

# Monitor split
curl http://localhost:9000/metrics | grep split
```

## Examples
```bash
# Check tablet sizes
yb-admin list_tablets | grep -E 'table_id|tablet_id'
# Monitor split operations
curl http://localhost:9000/metrics | grep split
```

