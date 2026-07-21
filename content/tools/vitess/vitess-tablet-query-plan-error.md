---
title: "[Solution] Vitess Tablet Query Plan Error"
description: "How to fix Vitess tablet query plan errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Query plan not cached
- Query plan too complex
- Query plan cache full

## How to Fix

```bash
curl http://vtgate-host:15001/debug/query_plans
```

## Examples

```bash
mysql -h vtgate-host -P 15306 -e "EXPLAIN FORMAT=VITESS SELECT * FROM users WHERE id = 1"
```
