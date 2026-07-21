---
title: "[Solution] Vitess Tablet Type Transition Error"
description: "Fix Vitess tablet type transition errors when changing tablet roles between replica types"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Type Transition Error

Tablet type transition errors occur when changing a tablet from one type to another (e.g., replica to primary) fails.

## Common Causes

- Tablet still serving queries during type change
- Replication not stopped before promoting to primary
- Tablet already transitioning to another type
- Topo server rejecting type change

## How to Fix

Stop replication before promotion:

```bash
vtctlclient ExecuteFetchAsDba cell1-tablet-101 "STOP REPLICA"
```

Change tablet type:

```bash
vtctlclient ChangeTabletType cell1-tablet-101 master
```

Check current type:

```bash
vtctlclient GetTablet cell1-tablet-101
```

## Examples

```bash
vtctlclient ChangeTabletType cell1-tablet-100 replica
```
