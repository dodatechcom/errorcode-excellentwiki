---
title: "[Solution] MariaDB Data Comparison Error — How to Fix"
description: "Fix MariaDB data comparison mismatches between primary and replica, backup and production, or staging and live databases using diff tools"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB Data Comparison Error

Data comparison errors occur when comparing data between two MariaDB instances and finding mismatches in row counts, values, or schemas.

## Why It Happens

- Replication lag causes the replica to have stale data
- Migration scripts missed rows or applied changes incorrectly
- Data type or collation conversions change values
- Time zone differences cause datetime values to differ
- Triggers modified data on one instance but not the other

## Common Error Messages

```
Row count mismatch: primary has 15234 rows, replica has 15230 rows
```

```
Value mismatch at primary.id=12345: primary.name='Alice' vs replica.name='ALICE'
```

```
Schema mismatch: primary.email VARCHAR(255) vs replica.email VARCHAR(100)
```

```
Checksum mismatch for table 'orders': primary=abcdef123456 replica=789012fedcba
```

## How to Fix It

### 1. Compare Table Row Counts

```sql
SELECT table_name, table_rows
FROM information_schema.TABLES
WHERE table_schema = 'mydb' AND table_type = 'BASE TABLE'
ORDER BY table_name;
```

```bash
pt-table-checksum --host=primary-host --user=root --password=pass   --databases=mydb --tables=users,orders
```

### 2. Use pt-table-sync to Fix Differences

```bash
pt-table-sync --print --sync-to-master   --replicate mydb.checksums   h=replica-host,u=root,p=pass

pt-table-sync --execute --sync-to-master   h=replica-host,u=root,p=pass
```

### 3. Compare Schema Between Instances

```bash
mysqldump --no-data --host=primary-host -u root -p mydb > primary_schema.sql
mysqldump --no-data --host=replica-host -u root -p mydb > replica_schema.sql
diff primary_schema.sql replica_schema.sql
```

### 4. Checksum Individual Tables

```sql
CHECKSUM TABLE mydb.users;
```

### 5. Handle Time Zone Mismatches

```sql
SHOW VARIABLES LIKE 'time_zone';
SET GLOBAL time_zone = '+00:00';
SELECT CONVERT_TZ(created_at, @@session.time_zone, '+00:00') FROM users;
```

## Common Scenarios

- **Replica data drift after DDL**: Use `pt-table-sync` to reconcile.
- **Migration leaves orphaned rows**: Run foreign key consistency check.
- **Staging does not match production**: Restore from more recent backup.

## Prevent It

- Use `pt-table-checksum` weekly to detect replication drift
- Ensure both servers use the same time zone
- Run row count comparison after any migration

## Related Pages

- [MariaDB Replication Error](/tools/mariadb/mariadb-replication-error)
- [MariaDB Backup Error](/tools/mariadb/mariadb-backup-error)
- [MySQL Comparison Error](/tools/mysql/mysql-compare-error)
