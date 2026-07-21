---
title: "[Solution] YugabyteDB Tablet Creation Error"
description: "How to fix YugabyteDB tablet creation errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Tablet server not available
- Tablet creation timeout
- Too many tablets per server

## How to Fix

```bash
yb-admin list_tablets mydb mytable 0
```

## Examples

```bash
yb-admin get_tablet_disk_usage
```
