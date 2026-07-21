---
title: "[Solution] YugabyteDB Tablet IO Error"
description: "How to fix YugabyteDB tablet IO errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Disk I/O saturated
- IO latency too high
- IO scheduler misconfigured

## How to Fix

```bash
iostat -x 1
```

## Examples

```bash
iotop -o
```
