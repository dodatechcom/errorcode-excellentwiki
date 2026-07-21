---
title: "[Solution] Spring Transaction Management Error -- How to Fix"
description: "Fix Spring transaction management errors. Resolve transaction rollback, propagation, and isolation issues in Spring."
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

A Spring transaction management error occurs when transactions fail to start, commit, or roll back correctly. Spring provides declarative and programmatic transaction management, but misconfiguration can lead to data inconsistency.

## Why It Happens

Spring uses AOP proxies for transaction management. Errors occur when `@Transactional` is on a private method, when the method is called from within the same class (self-invocation), when exception handling swallows exceptions that should trigger rollback, when propagation settings are incorrect, or when the database doesn't support the required isolation level.

## Common Error Messages

```
UnexpectedRollbackException: Transaction rolled back because it has been marked as rollback-only
```

```
TransactionSystemException: Could not commit JPA transaction
```

```
IllegalTransactionStateException: Transaction is completed
```

```
OptimisticLockingFailureException: Entity was updated since loading
```

## How to Fix It

### 1. Use @Transactional Correctly

Apply the annotation to public methods in Spring beans:

```java
@Service
public class OrderService {

    // Correct: public method in a Spring bean
    @Transactional
    public Order createOrder(CreateOrderRequest request) {
        Order order = new Order(request);
        orderRepository.save(order);
        inventoryService.reserve(order.getItems());
        return order;
    }

    // Wrong: private method -- proxy won't intercept
    @Transactional
    private void internalMethod() { }

    // Wrong: self-invocation -- bypasses proxy
    public void outerMethod() {
        this.createOrder(new CreateOrderRequest());  // No transaction!
    }
}
```

### 2. Configure Rollback Rules

Specify when transactions should roll back:

```java
@Service
public class PaymentService {

    // Rollback on all exceptions (default behavior)
    @Transactional
    public void processPayment(Payment payment) {
        paymentGateway.charge(payment);
        payment.setStatus(PaymentStatus.COMPLETED);
        paymentRepository.save(payment);
    }

    // Rollback only on specific exceptions
    @Transactional(rollbackFor = PaymentException.class)
    public void refundPayment(Long paymentId) {
        Payment payment = paymentRepository.findById(paymentId)
            .orElseThrow(() -> new PaymentException("Payment not found"));
        paymentGateway.refund(payment);
    }

    // Don't rollback on specific exceptions
    @Transactional(noRollbackFor = ValidationException.class)
    public void updateWithValidation(Data data) {
        try {
            validate(data);
        } catch (ValidationException e) {
            log.warn("Validation failed: {}", e.getMessage());
            // Continue -- don't rollback
        }
        dataRepository.save(data);
    }
}
```

### 3. Set Propagation and Isolation Levels

Configure transaction behavior:

```java
@Service
public class InventoryService {

    // Requires new transaction (suspend current)
    @Transactional(propagation = Propagation.REQUIRES_NEW)
    public void auditStockChange(StockChange change) {
        auditRepository.save(change);
    }

    // Supports existing transaction
    @Transactional(propagation = Propagation.SUPPORTS)
    public List<Stock> getCurrentStock() {
        return stockRepository.findAll();
    }

    // Never run in a transaction
    @Transactional(propagation = Propagation.NOT_SUPPORTED)
    public String generateReport() {
        // This runs without a transaction
        return reportGenerator.generate();
    }

    // Isolation level for concurrent updates
    @Transactional(isolation = Isolation.SERIALIZABLE)
    public void decrementStock(Long productId, int quantity) {
        Product product = productRepository.findById(productId)
            .orElseThrow();
        if (product.getStock() >= quantity) {
            product.setStock(product.getStock() - quantity);
            productRepository.save(product);
        }
    }
}
```

### 4. Handle Programmatic Transactions

Use TransactionTemplate for complex scenarios:

```java
@Service
public class BatchService {

    private final TransactionTemplate transactionTemplate;

    public BatchService(PlatformTransactionManager transactionManager) {
        this.transactionTemplate = new TransactionTemplate(transactionManager);
    }

    public void processBatch(List<Item> items) {
        for (Item item : items) {
            transactionTemplate.execute(status -> {
                try {
                    processItem(item);
                    return null;
                } catch (Exception e) {
                    status.setRollbackOnly();
                    log.error("Failed to process item {}: {}", item.getId(), e.getMessage());
                    return null;
                }
            });
        }
    }
}
```

## Common Scenarios

**Scenario 1: Transaction doesn't roll back.**
Check that the exception is unchecked (RuntimeException). Checked exceptions don't trigger rollback by default. Use `rollbackFor = Exception.class` if needed.

**Scenario 2: `UnexpectedRollbackException` on method call.**
An inner transaction marked the outer transaction as rollback-only, but the outer transaction tried to commit. Use `Propagation.REQUIRES_NEW` or fix exception handling.

**Scenario 3: `@Transactional` ignored.**
This happens when the method is private, final, or called from the same class. Ensure the method is public and called through the Spring proxy.

## Prevent It

1. **Always catch exceptions explicitly** in `@Transactional` methods rather than relying on default rollback behavior.

2. **Use `@Transactional(readOnly = true)`** for read-only operations to optimize database performance.

3. **Test transaction boundaries** by verifying that database changes are rolled back on exceptions.
