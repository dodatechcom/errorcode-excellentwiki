---
title: "[Solution] MySQL Can't create table errno error"
description: "Fix MySQL 'Can't create table' file system error. Resolve table creation failures due to OS-level issues."
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# MySQL Can't create table errno error

ERROR 1005 (HY000): Can't create table 'db.tablename' (errno: 13)

This error occurs when MySQL cannot create the table file due to permission issues or filesystem errors.

## How to Fix

### Check MySQL Status

```bash
sudo systemctl status mysql
mysqladmin ping
```

### Check Error Log

```bash
sudo tail -100 /var/log/mysql/error.log
```

### Verify Configuration

```bash
mysql --help
sudo mysql -e "SHOW VARIABLES LIKE '%timeout%';"
```

## Related Errors

- [MySQL Connection Refused]({{< relref "/tools/mysql/mysql-connection-refused" >}}) — connection refused
- [MySQL Gone Away]({{< relref "/tools/mysql/mysql-gone-away" >}}) — connection lost
