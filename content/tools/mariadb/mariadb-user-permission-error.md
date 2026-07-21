---
title: "[Solution] MariaDB User Permission Error"
description: "Fix MariaDB user permission errors when GRANT or REVOKE operations fail"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB User Permission Error

User permission errors occur when MariaDB cannot grant or revoke privileges correctly.

## Common Causes

- User does not exist for GRANT
- Granting privileges user does not have
- Table or database does not exist
- Permission already granted (no-op)

## Common Error Messages

```
ERROR 1141 (42000): You do not have the GRANT privilege
```

## How to Fix It

### 1. Check User Grants

```sql
SHOW GRANTS FOR 'user'@'host';
```

### 2. Grant Permissions

```sql
GRANT SELECT, INSERT ON mydb.* TO 'user'@'%';
FLUSH PRIVILEGES;
```

### 3. Revoke Permissions

```sql
REVOKE INSERT ON mydb.* FROM 'user'@'%';
```

## Examples

```sql
SELECT user, host, plugin FROM mysql.user WHERE user = 'app_user';
```
