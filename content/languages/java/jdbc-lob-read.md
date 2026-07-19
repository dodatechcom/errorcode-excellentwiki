---
title: "[Solution] JDBC Could Not Materialize LOB — LOB Read/Write Error"
description: "Fix java.sql.SQLException Could not materialize LOB. Handle Large Object read/write errors in JDBC."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Could Not Materialize LOB — LOB Read/Write Error

A `SQLException` with message `Could not materialize LOB` occurs when the JDBC driver fails to read or write a Large Object (BLOB/CLOB) from the database. This typically happens when the LOB locator becomes invalid or the connection used to create the LOB is no longer available.

## What This Error Means

LOBs (Large Binary Objects, Large Character Objects) in JDBC are accessed through stream-based APIs. The driver maintains a locator or reference to the LOB data on the server. If this reference becomes stale (e.g., due to connection closure or transaction completion), reading from the LOB stream fails.

## Common Causes

```java
// Cause 1: Reading LOB after connection is closed
Blob blob;
try (Connection conn = dataSource.getConnection()) {
    PreparedStatement ps = conn.prepareStatement("SELECT image FROM photos WHERE id = ?");
    ps.setLong(1, photoId);
    ResultSet rs = ps.executeQuery();
    if (rs.next()) {
        blob = rs.getBlob(1);  // Get locator
    }
}
// Connection closed, LOB locator invalid
InputStream is = blob.getBinaryStream();  // Could not materialize LOB

// Cause 2: Reading LOB after transaction commit
Connection conn = dataSource.getConnection();
conn.setAutoCommit(false);
ResultSet rs = conn.prepareStatement("SELECT data FROM files WHERE id = 1").executeQuery();
rs.next();
Clob clob = rs.getClob(1);
conn.commit();  // Transaction ends, LOB locator may be invalidated
Reader reader = clob.getCharacterStream();  // Could not materialize

// Cause 3: LOB too large to materialize in memory
PreparedStatement ps = conn.prepareStatement("SELECT video FROM media WHERE id = ?");
Blob blob = ps.executeQuery().getBlob(1);
byte[] data = blob.getBytes(1, (int) blob.length());  // OutOfMemoryError or error
```

## How to Fix

### Fix 1: Read LOB data within the same transaction/connection

```java
try (Connection conn = dataSource.getConnection()) {
    conn.setAutoCommit(false);
    try (PreparedStatement ps = conn.prepareStatement("SELECT data FROM files WHERE id = ?")) {
        ps.setLong(1, fileId);
        try (ResultSet rs = ps.executeQuery()) {
            if (rs.next()) {
                Blob blob = rs.getBlob(1);
                InputStream is = blob.getBinaryStream();
                byte[] data = is.readAllBytes();
                // Process data while connection and transaction are active
            }
        }
    }
    conn.commit();
}
```

### Fix 2: Stream LOB data instead of materializing in memory

```java
try (Connection conn = dataSource.getConnection();
     PreparedStatement ps = conn.prepareStatement("SELECT image FROM photos WHERE id = ?")) {
    ps.setLong(1, photoId);
    try (ResultSet rs = ps.executeQuery()) {
        if (rs.next()) {
            Blob blob = rs.getBlob(1);
            try (InputStream is = blob.getBinaryStream();
                 OutputStream os = new FileOutputStream("output.jpg")) {
                byte[] buffer = new byte[8192];
                int bytesRead;
                while ((bytesRead = is.read(buffer)) != -1) {
                    os.write(buffer, 0, bytesRead);
                }
            }
        }
    }
}
```

### Fix 3: Use try-with-resources with auto-commit for simple LOB reads

```java
try (Connection conn = dataSource.getConnection();
     PreparedStatement ps = conn.prepareStatement("SELECT content FROM articles WHERE id = ?")) {
    ps.setLong(1, articleId);
    try (ResultSet rs = ps.executeQuery()) {
        if (rs.next()) {
            Clob clob = rs.getClob(1);
            String content = clob.getSubString(1, (int) clob.length());
            // Use content immediately
        }
    }
}
```

### Fix 4: Configure connection pool to avoid premature connection reclaim

```java
HikariConfig config = new HikariConfig();
config.setJdbcUrl("jdbc:postgresql://localhost:5432/mydb");
config.setMaxLifetime(1800000);    // 30 minutes — longer than LOB processing
config.setIdleTimeout(600000);     // 10 minutes
config.setLeakDetectionThreshold(60000);  // Warn if connection held > 60s
```

## Prevention Tips

- Always process LOB data within the same connection and transaction that retrieved it.
- Stream large LOBs instead of loading them entirely into memory.
- Use try-with-resources to ensure proper LOB and connection cleanup.
- Avoid passing LOB references across method boundaries or thread boundaries.

## Related Errors

- {{< relref "jdbc-closed-connection" >}} — Connection already closed
- {{< relref "jdbc-resultset-closed" >}} — ResultSet closed
- {{< relref "jdbc-conn" >}} — Connection errors
