---
title: "[Solution] Vitess Tablet Replication User Error"
description: "Fix Vitess replication user errors when replica cannot authenticate to primary"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Replication User Error

Replication user errors occur when the replica tablet cannot authenticate to the primary for replication.

## Common Causes

- Replication password changed on primary
- Replication user dropped or locked
- Authentication plugin mismatch
- Password expired for replication user

## How to Fix

Check replication user:

```sql
SELECT user, host, plugin FROM mysql.user WHERE user = 'repl_user';
```

Reset replication password:

```sql
ALTER USER 'repl_user'@'%' IDENTIFIED BY 'new_password';
FLUSH PRIVILEGES;
```

Update replication credentials:

```sql
STOP REPLICA;
CHANGE REPLICATION SOURCE TO SOURCE_PASSWORD='new_password';
START REPLICA;
```

## Examples

```bash
vtctlclient ExecuteFetchAsDba cell1-tablet-101 "SHOW REPLICA STATUS\G" | grep -i error
```
