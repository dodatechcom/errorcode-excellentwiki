---
title: "[Solution] MySQL Generated column error"
description: "Fix MySQL 'Generated column' error. Resolve virtual and stored column definition issues."
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# MySQL Generated column error

ERROR 3106 (HY000): Defining a generated column as <type> is not supported

This error occurs when the generated column definition is invalid.

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
