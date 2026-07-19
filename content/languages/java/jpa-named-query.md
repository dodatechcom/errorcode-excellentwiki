---
title: "[Solution] JPA NoResultException — Named Query Not Found"
description: "Fix javax.persistence.NoResultException No entity found for query. Handle named query not found and empty result errors."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# NoResultException — Named Query Not Found

A `NoResultException` with message `No entity found for query` occurs when a JPA named query or `createQuery()` returns zero results but the code expects at least one row. This is different from a query that returns an empty list — `getSingleResult()` throws this exception on empty results.

## What This Error Means

When using `Query.getSingleResult()` or `TypedQuery.getSingleResult()`, JPA expects exactly one result. If the query returns no rows, a `NoResultException` is thrown. If it returns more than one row, a `NonUniqueResultException` is thrown instead.

## Common Causes

```java
// Cause 1: Using getSingleResult() on query returning no rows
@Query("SELECT u FROM User u WHERE u.email = :email")
User findByEmail(@Param("email") String email);

User user = userRepository.findByEmail("nonexistent@example.com");
// NoResultException — no user with that email

// Cause 2: Named query referencing non-existent entity
@NamedQuery(name = "User.findByStatus", query = "SELECT u FROM User u WHERE u.status = :status")
// Entity name changed from User to AppUser — query broken

// Cause 3: Query condition excludes all rows
Query query = entityManager.createQuery("SELECT u FROM User u WHERE u.active = true AND u.deleted = false");
User single = query.getSingleResult();  // NoResultException if no active non-deleted users
```

## How to Fix

### Fix 1: Use Optional or return list instead of getSingleResult()

```java
// Option A: Return Optional (Spring Data JPA)
Optional<User> findByEmail(String email);

// Option B: Use JPQL with Optional
@Query("SELECT u FROM User u WHERE u.email = :email")
Optional<User> findOptionalByEmail(@Param("email") String email);

// Option C: Use query with list
@Query("SELECT u FROM User u WHERE u.email = :email")
List<User> findAllByEmail(@Param("email") String email);
```

### Fix 2: Handle NoResultException gracefully

```java
public User findUserByEmail(String email) {
    try {
        return entityManager.createQuery(
                "SELECT u FROM User u WHERE u.email = :email", User.class)
            .setParameter("email", email)
            .getSingleResult();
    } catch (NoResultException e) {
        throw new UserNotFoundException("No user found with email: " + email);
    }
}
```

### Fix 3: Validate named query references exist

```java
@Entity
@NamedQuery(name = "User.findByStatus",
    query = "SELECT u FROM User u WHERE u.status = :status")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String status;
}

// Verify query exists at startup
@PersistenceUnit
private EntityManagerFactory emf;

@PostConstruct
public void validateQueries() {
    try {
        emf.createEntityManager().createNamedQuery("User.findByStatus");
        log.info("Named query User.findByStatus validated");
    } catch (Exception e) {
        log.error("Named query validation failed", e);
    }
}
```

### Fix 4: Use exists() check before getSingleResult()

```java
boolean exists = userRepository.existsByEmail(email);
if (!exists) {
    throw new UserNotFoundException("User not found: " + email);
}
User user = userRepository.findByEmail(email).orElseThrow();
```

## Prevention Tips

- Prefer `Optional<T>` return types over `getSingleResult()` in Spring Data JPA.
- Use `findBy...` returning `Optional<T>` to avoid `NoResultException`.
- Always handle `NoResultException` when using `getSingleResult()` directly.
- Validate named queries at application startup to catch typos early.

## Related Errors

- {{< relref "jpa-named-query" >}} — Named query errors
- {{< relref "hibernate-query-syntax" >}} — HQL/JPQL syntax errors
- {{< relref "jpa-criteria-api" >}} — Criteria API errors
