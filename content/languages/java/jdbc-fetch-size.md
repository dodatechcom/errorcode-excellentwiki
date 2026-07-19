---
title: "[Solution] PostgreSQL FETCH_SIZE Cannot Be Set with Adaptive Fetch"
description: "Fix org.postgresql.util.PSQLException FETCH_SIZE cannot be set when using adaptive fetch. Configure JDBC fetch size correctly."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# FETCH_SIZE Cannot Be Set with Adaptive Fetch

A `PSQLException` with message `FETCH_SIZE cannot be set when using adaptive fetch` occurs in PostgreSQL JDBC driver when you attempt to set the fetch size while the driver's adaptive fetch mode is enabled.

## What This Error Means

The PostgreSQL JDBC driver has an adaptive fetch feature that automatically determines the optimal fetch size based on the result set size and network conditions. When adaptive fetch is enabled, manually setting the fetch size is not allowed because the driver manages it internally.

## Common Causes

```java
// Cause 1: Setting fetch size with adaptive fetch enabled in URL
// URL: jdbc:postgresql://localhost/mydb?preferQueryMode=adaptive
Statement stmt = conn.createStatement();
stmt.setFetchSize(100);  // PSQLException: FETCH_SIZE cannot be set

// Cause 2: Setting fetch size via connection property
Properties props = new Properties();
props.setProperty("adaptiveFetch", "true");
Connection conn = DriverManager.getConnection(url, props);
PreparedStatement ps = conn.prepareStatement("SELECT * FROM large_table");
ps.setFetchSize(500);  // PSQLException

// Cause 3: Spring/JPA setting fetch size while driver has adaptive mode
@Query(value = "SELECT * FROM users", nativeQuery = true)
// Spring Data sets fetchSize on the statement, but driver rejects it
```

## How to Fix

### Fix 1: Disable adaptive fetch and set explicit fetch size

```java
// Connection URL without adaptive fetch
String url = "jdbc:postgresql://localhost:5432/mydb?preferQueryMode=simple";
Connection conn = DriverManager.getConnection(url, user, pass);
PreparedStatement ps = conn.prepareStatement("SELECT * FROM large_table");
ps.setFetchSize(500);
ResultSet rs = ps.executeQuery();
```

### Fix 2: Use connection properties to disable adaptive fetch

```java
Properties props = new Properties();
props.setProperty("user", "dbuser");
props.setProperty("password", "dbpass");
props.setProperty("preferQueryMode", "simple");  // or "extended"
props.setProperty("adaptiveFetch", "false");
Connection conn = DriverManager.getConnection(
    "jdbc:postgresql://localhost:5432/mydb", props);
```

### Fix 3: Let adaptive fetch handle it (recommended)

```java
// Don't set fetch size — let PostgreSQL driver optimize it
String url = "jdbc:postgresql://localhost:5432/mydb?preferQueryMode=adaptive";
Connection conn = DriverManager.getConnection(url, user, pass);
PreparedStatement ps = conn.prepareStatement("SELECT * FROM large_table");
// Do NOT call setFetchSize() — driver manages it
ResultSet rs = ps.executeQuery();
while (rs.next()) {
    processRow(rs);
}
```

### Fix 4: Use Spring Boot configuration

```properties
# application.properties
spring.datasource.url=jdbc:postgresql://localhost:5432/mydb?preferQueryMode=extended
spring.datasource.hikari.maximum-pool-size=20
# Then set fetch size in code
# jdbcTemplate.getJdbcTemplate().setFetchSize(100);
```

## Prevention Tips

- Choose either adaptive fetch or manual fetch size, not both.
- For most applications, adaptive fetch provides optimal performance.
- Set explicit fetch size only when you have specific memory or performance requirements.
- Test fetch size settings under realistic load conditions.

## Related Errors

- {{< relref "jdbc-conn" >}} — JDBC connection errors
- {{< relref "jdbc-timeout-query" >}} — Query timeout
- {{< relref "jdbc-types-mismatch" >}} — Type mismatch errors
