---
title: "[Solution] YugabyteDB Tablet Replica Error"
description: "How to fix YugabyteDB tablet replica errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Replica not catching up
- Replica lag too high
- Replica node down

## How to Fix

```bash
yb-admin list_tablets mydb mytable 0
```

## Examples

```bash
yb-admin table_statistics mydb mytable
```
