---
title: "MySQL Connection Refused Error"
description: "Client cannot connect to MySQL server"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# MySQL Connection Refused Error

Client cannot connect to MySQL server

## Common Causes

- MySQL server not running
- Bind-address set to 127.0.0.1 but connecting remotely
- User does not have permission from connecting host
- Port 3306 blocked by firewall

## How to Fix

1. Check MySQL status: `systemctl status mysql`
2. Check bind-address: `cat /etc/mysql/mysql.conf.d/mysqld.cnf | grep bind-address`
3. Verify user permissions: `SELECT user, host FROM mysql.user;`
4. Check firewall: `sudo ufw status | grep 3306`

## Examples

```bash
# Check MySQL status
sudo systemctl status mysql

# Check bind address
grep bind-address /etc/mysql/mysql.conf.d/mysqld.cnf

# Test connection
mysql -u root -p -h localhost
```
