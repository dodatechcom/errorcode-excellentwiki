---
title: "[Solution] YugabyteDB Tablet Deletion Error"
description: "How to fix YugabyteDB tablet deletion errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Tablet not empty
- Tablet leader not available
- Tablet in use

## How to Fix

```bash
yb-admin list_tablets mydb mytable 0
```

## Examples

```bash
yb-admin get_tablet_disk_usage
```
