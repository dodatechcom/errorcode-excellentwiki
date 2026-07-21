---
title: "[Solution] Vitess Tablet Spare Pool Error"
description: "Fix Vitess tablet spare pool errors when spare tablets cannot serve traffic"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Spare Pool Error

Spare pool errors occur when vtgate tries to use spare tablets but they are unavailable or in a bad state.

## Common Causes

- Spare tablet failed health check
- Tablet in Spare type but still initializing
- Too few spare tablets for failover needs
- Spare tablet MySQL not ready

## How to Fix

Check spare tablet health:

```bash
vtctlclient ListAllTablets cell1 | grep spare
```

Initialize spare tablet properly:

```bash
vttablet -init_keyspace keyspace1 -init_shard 0 -tablet_type spare -init_dbt
```

Change tablet to spare:

```bash
vtctlclient ChangeTabletType cell1-tablet-101 spare
```

## Examples

```bash
vtctlclient GetTablet cell1-tablet-101
```
