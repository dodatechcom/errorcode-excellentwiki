---
title: "[Solution] Java RollbackException — Transaction Rollback Fix"
description: "Fix javax.transaction.RollbackException by checking transaction status, handling EJB exceptions properly, and verifying transaction boundaries."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# RollbackException — Transaction Rollback Fix

A `RollbackException` is thrown when a transaction is rolled back by the container, usually due to an exception occurring within the transaction boundary. The transaction was already marked for rollback when the code attempted to commit.

## Description

RollbackException is a checked exception from the `javax.transaction` package. It indicates that the transaction manager decided to roll back the transaction before or during the commit phase. This typically happens when:

- An application exception was thrown within a `REQUIRED` transaction.
- The container detected a system exception.
- Another resource participating in the transaction failed.

Common message variants include:

- `RollbackException: Transaction rolled back because it has been marked as rollback-only`
- `RollbackException: Unable to commit transaction`
- `RollbackException: Transaction was rolled back`

## Common Causes

```java
// Cause 1: Setting rollback-only from inside a transaction
@TransactionAttribute(TransactionAttributeType.REQUIRED)
public void processOrder() {
    context.setRollbackOnly(); // Marks transaction as rollback-only
    // Later attempt to commit throws RollbackException
}

// Cause 2: Exception thrown in REQUIRED transaction
@TransactionAttribute(TransactionAttributeType.REQUIRED)
public void saveUser() {
    em.persist(user);
    throw new RuntimeException("Validation failed"); // Container rolls back
}

// Cause 3: HeuristicMixedException during multi-resource commit
// Resource 1 commits, Resource 2 throws — partial rollback
```

## Solutions

### Fix 1: Use REQUIRED_NEW to isolate transactions

```java
@TransactionAttribute(TransactionAttributeType.REQUIRES_NEW)
public void auditLog(AuditEntry entry) {
    // Runs in a separate transaction — won't affect caller's transaction
    em.persist(entry);
}

@TransactionAttribute(TransactionAttributeType.REQUIRED)
public void processOrder(Order order) {
    em.persist(order);
    auditLog(new AuditEntry("ORDER_CREATED", order.getId()));
    // If auditLog fails, processOrder transaction is not affected
}
```

### Fix 2: Handle rollback-only status properly

```java
@TransactionAttribute(TransactionAttributeType.REQUIRED)
public void transferFunds(Account from, Account to, BigDecimal amount) {
    try {
        from.setBalance(from.getBalance().subtract(amount));
        to.setBalance(to.getBalance().add(amount));
        em.merge(from);
        em.merge(to);
    } catch (Exception e) {
        // Don't set rollback-only — just throw or let exception propagate
        throw new EJBException("Transfer failed", e);
    }
    // Transaction commits normally if no exception
}
```

### Fix 3: Use NOT_SUPPORTED for non-transactional work

```java
@TransactionAttribute(TransactionAttributeType.NOT_SUPPORTED)
public void generateReport() {
    // Long-running read-only operation — no transaction
    // Won't interfere with caller's transaction
    List<User> users = em.createQuery("SELECT u FROM User u").getResultList();
    // Process without holding a transaction open
}
```

### Fix 4: Catch and rethrow as application exception

```java
@ApplicationException(rollback = false) // Prevents rollback
public class ValidationException extends Exception {
    public ValidationException(String message) {
        super(message);
    }
}

@TransactionAttribute(TransactionAttributeType.REQUIRED)
public void updateUser(User user) throws ValidationException {
    if (user.getName() == null) {
        throw new ValidationException("Name required");
        // Transaction is NOT rolled back — can be handled by caller
    }
    em.merge(user);
}
```

## Prevention Checklist

- Avoid calling `setRollbackOnly()` unless absolutely necessary.
- Use `REQUIRES_NEW` to isolate audit/logging from business transactions.
- Mark non-critical exceptions with `@ApplicationException(rollback = false)`.
- Keep transaction scopes as small as possible.
- Test transaction rollback behavior in integration tests.

## Related Errors

- [SystemException](../systemexception) — Transaction manager system error.
- [HeuristicMixedException](../heuristicmixedexception) — Mixed commit/rollback across resources.
- [HeuristicCompletionException](../heuristiccompletionexception) — Heuristic decision completed.
