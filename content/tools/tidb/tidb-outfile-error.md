---
title: "[Solution] TiDB Outfile Error — How to Fix"
description: "Fix TiDB SELECT INTO OUTFILE errors by resolving file permission issues, fixing export format problems, and handling large result set exports"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Outfile Error

TiDB outfile errors occur when SELECT INTO OUTFILE fails to write query results to a file on the TiDB server due to permissions, format, or path issues.

## Why It Happens

- TiDB server process does not have write permission to the target directory
- File already exists at the specified path
- OUTFILE format options are invalid
- Query result contains characters incompatible with the file encoding
- Disk space on TiDB server is exhausted
- Secure file path restrictions block the operation

## Common Error Messages

```
ERROR: Can't create/write to file
```

```
ERROR: The MySQL server is running with the --secure-file-priv option
```

```
ERROR: SELECT ... INTO is not allowed in stored function
```

```
ERROR: file already exists
```

## How to Fix It

### 1. Fix File Permissions

```sql
-- Use OUTFILE with correct path
SELECT * FROM orders
INTO OUTFILE '/tmp/orders_export.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

-- Check TiDB secure file path
SHOW VARIABLES LIKE 'secure_file_priv';
```

```bash
# Ensure TiDB process can write to the directory
ls -la /tmp/
chmod 777 /tmp/

# Or create a dedicated export directory
mkdir -p /data/export
chown tidb:tidb /data/export
```

### 2. Fix Format Options

```sql
-- CSV export with proper formatting
SELECT id, name, created_at
FROM users
INTO OUTFILE '/tmp/users.csv'
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

-- Tab-separated export
SELECT * FROM orders
INTO OUTFILE '/tmp/orders.tsv'
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n';
```

### 3. Handle File Already Exists

```sql
-- Use REPLACE or remove the file first
-- TiDB does not support OVERWRITE, so delete first

-- Export with unique filename
SELECT * FROM orders
INTO OUTFILE CONCAT('/tmp/orders_', DATE_FORMAT(NOW(), '%Y%m%d_%H%i%S'), '.csv')
FIELDS TERMINATED BY ',';
```

```bash
# Delete existing file before export
rm -f /tmp/orders_export.csv
```

### 4. Use LOAD DATA for Import

```sql
-- Import data back from outfile
LOAD DATA LOCAL INFILE '/tmp/orders.csv'
INTO TABLE orders
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(id, name, total, created_at);
```

## Common Scenarios

- **Permission denied on /var/lib/tidb**: Use `/tmp` or a directory owned by the TiDB process.
- **Secure file privilege blocks export**: Move the export directory to the allowed path.
- **Export is too slow**: Reduce the result set with WHERE clause or LIMIT.

## Prevent It

- Use dedicated export directories with proper permissions
- Test export with small datasets first
- Automate file cleanup after exports

## Related Pages

- [TiDB DML Error](/tools/tidb/tidb-dml-error)
- [TiDB Import Error](/tools/tidb/tidb-import-error)
- [TiDB Statement Error](/tools/tidb/tidb-statement-error)
