---
title: "[Solution] MySQL InnoDB deadlock error"
description: "Fix MySQL 'InnoDB deadlock' error. Resolve transaction deadlock detection issues."
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# MySQL InnoDB deadlock error

ERROR 1213 (40001): Deadlock found when trying to get lock; try restarting transaction

This error occurs when two or more transactions hold locks the other needs.

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
