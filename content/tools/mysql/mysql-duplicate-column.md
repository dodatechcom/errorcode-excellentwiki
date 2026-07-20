---
title: "[Solution] MySQL Duplicate column name error"
description: "Fix MySQL 'Duplicate column name' error. Resolve ALTER TABLE failures when adding a column that already exists."
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# MySQL Duplicate column name error

ERROR 1060 (42S21): Duplicate column name 'col'

This error occurs when you try to add a column that already exists in the table.

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
