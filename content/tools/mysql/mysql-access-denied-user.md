---
title: "[Solution] MySQL Access denied for user"
description: "Fix MySQL 'Access denied for user' error. Resolve authentication failures when connecting to the MySQL server."
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# MySQL Access denied for user

ERROR 1045 (28000): Access denied for user 'user'@'host' (using password: YES)

This error occurs when the username or password is incorrect, or the user does not have permission to connect from the specified host.

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
