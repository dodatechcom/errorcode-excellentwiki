---
title: "[Solution] JPA OptimisticLockException — Row Updated by Another Transaction"
description: "Fix javax.persistence.OptimisticLockException Row was updated or deleted by another transaction. Implement optimistic locking."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# OptimisticLockException — Row Updated by Another Transaction

An `OptimisticLockException` with message `Row was updated or deleted by another transaction` occurs when JPA's optimistic locking mechanism detects that the entity was modified by another transaction between the time it was read and the time the current transaction attempts to update it.

## What This Error Means

Optimistic locking uses a version column (`@Version`) to detect concurrent modifications. When entity A is loaded with version 1, and entity B updates the same row (incrementing version to 2), entity A's attempt to update will fail because the version no longer matches.

## Common Causes

```java
// Cause 1: Two users editing the same record simultaneously
@Entity
public class Product {
    @Id
    private Long id;
    @Version
    private Long version;
    private String name;
    private BigDecimal price;
}

// User A loads product (version=1)
// User B loads product (version=1)
// User B saves (version becomes 2)
// User A saves — OptimisticLockException (version mismatch)

// Cause 2: Stale entity used after long processing
Product product = productRepository.findById(1L).get();
// Long processing...
Thread.sleep(60_000);
product.setPrice(newPrice);
productRepository.save(product);  // May fail if another thread updated it

// Cause 3: Multiple services updating same entity
@Service
public class InventoryService {
    @Transactional
    public void decrementStock(Product product) {
        product.setStock(product.getStock() - 1);
        productRepository.save(product);
    }
}

@Service
public class PriceService {
    @Transactional
    public void updatePrice(Product product, BigDecimal newPrice) {
        product.setPrice(newPrice);
        productRepository.save(product);  // Conflict if InventoryService updated first
    }
}
```

## How to Fix

### Fix 1: Catch and retry on OptimisticLockException

```java
@Transactional
public Product updateProductWithRetry(Long productId, String newName) {
    int maxRetries = 3;
    for (int attempt = 1; attempt <= maxRetries; attempt++) {
        try {
            Product product = productRepository.findById(productId).orElseThrow();
            product.setName(newName);
            return productRepository.save(product);
        } catch (OptimisticLockException e) {
            if (attempt == maxRetries) {
                throw new ConcurrencyException("Failed to update after " + maxRetries + " attempts", e);
            }
            log.warn("Optimistic lock conflict on attempt {}, retrying...", attempt);
        }
    }
    throw new IllegalStateException("Unreachable code");
}
```

### Fix 2: Use @Retryable from Spring Retry

```java
@Service
public class ProductService {
    @Retryable(
        value = OptimisticLockException.class,
        maxAttempts = 3,
        backoff = @Backoff(delay = 100)
    )
    @Transactional
    public Product updateProduct(Long id, String name) {
        Product product = productRepository.findById(id).orElseThrow();
        product.setName(name);
        return productRepository.save(product);
    }

    @Recover
    public Product recoverUpdate(OptimisticLockException e, Long id, String name) {
        throw new ConcurrencyException("Unable to update product " + id + " after retries");
    }
}
```

### Fix 3: Use version-aware updates

```java
@Modifying
@Query("UPDATE Product p SET p.name = :name, p.version = p.version + 1 WHERE p.id = :id AND p.version = :version")
int updateProductName(@Param("id") Long id, @Param("name") String name, @Param("version") Long version);

// Check return value — 0 means version conflict
int updated = productRepository.updateProductName(id, newName, currentVersion);
if (updated == 0) {
    throw new OptimisticLockException("Product was modified by another user");
}
```

### Fix 4: Display version to user for manual conflict resolution

```java
@GetMapping("/products/{id}")
public ResponseEntity<ProductDto> getProduct(@PathVariable Long id) {
    Product product = productRepository.findById(id).orElseThrow();
    ProductDto dto = toDto(product);
    return ResponseEntity.ok()
        .header("ETag", String.valueOf(product.getVersion()))
        .body(dto);
}

@PutMapping("/products/{id}")
public ResponseEntity<ProductDto> updateProduct(
        @PathVariable Long id,
        @RequestBody ProductDto dto,
        @RequestHeader("If-Match") Long clientVersion) {
    Product product = productRepository.findById(id).orElseThrow();
    if (!product.getVersion().equals(clientVersion)) {
        return ResponseEntity.status(409).build();  // Conflict
    }
    product.setName(dto.getName());
    productRepository.save(product);
    return ResponseEntity.ok(toDto(product));
}
```

## Prevention Tips

- Always use `@Version` on entities that may be concurrently modified.
- Implement retry logic for optimistic lock failures in high-concurrency systems.
- Use ETags or version fields in REST APIs to prevent lost updates.
- Keep transactions short to reduce the window for concurrent modifications.

## Related Errors

- {{< relref "jpa-entity-exists" >}} — EntityExistsException
- {{< relref "jpa-detached-entity" >}} — Detached entity errors
- {{< relref "jpa-constraint" >}} — ConstraintViolationException
