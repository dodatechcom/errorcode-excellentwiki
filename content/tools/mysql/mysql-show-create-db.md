---
title: "[Solution] MySQL SHOW CREATE DATABASE error"
description: "Fix MySQL 'SHOW CREATE DATABASE' error. Resolve database definition display issues."
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# MySQL SHOW CREATE DATABASE error

ERROR 1049 (42000): Unknown database '<db>'

This error occurs when you try to show the create statement for a non-existent database.

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
