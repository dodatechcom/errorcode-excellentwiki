---
title: "[Solution] Vitess Tablet Semi-Sync Error"
description: "How to fix Vitess tablet semi-synchronous replication errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Semi-sync not enabled
- Semi-sync timeout
- No semi-sync replicas available

## How to Fix

```bash
mysql -h tablet-host -P 15306 -e "SHOW VARIABLES LIKE 'rpl_semi_sync%'
```

## Examples

```bash
mysql -h tablet-host -P 15306 -e "SHOW SLAVE STATUS"
```
