---
title: "[Solution] InfluxDB Flux Import Error"
description: "How to fix InfluxDB Flux import errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Import path wrong
- Package not available
- Circular import

## How to Fix

```flux
import "math"
import "date"
```

## Examples

```flux
import "strings"
from(bucket: "mybucket") |> filter(fn: (r) => strings.hasPrefix(v: r._field, prefix: "cpu"))
```
