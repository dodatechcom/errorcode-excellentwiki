---
title: "MySQL Access Denied for Root User"
description: "Root user cannot authenticate to MySQL server"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# MySQL Access Denied for Root User

Root user cannot authenticate to MySQL server

## Common Causes

- Root password not set or forgotten
- MySQL using auth_socket plugin for root
- Anonymous root access disabled
- Password changed and old client cached

## How to Fix

1. Stop MySQL: `sudo systemctl stop mysql`
2. Start in safe mode: `sudo mysqld_safe --skip-grant-tables`
3. Reset root password: `FLUSH PRIVILEGES; ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'newpassword';`
4. Restart MySQL normally

## Examples

```bash
# Stop MySQL
sudo systemctl stop mysql

# Start without grant tables
sudo mysqld_safe --skip-grant-tables &

# Reset password (in mysql client)
FLUSH PRIVILEGES;
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'newpassword';
```
