---
title: "[Solution] YugabyteDB Tablet CPU Error"
description: "How to fix YugabyteDB tablet CPU errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- CPU usage too high
- CPU throttling
- CPU starvation

## How to Fix

```bash
top -p $(pgrep -d',' yb-tserver)
```

## Examples

```bash
mpstat -P ALL 1
```
