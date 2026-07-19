---
title: "[Solution] Eclipse Database tools error"
description: "Database tools error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "eclipse"
tags: ["eclipse", "ide", "database", "jdbc", "datatools"]
severity: "error"
---

# Database tools error

## Error Message

```
Could not connect to database. Connection refused: connect. Verify the JDBC URL and ensure the database server is running and accepting connections.
```

## Common Causes

- The database server is not running or is not accepting connections on the specified host and port.
- The JDBC driver JAR file is missing from the project's build path.
- The connection URL, username, or password in the data source configuration is incorrect.

## Solutions

### Solution 1: Configure Database Connection in Eclipse

Open the **Database Development** perspective via **Window > Perspective > Open Perspective > Other > Database Development**. In the **Database Connections** view, right-click and select **New**. Choose your database type, fill in the connection details, and click **Test Connection** to verify.

```java
<!-- Example JDBC connection properties -->
jdbc.url=jdbc:mysql://localhost:3306/mydb?useSSL=false&serverTimezone=UTC
jdbc.username=root
jdbc.password=secret
jdbc.driver=com.mysql.cj.jdbc.Driver
```

### Solution 2: Add JDBC Driver to Build Path

Download the appropriate JDBC driver for your database (MySQL Connector/J, PostgreSQL JDBC Driver, etc.) and add it to the project. Right-click the project, go to **Build Path > Add External Archives**, and select the driver JAR. Alternatively, add the Maven dependency to your `pom.xml`.

```bash
<!-- pom.xml - Add JDBC driver dependency -->
<dependency>
    <groupId>com.mysql</groupId>
    <artifactId>mysql-connector-j</artifactId>
    <version>8.2.0</version>
</dependency>

<!-- PostgreSQL -->
<dependency>
    <groupId>org.postgresql</groupId>
    <artifactId>postgresql</artifactId>
    <version>42.7.1</version>
</dependency>
```

## Prevention Tips

- Use the **SQL Scrapbook** (Ctrl+Shift+D) to test SQL queries without leaving Eclipse.
- Enable **Database Development > SQL validation** for real-time SQL syntax checking.
- Store database credentials in environment variables rather than hardcoding them in configuration files.

## Related Errors

- [jpa-error]({{< relref "/tools/eclipse/jpa-error" >}})
- [build-path-error]({{< relref "/tools/eclipse/build-path-error" >}})
- [web-tools-error]({{< relref "/tools/eclipse/web-tools-error" >}})
