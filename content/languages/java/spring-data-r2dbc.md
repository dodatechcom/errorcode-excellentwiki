---
title: "[Solution] DataIntegrityViolationException R2DBC — Reactive Database Fix"
description: "Fix DataIntegrityViolationException in Spring Data R2DBC. Handle reactive database constraint violations."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# DataIntegrityViolationException R2DBC — Reactive Database Fix

A `DataIntegrityViolationException` in R2DBC context occurs when a reactive database operation violates a constraint. This is the reactive equivalent of JPA constraint violations.

## What This Error Means

Common message:

- `DataIntegrityViolationException: Duplicate entry`
- `DataIntegrityViolationException: Null value in non-null column`

## Common Causes

```java
// Cause 1: Unique constraint violation
public interface UserRepository extends ReactiveCrudRepository<User, Long> {
}

// Inserting duplicate email

// Cause 2: NOT NULL constraint violation
User user = new User();
user.setName(null);  // Column has NOT NULL constraint
```

## How to Fix

### Fix 1: Handle constraint violations reactively

```java
public Mono<User> createUser(User user) {
    return userRepository.save(user)
        .onErrorResume(DataIntegrityViolationException.class, ex -> {
            if (ex.getMessage().contains("Duplicate entry")) {
                return Mono.error(new DuplicateEmailException("Email exists"));
            }
            return Mono.error(ex);
        });
}
```

### Fix 2: Use upsert for PostgreSQL

```java
@Query("INSERT INTO users (email, name) VALUES (:email, :name) " +
       "ON CONFLICT (email) DO UPDATE SET name = :name")
Mono<Void> upsertUser(@Param("email") String email, @Param("name") String name);
```

### Fix 3: Validate before persisting

```java
public Mono<User> createUser(User user) {
    return userRepository.existsByEmail(user.getEmail())
        .flatMap(exists -> {
            if (exists) {
                return Mono.error(new DuplicateEmailException("Email exists"));
            }
            return userRepository.save(user);
        });
}
```

## Related Errors

- {{< relref "jpa-constraint" >}} — ConstraintViolationException
- {{< relref "spring-data-elasticsearch" >}} — ElasticsearchException
- {{< relref "spring-webflux" >}} — WebExchangeBindException
