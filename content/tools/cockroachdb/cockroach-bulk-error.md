---
title: "[Solution] CockroachDB Bulk Error — How to Fix"
description: "Fix CockroachDB bulk import and export errors by tuning CSV configuration, resolving encoding issues, handling foreign key constraints, and optimizing batch sizes."
tools: ["cockroachdb"]
error-types: ["bulk-error"]
severities: ["error"]
weight: 5
comments: true
---

A CockroachDB bulk error occurs when importing or exporting large datasets using `IMPORT`, `EXPORT`, `COPY`, or `SELECT INTO` statements. Bulk operations are resource-intensive and have strict requirements around file format, encoding, and schema compatibility.

## Why It Happens

Bulk operations in CockroachDB must parse data files, validate them against the table schema, and insert rows while maintaining indexes and constraints. Failures at any stage produce bulk errors.

- The CSV file has incorrect delimiters, quoting, or encoding
- Data values do not match the target column types (e.g., string in an integer column)
- Foreign key constraints are violated by the imported data
- The data file contains duplicate primary keys
- The import job runs out of memory or disk space
- The CSV file has inconsistent column counts across rows
- The `NULL` representation in the file does not match the `AS` clause
- The import job exceeds the configured timeout
- Network issues interrupt the data transfer from external storage

## Common Error Messages

```text
ERROR: csv row has 4 columns, but expected 5
```

The CSV row has fewer columns than the target table. Check for missing delimiters or escaped characters.

```text
ERROR: row 1: column 3: parsing argument "abc" as type INT: parse error
```

A string value was found in an integer column. The data type mismatch prevents the import.

```text
ERROR: duplicate key value violates unique constraint "primary"
```

The imported data contains duplicate primary key values. Remove duplicates before importing.

```text
ERROR: foreign key violation: value(s) in columns (user_id) references table "users" (id) not found
```

The imported data references rows that do not exist in the referenced table.

## How to Fix It

### 1. Fix CSV Format Issues

```sql
-- Import with explicit CSV options
IMPORT TABLE users (
    id INT PRIMARY KEY,
    name STRING,
    email STRING,
    created_at TIMESTAMP
)
CSV DATA ('gs://bucket/users.csv')
WITH
    delimiter = ',',
    quote = '"',
    escape = '\\',
    nullif = '',
    skip = '1';  -- Skip header row;
```

```sql
-- Fix common CSV issues
-- Tab-separated values
IMPORT TABLE events (
    id INT PRIMARY KEY,
    data STRING
)
CSV DATA ('s3://bucket/events.tsv')
WITH delimiter = E'\t';

-- Pipe-delimited
IMPORT TABLE logs (
    id INT PRIMARY KEY,
    message STRING
)
CSV DATA ('gs://bucket/logs.csv')
WITH delimiter = '|';
```

### 2. Handle Data Type Mismatches

```sql
-- Import with type casting using a staging table
CREATE TABLE users_staging (
    id STRING,
    name STRING,
    email STRING,
    created_at STRING
);

IMPORT INTO users_staging CSV DATA ('gs://bucket/users.csv');

-- Cast and insert into the final table
INSERT INTO users (id, name, email, created_at)
SELECT 
    id::INT,
    name,
    email,
    created_at::TIMESTAMP
FROM users_staging;

-- Clean up
DROP TABLE users_staging;
```

### 3. Handle Foreign Key Constraints

```sql
-- Option 1: Disable foreign key checks during import
SET CLUSTER SETTING sql.defaults.foreign_key_checks.enabled = false;

-- Import the data
IMPORT TABLE orders CSV DATA ('gs://bucket/orders.csv');

-- Re-enable foreign key checks
SET CLUSTER SETTING sql.defaults.foreign_key_checks.enabled = true;

-- Option 2: Import in the correct order
-- 1. Import parent tables first (users)
-- 2. Then import child tables (orders)
IMPORT TABLE users CSV DATA ('gs://bucket/users.csv');
IMPORT TABLE orders CSV DATA ('gs://bucket/orders.csv');
```

### 4. Use COPY for Smaller Datasets

```sql
-- COPY is better for datasets under 1GB
COPY users (id, name, email, created_at)
FROM STDIN
WITH CSV HEADER;

-- From the command line:
-- cat users.csv | cockroach sql --insecure -d mydb -e "COPY users FROM STDIN WITH CSV HEADER"
```

### 5. Export Data Correctly

```sql
-- Export to CSV
EXPORT INTO CSV 'gs://bucket/export/users'
WITH delimiter = ','
AS SELECT * FROM users WHERE created_at > '2024-01-01';

-- Export to JSON
EXPORT INTO JSON 'gs://bucket/export/events'
AS SELECT * FROM events;

-- Export with specific formatting
EXPORT INTO CSV 'gs://bucket/export/orders'
WITH
    delimiter = '|',
    nullif = 'NULL',
    escape = '"'
AS SELECT id, name, status FROM orders;
```

### 6. Fix Encoding Issues

```sql
-- Import with explicit encoding
IMPORT TABLE users CSV DATA ('gs://bucket/users.csv')
WITH
    encoding = 'UTF-8',
    nullif = '';

-- For non-UTF-8 files, convert first
-- iconv -f ISO-8859-1 -t UTF-8 input.csv > output.csv
```

### 7. Manage Import Job Failures

```sql
-- Check import job status
SHOW JOBS;

-- Resume a failed import
RESUME JOB <job_id>;

-- Cancel a stuck import
CANCEL JOB <job_id>;

-- Check for import errors in the job details
SELECT job_id, status, error, fraction_completed
FROM [SHOW JOBS]
WHERE job_type = 'IMPORT'
ORDER BY created DESC;
```

## Common Scenarios

**Import fails with OOM on large files.** Split the CSV into smaller files (under 500MB each) and import them in parallel. Use `IMPORT INTO` with individual files rather than one large file.

**Import succeeds but data is wrong.** The CSV parser silently handles malformed rows differently than expected. Check `NULL` handling with the `nullif` option and verify data types with `SHOW TABLE`.

**Export creates files that are too large.** Use `WHERE` clauses to split exports into manageable chunks. Export by date range or partition key to create smaller files.

## Prevent It

- Always test bulk imports on a staging cluster with a sample of production data before running on production
- Use the `--dry-run` option where available to validate data before committing the import
- Monitor import job progress with `SHOW JOBS` and set alerts for jobs that have been running longer than expected
