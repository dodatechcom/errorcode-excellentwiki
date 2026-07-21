---
title: "[Solution] ScyllaDB CDC Stream Error — How to Fix"
description: "Fix ScyllaDB CDC stream errors when Change Data Capture streams fail to deliver change events to consumers"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB CDC Stream Error

CDC stream errors occur when ScyllaDB Change Data Capture fails to generate or deliver change events from the preimage or postimage tables.

## Why It Happens

- CDC log table is not created with the correct options
- Stream consumer is too slow and falls behind the retention window
- CDC log table has too many tombstones from expired data
- EnableCDC is set to false at the cluster level
- CDC query spans beyond the CDC log TTL window

## Common Error Messages

```
CDC: stream error: log table not found
```

```
error: CDC query returned empty stream, data may have expired
```

```
CDC log table has too many deleted entries, performance degraded
```

## How to Fix It

### 1. Verify CDC is Enabled

```cql
DESCRIBE TABLE mykeyspace.users WITH CDC = true;
```

### 2. Create Table with CDC

```cql
CREATE TABLE mykeyspace.users (
    id UUID PRIMARY KEY,
    name TEXT,
    email TEXT
) WITH cdc = {'enabled': 'true', 'preimage': 'true', 'postimage': 'true', 'ttl': '86400'};
```

### 3. Query CDC Log

```cql
SELECT * FROM mykeyspace.users_scylla_cdc_log WHERE system_time >= '2024-01-15 10:00:00' AND system_time < '2024-01-15 11:00:00';
```

### 4. Tune CDC Log TTL

```cql
ALTER TABLE mykeyspace.users WITH cdc = {'enabled': 'true', 'ttl': '604800'};
```

## Examples

```
SELECT system_time, operation, "name" FROM users_scylla_cdc_log;
system_time                      | operation | name
---------------------------------+-----------+------
2024-01-15 10:30:00.000000+0000 |     INSERT | Alice
2024-01-15 10:31:00.000000+0000 |     UPDATE | Alice Smith
```

## Prevent It

- Set CDC TTL based on consumer processing time
- Monitor CDC log table size and growth rate
- Implement consumer offset tracking for reliable delivery

## Related Pages

- [ScyllaDB CDC Error](/tools/scylladb/scylladb-cdc-error)
- [ScyllaDB Query Error](/tools/scylladb/scylladb-query-error)
- [ScyllaDB Schema Error](/tools/scylladb/scylladb-schema-error)
