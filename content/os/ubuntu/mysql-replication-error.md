---
title: "[Solution] Ubuntu Server: mysql-replication-error"
description: "Fix Ubuntu mysql-replication-error. MySQL master-slave replication fails."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# MySQL Replication Error

MySQL replication between master and slave fails.

## Common Causes
- Slave IO thread not running
- Binary log position wrong
- GTID mismatch
- Replication user password expired

## How to Fix
1. Check replication status
```bash
mysql -u root -p -e "SHOW SLAVE STATUS\G"
```
2. Start slave
```bash
mysql -u root -p -e "START SLAVE;"
```
3. Fix replication position
```bash
mysql -u root -p -e "CHANGE MASTER TO MASTER_LOG_FILE='mysql-bin.000003', MASTER_LOG_POS=154;"
```

## Examples
```bash
$ mysql -u root -p -e "SHOW SLAVE STATUS\G"
 Slave_IO_Running: Connecting
 Slave_SQL_Running: Yes
```