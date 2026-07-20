---
title: "[Solution] MySQL Unknown column in where clause"
description: "Fix MySQL 'Unknown column in where clause' error. Resolve query failures from invalid column references."
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# MySQL Unknown column in where clause

ERROR 1054 (42S22): Unknown column 'col' in 'where clause'

This error occurs when a column referenced in the WHERE clause does not exist in the table.

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
