---
title: "[Solution] YugabyteDB TServer Not Found"
description: "How to fix YugabyteDB TServer not found errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- TServer not registered with master
- TServer crashed and restarted
- Network partition

## How to Fix

```bash
yb-admin list_tablet_servers
```

## Examples

```bash
yb-admin master_leader_status
```
