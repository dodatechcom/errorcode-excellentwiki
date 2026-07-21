---
title: "[Solution] YugabyteDB Tablet Status Error"
description: "How to fix YugabyteDB tablet status errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Tablet status not available
- Tablet status stale
- Tablet status query failing

## How to Fix

```bash
yb-admin list_tablets mydb mytable 0
```

## Examples

```bash
yb-admin get_tablet_disk_usage
```
