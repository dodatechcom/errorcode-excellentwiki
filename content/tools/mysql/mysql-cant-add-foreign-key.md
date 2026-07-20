---
title: "[Solution] MySQL Can't add foreign key error"
description: "Fix MySQL 'Can't add foreign key' error. Resolve foreign key constraint creation failures."
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# MySQL Can't add foreign key error

ERROR 1215 (HY000): Cannot add foreign key constraint

This error occurs when the foreign key references a column that does not exist, has incompatible types, or the referenced table/column does not exist.

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
