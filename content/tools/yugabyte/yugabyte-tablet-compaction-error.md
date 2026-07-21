---
title: "[Solution] YugabyteDB Tablet Compaction Error"
description: "How to fix YugabyteDB tablet compaction errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Compaction lag
- Compaction failing
- Too many SST files

## How to Fix

```bash
yb-admin list_tablets mydb mytable 0
```

## Examples

```bash
yb-admin get_tablet_disk_usage
```
