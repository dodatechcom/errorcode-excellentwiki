---
title: "[Solution] CockroachDB Concurrent Schema Change - Fix DDL Conflicts"
description: "Fix CockroachDB concurrent schema change not allowed errors by serializing DDL operations, checking SHOW JOBS status, and waiting for each change to complete"
tools: ["cockroachdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A CockroachDB concurrent schema change error occurs when two or more schema change operations (DDL) are executed simultaneously on the same table. CockroachDB serializes schema changes and rejects concurrent modifications with error code `40001`.

## What This Error Means

CockroachDB ensures schema consistency by serializing all DDL operations. When one schema change is in progress, any subsequent DDL on the same table is rejected until the first completes. The error message is `schema change cancelled` or `another schema change is still in progress for table`.

This is not a bug but a design constraint. Schema changes in CockroachDB are online (non-blocking) but must execute sequentially to prevent conflicting metadata states.

## Why It Happens

- Two migrations running simultaneously against the same table
- CI/CD pipeline deploying multiple migrations in parallel
- Application startup that runs DDL concurrently with a migration tool
- Adding a column while an index is being created on the same table
- Rolling deployment that restarts migration scripts before the previous one finished
- Schema change taking longer than expected due to large tables

## How to Fix It

### 1. Serialize Schema Changes

```sql
-- Run DDL statements sequentially, not in parallel
ALTER TABLE my_table ADD COLUMN status STRING;
-- Wait for completion before next change
ALTER TABLE my_table ADD INDEX idx_status (status);
```

### 2. Check Schema Change Status

```sql
-- See if a schema change is in progress
SHOW JOBS;
SELECT * FROM [SHOW JOBS] WHERE job_type = 'SCHEMA CHANGE';
```

### 3. Wait for Schema Change to Complete

```sql
-- Wait for a specific job to finish
SHOW JOB WHEN COMPLETE <job_id>;
```

### 4. Use a Migration Lock

```go
// Use a distributed lock before running migrations
func runMigrations(db *sql.DB) error {
    // Acquire advisory lock
    _, err := db.Exec("SELECT pg_advisory_lock(1)")
    if err != nil {
        return err
    }
    defer db.Exec("SELECT pg_advisory_unlock(1)")

    // Run migrations sequentially
    for _, migration := range migrations {
        _, err := db.Exec(migration)
        if err != nil {
            return err
        }
    }
    return nil
}
```

### 5. Increase Migration Timeout

```sql
-- Default timeout for schema changes
SET CLUSTER SETTING sql.defaults.schema_change_coalesce_wait_time = '5s';
```

### 6. Use Online Schema Changes for Large Tables

```sql
-- CockroachDB performs online schema changes by default
-- For large tables, ensure the node has enough resources
ALTER TABLE large_table ADD COLUMN new_col STRING DEFAULT 'default';
-- Monitor progress
SHOW JOBS;
```

## Common Mistakes

- Running multiple migration tools (e.g., Flyway and golang-migrate) against the same database
- Not checking `SHOW JOBS` before starting a new schema change
- Assuming schema changes are instant on large tables
- Not retrying schema change failures (they may succeed on retry if the previous change completed)

## Related Pages

- [CockroachDB Schema Error](/tools/cockroachdb/cockroach-schema-error)
- [CockroachDB Deadlock](/tools/cockroachdb/cockroach-deadlock)
- [CockroachDB Serializable Error](/tools/cockroachdb/cockroach-serializable-error)
