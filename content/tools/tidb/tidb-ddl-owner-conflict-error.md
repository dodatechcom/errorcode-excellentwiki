---
title: "[Solution] TiDB DDL Owner Conflict Error — How to Fix"
description: "Fix TiDB DDL owner conflicts when multiple TiDB nodes compete for the DDL owner lease"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB DDL Owner Conflict Error

DDL owner conflict errors occur when multiple TiDB nodes attempt to become the DDL owner, or when the DDL owner lease cannot be transferred properly.

## Why It Happens

- PD cannot elect a stable DDL owner
- Network partition prevents leader election
- TiDB node crashes during DDL owner lease renewal
- Too many TiDB nodes competing for owner role
- PD cluster is unhealthy

## Common Error Messages

```
ddl: failed to campaign DDL owner
```

```
error: DDL owner lease is not valid
```

```
DDL: owner conflict detected, unable to proceed
```

## How to Fix It

### 1. Check DDL Owner Status

```sql
SELECT * FROM tidb_ddl_owner;
SHOW DDL JOBS;
```

### 2. Check PD Health

```bash
pd-ctl member list
pd-ctl cluster status
```

### 3. Transfer DDL Owner

```sql
-- Force DDL owner transfer
admin cancel ddl jobs 1,2,3;
```

### 4. Reduce TiDB Nodes

```bash
# Stop extra TiDB nodes temporarily
sudo systemctl stop tidb-server
```

## Examples

```
$ pd-ctl member list
{
  "members": [
    {"name": "pd1", "leader": true, "client_urls": ["http://pd1:2379"]},
    {"name": "pd2", "leader": false},
    {"name": "pd3", "leader": false}
  ]
}
```

## Prevent It

- Maintain a healthy PD cluster (3 or 5 nodes)
- Limit the number of TiDB instances
- Monitor DDL owner status

## Related Pages

- [TiDB DDL Owner Error](/tools/tidb/tidb-ddl-owner-error)
- [TiDB DDL Error](/tools/tidb/tidb-ddl-error)
- [TiDB PD Error](/tools/tidb/tidb-pd-error)
