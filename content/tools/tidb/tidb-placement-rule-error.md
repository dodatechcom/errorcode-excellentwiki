---
title: "[Solution] TiDB Placement Rule Error"
description: "How to fix TiDB PD placement rule errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Placement rule not found in PD
- Rule constraint not met
- Rule priority conflict

## How to Fix

```bash
tiup ctl pd-ctl placement-rules
```

## Examples

```bash
tiup ctl pd-ctl config show-rules
```
