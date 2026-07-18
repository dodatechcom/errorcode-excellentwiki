---
title: "[Solution] MySQL Packet Bigger Than max_allowed_packet - Fix Large Query Errors"
description: "Fix MySQL packet bigger than max_allowed_packet errors by increasing the limit, compressing data, and splitting large INSERT statements"
tools: ["mysql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# MySQL Packet Bigger Than max_allowed_packet

This error occurs when a client sends a SQL packet (statement or data) that exceeds the `max_allowed_packet` size configured on the server. The server rejects the packet and closes the connection.

## What This Error Means

MySQL returns this error when the packet size limit is exceeded:

```
ERROR 1153 (08S01): Packet bigger than 'max_allowed_packet' bytes
```

The `max_allowed_packet` setting controls the maximum size of a single MySQL packet, which includes any single SQL statement, row data in an `INSERT`, or result set row. The default in MySQL 5.7 is 4MB and in MySQL 8.0 is 64MB.

When the limit is exceeded, the server aborts the connection because it cannot safely read the rest of the packet.

## Why It Happens

- A single `INSERT` statement includes thousands of rows or very large `BLOB`/`TEXT` data
- A `SELECT` returns rows with large `TEXT` or `BLOB` columns
- Binary data (images, files) is being stored directly in the database
- The application accumulates too much data in a single prepared statement
- Replication events exceed the configured limit
- A stored procedure generates a result set larger than the limit

## How to Fix It

### 1. Check the Current Limit

```sql
SHOW VARIABLES LIKE 'max_allowed_packet';
```

### 2. Increase max_allowed_packet

```sql
-- Runtime change (does not persist across restarts)
SET GLOBAL max_allowed_packet = 67108864;  -- 64MB

-- For persistence, edit my.cnf
[mysqld]
max_allowed_packet = 64M
```

### 3. Split Large INSERT Statements

```sql
-- WRONG: one massive INSERT
INSERT INTO logs (data) VALUES ('...very long string...'), ('...next...'), ...;

-- BETTER: batch into smaller chunks
INSERT INTO logs (data) VALUES
    ('row1'), ('row2'), ('row3'), ...;  -- up to 1000 rows per batch
```

### 4. Use LOAD DATA INFILE for Bulk Imports

```sql
-- More efficient and avoids packet size issues
LOAD DATA INFILE '/path/to/data.csv'
INTO TABLE mytable
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
```

### 5. Compress Data Before Storing

```sql
-- Use COMPRESS() for large text
INSERT INTO logs (data) VALUES (COMPRESS('...long string...'));

-- Retrieve with UNCOMPRESS()
SELECT UNCOMPRESS(data) FROM logs WHERE id = 1;
```

### 6. Set max_allowed_packet on the Client Too

```bash
# When connecting from command line
mysql --max_allowed_packet=64M -u root -p

# Or in my.cnf on the client side
[client]
max_allowed_packet = 64M
```

## Common Mistakes

- Only increasing `max_allowed_packet` on the server without also setting it on the client
- Using the default 4MB limit for applications that handle large text or binary data
- Not considering that prepared statements also count toward the packet limit
- Storing files directly in the database instead of using a file system or object storage
- Forgetting that `max_allowed_packet` must be set on both the server and any replica servers in replication setups

## Related Pages

- [MySQL InnoDB Error](/tools/mysql/mysql-innodb-error)
- [MySQL Data Too Long](/tools/mysql/mysql-data-too-long)
- [MySQL Crash Recovery](/tools/mysql/mysql-crash-recovery)
- [PostgreSQL Disk Full](/tools/postgresql/pg-disk-full)
