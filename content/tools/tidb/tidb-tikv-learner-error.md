---
title: "[Solution] TiDB TiKV Learner Error"
description: "How to fix TiDB TiKV learner errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Learner not catching up
- Learner node down
- Learner lag too high

## How to Fix

```bash
tiup ctl pd-ctl region peer
```

## Examples

```bash
tiup ctl pd-ctl stores
```
