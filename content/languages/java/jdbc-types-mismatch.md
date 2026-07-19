---
title: "[Solution] PostgreSQL Type Mismatch — Column Type vs Expression Type"
description: "Fix org.postgresql.util.PSQLException column is of type X but expression is of type Y. Resolve SQL type mismatch errors."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PostgreSQL Type Mismatch — Column Type vs Expression Type

A `PSQLException` with message `ERROR: column is of type X but expression is of type Y` occurs in PostgreSQL when the data type of a value being inserted or compared does not match the declared column type.

## What This Error Means

PostgreSQL is strongly typed and requires explicit type matching. Unlike MySQL, PostgreSQL does not implicitly cast between many type pairs (e.g., `text` to `integer`, `varchar` to `uuid`). This strictness causes errors when parameters or literal values have mismatched types.

## Common Causes

```java
// Cause 1: Passing string for UUID column
PreparedStatement ps = conn.prepareStatement("INSERT INTO users (id, name) VALUES (?, ?)");
ps.setString(1, "550e8400-e29b-41d4-a716-446655440000");  // String
ps.setString(2, "John");
ps.executeUpdate();
// ERROR: column "id" is of type uuid but expression is of type character varying

// Cause 2: Passing integer for numeric column with precision
ps.setInt(1, 42);
// Column defined as NUMERIC(10,2) — expects decimal

// Cause 3: Comparing varchar to integer
PreparedStatement ps = conn.prepareStatement("SELECT * FROM users WHERE age = ?");
ps.setString(1, "25");  // Passing string for integer column
// ERROR: column "age" is of type integer but expression is of type character varying
```

## How to Fix

### Fix 1: Use explicit type casting in SQL

```java
// Cast string to UUID in the query
PreparedStatement ps = conn.prepareStatement(
    "INSERT INTO users (id, name) VALUES (?::uuid, ?)");
ps.setString(1, "550e8400-e29b-41d4-a716-446655440000");
ps.setString(2, "John");
ps.executeUpdate();
```

### Fix 2: Use the correct Java type for PreparedStatement parameters

```java
// For UUID column, use setObject with java.util.UUID
PreparedStatement ps = conn.prepareStatement(
    "INSERT INTO users (id, name) VALUES (?, ?)");
UUID uuid = UUID.fromString("550e8400-e29b-41d4-a716-446655440000");
ps.setObject(1, uuid, Types.OTHER);  // PostgreSQL UUID type
ps.setString(2, "John");
ps.executeUpdate();
```

### Fix 3: Use native query with explicit casting for complex types

```java
@Query(value = "INSERT INTO events (event_date, metadata) " +
    "VALUES (CAST(:date AS TIMESTAMP), CAST(:json AS JSONB))", nativeQuery = true)
void insertEvent(@Param("date") String date, @Param("json") String json);
```

### Fix 4: Define parameters with explicit types in stored procedures

```sql
-- Instead of:
CREATE PROCEDURE update_price(product_id TEXT, price DECIMAL)
-- Use:
CREATE PROCEDURE update_price(product_id UUID, price NUMERIC(10,2))
```

### Fix 5: Handle type conversion in application layer

```java
public PreparedStatement prepareWithTypes(Connection conn, Order order) throws SQLException {
    PreparedStatement ps = conn.prepareStatement(
        "INSERT INTO orders (id, amount, currency) VALUES (?::uuid, ?::numeric, ?::varchar)");
    ps.setObject(1, order.getId(), Types.OTHER);       // UUID
    ps.setBigDecimal(2, order.getAmount());              // Numeric
    ps.setString(3, order.getCurrency().name());         // Varchar
    return ps;
}
```

## Prevention Tips

- Always match Java types to PostgreSQL column types in PreparedStatement parameters.
- Use `::type` casting in PostgreSQL queries when types do not align naturally.
- Use `setObject()` with appropriate `java.sql.Types` constants instead of `setString()` for non-text columns.
- Test type conversions against the actual PostgreSQL schema before deployment.

## Related Errors

- {{< relref "jdbc-conn" >}} — JDBC connection errors
- {{< relref "hibernate-type-error" >}} — Hibernate type mapping errors
- {{< relref "jpa-criteria-api" >}} — Criteria API type mismatch
