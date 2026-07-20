---
title: "[Solution] Java SQLTransactionRollbackException — Transaction Rolled Back Fix"
description: "Fix Java SQLTransactionRollbackException by handling rollback, retrying transaction, checking isolation level, and implementing compensating transactions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 427
---

# SQLTransactionRollbackException — Transaction Rolled Back Fix

A `SQLTransactionRollbackException` is thrown when an SQL transaction is rolled back due to a deadlock, serialization failure, or other condition that requires the transaction to be abandoned. This is a subclass of `SQLTransientException` because retrying may succeed.

## Description

`java.sql.SQLTransactionRollbackException` extends `SQLTransientException` and indicates that the current transaction was rolled back. The most common cause is a deadlock detected by the database, but it can also occur due to serialization failures, integrity constraint violations detected during commit, or statement-level rollback triggers.

Common message variants:

- `SQLTransactionRollbackException: Deadlock detected`
- `SQLTransactionRollbackException: Serialization failure`
- `SQLTransactionRollbackException: Transaction rollback due to statement abort`
- `SQLTransactionRollbackException: Could not complete validation`

## Common Causes

```java
// Cause 1: Deadlock — two transactions waiting on each other
// Transaction 1: UPDATE accounts SET balance = 100 WHERE id = 1
// Transaction 2: UPDATE accounts SET balance = 200 WHERE id = 2
// Transaction 1: UPDATE accounts SET balance = 100 WHERE id = 2  (waits for T2)
// Transaction 2: UPDATE accounts SET balance = 200 WHERE id = 1  (waits for T1)
// Database detects deadlock — rolls back one transaction: SQLTransactionRollbackException

// Cause 2: Serialization failure in SERIALIZABLE isolation
conn.setTransactionIsolation(Connection.TRANSACTION_SERIALIZABLE);
Statement stmt = conn.createStatement();
stmt.execute("INSERT INTO orders (id, total) VALUES (1, 100)");
// Another transaction inserted id=1 concurrently — serialization failure

// Cause 3: Statement timeout causing statement-level rollback
Statement stmt = conn.createStatement();
stmt.setQueryTimeout(5);
stmt.executeUpdate("UPDATE large_table SET col = 'value' WHERE complex_condition");
// Timeout causes statement abort — SQLTransactionRollbackException

// Cause 4: Savepoint rollback cascading
conn.setSavepoint();
// ... perform operations ...
conn.rollback(savepoint);  // Rolling back part of transaction
// Subsequent operations may encounter SQLTransactionRollbackException

// Cause 5: Trigger causing rollback
// A BEFORE INSERT trigger raises an exception in the database
PreparedStatement ps = conn.prepareStatement("INSERT INTO audit_log (msg) VALUES (?)");
ps.setString(1, "test");
ps.executeUpdate();  // Trigger aborts — SQLTransactionRollbackException
```

## Solutions

### Fix 1: Implement automatic retry for deadlocks

```java
public static <T> T executeWithDeadlockRetry(Connection conn, TransactionOperation<T> operation, int maxRetries)
        throws SQLException {
    for (int attempt = 0; attempt <= maxRetries; attempt++) {
        try {
            conn.setAutoCommit(false);
            T result = operation.execute(conn);
            conn.commit();
            return result;
        } catch (SQLTransactionRollbackException e) {
            conn.rollback();
            if (e.getMessage().toLowerCase().contains("deadlock") && attempt < maxRetries) {
                System.err.println("Deadlock detected, retrying (attempt " + (attempt + 1) + ")");
                Thread.sleep(1000L * (attempt + 1));  // Linear backoff for deadlocks
                continue;
            }
            throw e;
        }
    }
    throw new SQLException("Transaction failed after " + maxRetries + " retries");
}

@FunctionalInterface
interface TransactionOperation<T> {
    T execute(Connection conn) throws SQLException;
}

// Usage
Long orderId = executeWithDeadlockRetry(conn, c -> {
    PreparedStatement ps = c.prepareStatement(
        "INSERT INTO orders (customer_id, total) VALUES (?, ?)", Statement.RETURN_GENERATED_KEYS);
    ps.setInt(1, customerId);
    ps.setBigDecimal(2, total);
    ps.executeUpdate();
    ResultSet keys = ps.getGeneratedKeys();
    return keys.next() ? keys.getLong(1) : -1L;
}, 3);
```

### Fix 2: Use finer-grained locking to reduce deadlock probability

```java
// Instead of locking entire rows, use SELECT FOR UPDATE SKIP LOCKED
public static void safeTransfer(Connection conn, int fromId, int toId, BigDecimal amount)
        throws SQLException {
    conn.setAutoCommit(false);
    try {
        // Lock rows in a consistent order to prevent deadlock
        int firstId = Math.min(fromId, toId);
        int secondId = Math.max(fromId, toId);

        PreparedStatement lockStmt = conn.prepareStatement(
            "SELECT id, balance FROM accounts WHERE id = ? FOR UPDATE");
        lockStmt.setInt(1, firstId);
        lockStmt.executeQuery();
        lockStmt.setInt(1, secondId);
        lockStmt.executeQuery();

        // Now perform the transfer
        PreparedStatement debit = conn.prepareStatement(
            "UPDATE accounts SET balance = balance - ? WHERE id = ?");
        debit.setBigDecimal(1, amount);
        debit.setInt(2, fromId);
        debit.executeUpdate();

        PreparedStatement credit = conn.prepareStatement(
            "UPDATE accounts SET balance = balance + ? WHERE id = ?");
        credit.setBigDecimal(1, amount);
        credit.setInt(2, toId);
        credit.executeUpdate();

        conn.commit();
    } catch (SQLTransactionRollbackException e) {
        conn.rollback();
        throw e;
    }
}
```

### Fix 3: Implement compensating transactions for failed operations

```java
public class TransactionManager {
    public static <T> T executeWithCompensation(Connection conn, TransactionWithCompensation<T> operation)
            throws SQLException {
        List<Runnable> compensations = new ArrayList<>();

        try {
            conn.setAutoCommit(false);
            T result = operation.execute(conn, compensations);
            conn.commit();
            return result;
        } catch (SQLTransactionRollbackException e) {
            conn.rollback();
            // Execute compensating actions in reverse order
            for (int i = compensations.size() - 1; i >= 0; i--) {
                try {
                    compensations.get(i).run();
                } catch (Exception ex) {
                    System.err.println("Compensation failed: " + ex.getMessage());
                }
            }
            throw e;
        }
    }

    @FunctionalInterface
    interface TransactionWithCompensation<T> {
        T execute(Connection conn, List<Runnable> compensations) throws SQLException;
    }
}
```

### Fix 4: Check and set appropriate isolation level

```java
public static void configureIsolationLevel(Connection conn, boolean needsStrongConsistency)
        throws SQLException {
    if (needsStrongConsistency) {
        conn.setTransactionIsolation(Connection.TRANSACTION_SERIALIZABLE);
    } else {
        // Use READ_COMMITTED to reduce deadlock and serialization failures
        conn.setTransactionIsolation(Connection.TRANSACTION_READ_COMMITTED);
    }
    System.out.println("Transaction isolation: " + conn.getTransactionIsolation());
}
```

## Prevention Checklist

- Always wrap transactions in try-catch with rollback on failure.
- Lock rows in a consistent order across all transactions to prevent deadlocks.
- Use appropriate isolation levels — avoid SERIALIZABLE unless necessary.
- Implement retry logic with backoff for deadlock and serialization failures.
- Keep transactions short to minimize lock hold time.

## Related Errors

- [SQLTransientException](../sqltransientexception) — parent class for transient SQL failures.
- [SQLTimeoutException](../sqltimeoutexception) — query execution timed out.
- [SQLDeadlockException](../sqldeadlockexception) — database deadlock detected.
