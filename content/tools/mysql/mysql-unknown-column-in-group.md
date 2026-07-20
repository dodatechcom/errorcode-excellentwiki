---
title: "[Solution] MySQL Unknown column in group clause"
description: "Fix MySQL 'Unknown column in group clause' error. Resolve GROUP BY query failures."
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# MySQL Unknown column in group clause

ERROR 1054 (42S22): Unknown column 'col' in 'group statement'

This error occurs when a column referenced in GROUP BY does not exist.

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
