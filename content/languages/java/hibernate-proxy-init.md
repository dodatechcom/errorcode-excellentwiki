---
title: "[Solution] Hibernate LazyInitializationException — No Session Found for Current Thread"
description: "Fix org.hibernate.LazyInitializationException No Session found for current thread. Initialize Hibernate proxies within session boundaries."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# LazyInitializationException — No Session Found for Current Thread

A `LazyInitializationException` with message `No Session found for current thread` occurs when Hibernate tries to initialize a proxy (lazy-loaded entity or property) but there is no active Hibernate Session bound to the current thread.

## What This Error Means

Hibernate binds Sessions to threads using `ThreadLocal`. When a `@Transactional` method completes, the Session is closed. If proxy initialization is attempted after the transaction ends (e.g., in a different thread, in a scheduled job, or after a method returns), this exception occurs.

## Common Causes

```java
// Cause 1: Lazy entity accessed after transaction ends
@Transactional(readOnly = true)
public User findUser(Long id) {
    return userRepository.findById(id).orElseThrow();
    // Session closes here
}

public UserDTO toDTO(User user) {
    return new UserDTO(user.getId(), user.getName());
    // If user has lazy proxy for profile, accessing it fails
}

// Cause 2: Accessing lazy entity in async method
@Async
public void processUser(User user) {
    Profile profile = user.getProfile();  // LazyInitializationException!
}

// Cause 3: Entity returned from repository in non-transactional context
public User getUserFromCache(Long id) {
    return userCache.get(id);
    // Entity was cached outside transaction, proxy uninitialized
}
```

## How to Fix

### Fix 1: Initialize proxy within the transaction boundary

```java
@Transactional(readOnly = true)
public UserDTO findUser(Long id) {
    User user = userRepository.findById(id).orElseThrow();
    // Access lazy fields while Session is open
    return new UserDTO(user.getId(), user.getName(), user.getProfile().getBio());
}
```

### Fix 2: Use JOIN FETCH to load entity eagerly

```java
@Query("SELECT u FROM User u JOIN FETCH u.profile WHERE u.id = :id")
User findByIdWithProfile(@Param("id") Long id);
```

### Fix 3: Use Hibernate.initialize() before closing transaction

```java
@Transactional
public User loadUserFully(Long id) {
    User user = userRepository.findById(id).orElseThrow();
    Hibernate.initialize(user.getProfile());
    Hibernate.initialize(user.getOrders());
    return user;
}
```

### Fix 4: Configure Open Session in View filter (use with caution)

```java
// Spring Boot configuration
@Bean
public OpenEntityManagerInViewFilter openEntityManagerInViewFilter() {
    return new OpenEntityManagerInViewFilter();
}
// OR in application.properties:
// spring.jpa.open-in-view=true  (default is true in Spring Boot)
```

### Fix 5: Create DTO within transaction

```java
@Service
public class UserService {
    @Transactional(readOnly = true)
    public UserDTO getUserAsDTO(Long id) {
        User user = userRepository.findById(id).orElseThrow();
        // Build DTO while Session is open
        return UserDTO.builder()
            .id(user.getId())
            .name(user.getName())
            .profileBio(user.getProfile().getBio())
            .orderCount(user.getOrders().size())
            .build();
    }
}
```

## Prevention Tips

- Keep all entity access within `@Transactional` boundaries.
- Prefer DTOs built inside transactions over returning entities directly.
- Use `JOIN FETCH` or `@EntityGraph` for queries that need related entities.
- Be cautious with `spring.jpa.open-in-view=true` — it can cause performance issues.

## Related Errors

- {{< relref "hibernate-collection-init" >}} — Collection initialization errors
- {{< relref "hibernate-lazy" >}} — LazyInitializationException general
- {{< relref "jpa-detached-entity" >}} — Detached entity errors
