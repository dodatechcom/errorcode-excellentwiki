---
title: "[Solution] EntityNotFoundException — JPA Entity Not Found Fix"
description: "Fix JPA EntityNotFoundException when an entity does not exist in the database. Handle missing entities gracefully."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# EntityNotFoundException — JPA Entity Not Found Fix

An `EntityNotFoundException` is thrown when JPA cannot find an entity with the given identifier. This is an unchecked exception introduced in JPA 2.1.

## What This Error Means

Common message:

- `No entity found for [User] with id [42]`

## Common Causes

```java
// Cause 1: Entity does not exist
User user = entityManager.find(User.class, 999L);
// Returns null, not EntityNotFoundException

// Cause 2: getReferenceById with deleted entity
User user = entityManager.getReferenceById(User.class, 999L);
// EntityNotFoundException if ID doesn't exist

// Cause 3: Entity was deleted by another transaction
// Between check and access, entity was deleted
```

## How to Fix

### Fix 1: Use Optional return type

```java
Optional<User> user = userRepository.findById(id);
if (user.isPresent()) {
    // Process user
} else {
    // Handle not found
}
```

### Fix 2: Throw custom exception

```java
User user = userRepository.findById(id)
    .orElseThrow(() -> new ResourceNotFoundException("User not found: " + id));
```

### Fix 3: Handle in global exception handler

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(EntityNotFoundException.class)
    public ResponseEntity<Map<String, String>> handleNotFound(EntityNotFoundException ex) {
        return ResponseEntity.status(HttpStatus.NOT_FOUND)
            .body(Map.of("error", ex.getMessage()));
    }
}
```

## Related Errors

- {{< relref "jpa-constraint" >}} — ConstraintViolationException
- {{< relref "jpa-transaction" >}} — UnexpectedRollbackException
- {{< relref "hibernate-mapping" >}} — MappingException
