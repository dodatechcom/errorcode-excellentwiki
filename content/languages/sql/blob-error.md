---
title: "[Solution] BLOB/CLOB Error"
description: "Fix 'BLOB/CLOB error' when operations on large object columns fail."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "data-type, blob, clob"]
severity: "error"
---

# BLOB/CLOB Error

## Error Message

```
ERROR 1153: Packet of data is too large /ORA-01704: string literal too long — Operation on BLOB or CLOB column failed due to size or usage restrictions.
```

## Common Causes

- BLOB or CLOB value exceeds the maximum allowed packet size or storage limit
- Using BLOB/CLOB columns in comparison or DISTINCT operations which databases may not support
- Attempting to use a BLOB/CLOB column as part of an index or primary key
- Inadequate memory allocation for handling large objects during query execution

## Solutions

### Solution 1: Increase max_allowed_packet or equivalent setting

Configure the database to handle larger data transfers and storage.

```sql
-- MySQL: check current max_allowed_packet
SHOW VARIABLES LIKE 'max_allowed_packet';

-- MySQL: increase to 64MB
SET GLOBAL max_allowed_packet = 67108864;

-- PostgreSQL: check large object support
SHOW lo_compat_privileges;

-- SQL Server: check max packet size
EXEC sp_configure 'network packet size';
```

### Solution 2: Store large files on disk and reference by path

Instead of storing the actual data in the database, store a file path or URL.

```sql
-- Instead of BLOB, store file path
CREATE TABLE documents (
    id INT PRIMARY KEY,
    filename VARCHAR(255) NOT NULL,
    file_path VARCHAR(1000) NOT NULL,
    mime_type VARCHAR(100),
    file_size BIGINT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert reference to file
INSERT INTO documents (id, filename, file_path, mime_type, file_size)
VALUES (1, 'report.pdf', '/uploads/2026/report.pdf', 'application/pdf', 2048576);

-- Retrieve file path for application to serve
SELECT file_path FROM documents WHERE id = 1;
```

### Solution 3: Use streaming or chunked reads for BLOB/CLOB data

Read and write large objects in chunks to avoid memory issues.

```sql
-- MySQL: insert BLOB data using LOAD_FILE
INSERT INTO documents (id, name, content)
VALUES (1, 'report', LOAD_FILE('/path/to/report.pdf'));

-- PostgreSQL: use lo_import for large objects
INSERT INTO documents (id, name, content)
VALUES (1, 'report', lo_import('/path/to/report.pdf'));

-- SQL Server: use OPENROWSET for file streaming
INSERT INTO documents (id, name, content)
SELECT 1, 'report', BulkColumn
FROM OPENROWSET(BULK '/path/to/report.pdf', SINGLE_BLOB) AS x;

-- Read BLOB in chunks (MySQL)
SELECT content FROM documents WHERE id = 1;
```

## Prevention Tips

- Consider storing large files on disk or in object storage and referencing them by path in the database
- Use streaming APIs to read and write BLOB data instead of loading it entirely into memory
- Set appropriate max_allowed_packet or large object limits based on your application's needs

## Related Errors

- [Memory Error]({{< relref "/languages/sql/memory-error.md" >}})
- [String Truncation]({{< relref "/languages/sql/string-truncation.md" >}})
- [Data Type Mismatch]({{< relref "/languages/sql/data-type-mismatch.md" >}})
