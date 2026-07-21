---
title: "[Solution] TiDB Sequence Function Error — How to Fix"
description: "Fix TiDB sequence function errors when AUTO_INCREMENT sequences fail or produce unexpected values"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Sequence Function Error

Sequence function errors occur when TiDB's sequence generator produces unexpected values or fails to allocate new sequence numbers.

## Why It Happens

- Sequence cache is exhausted
- Sequence increment is set to zero
- Sequence has reached its maximum value
- Sequence is shared by too many concurrent sessions
- Sequence type does not match the use case

## Common Error Messages

```
ERROR 3878: Sequence 'my_seq' has run out
```

```
ERROR 1365: Division by 0 in sequence increment
```

```
ERROR: sequence value out of range
```

## How to Fix It

### 1. Check Sequence Status

```sql
SHOW CREATE SEQUENCE my_seq;
SELECT * FROM information_schema.sequences WHERE sequence_name = 'my_seq';
```

### 2. Increase Sequence Cache

```sql
CREATE SEQUENCE IF NOT EXISTS my_seq CACHE 1000 MAXVALUE 999999999 INCREMENT BY 1;
```

### 3. Reset Sequence

```sql
ALTER SEQUENCE my_seq RESTART WITH 1;
```

### 4. Use Sequence Properly

```sql
-- Use NEXT VALUE FOR to get next value
SELECT NEXT VALUE FOR my_seq;

-- Use in INSERT
INSERT INTO mytable VALUES (NEXT VALUE FOR my_seq, 'data');
```

## Examples

```
mysql> CREATE SEQUENCE my_seq CACHE 100 MAXVALUE 1000;
Query OK, 0 rows affected

mysql> SELECT NEXT VALUE FOR my_seq;
+------------------+
| NEXTVAL(my_seq)  |
+------------------+
|                1 |
+------------------+
```

## Prevent It

- Set MAXVALUE high enough for expected usage
- Use CACHE for high-throughput sequences
- Monitor sequence utilization

## Related Pages

- [TiDB Sequence Error](/tools/tidb/tidb-sequence-error)
- [TiDB Auto Increment Error](/tools/tidb/tidb-auto-increment-error)
- [TiDB Statement Error](/tools/tidb/tidb-statement-error)
