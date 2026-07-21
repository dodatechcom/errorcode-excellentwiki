---
title: "[Solution] Vitess Tablet Transaction Error"
description: "How to fix Vitess tablet transaction errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Transaction not found
- Transaction timeout
- Transaction lock conflict

## How to Fix

```bash
mysql -h vtgate-host -P 15306 -e "SELECT * FROM users WHERE id = 1"
```

## Examples

```bash
curl http://vtgate-host:15001/debug/tx_stats
```
