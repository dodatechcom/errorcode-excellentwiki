---
title: "[Solution] MariaDB Federation Engine Error — How to Fix"
description: "Fix MariaDB FEDERATED storage engine errors including connection failures, table definition mismatches, and remote server access issues"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB Federation Engine Error

The FEDERATED engine allows accessing remote databases through a local table definition. Errors occur when connections fail, table definitions do not match, or the engine is not enabled.

## Why It Happens

- The FEDERATED engine is not loaded
- The connection string is incorrect
- The remote server is unreachable
- Local and remote table schemas do not match
- The remote user lacks SELECT privileges

## Common Error Messages

```
ERROR 1434 (HY000): Could not find trusted driver
```

```
ERROR 1286 (HY000): Unknown storage engine 'FEDERATED'
```

```
ERROR 1429 (HY000): Unable to create a connection to remote table;
return code: 'Can't connect to MySQL server'
```

```
ERROR 1146 (42S02): Table 'mydb.remote_table' doesn't exist
```

## How to Fix It

### 1. Enable the FEDERATED Engine

```ini
[mysqld]
federated
```

```bash
sudo systemctl restart mariadb
mysql -e "SHOW ENGINES;" | grep FEDERATED
```

### 2. Create Properly Defined FEDERATED Table

```sql
CREATE TABLE federated_users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(255)
) ENGINE=FEDERATED
CONNECTION='mysql://remote_user:password@remote_host:3306/mydb/remote_users';
```

### 3. Fix Connection String Issues

```sql
-- URL-encode special characters in password
-- @ -> %40, # -> %23, % -> %25
CONNECTION='mysql://user:p%40ssw%23rd@remote_host:3306/mydb/remote_users'

-- With SSL
CONNECTION='mysql://user:password@remote_host:3306/mydb/remote_users?ssl-ca=/path/to/ca.pem'
```

### 4. Verify Remote Access

```bash
mysql -h remote_host -u remote_user -p -D mydb -e "SELECT * FROM remote_users;"
```

## Common Scenarios

- **Federated query returns stale data**: FEDERATED hits remote server on every SELECT.
- **Cannot INSERT into federated table**: Schemas do not match. Ensure they match exactly.
- **Connection string with special chars fails**: URL-encode the special characters.

## Prevent It

- FEDERATED is best for read-only remote access
- Use replication instead of FEDERATED for distributed data access
- Test connections manually before creating federated tables

## Related Pages

- [MariaDB Connection Error](/tools/mariadb/mariadb-connection-error)
- [MariaDB Schema Error](/tools/mariadb/mariadb-schema-error)
- [MySQL Federation Error](/tools/mysql/mysql-federation-error)
