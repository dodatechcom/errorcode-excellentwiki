---
title: "[Solution] Vitess Tablet Auto-Increment Error"
description: "Fix Vitess auto-increment errors when generating IDs across multiple shards"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Auto-Increment Error

Auto-increment errors occur when vtgate cannot properly generate unique IDs across sharded tables.

## Common Causes

- Auto-increment column not configured in VSchema
- Two shards generating same ID range
- Sequence table not initialized
- Hash vindex producing non-sequential values

## How to Fix

Configure vschema auto-increment:

```bash
vtctlclient ApplyVSchema -vschema={"sharded":true,"vindexes":{"hash":{"type":"hash"}},"tables":{"users":{"column_vindexes":[{"column":"id","name":"hash"}],"auto_increment":{"column":"id","sequence":"user_seq"}}}}
```

Initialize sequence table:

```bash
vtctlclient ExecuteVtgrpw cell1-tablet-100 "INSERT INTO user_seq (val) VALUES (0)"
```

Check sequence allocation:

```sql
SELECT * FROM user_seq;
```

## Examples

```bash
vtctlclient GetVSchema keyspace1
```
