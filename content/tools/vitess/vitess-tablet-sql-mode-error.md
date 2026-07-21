---
title: "[Solution] Vitess Tablet SQL Mode Error"
description: "How to fix Vitess tablet SQL mode errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- SQL mode not compatible
- Strict mode blocking queries
- SQL mode not set

## How to Fix

```bash
mysql -h tablet-host -P 15306 -e "SHOW VARIABLES LIKE 'sql_mode'"
```

## Examples

```bash
mysql -h tablet-host -P 15306 -e "SET SESSION sql_mode = 'STRICT_TRANS_TABLES'"
```
