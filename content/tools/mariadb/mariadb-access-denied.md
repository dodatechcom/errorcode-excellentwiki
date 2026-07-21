---
title: "[Solution] MariaDB Access Denied Error"
description: "Fix MariaDB access denied error. Resolve user authentication issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Access Denied Error

The client cannot authenticate with the MariaDB server. The username or password is wrong.

## Common Causes

- Username or password is incorrect
- User does not exist
- User lacks permission from client host

## How to Fix

### Solution 1

```bash
mysql -u root -e "SELECT user, host FROM mysql.user;"
```

### Solution 2

```bash
mysql -u root -e "GRANT ALL PRIVILEGES ON *.* TO 'myuser'@'%' IDENTIFIED BY 'password';"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
