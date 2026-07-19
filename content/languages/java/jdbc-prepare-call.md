---
title: "[Solution] JDBC prepareCall Failed — Procedure Not Found"
description: "Fix java.sql.SQLSyntaxErrorException procedure not found when using prepareCall. Resolve stored procedure access issues."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# prepareCall Failed — Procedure Not Found

A `SQLSyntaxErrorException` with message `procedure not found` occurs when `Connection.prepareCall()` references a stored procedure that does not exist in the database, is in the wrong schema, or is called with incorrect syntax.

## What This Error Means

`prepareCall()` creates a `CallableStatement` to execute stored procedures. The procedure name must match exactly (including schema, case sensitivity, and parameter types) as registered in the database.

## Common Causes

```java
// Cause 1: Procedure name wrong or in wrong schema
CallableStatement cs = conn.prepareCall("{call my_procedure(?)}");
// Actual procedure is in schema "public": public.my_procedure

// Cause 2: Case sensitivity mismatch
CallableStatement cs = conn.prepareCall("{call GetUserById(?)}");
// PostgreSQL stores as lowercase: getuserbyid

// Cause 3: Procedure does not exist (typo or not deployed)
CallableStatement cs = conn.prepareCall("{call calculate_tax(?)}");
// Procedure named "calculate_taxes" (plural)

// Cause 4: Wrong parameter count or types
CallableStatement cs = conn.prepareCall("{call update_status(?, ?)}");
// Procedure only accepts one parameter
```

## How to Fix

### Fix 1: Verify procedure exists using database metadata

```java
DatabaseMetaData meta = conn.getMetaData();
ResultSet rs = meta.getProcedures(null, null, "my_procedure");
if (!rs.next()) {
    throw new SQLException("Procedure 'my_procedure' not found in database");
}
```

### Fix 2: Use fully qualified procedure name with schema

```java
// PostgreSQL
CallableStatement cs = conn.prepareCall("{call public.my_procedure(?)}");

// SQL Server
CallableStatement cs = conn.prepareCall("{call dbo.my_procedure(?)}");

// MySQL
CallableStatement cs = conn.prepareCall("{call mydb.my_procedure(?)}");
```

### Fix 3: Handle case sensitivity for PostgreSQL

```java
// PostgreSQL lowercases unquoted identifiers
// If procedure was created as "GetUserById", call it quoted:
CallableStatement cs = conn.prepareCall("{call \"GetUserById\"(?)}");

// Or create with lowercase name:
// CREATE PROCEDURE get_user_by_id(IN p_id BIGINT) ...
CallableStatement cs = conn.prepareCall("{call get_user_by_id(?)}");
```

### Fix 4: List available procedures for debugging

```java
DatabaseMetaData meta = conn.getMetaData();
ResultSet rs = meta.getProcedures(null, "public", "%");
while (rs.next()) {
    System.out.println("Procedure: " + rs.getString("PROCEDURE_NAME"));
    System.out.println("Schema: " + rs.getString("PROCEDURE_SCHEM"));
    System.out.println("Remarks: " + rs.getString("REMARKS"));
}
```

## Prevention Tips

- Always verify stored procedures exist before deploying code that calls them.
- Use database migration tools (Flyway, Liquibase) to manage procedure definitions.
- Test stored procedure calls against a staging database before production.
- Prefer JPA/HQL over native stored procedures when possible.

## Related Errors

- {{< relref "jdbc-conn" >}} — JDBC connection errors
- {{< relref "hibernate-query-syntax" >}} — HQL syntax errors
- {{< relref "jdbc-types-mismatch" >}} — SQL type mismatch
