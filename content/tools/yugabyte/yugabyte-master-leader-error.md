---
title: "[Solution] YugabyteDB Master Leader Error"
description: "How to fix YugabyteDB master leader election errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- No master leader elected
- Split-brain condition
- Master quorum lost

## How to Fix

```bash
yb-admin master_leader_status
```

## Examples

```bash
yb-admin list_masters
```
