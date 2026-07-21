---
title: "[Solution] Vitess Tablet Type Error"
description: "How to fix Vitess tablet type mismatch errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Tablet type not set correctly
- Wrong tablet type for role
- Tablet promoted without type change

## How to Fix

```bash
vtctlclient SetTabletType tablet-alias replica
```

## Examples

```bash
vtctlclient ListAllTablets
```
