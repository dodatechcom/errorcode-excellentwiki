---
title: "[Solution] MySQL caching_sha2_password error"
description: "Fix MySQL 'caching_sha2_password' authentication error. Resolve newer MySQL authentication issues with older clients."
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# MySQL caching_sha2_password error

ERROR 2061 (HY000): Authentication plugin 'caching_sha2_password' cannot be loaded

This error occurs when the client does not support the caching_sha2_password plugin (MySQL 8.0+).

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
