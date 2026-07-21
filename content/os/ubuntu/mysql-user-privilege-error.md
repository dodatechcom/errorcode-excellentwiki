---
title: "MySQL User Privilege Error"
description: "MySQL user lacks required privileges for operation"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# MySQL User Privilege Error

MySQL user lacks required privileges for operation

## Common Causes

- GRANT statement not executed for user
- User account limited to specific hosts
- Privilege revoked accidentally
- Global vs database-level privileges mismatch

## How to Fix

1. Check privileges: `SHOW GRANTS FOR 'user'@'host';`
2. Grant privileges: `GRANT ALL PRIVILEGES ON db.* TO 'user'@'host';`
3. Flush privileges: `FLUSH PRIVILEGES;`
4. Check user hosts: `SELECT user, host FROM mysql.user;`

## Examples

```sql
-- Check user privileges
SHOW GRANTS FOR 'webuser'@'localhost';

-- Grant database privileges
GRANT ALL PRIVILEGES ON mydb.* TO 'webuser'@'localhost';

-- Reload privileges
FLUSH PRIVILEGES;
```
