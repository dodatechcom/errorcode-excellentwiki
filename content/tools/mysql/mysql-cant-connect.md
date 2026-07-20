---
title: "[Solution] MySQL Can't connect to server"
description: "Fix MySQL 'Can't connect to MySQL server' error. Resolve connection failures when the MySQL server is unreachable."
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# MySQL Can't connect to server

ERROR 2003 (HY000): Can't connect to MySQL server on 'host' (111)

This error occurs when the MySQL client cannot connect to the MySQL server. The server may not be running, the hostname may be wrong, or a firewall may be blocking the connection.

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
