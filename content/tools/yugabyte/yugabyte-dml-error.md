---
title: "[Solution] YugabyteDB DML Error — How to Fix"
description: "Fix YugabyteDB DML errors by resolving INSERT/UPDATE/DELETE failures, fixing batch operation issues, and handling write conflicts"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB DML Error

YugabyteDB DML errors occur when Data Manipulation Language operations like INSERT, UPDATE, or DELETE fail due to distributed execution issues.

## Why It Happens

- Write operation targets a tablet without a leader
- Insert violates unique constraint
- Update/Delete exceeds timeout limits
- Batch operations are too large
- Write conflicts with concurrent transactions
- TServer cannot accept writes (disk full)

## Common Error Messages

```
ERROR: tablet leader not found for write
```

```
ERROR: duplicate key value violates unique constraint
```

```
ERROR: write operation timed out
```

```
ERROR: disk full cannot accept writes
```

## How to Fix It

### 1. Fix INSERT Errors

```sql
-- Insert with proper primary key
INSERT INTO users (user_id, name, email)
VALUES (gen_random_uuid(), 'Alice', 'alice@example.com');

-- Handle duplicate key errors
INSERT INTO users (user_id, name, email)
VALUES (gen_random_uuid(), 'Alice', 'alice@example.com')
ON CONFLICT (email) DO UPDATE SET name = EXCLUDED.name;

-- Bulk insert
INSERT INTO sensor_data SELECT * FROM staging_data;
```

### 2. Fix UPDATE/DELETE Errors

```sql
-- Update with WHERE clause
UPDATE users SET name = 'Bob' WHERE user_id = 'uuid-here';

-- Delete with conditions
DELETE FROM sensor_data WHERE event_time < NOW() - INTERVAL '1 year';

-- Batch delete
DELETE FROM sensor_data
WHERE sensor_id = 'sensor1'
AND event_time < '2024-01-01'
RETURNING *;
```

### 3. Handle Write Conflicts

```sql
-- Use explicit locking
BEGIN;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;

-- Use advisory locks
SELECT pg_advisory_lock(12345);
-- ... perform operations ...
SELECT pg_advisory_unlock(12345);
```

### 4. Optimize Write Performance

```sql
-- Use UPSERT for idempotent writes
INSERT INTO sensor_data (sensor_id, event_time, temperature)
VALUES ('sensor1', NOW(), 22.5)
ON CONFLICT (sensor_id, event_time) DO UPDATE
SET temperature = EXCLUDED.temperature;

-- Batch writes in single transaction
BEGIN;
INSERT INTO sensor_data VALUES ('s1', NOW(), 22.0);
INSERT INTO sensor_data VALUES ('s2', NOW(), 23.0);
COMMIT;
```

## Common Scenarios

- **Write fails with no leader**: Check TServer health and tablet leader status.
- **Duplicate key error**: Use ON CONFLICT clause for upsert behavior.
- **Write timeout**: Increase timeout or reduce batch size.

## Prevent It

- Use connection pooling for write operations
- Handle duplicate key errors with ON CONFLICT
- Monitor write latency and throughput

## Related Pages

- [YugabyteDB Query Error](/tools/yugabyte/yugabyte-query-error)
- [YugabyteDB Transaction Error](/tools/yugabyte/yugabyte-transaction-error)
- [YugabyteDB TServer Error](/tools/yugabyte/yugabyte-tserver-error)
