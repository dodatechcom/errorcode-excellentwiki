---
title: "[Solution] Vitess Tablet Admission Control Error"
description: "Fix Vitess tablet admission control errors when query rate limits are exceeded"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Admission Control Error

Admission control errors occur when the tablet rejects queries because the configured rate or concurrency limits have been reached.

## Common Causes

- Query rate exceeding configured QPS limits
- Too many concurrent in-flight transactions
- Tablet in degraded state reducing effective capacity
- Traffic spike overwhelming tablet resources

## How to Fix

Adjust admission control limits:

```bash
vtgate -enable_hot_row_protection -hot_row_protection_max_tables=256
```

Check current load:

```bash
vtctlclient ExecuteFetchAsDba cell1-tablet-100 "SHOW STATUS LIKE 'Queries%'"
```

Scale horizontally by adding replicas:

```bash
vtctlclient InitTablet -init_dbt -sql_port 3306 cell1-tablet-101 replica
```

## Examples

```bash
vtgate -enable_hot_row_protection -hot_row_protection_max_rows=10000
```
