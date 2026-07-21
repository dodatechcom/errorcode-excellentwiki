---
title: "[Solution] Vitess Tablet Master Position Error"
description: "How to fix Vitess tablet master position errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Master position not found
- Master position stale
- Master position not updated

## How to Fix

```bash
vtctlclient ListTablets | grep -i master
```

## Examples

```bash
mysql -h tablet-host -P 15306 -e "SHOW MASTER STATUS"
```
