---
title: "[Solution] JDBC ResultSetMetaData Not Available"
description: "Fix java.sql.SQLException ResultSetMetaData not available. Handle metadata access errors in JDBC."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ResultSetMetaData Not Available

A `SQLException` with message `ResultSetMetaData not available` occurs when code attempts to access metadata about a `ResultSet` (column names, types, counts) but the result set is not in a state that supports metadata retrieval, typically because it is closed or was never properly executed.

## What This Error Means

`ResultSet.getMetaData()` requires an open, valid result set. If the result set has been closed, scrolled past its bounds, or was created from a statement that did not return a result set, metadata access fails.

## Common Causes

```java
// Cause 1: Getting metadata from closed ResultSet
ResultSet rs = stmt.executeQuery("SELECT * FROM users");
rs.close();
ResultSetMetaData meta = rs.getMetaData();  // SQLException

// Cause 2: Getting metadata before executing query
PreparedStatement ps = conn.prepareStatement("SELECT * FROM users");
ResultSetMetaData meta = ps.getMetaData();  // Returns null or error

// Cause 3: ResultSet from executeUpdate instead of executeQuery
int affected = stmt.executeUpdate("INSERT INTO users (name) VALUES ('John')");
// No ResultSet returned — metadata not available

// Cause 4: Using metadata after result set scroll limit
ResultSet rs = stmt.executeQuery("SELECT * FROM users");
rs.setType(ResultSet.TYPE_FORWARD_ONLY);
rs.afterLast();  // Scrolled past end
ResultSetMetaData meta = rs.getMetaData();  // May fail on some drivers
```

## How to Fix

### Fix 1: Access metadata while ResultSet is open

```java
try (PreparedStatement ps = conn.prepareStatement("SELECT * FROM users")) {
    try (ResultSet rs = ps.executeQuery()) {
        ResultSetMetaData meta = rs.getMetaData();
        int columnCount = meta.getColumnCount();
        for (int i = 1; i <= columnCount; i++) {
            System.out.println(meta.getColumnName(i) + " : " + meta.getColumnTypeName(i));
        }
    }
}
```

### Fix 2: Use Statement.getMetaData() before executing query

```java
// Some drivers allow getting parameter metadata before execution
PreparedStatement ps = conn.prepareStatement("SELECT * FROM users WHERE id = ?");
ParameterMetaData paramMeta = ps.getParameterMetaData();
// This gives parameter metadata, not result set metadata
// Result set metadata is only available after executeQuery()
```

### Fix 3: Build dynamic result set mapping with metadata

```java
public List<Map<String, Object>> queryToMap(Connection conn, String sql) throws SQLException {
    List<Map<String, Object>> results = new ArrayList<>();
    try (PreparedStatement ps = conn.prepareStatement(sql);
         ResultSet rs = ps.executeQuery()) {
        ResultSetMetaData meta = rs.getMetaData();
        int cols = meta.getColumnCount();
        while (rs.next()) {
            Map<String, Object> row = new LinkedHashMap<>();
            for (int i = 1; i <= cols; i++) {
                row.put(meta.getColumnLabel(i), rs.getObject(i));
            }
            results.add(row);
        }
    }
    return results;
}
```

### Fix 4: Guard metadata access with state checks

```java
public static void printMetadata(ResultSet rs) throws SQLException {
    if (rs == null || rs.isClosed()) {
        throw new SQLException("ResultSet is null or closed, metadata not available");
    }
    ResultSetMetaData meta = rs.getMetaData();
    if (meta == null) {
        throw new SQLException("ResultSetMetaData is null");
    }
    for (int i = 1; i <= meta.getColumnCount(); i++) {
        System.out.printf("Column %d: %s (%s)%n",
            i, meta.getColumnName(i), meta.getColumnTypeName(i));
    }
}
```

## Prevention Tips

- Always access `ResultSetMetaData` within the same try-with-resources block as the `ResultSet`.
- Use metadata for dynamic SQL result mapping to avoid hardcoding column names.
- Prefer explicit column selection over `SELECT *` for better metadata predictability.

## Related Errors

- {{< relref "jdbc-resultset-closed" >}} — ResultSet closed
- {{< relref "jdbc-statement-closed" >}} — Statement closed
- {{< relref "jdbc-closed-connection" >}} — Connection already closed
