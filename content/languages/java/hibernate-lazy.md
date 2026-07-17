---
title: "[Solution] LazyInitializationException — Hibernate Lazy Loading Fix"
description: "Fix Hibernate LazyInitializationException when accessing uninitialized lazy collections outside a session. Use JOIN FETCH, @EntityGraph, or OpenSessionInView."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# LazyInitializationException — Hibernate Lazy Loading Fix

A `LazyInitializationException` is thrown when you try to access a lazily loaded collection or proxy outside of an active Hibernate Session. Hibernate uses proxies for lazy loading, and once the session is closed, the proxy cannot fetch data from the database.

## What This Error Means

The exception occurs when code attempts to access a lazy property after the persistence context has ended. Common message:

- `could not initialize proxy - no Session`

## Common Causes

```java
// Cause 1: Accessing lazy collection outside transaction
@Entity
public class User {
    @OneToMany(fetch = FetchType.LAZY)
    private List<Order> orders;
}

// In service
User user = userRepository.findById(1L).get();  // Session closes
List<Order> orders = user.getOrders();  // LazyInitializationException!

// Cause 2: Returning entity with lazy collection from controller
@GetMapping("/users/{id}")
public User getUser(@PathVariable Long id) {
    return userRepository.findById(id).get();  // Session closes, orders not loaded
}
```

## How to Fix

### Fix 1: Use JOIN FETCH in JPQL

```java
@Query("SELECT u FROM User u JOIN FETCH u.orders WHERE u.id = :id")
User findByIdWithOrders(@Param("id") Long id);
```

### Fix 2: Use @EntityGraph

```java
@EntityGraph(attributePaths = {"orders"})
@Query("SELECT u FROM User u WHERE u.id = :id")
User findByIdWithOrders(@Param("id") Long id);
```

### Fix 3: Initialize within transaction boundary

```java
@Transactional
public User getUserWithOrders(Long id) {
    User user = userRepository.findById(id).get();
    Hibernate.initialize(user.getOrders());
    return user;
}
```

### Fix 4: Use @BatchSize to reduce N+1

```java
@Entity
public class User {
    @OneToMany(fetch = FetchType.LAZY)
    @BatchSize(size = 20)
    private List<Order> orders;
}
```

## Related Errors

- {{< relref "hibernate-mapping" >}} — MappingException in Hibernate
- {{< relref "hibernate-dialect" >}} — SQLDialect not found
- {{< relref "hibernate-detached" >}} — DetachedEntityPassivationException
