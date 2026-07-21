---
title: "[Solution] YugabyteDB Tablet Migration Error"
description: "How to fix YugabyteDB tablet migration errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Tablet migration failing
- Tablet migration stuck
- Tablet migration timeout

## How to Fix

```bash
yb-admin list_tablets mydb mytable 0
```

## Examples

```bash
yb-admin get_tablet_disk_usage
```
