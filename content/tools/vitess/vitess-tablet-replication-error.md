---
title: "[Solution] Vitess Tablet Replication Lag Error"
description: "How to fix Vitess tablet replication lag errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Replica falling behind master
- Network latency between master and replica
- Replica overloaded

## How to Fix

```bash
vtctlclient ListTablets
```

## Examples

```bash
vtctlclient GetTablet tablet-alias | grep -i lag
```
