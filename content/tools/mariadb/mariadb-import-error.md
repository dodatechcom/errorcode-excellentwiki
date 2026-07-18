---
title: "[Solution] MariaDB Import Error — How to Fix"
description: "Fix MariaDB import errors from LOAD DATA, INSERT failures, character encoding issues, and file permission problems when importing data"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB Import Error

Import errors occur when loading data from CSV files, SQL dumps, or other sources. These range from file access problems to data format mismatches and constraint violations.

## Why It Happens

- The file does not exist at the specified path or the server cannot access it
- CSV format does not match the expected delimiters
- Character encoding of the source file does not match the database charset
- Data violates NOT NULL, UNIQUE, or CHECK constraints
- `max_allowed_packet` is too large for the import
- `local_infile` is disabled on the server

## Common Error Messages

```
ERROR 29 (HY000): File '/data/users.csv' not found (Errcode: 13 "Permission denied")
```

```
ERROR 1366 (HY007): Incorrect string value: '\xC3\xA9' for column 'name' at row 1
```

```
ERROR 1062 (23000): Duplicate entry '123' for key 'PRIMARY'
```

```
ERROR 1148 (42000): The used command is not allowed with this MariaDB version
```

## How to Fix It

### 1. Fix File Access Permissions

```bash
chmod 644 /data/users.csv
sudo chown mysql:mysql /data/users.csv

mysql -u root -e "SET GLOBAL local_infile = 1;"
mysql --local-infile=1 -u root mydb < import.sql
```

### 2. Fix CSV Format Mismatch

```sql
LOAD DATA LOCAL INFILE '/data/users.csv'
INTO TABLE users
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id, name, email, created_at);
```

### 3. Fix Character Encoding Issues

```sql
SET NAMES utf8mb4;
LOAD DATA LOCAL INFILE '/data/users.csv'
INTO TABLE users CHARACTER SET utf8mb4
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES;
```

```bash
iconv -f ISO-8859-1 -t UTF-8 /data/users.csv > /data/users_utf8.csv
```

### 4. Increase max_allowed_packet

```sql
SET GLOBAL max_allowed_packet = 268435456;  -- 256MB
```

## Common Scenarios

- **CSV import fails with encoding errors**: Convert file with `iconv` before importing.
- **LOAD DATA fails with file not found**: Use `LOCAL` keyword for client-side reading.
- **Large SQL dump import is slow**: Wrap in explicit transactions with batched inserts.

## Prevent It

- Test CSV imports on a staging table first
- Validate CSV files before running LOAD DATA
- Use strict SQL mode to catch data issues early

## Related Pages

- [MariaDB Schema Error](/tools/mariadb/mariadb-schema-error)
- [MariaDB Charset Error](/tools/mariadb/mariadb-charset-error)
- [MySQL Import Error](/tools/mysql/mysql-import-error)
