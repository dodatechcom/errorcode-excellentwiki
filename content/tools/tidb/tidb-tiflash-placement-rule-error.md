---
title: "[Solution] TiDB TiFlash Placement Rule Error"
description: "How to fix TiDB TiFlash placement rule errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Placement rule not configured
- TiFlash not in placement rule
- Label not matching

## How to Fix

```bash
tiup ctl pd-ctl config placement-rules
```

## Examples

```bash
tiup ctl pd-ctl config show-rules
```
