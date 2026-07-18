---
title: "[Solution] MariaDB Connection Error — How to Fix"
description: "Fix MariaDB connection errors by checking socket paths, max connections, bind addresses, firewall rules, and authentication settings"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB Connection Error

A MariaDB connection error means the client cannot establish a connection to the database server. This can happen at the network level, server level, or authentication level.

## Why It Happens

- MariaDB is bound to `127.0.0.1` and the client connects remotely
- The `max_connections` limit has been reached
- The Unix socket file path is wrong or missing
- The user account lacks permission to connect from the client's host
- The firewall blocks port 3306
- The MariaDB service is stopped or crashed
- Authentication plugin mismatch between client and server

## Common Error Messages

```
ERROR 2003 (HY000): Can't connect to MySQL server on '192.168.1.100' (111)
```

```
ERROR 1045 (28000): Access denied for user 'myuser'@'localhost' (using password: YES)
```

```
ERROR 1040 (08004): Too many connections
```

```
ERROR 2002 (HY000): Can't connect to local MySQL server through socket
'/var/run/mysqld/mysqld.sock' (2)
```

## How to Fix It

### 1. Check and Fix the Bind Address

```ini
# In /etc/mysql/mariadb.conf.d/50-server.cnf
[mysqld]
bind-address = 0.0.0.0
```

```bash
sudo systemctl restart mariadb
```

### 2. Increase max_connections

```sql
SHOW VARIABLES LIKE 'max_connections';
SET GLOBAL max_connections = 500;

-- In my.cnf
-- [mysqld]
-- max_connections = 500
```

### 3. Fix Socket Connection Issues

```bash
# Find the actual socket path
mysql -e "SHOW VARIABLES LIKE 'socket';"

# Create symlink if paths differ
ln -sf /var/lib/mysql/mysql.sock /var/run/mysqld/mysqld.sock

# Or connect via TCP
mysql -h 127.0.0.1 -P 3306 -u myuser -p
```

### 4. Reset Password and Fix Grants

```sql
ALTER USER 'myuser'@'%' IDENTIFIED BY 'new_password';
GRANT ALL PRIVILEGES ON mydb.* TO 'myuser'@'%';
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'myuser'@'%';
```

## Common Scenarios

- **New deployment with remote access**: App connects to remote MariaDB but `bind-address` is `127.0.0.1`. Change to `0.0.0.0`.
- **Peak traffic exhausting connections**: Sudden spike exceeds `max_connections`. Increase limit and add connection pooling.
- **Socket path mismatch after upgrade**: MariaDB upgrades change the socket path. Update client configs or symlink.

## Prevent It

- Use a connection pooler (ProxySQL, HikariCP) to reuse connections
- Set `bind-address = 0.0.0.0` and secure with firewall rules and SSL
- Monitor connection count and alert before hitting the limit

## Related Pages

- [MariaDB User Error](/tools/mariadb/mariadb-user-error)
- [MariaDB SSL Error](/tools/mariadb/mariadb-ssl-error)
- [MySQL Connection Refused](/tools/mysql/mysql-connection-refused)
