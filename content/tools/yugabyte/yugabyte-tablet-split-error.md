---
title: "[Solution] YugabyteDB Tablet Split Error"
description: "How to fix YugabyteDB tablet split errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Tablet too large to split
- Split during high write load
- Tablet server not available

## How to Fix

```bash
yb-admin list_tablets mydb mytable 0
```

## Examples

```bash
yb-admin master_leader_status
```
