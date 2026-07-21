---
title: "[Solution] YugabyteDB Tablet Snapshot Error"
description: "How to fix YugabyteDB tablet snapshot errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Snapshot creation failing
- Snapshot storage not accessible
- Snapshot cleanup failing

## How to Fix

```bash
yb-admin list_snapshots
```

## Examples

```bash
yb-admin backup_snapshots start my_backup
```
