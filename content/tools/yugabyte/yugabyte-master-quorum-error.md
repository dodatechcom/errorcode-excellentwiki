---
title: "[Solution] YugabyteDB Master Quorum Error"
description: "How to fix YugabyteDB master quorum errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Not enough masters for quorum
- Master node down
- Network partition

## How to Fix

```bash
yb-admin list_masters
```

## Examples

```bash
yb-admin master_leader_status
```
