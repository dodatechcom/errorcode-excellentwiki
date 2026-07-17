---
title: "[Solution] ConstraintViolationException Duplicate Entry — JPA Fix"
description: "Fix JPA ConstraintViolationException when inserting duplicate values. Handle unique constraint violations gracefully."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ConstraintViolationException Duplicate Entry — JPA Fix

A `ConstraintViolationException` is thrown when a database constraint is violated, most commonly a unique constraint when inserting or updating duplicate values.

## What This Error Means

Common message:

- `Duplicate entry 'value' for key 'idx_unique_email'`
- `Unique index or primary key violation`

## Common Causes

```java
// Cause 1: Duplicate unique value
@Entity
@Table(name = "users", uniqueConstraints =
    @UniqueConstraint(columnNames = "email"))
public class User {
    @Column(unique = true)
    private String email;
}
// Inserting two users with same email

// Cause 2: Race condition
// Thread A checks: email not exists
// Thread B checks: email not exists
// Thread A inserts: success
// Thread B inserts: ConstraintViolationException
```

## How to Fix

### Fix 1: Catch and handle the exception

```java
try {
    userRepository.save(user);
} catch (DataIntegrityViolationException ex) {
    if (ex.getMessage().contains("Duplicate entry")) {
        throw new DuplicateEmailException("Email already exists: " + user.getEmail());
    }
    throw ex;
}
```

### Fix 2: Use upsert / merge pattern

```java
@Modifying
@Query(value = "INSERT INTO users (email, name) VALUES (:email, :name) " +
    "ON DUPLICATE KEY UPDATE name = :name", nativeQuery = true)
void upsertUser(@Param("email") String email, @Param("name") String name);
```

### Fix 3: Check existence before insert

```java
boolean exists = userRepository.existsByEmail(user.getEmail());
if (exists) {
    throw new DuplicateEmailException("Email already exists");
}
```

## Related Errors

- {{< relref "jpa-entity" >}} — EntityNotFoundException
- {{< relref "jpa-transaction" >}} — UnexpectedRollbackException
- {{< relref "sql-exception" >}} — SQL exception
