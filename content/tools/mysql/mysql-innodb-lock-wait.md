---
title: "[Solution] MySQL InnoDB lock wait timeout"
description: "Fix MySQL 'InnoDB lock wait timeout' error. Resolve transaction lock waiting issues."
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# MySQL InnoDB lock wait timeout

ERROR 1205 (HY000): Lock wait timeout exceeded; try restarting transaction

This error occurs when a transaction waits too long for a lock.

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
