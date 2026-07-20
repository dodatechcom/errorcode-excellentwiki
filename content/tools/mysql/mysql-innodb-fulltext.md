---
title: "[Solution] MySQL InnoDB FULLTEXT error"
description: "Fix MySQL 'InnoDB FULLTEXT' error. Resolve InnoDB full-text search issues."
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# MySQL InnoDB FULLTEXT error

ERROR 3809 (HY000): InnoDB: Fulltext index <n> is not usable

This error occurs when an InnoDB FULLTEXT index is corrupted.

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
