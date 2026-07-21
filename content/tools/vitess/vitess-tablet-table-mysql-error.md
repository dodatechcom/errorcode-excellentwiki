---
title: "[Solution] Vitess Tablet MySQL Connection Error"
description: "Fix Vitess tablet MySQL connection errors when vttablet cannot connect to backend MySQL"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet MySQL Connection Error

MySQL connection errors occur when vttablet cannot establish a connection to its local MySQL instance.

## Common Causes

- MySQL service stopped on tablet host
- MySQL socket file path misconfigured
- MySQL user credentials incorrect
- MySQL max_connections reached

## How to Fix

Check MySQL status:

```bash
systemctl status mysql
```

Verify socket path:

```bash
mysql -u vt_dba -S /var/run/mysqld/mysqld.sock -e "SELECT 1"
```

Check MySQL error log:

```bash
tail -100 /var/log/mysql/error.log
```

Restart vttablet after MySQL is up:

```bash
systemctl restart vttablet
```

## Examples

```bash
mysql -u vt_dba -S /var/run/mysqld/mysqld.sock -e "SHOW PROCESSLIST"
```
