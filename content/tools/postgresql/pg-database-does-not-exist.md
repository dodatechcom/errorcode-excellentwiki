---
title: "[Solution] PostgreSQL Database Does Not Exist - Fix Missing Database Errors"
description: "Fix PostgreSQL database does not exist errors by creating the database, verifying the name spelling, and checking connection parameters"
tools: ["postgresql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# PostgreSQL Database Does Not Exist

This error means the PostgreSQL server received a connection request or SQL command that references a database name not found in the cluster's system catalog.

## What This Error Means

PostgreSQL returns this error when you attempt to connect to or query a database that does not exist:

```
FATAL: database "mydb" does not exist
```

The error can also appear mid-query when a `dblink` function or foreign data wrapper references a nonexistent database. PostgreSQL databases are defined at the cluster level and stored in the `pg_database` system catalog.

## Why It Happens

- The database was never created or was dropped without the application knowing
- A typo in the database name -- PostgreSQL database names are case-sensitive unless quoted
- The application is configured to connect to a different PostgreSQL cluster
- A migration script creates tables without first creating the database
- Restoring from a backup that does not include the database creation step
- Using `dblink` or FDW to reference a database on the same server that does not exist

## How to Fix It

### 1. List All Databases

```sql
SELECT datname FROM pg_database WHERE datistemplate = false ORDER BY datname;
```

Or from the command line:

```bash
psql -l
# Or
psql -U postgres -c "\l"
```

### 2. Create the Missing Database

```sql
CREATE DATABASE mydb;
```

With options:

```sql
CREATE DATABASE mydb
    WITH OWNER = myuser
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.UTF-8'
    LC_CTYPE = 'en_US.UTF-8'
    TEMPLATE = template0;
```

### 3. Use IF NOT EXISTS for Idempotent Scripts

```sql
CREATE DATABASE IF NOT EXISTS mydb;
```

### 4. Check Your Connection String

```bash
# Verify the connection parameters
psql -h localhost -p 5432 -U myuser -d mydb

# If the database name has special characters or mixed case
psql -h localhost -U myuser -d "MyDB"
```

### 5. Restore from a Backup

```bash
# If the database was accidentally dropped
createdb -O myuser mydb
pg_restore -d mydb backup.dump

# Or from a plain SQL dump
psql -d mydb -f mydb_backup.sql
```

## Common Mistakes

- Assuming `template1` is the default database for all connections -- each PostgreSQL install may differ
- Creating the database with a case-sensitive name but connecting without quotes
- Not checking whether the PostgreSQL cluster itself is the one you intended to connect to
- Running `DROP DATABASE` in a migration script without a corresponding `CREATE DATABASE`
- Forgetting to create the database before restoring objects that belong to it

## Related Pages

- [PostgreSQL Role Does Not Exist](/tools/postgresql/pg-role-does-not-exist)
- [PostgreSQL Connection Refused](/tools/postgresql/pg-connection-refused)
- [PostgreSQL Config Error](/tools/postgresql/pg-config-error)
- [MySQL Table Does Not Exist](/tools/mysql/mysql-table-doesnt-exist)
