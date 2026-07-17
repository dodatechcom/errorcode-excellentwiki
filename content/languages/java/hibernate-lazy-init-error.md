---
title: "[Solution] Hibernate LazyInitializationException Fix"
description: "Fix Hibernate LazyInitializationException when accessing lazy-loaded entities outside session. Use fetch joins, Open Session in View, or DTOs."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Hibernate LazyInitializationException Fix

A `LazyInitializationException` is thrown when Hibernate attempts to initialize a lazy-loaded proxy or collection outside the bounds of an active session.

## What This Error Means

Common messages:

- `LazyInitializationException: could not initialize proxy - no Session`
- `LazyInitializationException: failed to lazily initialize a collection`

Hibernate proxies and collections are only loaded within an open Session. Once the Session closes (typically at the end of a transaction), accessing unloaded properties throws this exception.

## Common Causes

```java
// Cause 1: Accessing lazy collection after transaction commits
@Transactional
public List<Order> getOrders() {
    List<Order> orders = orderRepository.findAll();
    return orders;  // Session closes
}

// In caller — outside transaction:
List<Order> orders = getOrders();
orders.get(0).getItems().size();  // LazyInitializationException

// Cause 2: N+1 query problem without fetching
@Entity
public class User {
    @OneToMany(fetch = FetchType.LAZY)
    private List<Order> orders;
}

// Accessing orders in separate method without session

// Cause 3: Jackson serializing lazy proxy
// @RestController returns entity with lazy fields
@GetMapping("/users/{id}")
public User getUser(@PathVariable Long id) {
    return userRepository.findById(id).orElseThrow();
    // Jackson tries to access lazy collection
}
```

## How to Fix

### Fix 1: Use @Transactional on the access method

```java
@Transactional(readOnly = true)
public User getUserWithOrders(Long userId) {
    User user = userRepository.findById(userId).orElseThrow();
    user.getOrders().size(); // Force initialization within transaction
    return user;
}
```

### Fix 2: Use JOIN FETCH in JPQL

```java
@Query("SELECT u FROM User u JOIN FETCH u.orders WHERE u.id = :id")
Optional<User> findByIdWithOrders(@Param("id") Long id);
```

### Fix 3: Use EntityGraph

```java
@EntityGraph(attributePaths = {"orders", "orders.items"})
@Query("SELECT u FROM User u WHERE u.id = :id")
Optional<User> findByIdWithOrders(@Param("id") Long id);
```

### Fix 4: Return DTO instead of entity

```java
@Query("SELECT new com.example.UserDTO(u.name, u.email) FROM User u WHERE u.id = :id")
Optional<UserDTO> findUserDtoById(@Param("id") Long id);
```

### Fix 5: Use @Column(insertable = false, updatable = false) for read-only joins

```java
@Entity
public class UserSummary {
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "order_id", insertable = false, updatable = false)
    private Order lastOrder;
}
```

### Fix 6: Configure Open Session in View filter

```java
// application.properties
spring.jpa.open-in-view=true  // Keeps session open during view rendering
```

## Related Errors

- {{< relref "hibernate-mapping" >}} — Hibernate mapping configuration error.
- {{< relref "hibernate-detached" >}} — Hibernate detached entity error.
