---
title: "[Solution] MySQL Subquery returns more than one row"
description: "Fix MySQL 'Subquery returns more than one row' error. Resolve single-value subquery issues."
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# MySQL Subquery returns more than one row

ERROR 1242 (21000): Subquery returns more than 1 row

This error occurs when a subquery used with =, <, >, etc. returns multiple rows.

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
