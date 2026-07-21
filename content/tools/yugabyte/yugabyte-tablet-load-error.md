---
title: "[Solution] YugabyteDB Tablet Load Error"
description: "How to fix YugabyteDB tablet load errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Tablet load failed
- Tablet server overloaded
- Tablet data corrupted

## How to Fix

```bash
yb-admin list_tablet_servers
```

## Examples

```bash
yb-admin get_tablet_disk_usage
```
