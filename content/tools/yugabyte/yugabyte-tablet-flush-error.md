---
title: "[Solution] YugabyteDB Tablet Flush Error"
description: "How to fix YugabyteDB tablet flush errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Flush not completing
- Flush failing
- Flush lag too high

## How to Fix

```bash
yb-admin list_tablets mydb mytable 0
```

## Examples

```bash
yb-admin get_tablet_disk_usage
```
