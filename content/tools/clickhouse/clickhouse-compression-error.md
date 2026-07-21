---
title: "[Solution] ClickHouse Compression Error"
description: "Fix ClickHouse compression errors when data encoding fails during storage"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Compression Error

Compression errors occur when ClickHouse cannot compress or decompress data parts correctly.

## Common Causes

- Codec not available in ClickHouse build
- Compression level exceeding data bounds
- Data corruption during compression
- Codec mismatch between replicas

## How to Fix

Check available codecs:

```sql
SELECT name FROM system.codecs;
```

Check compression settings:

```sql
SELECT name, value FROM system.settings WHERE name LIKE '%codec%';
```

Set compression codec:

```sql
ALTER TABLE my_table MODIFY COLUMN data CODEC(ZSTD(3));
```

Verify compression:

```sql
SELECT column, compression_codec FROM system.columns WHERE table = 'my_table';
```

## Examples

```sql
CREATE TABLE t (data String CODEC(LZ4)) ENGINE = MergeTree() ORDER BY tuple();
```
