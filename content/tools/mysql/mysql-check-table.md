---
title: "[Solution] MySQL CHECK TABLE error"
description: "Fix MySQL 'CHECK TABLE' error. Resolve table checking and repair issues."
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# MySQL CHECK TABLE error

Warning: Table is marked as crashed

This warning appears when a table check finds corruption.

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
