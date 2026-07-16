---
title: "Transaction error"
description: "Spring throws UnexpectedRollbackException or TransactionSystemException when a transaction fails"
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["transaction", "@transactional", "rollback", "jpa"]
weight: 5
---

This error occurs when a Spring-managed transaction fails to commit, rolls back unexpectedly, or encounters a constraint violation during the commit phase. Transactions annotated with `@Transactional` automatically roll back on unchecked exceptions.

## Common Causes

- Database constraint violation during commit (e.g. unique constraint)
- `@Transactional` method catching exceptions before Spring can roll back
- Optimistic locking failure (`@Version` conflict)
- Self-invocation (calling a `@Transactional` method from within the same class)

## How to Fix

1. Do not catch exceptions in `@Transactional` methods:

```java
// WRONG — prevents rollback
@Transactional
public void transferMoney(Long from, Long to, BigDecimal amount) {
    try {
        debit(from, amount);
        credit(to, amount);
    } catch (Exception e) {
        log.error("Transfer failed", e); // exception swallowed — no rollback
    }
}

// CORRECT — let exceptions propagate
@Transactional
public void transferMoney(Long from, Long to, BigDecimal amount) {
    debit(from, amount);
    credit(to, amount);
}
```

2. Use `propagation` and `readOnly` correctly:

```java
@Transactional(readOnly = true)
public List<User> getAllUsers() {
    return userRepository.findAll();
}

@Transactional(propagation = Propagation.REQUIRES_NEW)
public void createLog(LogEntry entry) {
    logRepository.save(entry);
}
```

3. Avoid self-invocation — inject the proxy or use AopContext:

```java
@Service
public class UserService {
    @Autowired
    private UserRepository userRepository;

    public void createUserWithProfile(UserDto dto) {
        // WRONG — no transaction
        // this.saveUser(dto);

        // CORRECT — call through the proxy
        AopContext.currentProxy();
    }
}
```

## Examples

```java
@Transactional
public void updateInventory(Long productId, int quantity) {
    Product p = productRepository.findById(productId).orElseThrow();
    p.setStock(p.getStock() - quantity);
    productRepository.save(p);
    // Unique constraint on another table violated during commit
}
```

```text
org.springframework.transaction.UnexpectedRollbackException:
Transaction silently rolled back because it has been marked as rollback-only
```

## Related Errors

- [HttpClientErrorException]({{< relref "/frameworks/spring/http-error" >}})
