---
title: "[Solution] UnexpectedRollbackException — JPA Transaction Fix"
description: "Fix UnexpectedRollbackException when a transaction is rolled back unexpectedly. Handle nested transaction propagation properly."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# UnexpectedRollbackException — JPA Transaction Fix

An `UnexpectedRollbackException` is thrown when a transaction is rolled back but the caller did not expect it. This typically happens with nested transactions where an inner transaction causes a rollback that affects the outer transaction.

## What This Error Means

Common message:

- `UnexpectedRollbackException: Transaction rolled back because it has been marked as rollback-only`

## Common Causes

```java
// Cause 1: Inner transaction marks outer as rollback-only
@Service
public class OrderService {

    @Transactional
    public void processOrder() {
        try {
            paymentService.charge(order);  // Throws exception
        } catch (Exception e) {
            log.error("Payment failed", e);
        }
        // When outer transaction commits, it finds rollback-only flag
        // and throws UnexpectedRollbackException
    }
}

// Cause 2: Exception in @Transactional method
@Transactional
public void updateStock() {
    // Database error occurs
    // Spring marks transaction as rollback-only
}
```

## How to Fix

### Fix 1: Use Propagation.NESTED

```java
@Service
public class OrderService {

    @Transactional
    public void processOrder() {
        try {
            paymentService.charge(order);
        } catch (Exception e) {
            log.error("Payment failed", e);
        }
    }
}

@Service
public class PaymentService {
    @Transactional(propagation = Propagation.NESTED)
    public void charge(Order order) {
        // Nested transaction — rollback doesn't affect outer
    }
}
```

### Fix 2: Rethrow the exception

```java
@Transactional
public void processOrder() {
    try {
        paymentService.charge(order);
    } catch (Exception e) {
        throw new OrderProcessingException("Payment failed", e);
    }
}
```

### Fix 3: Set noRollbackFor

```java
@Transactional(noRollbackFor = PaymentException.class)
public void processOrder() {
    try {
        paymentService.charge(order);
    } catch (PaymentException e) {
        log.warn("Payment failed, continuing", e);
    }
}
```

## Related Errors

- {{< relref "jpa-constraint" >}} — ConstraintViolationException
- {{< relref "jpa-entity" >}} — EntityNotFoundException
- {{< relref "sql-exception" >}} — SQL exception
