---
title: "[Solution] Vitess Tablet Slave Error"
description: "How to fix Vitess tablet slave errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Slave not following master
- Slave lag too high
- Slave replication stopped

## How to Fix

```bash
vtctlclient ListTablets myks 0
```

## Examples

```bash
mysql -h tablet-host -P 15306 -e "SHOW SLAVE STATUS\G"
```
