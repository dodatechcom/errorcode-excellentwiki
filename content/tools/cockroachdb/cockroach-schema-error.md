---
title: "[Solution] CockroachDB Schema Error — How to Fix"
description: "Fix CockroachDB schema change failures by resolving DDL conflicts, tuning schema change settings, handling retries, and coordinating multi-region migrations."
tools: ["cockroachdb"]
error-types: ["schema-error"]
severities: ["error"]
weight: 5
comments: true
---

A CockroachDB schema change error occurs when a DDL operation (CREATE TABLE, ALTER TABLE, CREATE INDEX) fails or is rolled back. CockroachDB uses an asynchronous schema change mechanism that can fail silently or retry automatically.

## Why It Happens

CockroachDB schema changes are online and asynchronous. They execute in multiple phases and can fail at any point due to resource constraints, conflicts, or node failures.

- Another schema change is in progress on the same table and conflicts
- The schema change requires rewriting the table and runs out of disk space
- A node failure during schema change causes the operation to abort
- The schema change references a table or column that does not exist
- An index creation fails because the table is too large to process within the timeout
- The schema change uses unsupported syntax or data types
- Concurrent DDL and DML create write-too-old errors that force rollback
- Multi-region schema changes require extra coordination and can timeout

## Common Error Messages

```text
ERROR: relation "users" already exists
```

The table already exists. Use `CREATE TABLE IF NOT EXISTS` or drop the existing table first.

```text
ERROR: current schema change still running; please retry later
```

A previous schema change on the same table has not completed. Wait for it to finish or cancel it.

```text
ERROR: unimplemented: this syntax
```

CockroachDB does not support the specific SQL syntax used. Check the CockroachDB documentation for supported DDL.

```text
ERROR: write-too-old: failed to write with timestamp ...
```

Concurrent DML is conflicting with the schema change. The schema change may need to be retried.

## How to Fix It

### 1. Wait for or Cancel In-Progress Schema Changes

```sql
-- Check for in-progress schema changes
SHOW JOBS;

-- Cancel a stuck schema change
CANCEL JOB <job_id>;

-- Retry the schema change
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name STRING NOT NULL,
    email STRING UNIQUE,
    created_at TIMESTAMP DEFAULT now()
);
```

### 2. Use IF NOT EXISTS and IF EXISTS

```sql
-- Safe creation that won't fail if table exists
CREATE TABLE IF NOT EXISTS orders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id),
    total DECIMAL(10, 2),
    status STRING DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT now()
);

-- Safe drop that won't fail if table doesn't exist
DROP TABLE IF EXISTS old_table;

-- Safe column addition
ALTER TABLE users ADD COLUMN IF NOT EXISTS phone STRING;
```

### 3. Handle Large Table Schema Changes

```sql
-- For large tables, schema changes can take a long time
-- Increase the schema change timeout
SET CLUSTER SETTING sql.schema.default_timeout = '30m';

-- Check progress of the schema change
SHOW JOBS WHEN COMPLETE;
-- Or monitor asynchronously:
SELECT job_id, status, fraction_completed
FROM [SHOW JOBS]
WHERE job_type = 'SCHEMA CHANGE'
ORDER BY created DESC LIMIT 5;
```

### 4. Fix Multi-Region Schema Changes

```sql
-- When adding a column to a multi-region table, the change
-- must propagate across all regions
ALTER TABLE users ADD COLUMN region STRING DEFAULT 'us-east1';

-- For region-specific tables, use locality-optimized tables
ALTER TABLE users ADD REGION us-east1;
ALTER TABLE users ADD REGION eu-west1;

-- Verify regions are configured correctly
SHOW REGIONS FROM DATABASE mydb;
```

### 5. Retry Schema Changes Programmatically

```go
// Go: Retry schema changes with exponential backoff
func executeSchemaChange(db *sql.DB, ddl string) error {
    maxRetries := 5
    for i := 0; i < maxRetries; i++ {
        _, err := db.Exec(ddl)
        if err == nil {
            return nil
        }
        if strings.Contains(err.Error(), "still running") ||
           strings.Contains(err.Error(), "write-too-old") {
            time.Sleep(time.Duration(math.Pow(2, float64(i))) * time.Second)
            continue
        }
        return err
    }
    return fmt.Errorf("schema change failed after %d retries", maxRetries)
}
```

```python
# Python: Retry with tenacity
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, max=30))
def execute_schema_change(conn, ddl):
    with conn.cursor() as cur:
        cur.execute(ddl)
        conn.commit()
```

## Common Scenarios

**Schema change stuck in pending state.** A node failure during schema change can leave it stuck. Check `SHOW JOBS` for the status. If it is `pending` for more than 10 minutes, cancel it and retry.

**Index creation fails on a large table.** Creating an index on a multi-GB table can timeout. Increase `sql.schema.default_timeout` and ensure sufficient disk space for the temporary index data.

**Concurrent DDL and DML cause write-too-old errors.** CockroachDB serializes schema changes with DML. During a schema change, writes may retry automatically. If retries are excessive, schedule schema changes during low-traffic periods.

## Prevent It

- Always use `IF NOT EXISTS` and `IF EXISTS` in DDL statements to make them idempotent
- Test schema changes on a staging cluster with production-sized data before deploying
- Schedule large schema changes (index creation, column additions) during maintenance windows
