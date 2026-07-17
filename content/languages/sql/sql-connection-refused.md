---
title: "[Solution] SQL Connection Refused Fix"
description: "Fix 'Can't connect to MySQL server' when the database server is unreachable."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["connection-refused", "connect", "mysql", "server", "network"]
weight: 5
---

This error occurs when the SQL client cannot establish a connection to the database server. The message reads: `Can't connect to MySQL server on 'host:port'`.

## What This Error Means

The database server is not accepting connections on the specified host and port. This can be because the server is not running, the port is wrong, or a firewall is blocking the connection.

## Common Causes

- MySQL server is not running
- Wrong host or port number
- Firewall blocking port 3306
- `bind-address` in `my.cnf` only allows localhost
- Max connections reached on the server

## How to Fix

### Fix 1: Verify MySQL is running

```bash
# Check MySQL status
sudo systemctl status mysql

# Start MySQL if stopped
sudo systemctl start mysql
```

### Fix 2: Check MySQL configuration

```bash
# Check bind-address in my.cnf
grep bind-address /etc/mysql/my.cnf

# Allow remote connections
# bind-address = 0.0.0.0
```

### Fix 3: Test connection manually

```bash
mysql -h localhost -P 3306 -u root -p
```

### Fix 4: Check firewall rules

```bash
# Check if port 3306 is open
sudo ufw status
sudo ufw allow 3306
```

## Examples

```bash
mysql -h 192.168.1.100 -u root -p
# ERROR 2003: Can't connect to MySQL server on '192.168.1.100' (111)
```

## Related Errors

- [Access Denied](access-denied.md) — connected but no permission
- [Lock Timeout](lock-timeout.md) — connected but waiting for lock
