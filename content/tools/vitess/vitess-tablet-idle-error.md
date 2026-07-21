---
title: "[Solution] Vitess Tablet Idle Error"
description: "How to fix Vitess tablet idle errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Tablet not serving queries
- Tablet marked idle
- Tablet not registered

## How to Fix

```bash
vtctlclient ListTablets
```

## Examples

```bash
curl http://tablet-host:15100/debug/status
```
