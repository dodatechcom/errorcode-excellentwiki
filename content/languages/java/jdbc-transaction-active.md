---
title: "[Solution] JDBC Operation Not Allowed While Transaction Active"
description: "Fix java.sql.SQLException Operation not allowed while a transaction is active. Manage autocommit and transaction boundaries correctly."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Operation Not Allowed While a Transaction Is Active

A `SQLException` with message `Operation not allowed while a transaction is active` occurs when you attempt to change the autocommit mode, set a savepoint, or perform certain connection operations while a transaction is already in progress.

## What This Error Means

JDBC connections operate in one of two modes: autocommit (each statement is its own transaction) or manual transaction control. Certain operations like changing `setAutoCommit()` are not permitted while a transaction is actively running.

## Common Causes

```java
// Cause 1: Changing autocommit mid-transaction
Connection conn = dataSource.getConnection();
conn.setAutoCommit(false);  // Transaction begins
conn.prepareStatement("INSERT INTO orders ...").executeUpdate();
conn.setAutoCommit(true);   // SQLException! Transaction still active

// Cause 2: Nested transaction control in frameworks
// Spring calls setAutoCommit while JTA transaction is active

// Cause 3: Database driver restriction
// Some drivers (e.g., MySQL) throw if you call setAutoCommit(false)
// when autocommit is already false
conn.setAutoCommit(false);
conn.setAutoCommit(false);  // May throw on certain drivers
```

## How to Fix

### Fix 1: Check autocommit state before changing it

```java
if (conn.getAutoCommit() != desiredAutoCommit) {
    conn.setAutoCommit(desiredAutoCommit);
}
```

### Fix 2: Use proper transaction boundaries

```java
// Correct pattern: set autocommit once, then commit/rollback
Connection conn = dataSource.getConnection();
try {
    conn.setAutoCommit(false);
    PreparedStatement ps = conn.prepareStatement("INSERT INTO orders ...");
    ps.executeUpdate();
    conn.commit();
} catch (SQLException e) {
    conn.rollback();
    throw e;
} finally {
    conn.setAutoCommit(true);
    conn.close();
}
```

### Fix 3: Let the framework manage transactions

```java
@Transactional
public void createOrder(Order order) {
    // Spring manages autocommit and transaction boundaries
    orderRepository.save(order);
    inventoryService.reserve(order.getItems());
    // Automatic commit on success, rollback on exception
}
```

### Fix 4: Use savepoints for nested operations

```java
Connection conn = dataSource.getConnection();
conn.setAutoCommit(false);
Savepoint savepoint = conn.setSavepoint("after_order");
try {
    conn.prepareStatement("UPDATE inventory ...").executeUpdate();
    conn.commit();
} catch (SQLException e) {
    conn.rollback(savepoint);  // Roll back to savepoint, not full transaction
}
```

## Prevention Tips

- Avoid calling `setAutoCommit()` inside business logic; configure it at pool setup.
- Use framework-managed transactions (`@Transactional` in Spring) to avoid manual autocommit handling.
- Set autocommit once during connection initialization and rely on commit/rollback.

## Related Errors

- {{< relref "jdbc-conn" >}} — Cannot establish JDBC connection
- {{< relref "jdbc-savepoint" >}} — Savepoint creation failed
- {{< relref "jpa-optimistic-lock" >}} — Optimistic lock exception
