---
title: "[Solution] Vitess Tablet Serving Error"
description: "How to fix Vitess tablet serving errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Tablet not in serving state
- Tablet under maintenance
- Tablet query service disabled

## How to Fix

```bash
vtctlclient ListTablets | grep serving
```

## Examples

```bash
curl http://tablet-host:15100/debug/status | grep serving
```
