---
title: "[Solution] YugabyteDB Tablet Heap Error"
description: "How to fix YugabyteDB tablet heap errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Heap size too small
- Heap allocation failure
- Heap fragmentation

## How to Fix

```bash
yb-tserver --memory_limit_hard_bytes=10737418240
```

## Examples

```bash
free -h
```
