---
title: "[Solution] MySQL InnoDB log full error"
description: "Fix MySQL 'InnoDB log full' error. Resolve InnoDB redo log exhaustion issues."
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# MySQL InnoDB log full error

ERROR 1114 (HY000): The table '<table>' is full

This error can occur when the InnoDB redo log fills up before a checkpoint completes.

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
