---
title: "[Solution] Vitess Tablet Query Timeout Error"
description: "How to fix Vitess tablet query timeout errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Query timeout too short
- Query too slow
- Network timeout

## How to Fix

```bash
mysql -h vtgate-host -P 15306 --max-allowed-packet=67108864 -e "SELECT 1"
```

## Examples

```bash
mysql -h vtgate-host -P 15306 -e "SHOW VARIABLES LIKE 'net_read_timeout'
```
