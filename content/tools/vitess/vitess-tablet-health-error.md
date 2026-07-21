---
title: "[Solution] Vitess Tablet Health Error"
description: "How to fix Vitess tablet health check errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Tablet not responding to health checks
- MySQL process down behind tablet
- Replication lag too high

## How to Fix

```bash
vtctlclient ListAllTablets
```

## Examples

```bash
vtctlclient GetTablet tablet-alias
```
