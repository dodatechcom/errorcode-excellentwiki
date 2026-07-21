---
title: "[Solution] Vitess Tablet XA Block Error"
description: "Fix Vitess XA transaction blocking errors during two-phase commit across shards"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet XA Block Error

XA block errors occur when two-phase commit transactions hang in the prepared state and cannot complete or roll back.

## Common Causes

- Coordinator vtgate crashed after XA PREPARE
- Tablet restarted during XA transaction
- Network partition preventing XA COMMIT broadcast
- Stale XA transactions consuming resources

## How to Fix

List active XA transactions:

```bash
vtctlclient ExecuteFetchAsDba cell1-tablet-100 "SHOW ENGINE INNODB STATUS"
```

Recover prepared XA transactions:

```bash
vtctlclient ExecuteFetchAsDba cell1-tablet-100 "XA RECOVER"
```

Force rollback stale XA:

```bash
vtctlclient ExecuteFetchAsDba cell1-tablet-100 "XA ROLLBACK xid"
```

## Examples

```bash
vtctlclient ExecuteFetchAsDba cell1-tablet-100 "XA RECOVER"
```
