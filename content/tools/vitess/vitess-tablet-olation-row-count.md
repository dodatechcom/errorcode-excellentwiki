---
title: "[Solution] Vitess Tablet Row Count Mismatch Error"
description: "Fix Vitess row count mismatch errors when shard data diverges after resharding"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Row Count Mismatch Error

Row count mismatch errors indicate that the number of rows in a table differs between source and target shards after a resharding operation.

## Common Causes

- Resharding filter excluded some rows
- Duplicate rows caused by overlapping key ranges
- Rows inserted during resharding not captured
- Vreplication stream missed events

## How to Fix

Compare row counts:

```bash
vtctlclient ExecuteFetchAsDba cell1-tablet-100 "SELECT COUNT(*) FROM orders"
vtctlclient ExecuteFetchAsDba cell1-tablet-200 "SELECT COUNT(*) FROM orders"
```

Verify filter coverage:

```bash
vtctlclient ExecuteFetchAsDba cell1-tablet-100 "SELECT COUNT(*) FROM orders WHERE customer_id BETWEEN 1 AND 1000"
```

Complete resharding:

```bash
vtctlclient MoveTables Complete keyspace1 keyspace2
```

## Examples

```bash
vtctlclient CompareSchema keyspace1 keyspace2
```
