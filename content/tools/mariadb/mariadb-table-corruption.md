---
title: "[Solution] MariaDB Table Corruption — How to Fix"
description: "Fix MariaDB table corruption using CHECK TABLE, REPAIR TABLE, InnoDB recovery modes, and mysqldump restore strategies for damaged tables"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB Table Corruption

Table corruption in MariaDB affects both MyISAM and InnoDB tables. MyISAM corruption is usually repairable with `REPAIR TABLE`, while InnoDB requires crash recovery modes and tablespace reimport.

## Why It Happens

- A crash or power loss occurred while InnoDB was flushing data pages
- Disk hardware failure or bad sectors on the storage device
- Running out of disk space during a write operation
- Filesystem corruption after a kernel panic
- Copying InnoDB files while the server is running

## Common Error Messages

```
Table 'mydb.users' is marked as crashed and should be repaired
```

```
[ERROR] InnoDB: Space allocation failed for tablespace 'mydb/t1'
InnoDB: Cannot open or delete tablespace 'mydb/t1'
```

```
InnoDB: PAGE_CHECKSUM mismatch on page 3 of tablespace mydb/t1
```

```
ERROR 145 (HY000): Table './mydb/orders' is marked as crashed and should be repaired
```

## How to Fix It

### 1. Check and Repair MyISAM Tables

```sql
CHECK TABLE mydb.myisam_table EXTENDED;
REPAIR TABLE mydb.myisam_table;
```

```bash
# From command line
myisamchk --check /var/lib/mysql/mydb/myisam_table
myisamchk --recover /var/lib/mysql/mydb/myisam_table
```

### 2. Use InnoDB Force Recovery

```bash
mysqld_safe --innodb_force_recovery=1
# If fails, try level 3
mysqld_safe --innodb_force_recovery=3
# Dump data
mysqldump --all-databases > /backup/full_dump.sql
```

### 3. Reimport InnoDB Tablespace

```sql
ALTER TABLE mydb.corrupt_table DISCARD TABLESPACE;
```

```bash
cp /backup/corrupt_table.ibd /var/lib/mysql/mydb/
chown mysql:mysql /var/lib/mysql/mydb/corrupt_table.ibd
```

```sql
ALTER TABLE mydb.corrupt_table IMPORT TABLESPACE;
```

### 4. Full Restore from Backup

```bash
mysqld_safe --innodb_force_recovery=3
mysqldump --all-databases --flush-logs > /backup/rescue.sql
sudo systemctl stop mariadb
sudo mv /var/lib/mysql /var/lib/mysql.old
mysql_install_db --user=mysql
sudo systemctl start mariadb
mysql < /backup/rescue.sql
```

## Common Scenarios

- **Power loss during large INSERT**: InnoDB cannot complete crash recovery. Use `innodb_force_recovery=3` to dump data.
- **Disk sector failure**: Bad sector corrupts a single table. Identify with `CHECK TABLE` and restore from backup.
- **Upgrade on old filesystem**: ext4 journal corruption causes InnoDB errors. Repair filesystem first with `fsck`.

## Prevent It

- Use a UPS or redundant power supply
- Monitor disk health with SMART tools (`smartctl -a /dev/sda`)
- Regularly back up with `mariabackup` and verify restores

## Related Pages

- [MariaDB InnoDB Error](/tools/mariadb/mariadb-innodb-error)
- [MariaDB Backup Error](/tools/mariadb/mariadb-backup-error)
- [MySQL Disk Full](/tools/mysql/mysql-disk-full)
