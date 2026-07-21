---
title: "[Solution] Vitess Tablet Replication Position Error"
description: "How to fix Vitess tablet replication position errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Replication position not found
- Replication position stale
- Replication position too old

## How to Fix

```bash
vtctlclient ListTablets | grep -i position
```

## Examples

```bash
mysql -h tablet-host -P 15306 -e "SHOW MASTER STATUS"
```
