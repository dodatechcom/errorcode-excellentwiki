---
title: "[Solution] Vitess Tablet Sequence Error"
description: "Fix Vitess auto-increment sequence errors when using vschema sequences"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Sequence Error

Sequence errors occur when the vschema auto-increment sequence table cannot generate new values or is misconfigured.

## Common Causes

- Sequence table does not exist in the keyspace
- Sequence cache exhausted causing gaps
- Sequence allocation size too small for workload
- Two keyspace routing to same sequence table

## How to Fix

Create sequence table:

```bash
vtctlclient ExecuteVtgrpw cell1-tablet-100 "CREATE TABLE IF NOT EXISTS _vt.seq(id INT AUTO_INCREMENT, val INT, PRIMARY KEY(id))"
```

Increase cache size:

```bash
vtctlclient ApplyVSchema -vschema={"tables":{"orders":{"auto_increment":{"column":"id","sequence":"seq_table"}}}}
```

Reset sequence:

```sql
ALTER TABLE _vt.seq AUTO_INCREMENT = 1;
```

## Examples

```bash
vtctlclient GetVSchema keyspace1
```
