---
title: "[Solution] Vitess Tablet Slave Position Error"
description: "How to fix Vitess tablet slave position errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Slave position not found
- Slave position stale
- Slave position not updated

## How to Fix

```bash
vtctlclient ListTablets | grep -i slave
```

## Examples

```bash
mysql -h tablet-host -P 15306 -e "SHOW SLAVE STATUS"
```
