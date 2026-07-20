---
title: "[Solution] MySQL Incorrect key file error"
description: "Fix MySQL 'Incorrect key file' error. Resolve MyISAM table index corruption."
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# MySQL Incorrect key file error

ERROR 126 (HY000): Incorrect key file for table 'tablename'; try to repair it

This error occurs when a MyISAM table's index file is corrupted.

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
