---
title: "[Solution] MySQL No default value error"
description: "Fix MySQL 'No default value' error. Resolve INSERT failures when a column has no default value and is not specified."
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# MySQL No default value error

ERROR 1364 (HY000): Field 'fieldname' doesn't have a default value

This error occurs when you insert a row without specifying a value for a column that has no default and is NOT NULL.

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
