---
title: "[Solution] Vitess Tablet Query Cache Error"
description: "How to fix Vitess tablet query cache errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Query cache not enabled
- Query cache size too small
- Query cache invalidated

## How to Fix

```bash
mysql -h tablet-host -P 15306 -e "SHOW VARIABLES LIKE 'query_cache%'
```

## Examples

```bash
mysql -h tablet-host -P 15306 -e "SHOW STATUS LIKE 'Qcache%'
```
