---
title: "[Solution] JDBC Connection Is Read-Only — Cannot Modify Data"
description: "Fix java.sql.SQLException Connection is read-only when trying to set autocommit in a read-only transaction. Handle read-only connections properly."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Connection Is Read-Only — Cannot Modify Data

A `SQLException` with message `Connection is read-only. Queries leading to data modification are not allowed` occurs when you attempt to perform INSERT, UPDATE, or DELETE operations on a connection that has been set to read-only mode.

## What This Error Means

JDBC connections can be marked as read-only to optimize them for SELECT queries only. Some connection pools and frameworks (including Spring) set connections to read-only for read-only transactions. Attempting to modify data on such a connection will fail.

## Common Causes

```java
// Cause 1: Connection set to read-only by the framework
Connection conn = dataSource.getConnection();
conn.setReadOnly(true);
conn.prepareStatement("INSERT INTO users ...").executeUpdate();
// SQLException: Connection is read-only

// Cause 2: Spring @Transactional(readOnly = true) leaking
@Transactional(readOnly = true)
public void updateUser(Long id, String name) {
    // This transaction is read-only, cannot write
    userRepository.updateName(id, name);
}

// Cause 3: Connection pool configured with read-only default
HikariConfig config = new HikariConfig();
config.setReadOnly(true);  // All connections are read-only
```

## How to Fix

### Fix 1: Do not set read-only for write operations

```java
Connection conn = dataSource.getConnection();
if (conn.isReadOnly()) {
    conn.setReadOnly(false);
}
PreparedStatement ps = conn.prepareStatement("UPDATE users SET name = ? WHERE id = ?");
ps.setString(1, name);
ps.setLong(2, id);
ps.executeUpdate();
```

### Fix 2: Separate read and write transactions in Spring

```java
@Transactional(readOnly = true)
public User findById(Long id) {
    return userRepository.findById(id).orElseThrow();
}

@Transactional  // No readOnly = true for write operations
public void updateUser(Long id, String name) {
    User user = userRepository.findById(id).orElseThrow();
    user.setName(name);
    userRepository.save(user);
}
```

### Fix 3: Configure pool to allow read-only switch

```java
HikariConfig config = new HikariConfig();
config.setJdbcUrl("jdbc:postgresql://localhost:5432/mydb");
config.setReadOnly(false);  // Allow read-write operations
```

### Fix 4: Use separate data sources for read and write

```java
@Configuration
public class DataSourceConfig {
    @Bean("readDataSource")
    public DataSource readDataSource() {
        HikariConfig config = new HikariConfig();
        config.setJdbcUrl("jdbc:postgresql://read-replica:5432/mydb");
        config.setReadOnly(true);
        return new HikariDataSource(config);
    }

    @Bean("writeDataSource")
    public DataSource writeDataSource() {
        HikariConfig config = new HikariConfig();
        config.setJdbcUrl("jdbc:postgresql://primary:5432/mydb");
        config.setReadOnly(false);
        return new HikariDataSource(config);
    }
}
```

## Prevention Tips

- Only set `readOnly = true` for queries that genuinely only read data.
- Review Spring `@Transactional(readOnly = true)` annotations to ensure write methods do not inherit them.
- Use separate read/write data sources in high-throughput applications.

## Related Errors

- {{< relref "jdbc-transaction-active" >}} — Transaction active error
- {{< relref "jdbc-conn" >}} — Connection establishment errors
- {{< relref "jdbc-pool-timeout" >}} — Pool timeout waiting
