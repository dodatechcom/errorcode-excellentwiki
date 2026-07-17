---
title: "DataIntegrityViolationException - R2DBC"
description: "Spring Data R2DBC throws DataIntegrityViolationException when a reactive database operation violates data integrity constraints"
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["r2dbc", "reactive", "database", "constraint", "spring-data"]
weight: 5
---

This error occurs when a reactive database operation in Spring Data R2DBC violates a uniqueness, foreign key, or not-null constraint. It throws `DataIntegrityViolationException`.

## Common Causes

- Unique constraint violation on insert or update
- Foreign key references a non-existent record
- Not-null column receiving a null value
- Data type mismatch between application and database
- Batch insert contains duplicate keys

## How to Fix

1. Use reactive repositories with proper error handling:

```java
public interface UserRepository extends ReactiveCrudRepository<User, Long> {

    @Query("SELECT * FROM users WHERE email = :email")
    Mono<User> findByEmail(String email);
}
```

2. Handle constraint violations reactively:

```java
@Service
public class UserService {

    private final UserRepository userRepository;

    public Mono<User> createUser(User user) {
        return userRepository.save(user)
            .onErrorResume(DataIntegrityViolationException.class, ex -> {
                if (ex.getMessage().contains("unique")) {
                    return Mono.error(new DuplicateEmailException(user.getEmail()));
                }
                return Mono.error(ex);
            });
    }
}
```

3. Use `onErrorMap` for better error messages:

```java
repository.save(order)
    .onErrorMap(
        DataIntegrityViolationException.class,
        ex -> new ServiceException("Order creation failed: " + ex.getMessage())
    );
```

## Examples

```java
// Duplicate email violates unique constraint
userRepository.save(new User("test@example.com"))
    .subscribe(
        user -> log.info("Created: {}", user),
        error -> log.error("Failed: {}", error.getMessage())
    );
// DataIntegrityViolationException: Duplicate entry for unique constraint
```

## Related Errors

- [R2DBC connection error]({{< relref "/frameworks/spring/data-r2dbc-error" >}})
- [Data JPA error]({{< relref "/frameworks/spring/data-jpa-error" >}})
