---
title: "[Solution] MySQL Fulltext error"
description: "Fix MySQL 'Fulltext' error. Resolve FULLTEXT index and search issues."
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# MySQL Fulltext error

ERROR 1191 (HY000): Can't find FULLTEXT index matching the column list

This error occurs when a FULLTEXT search references columns without a FULLTEXT index.

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
