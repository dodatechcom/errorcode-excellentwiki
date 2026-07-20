---
title: "[Solution] Java BatchUpdateException — JDBC Batch Failure Fix"
description: "Fix Java BatchUpdateException by checking SQL syntax, handling constraint violations, using savepoints, and retrying individual statements."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# BatchUpdateException — JDBC Batch Failure Fix

A `BatchUpdateException` is thrown when a batch update fails during execution. This exception contains update counts for any statements that executed successfully before the failure, allowing partial success detection.

## Description

`java.sql.BatchUpdateException` extends `SQLException` and provides:

- The update count for each successfully executed statement in the batch
- The index of the statement that failed (in some drivers)
- The underlying SQL exception as the cause

Common message variants:

- `java.sql.BatchUpdateException: Batch entry N was aborted`
- `BatchUpdateException: Could not execute batch statement`
- `Batch entry N is invalid: statement count mismatch`

The `getUpdateCounts()` method returns an array of integers showing how many rows were affected by each statement before the failure.

## Common Causes

```java
// Cause 1: Constraint violation in one statement of the batch
PreparedStatement ps = conn.prepareStatement("INSERT INTO users (id, name) VALUES (?, ?)");
ps.setInt(1, 1);
ps.setString(2, "Alice");
ps.addBatch();

ps.setInt(1, 1);  // Duplicate key — violates unique constraint
ps.setString(2, "Bob");
ps.addBatch();

int[] counts = ps.executeBatch();  // BatchUpdateException on second statement

// Cause 2: SQL syntax error in one batch statement
Statement stmt = conn.createStatement();
stmt.addBatch("INSERT INTO users (id, name) VALUES (1, 'Alice')");
stmt.addBatch("INSERT INTO users (id, name) VALUES (2, 'Bob')");
stmt.addBatch("INSERT INTO userss (id, name) VALUES (3, 'Charlie')");  // Typo: userss
int[] counts = stmt.executeBatch();  // BatchUpdateException

// Cause 3: Data type mismatch
ps.setInt(1, 1);
ps.setString(2, "Alice");
ps.addBatch();

ps.setString(1, "not a number");  // Type mismatch
ps.setString(2, "Bob");
ps.addBatch();

// Cause 4: Connection lost during batch execution
// Large batch on a connection that times out or drops
for (int i = 0; i < 10000; i++) {
    ps.setInt(1, i);
    ps.setString(2, "User" + i);
    ps.addBatch();
}
int[] counts = ps.executeBatch();  // May fail partway through
```

## Solutions

### Fix 1: Use try-catch and inspect update counts

```java
try {
    int[] updateCounts = statement.executeBatch();
    System.out.println("All " + updateCounts.length + " statements executed");
} catch (BatchUpdateException e) {
    int[] updateCounts = e.getUpdateCounts();
    System.out.println("Failed at statement " + updateCounts.length);
    for (int i = 0; i < updateCounts.length; i++) {
        System.out.println("Statement " + i + ": " + updateCounts[i]);
    }
}
```

### Fix 2: Use savepoints for partial rollback

```java
conn.setAutoCommit(false);
Savepoint savepoint = null;

try {
    savepoint = conn.setSavepoint();
    PreparedStatement ps = conn.prepareStatement("INSERT INTO users (id, name) VALUES (?, ?)");
    ps.setInt(1, 1);
    ps.setString(2, "Alice");
    ps.addBatch();
    ps.setInt(1, 2);
    ps.setString(2, "Bob");
    ps.addBatch();
    ps.executeBatch();
    conn.commit();
} catch (BatchUpdateException e) {
    if (savepoint != null) {
        conn.rollback(savepoint);
    }
    System.err.println("Batch failed: " + e.getMessage());
}
```

### Fix 3: Validate statements before adding to batch

```java
public static void executeBatchWithValidation(Connection conn, List<String[]> records)
        throws SQLException {
    try (PreparedStatement ps = conn.prepareStatement(
            "INSERT INTO users (id, name) VALUES (?, ?)")) {
        for (String[] record : records) {
            int id = Integer.parseInt(record[0]);
            String name = record[1];

            if (name == null || name.isEmpty()) {
                throw new IllegalArgumentException("Name cannot be empty for id: " + id);
            }

            ps.setInt(1, id);
            ps.setString(2, name);
            ps.addBatch();
        }
        ps.executeBatch();
    }
}
```

### Fix 4: Retry individual statements on failure

```java
public static void executeWithRetry(Connection conn, List<String> statements)
        throws SQLException {
    for (String sql : statements) {
        int retries = 3;
        while (retries > 0) {
            try (Statement stmt = conn.createStatement()) {
                stmt.execute(sql);
                break;
            } catch (SQLException e) {
                retries--;
                if (retries == 0) {
                    System.err.println("Failed after retries: " + sql);
                    throw e;
                }
                Thread.sleep(1000);
            }
        }
    }
}
```

## Prevention Checklist

- Always inspect `getUpdateCounts()` after a `BatchUpdateException` to determine partial success.
- Use transactions with savepoints to enable partial rollback.
- Validate all batch parameters before calling `executeBatch()`.
- Consider smaller batch sizes for better error isolation.
- Use `addBatch()` and `executeBatch()` within the same transaction for atomicity.

## Related Errors

- [SQLException](../sql-exception) — parent class for SQL failures.
- [SQLIntegrityConstraintViolationException](../sqlintegrityconstraintviolationexception) — constraint violation in SQL.
- [SQLSyntaxErrorException](../sqlsyntaxerrorsexception) — SQL syntax error.
