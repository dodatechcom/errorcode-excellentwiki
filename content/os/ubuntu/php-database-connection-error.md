---
title: "PHP Database Connection Error"
description: "PHP application cannot connect to database server"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# PHP Database Connection Error

PHP application cannot connect to database server

## Common Causes

- Database credentials incorrect in PHP config
- Database server not running or unreachable
- PHP database extension not installed (php-mysql, php-pgsql)
- Connection limit reached on database server

## How to Fix

1. Check PHP extensions: `php -m | grep -i mysql`
2. Test connection: `php -r "new PDO('mysql:host=localhost', 'user', 'pass');"`
3. Verify credentials in config file
4. Check database server status

## Examples

```bash
# Check PHP database extensions
php -m | grep -i mysql

# Test MySQL connection
php -r "try { new PDO('mysql:host=localhost', 'root', 'pass'); echo 'Connected'; } catch(Exception $e) { echo $e->getMessage(); }"

# Install PHP MySQL extension
sudo apt-get install php8.1-mysql
```
