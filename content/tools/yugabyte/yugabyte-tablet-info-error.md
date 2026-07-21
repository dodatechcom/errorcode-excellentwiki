---
title: "[Solution] YugabyteDB Tablet Info Error"
description: "How to fix YugabyteDB tablet info errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Tablet info not found
- Tablet info stale
- Tablet info query failing

## How to Fix

```bash
yb-admin list_tablets mydb mytable 0
```

## Examples

```bash
yb-admin get_tablet_disk_usage
```
