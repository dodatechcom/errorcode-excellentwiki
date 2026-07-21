---
title: "[Solution] Vitess Tablet DDL Error"
description: "Fix Vitess tablet DDL errors when online schema changes fail during execution"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet DDL Error

DDL errors occur when schema change operations fail on tablets due to conflicts or resource issues.

## Common Causes

- DDL conflicts with ongoing transactions
- Schema change exceeding online DDL timeout
- Foreign key constraint preventing ALTER
- Disk space insufficient for temporary table creation

## How to Fix

Check online DDL status:

```bash
vtctlclient ExecuteFetchAsDba cell1-tablet-100 "SELECT * FROM _vt.schema_migration WHERE status != 'complete'"
```

Cancel stuck DDL:

```bash
vtctlclient OnlineDDL Complete keyspace1 uuid-string
```

Retry DDL on specific tablet:

```bash
vtctlclient ExecuteFetchAsDba cell1-tablet-100 "ALTER TABLE users ADD INDEX idx_email (email)"
```

## Examples

```bash
vtctlclient OnlineDDL Query keyspace1 "ALTER TABLE users ADD COLUMN status VARCHAR(20) DEFAULT 'active'"
```
