---
title: "[Solution] MySQL InnoDB tablespace full"
description: "Fix MySQL 'InnoDB tablespace full' error. Resolve InnoDB tablespace exhaustion issues."
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# MySQL InnoDB tablespace full

ERROR 1114 (HY000): The table '<table>' is full

This error occurs when the InnoDB tablespace runs out of space.

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
