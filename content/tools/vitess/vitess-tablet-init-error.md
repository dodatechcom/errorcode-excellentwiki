---
title: "[Solution] Vitess Tablet Init Error"
description: "How to fix Vitess tablet initialization errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Init SQL file not found
- MySQL not started before tablet
- Init DB permissions wrong

## How to Fix

```bash
vttablet --init_db_sql_file=init_db.sql
```

## Examples

```bash
vtctlclient ListTablets
```
