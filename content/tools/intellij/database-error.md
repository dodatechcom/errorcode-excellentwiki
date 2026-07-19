---
title: "[Solution] IntelliJ IDEA Database connection failed"
description: "Fix IntelliJ IDEA Database tools connection failures. Resolve JDBC driver issues, connection timeouts, and database configuration errors."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "intellij"
tags: ["intellij", "ide", "database", "jdbc", "data-tools", "connection"]
severity: "error"
---

# Database connection failed

## Error Message

```
Database connection failed
Cannot connect to database 'mydb' at localhost:5432.
Connection refused: connect
Verify connection parameters and that the database server is running.

java.sql.SQLException: No suitable driver found for jdbc:postgresql://localhost:5432/mydb
```

## Common Causes

- Database server is not running or not accepting connections
- JDBC driver is missing or not configured in IDE
- Incorrect connection URL, username, or password
- Firewall blocking the database port
- Database requires SSL but it is not configured

## Solutions

### Solution 1: Add JDBC Driver in IDE

Download and configure the JDBC driver for your database. Open the Database tool window and add a new data source.

```
# In IDE:
View → Tool Windows → Database
# Click '+' → Data Source → Select your database type
# In the connection dialog, click 'Download' for the JDBC driver
# Fill in connection details:
#   Host: localhost
#   Port: 5432 (PostgreSQL) / 3306 (MySQL)
#   Database: mydb
#   User: your_username
#   Password: your_password
```

### Solution 2: Test Connection from Command Line

Verify database connectivity from the terminal to rule out network issues.

```bash
# PostgreSQL:
psql -h localhost -p 5432 -U myuser -d mydb

# MySQL:
mysql -h localhost -P 3306 -u myuser -p mydb

# Check if database port is listening:
netstat -tlnp | grep 5432
# or
ss -tlnp | grep 5432
```

### Solution 3: Configure Connection Properties

Fine-tune connection properties in the IDE Database settings for stability.

```
# In Database tool window, open data source properties:
# Advanced tab → Add properties:

# For PostgreSQL:
ssl=false
connectTimeout=30
socketTimeout=30

# For MySQL:
useSSL=false
serverTimezone=UTC
characterEncoding=UTF-8
allowPublicKeyRetrieval=true

# Connection pool settings:
# Session → Connection Properties → maximumPoolSize=10
```

### Solution 4: Configure SSH Tunnel for Remote Databases

Use SSH tunneling to securely connect to remote databases through a bastion host.

```
# In IDE Database connection dialog:
# Click 'SSH/SSL' tab:
#   Proxy host: bastion.company.com
#   Proxy user: tunnel_user
#   Proxy port: 22
#   Auth type: Key pair → select your private key

# Or configure manually in settings.xml:
# SSH tunnel command:
ssh -L 15432:db-host:5432 user@bastion-host -N
# Then connect IDE to localhost:15432
```

## Prevention Tips

- Use the Database tool window's 'Test Connection' button before saving data sources
- Store connection passwords in the IDE's credential store instead of hard-coding
- Use SSH tunneling for remote database connections instead of exposing ports
- Create separate data source configurations for development and production

## Related Errors

- [Terminal Error]({{< relref "/tools/intellij/terminal-error" >}})
- [External Tools Error]({{< relref "/tools/intellij/external-tools-error" >}})
- [Spring Boot Error]({{< relref "/tools/intellij/spring-boot-error" >}})
