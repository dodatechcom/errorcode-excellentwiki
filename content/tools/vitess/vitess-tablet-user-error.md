---
title: "[Solution] Vitess Tablet User Error"
description: "How to fix Vitess tablet user management errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- User not found in MySQL
- User privileges wrong
- User not registered in VTGate

## How to Fix

```bash
mysql -h tablet-host -P 15306 -e "CREATE USER 'myuser'@'%' IDENTIFIED BY 'pass'"
```

## Examples

```bash
mysql -h tablet-host -P 15306 -e "SHOW GRANTS FOR 'myuser'@'%'
```
