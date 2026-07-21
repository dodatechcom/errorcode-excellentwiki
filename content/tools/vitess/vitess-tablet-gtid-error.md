---
title: "[Solution] Vitess Tablet GTID Error"
description: "How to fix Vitess tablet GTID errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- GTID not enabled
- GTID mode wrong
- GTID position not found

## How to Fix

```bash
mysql -h tablet-host -P 15306 -e "SHOW VARIABLES LIKE 'gtid_mode'"
```

## Examples

```bash
mysql -h tablet-host -P 15306 -e "SHOW MASTER STATUS"
```
