---
title: "[Solution] JDBC Savepoint Creation Failed"
description: "Fix java.sql.SQLException Savepoint creation failed. Handle savepoint errors in JDBC transaction management."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Savepoint Creation Failed

A `SQLException` with message `Savepoint creation failed` occurs when the JDBC driver or database is unable to create a savepoint within the current transaction. This can happen due to driver limitations, transaction state issues, or resource exhaustion.

## What This Error Means

Savepoints allow partial rollback within a transaction. When creation fails, it typically indicates the driver does not support savepoints, the connection is in autocommit mode, or the database has reached its savepoint limit.

## Common Causes

```java
// Cause 1: Trying to create savepoint in autocommit mode
Connection conn = dataSource.getConnection();
// autocommit is true by default
Savepoint sp = conn.setSavepoint("checkpoint");  // SQLException

// Cause 2: Driver or database does not support savepoints
Connection conn = DriverManager.getConnection("jdbc:h2:mem:test");
// Some embedded databases have limited savepoint support

// Cause 3: Savepoint name conflict or resource limit
Connection conn = dataSource.getConnection();
conn.setAutoCommit(false);
for (int i = 0; i < 10000; i++) {
    conn.setSavepoint("sp_" + i);  // May hit internal limits
}
```

## How to Fix

### Fix 1: Ensure autocommit is disabled before creating savepoints

```java
Connection conn = dataSource.getConnection();
try {
    conn.setAutoCommit(false);  // Required for savepoints
    Savepoint sp = conn.setSavepoint("after_insert");
    try {
        conn.prepareStatement("INSERT INTO orders ...").executeUpdate();
        // Do more work
        conn.commit();
    } catch (SQLException e) {
        conn.rollback(sp);  // Roll back to savepoint
        log.warn("Rolled back to savepoint after_insert", e);
        conn.commit();      // Commit what succeeded before savepoint
    }
} finally {
    conn.setAutoCommit(true);
    conn.close();
}
```

### Fix 2: Use nested transaction patterns without savepoints

```java
@Transactional
public void processOrder(Order order) {
    try {
        orderService.createOrder(order);      // First operation
    } catch (DuplicateOrderException e) {
        log.warn("Order already exists, skipping creation");
    }
    // Continue with second operation regardless
    notificationService.sendConfirmation(order);
}
```

### Fix 3: Implement manual savepoint tracking

```java
public class ManualSavepoint<T> {
    private final T state;
    private final int point;

    public ManualSavepoint(T state, int point) {
        this.state = state;
        this.point = point;
    }

    public T getState() { return state; }
    public int getPoint() { return point; }
}

// Usage
List<String> log = new ArrayList<>();
ManualSavepoint<List<String>> sp = new ManualSavepoint<>(new ArrayList<>(log), log.size());
try {
    log.add("step1");
    doRiskyOperation();
    log.add("step2");
} catch (Exception e) {
    log = new ArrayList<>(sp.getState());  // Restore state
}
```

### Fix 4: Use Spring's transaction templates for nested operations

```java
TransactionTemplate outerTemplate = new TransactionTemplate(transactionManager);
TransactionTemplate innerTemplate = new TransactionTemplate(transactionManager);
innerTemplate.setPropagationBehavior(TransactionDefinition.PROPAGATION_REQUIRES_NEW);

outerTemplate.execute(status -> {
    // Outer transaction
    repository.save(entity);
    innerTemplate.execute(innerStatus -> {
        // Inner transaction (acts like a savepoint)
        auditService.logAction("entity created");
        return null;
    });
    return null;
});
```

## Prevention Tips

- Always disable autocommit before creating savepoints.
- Prefer Spring `@Transactional` with `PROPAGATION_NESTED` over manual savepoints.
- Test savepoint behavior with your specific database driver.
- Keep savepoint usage minimal; prefer commit/rollback at transaction boundaries.

## Related Errors

- {{< relref "jdbc-transaction-active" >}} — Transaction active error
- {{< relref "jdbc-conn" >}} — Connection errors
- {{< relref "jpa-optimistic-lock" >}} — Optimistic lock failures
