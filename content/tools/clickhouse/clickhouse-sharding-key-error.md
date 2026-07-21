---
title: "[Solution] ClickHouse Sharding Key Error"
description: "How to fix ClickHouse sharding key configuration errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Sharding key not specified for distributed table
- Sharding key produces uneven distribution
- Missing sharding expression

## How to Fix

Create distributed table with sharding key:

```sql
CREATE TABLE my_distributed AS my_local
ENGINE = Distributed(my_cluster, my_database, my_local, xxHash64(id));
```

## Examples

```sql
SELECT * FROM system.clusters;
SELECT shardNum(), hostName() FROM my_distributed;
```
