---
title: "[Solution] MySQL InnoDB read-only error"
description: "Fix MySQL 'InnoDB read-only' error. Resolve InnoDB read-only mode issues."
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# MySQL InnoDB read-only error

ERROR 1799 (HY000): Cannot execute statement: impossible to write to InnoDB

This error occurs when InnoDB is in read-only mode.

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
