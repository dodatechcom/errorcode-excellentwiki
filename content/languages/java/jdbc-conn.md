---
title: "[Solution] Java SQLException — cannot establish JDBC connection due to wrong URL, credentials, or network"
description: "Fix Java SQLException when cannot establish jdbc connection due to wrong url, credentials, or network with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# SQLException — cannot establish JDBC connection due to wrong URL, credentials, or network

A `SQLException` occurs when Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306");.

## Common Causes

```java
Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306");
```

## Solutions

```java
// Fix: validate params
String url = "jdbc:mysql://localhost:3306/mydb?useSSL=false";
try (Connection c = DriverManager.getConnection(url, user, pass)) {
    if (!c.isValid(5)) throw new SQLException("Connection invalid");
}

// Fix: connection pool
HikariConfig cfg = new HikariConfig();
	cfg.setJdbcUrl(url); cfg.setUsername(user); cfg.setPassword(pass);
	cfg.setConnectionTimeout(30000);
HikariDataSource ds = new HikariDataSource(cfg);
```

## Prevention Checklist

- Use connection pooling (HikariCP).
- Validate URL, credentials, network.
- Set connection and socket timeouts.
- Monitor pool metrics.

## Related Errors

ClassNotFoundException, SQLTransientConnectionException
