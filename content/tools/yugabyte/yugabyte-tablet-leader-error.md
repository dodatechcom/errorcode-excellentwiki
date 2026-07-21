---
title: "[Solution] YugabyteDB Tablet Leader Error"
description: "How to fix YugabyteDB tablet leader errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- No tablet leader elected
- Leader election failing
- Leader node down

## How to Fix

```bash
yb-admin list_tablets mydb mytable 0
```

## Examples

```bash
yb-admin get_tablet_disk_usage
```
