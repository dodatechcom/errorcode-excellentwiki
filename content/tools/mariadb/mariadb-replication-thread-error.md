---
title: "[Solution] MariaDB Replication Error"
description: "Fix MariaDB replication errors when slave SQL or IO thread stops"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB Replication Error

Replication errors occur when the replica SQL or IO thread encounters issues applying relay logs.

## Common Causes

- Duplicate key error on replica
- Table does not exist on replica
- Relay log corruption
- GTID gap in replication stream

## Common Error Messages

```
ERROR 1062 (23000): Duplicate entry for key 'PRIMARY'
```

## How to Fix It

### 1. Check Replication Status

```sql
SHOW REPLICA STATUS\G
```

### 2. Skip Duplicate Key Error

```sql
STOP REPLICA;
SET GLOBAL sql_replica_skip_counter = 1;
START REPLICA;
```

### 3. Reset Replication

```sql
STOP REPLICA;
RESET REPLICA;
CHANGE REPLICATION SOURCE TO SOURCE_AUTO_POSITION=1;
START REPLICA;
```

## Examples

```sql
SHOW REPLICA STATUS\G | grep -E "Running|Error|Behind"
```
