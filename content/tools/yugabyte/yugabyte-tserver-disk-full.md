---
title: "[Solution] YugabyteDB TServer Disk Full"
description: "How to fix YugabyteDB TServer disk full errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Write amplification filling disk
- Compaction lag
- Too many tablets

## How to Fix

```bash
yb-admin get_tablet_disk_usage
```

## Examples

```bash
df -h /var/lib/yugabyte/
```
