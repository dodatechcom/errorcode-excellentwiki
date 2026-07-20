---
title: "[Solution] MySQL Too big scale error"
description: "Fix MySQL 'Too big scale' error. Resolve DECIMAL scale specification errors."
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# MySQL Too big scale error

ERROR 1426 (42000): Too big scale <n> specified for 'col'. Maximum is 30.

This error occurs when the scale for a DECIMAL column exceeds the maximum of 30.

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
