---
title: "[Solution] MySQL OPTIMIZE TABLE error"
description: "Fix MySQL 'OPTIMIZE TABLE' error. Resolve table optimization failures."
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# MySQL OPTIMIZE TABLE error

ERROR 1062 (23000): Duplicate entry '<key>' for key <n>

This error can occur during OPTIMIZE TABLE if there are duplicate keys.

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
