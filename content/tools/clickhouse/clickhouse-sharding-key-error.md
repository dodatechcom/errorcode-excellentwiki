---
title: "[Solution] ClickHouse Sharding Key Error"
description: "Fix ClickHouse sharding key errors when distributed table routing fails"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Sharding Key Error

Sharding key errors occur when ClickHouse cannot determine the correct shard for data distribution.

## Common Causes

- Sharding key expression references non-existent column
- Modulo operation causing uneven distribution
- Sharding key type incompatible with hash function
- Missing sharding key in distributed table definition

## How to Fix

Check distributed table config:

```sql
SELECT name, engine, sharding_key FROM system.tables WHERE engine = 'Distributed';
```

Test shard routing:

```sql
SELECT shardNum(), hostName() FROM system.clusters;
```

Fix sharding key:

```sql
CREATE TABLE dist_table AS local_table
ENGINE = Distributed(my_cluster, default, local_table, xxHash64(user_id));
```

## Examples

```sql
SELECT toInt64(xxHash64(user_id)) % 4 AS shard FROM users;
```
