---
title: "[Solution] MySQL SHOW PROCESSLIST error"
description: "Fix MySQL 'SHOW PROCESSLIST' error. Resolve active connection listing issues."
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# MySQL SHOW PROCESSLIST error

ERROR 1227 (42000): Access denied; you need the PROCESS privilege

This error occurs when you do not have the PROCESS privilege to view other connections.

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
