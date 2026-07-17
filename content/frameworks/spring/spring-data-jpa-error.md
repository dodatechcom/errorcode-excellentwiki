---
title: "DataAccessException - JPA query failed"
description: "Spring Data JPA throws DataAccessException when a JPA query or database operation fails"
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["jpa", "hibernate", "database", "query", "spring-data"]
weight: 5
---

This error occurs when a JPA operation (query, persist, merge, delete) fails at the database level. Spring wraps the JPA exception in `DataAccessException` as part of its data access exception hierarchy.

## Common Causes

- JPQL or native SQL query has syntax errors
- Entity mapping does not match database schema
- Connection pool exhausted
- Transaction isolation level conflict
- Entity not in managed state during merge

## How to Fix

1. Use repository methods with proper error handling:

```java
public interface UserRepository extends JpaRepository<User, Long> {

    @Query("SELECT u FROM User u WHERE u.email = :email")
    Optional<User> findByEmail(@Param("email") String email);
}
```

2. Enable SQL logging for debugging:

```yaml
spring:
  jpa:
    show-sql: true
    properties:
      hibernate:
        format_sql: true
logging:
  level:
    org.hibernate.SQL: DEBUG
    org.hibernate.type.descriptor.sql.BasicBinder: TRACE
```

3. Handle data access exceptions in the service layer:

```java
@Service
@Transactional
public class UserService {

    public User createUser(CreateUserRequest request) {
        try {
            User user = new User(request.email(), request.name());
            return userRepository.save(user);
        } catch (DataAccessException e) {
            if (e.getRootCause() instanceof SQLIntegrityConstraintViolationException) {
                throw new DuplicateEmailException(request.email());
            }
            throw e;
        }
    }
}
```

4. Use `@Query` with named parameters:

```java
@Query(value = "SELECT * FROM users WHERE status = :status", nativeQuery = true)
List<User> findActiveUsers(@Param("status") String status);
```

## Examples

```java
// JPQL references non-existent field
@Query("SELECT u FROM User u WHERE u.username = :email")
Optional<User> findByEmail(@Param("email") String email);
// DataAccessException: Named parameter 'username' not found in query
```

## Related Errors

- [Elasticsearch error]({{< relref "/frameworks/spring/spring-data-elasticsearch-error" >}})
- [R2DBC error]({{< relref "/frameworks/spring/spring-data-r2dbc-error" >}})
