---
title: "[Solution] MySQL Mix of GROUP columns error"
description: "Fix MySQL 'mix of GROUP columns' error. Resolve ONLY_FULL_GROUP_BY SQL mode violations."
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# MySQL Mix of GROUP columns error

ERROR 1055 (42000): Expression of SELECT list is not in GROUP BY clause

This error occurs when a column in SELECT is not in GROUP BY and is not an aggregate function.

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
