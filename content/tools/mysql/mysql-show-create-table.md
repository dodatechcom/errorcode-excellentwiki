---
title: "[Solution] MySQL SHOW CREATE TABLE error"
description: "Fix MySQL 'SHOW CREATE TABLE' error. Resolve table definition display issues."
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# MySQL SHOW CREATE TABLE error

ERROR 1146 (42S02): Table '<db>.<table>' doesn't exist

This error occurs when you try to SHOW CREATE TABLE for a non-existent table.

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
