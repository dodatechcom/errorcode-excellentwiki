---
title: "[Solution] Vitess Tablet Undo Error"
description: "How to fix Vitess tablet undo log errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Undo log corrupted
- Undo log not flushed
- Undo log too large

## How to Fix

```bash
mysql -h tablet-host -P 15306 -e "SHOW VARIABLES LIKE 'innodb_undo%'"
```

## Examples

```bash
mysql -h tablet-host -P 15306 -e "SELECT * FROM information_schema.innodb_undo_tablespace"
```
