---
title: "[Solution] Vitess Tablet Replica Read Error"
description: "Fix Vitess replica read errors when queries routed to replica tablets return stale or missing data"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Replica Read Error

Replica read errors occur when vtgate routes read queries to replica tablets that cannot serve the data due to replication issues.

## Common Causes

- Replica SQL thread stopped due to error
- Replication lag exceeding staleness threshold
- Replica in read-only mode blocking certain operations
- Query requires data not yet replicated

## How to Fix

Check replica health:

```bash
vtctlclient ExecuteFetchAsDba cell1-tablet-101 "SHOW REPLICA STATUS\G"
```

Restart SQL thread:

```bash
vtctlclient ExecuteFetchAsDba cell1-tablet-101 "START REPLICA SQL_THREAD"
```

Route reads to primary temporarily:

```bash
vtgate -allowed_tablet_types=MASTER
```

## Examples

```bash
vtctlclient ExecuteFetchAsDba cell1-tablet-101 "SELECT @@global.gtid_executed"
```
