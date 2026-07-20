---
title: "[Solution] Java QueryException — Hibernate HQL or JPQL query error"
description: "Fix Java QueryException by checking HQL syntax, verifying entity names, and handling mapping issues. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 108
---

# QueryException — Hibernate HQL or JPQL query error

A `QueryException` is thrown when Hibernate encounters an invalid HQL/JPQL query, a reference to an unmapped entity or property, or incorrect query parameters. This covers syntax errors, type mismatches, and mapping problems.

## Description

Hibernate parses HQL/JPQL queries and translates them to SQL. Errors occur during parsing, validation, or execution. Common message variants include:

- `unexpected token: X near line Y, column Z`
- `could not resolve property: X in: com.example.Entity`
- `org.hibernate.QueryException: could not resolve collection`
- `Wrong number of arguments for named parameters`
- `Parameter value X did not match expected type Y`

## Common Causes

```java
// Cause 1: Incorrect HQL syntax
session.createQuery("SELECT u FROM Users WHERE u.name = :name");  // "Users" should be "User"

// Cause 2: Referencing unmapped property
session.createQuery("SELECT u.fullName FROM User u");  // Field is "name" not "fullName"

// Cause 3: Wrong parameter count
session.createQuery("SELECT u FROM User u WHERE u.name = :name AND u.age = :age")
    .setParameter("name", "John")  // Missing :age parameter
    .list();

// Cause 4: Type mismatch in parameter
@Query("SELECT u FROM User u WHERE u.id = :id")
List<User> findByName(@Param("id") String id);  // id is Long, not String

// Cause 5: Using entity name instead of alias
session.createQuery("FROM User User WHERE User.name = :name");  // Name collision
```

## Solutions

### Fix 1: Use entity class names, not table names

```java
// WRONG — table name
session.createQuery("SELECT u FROM users u WHERE u.name = :name");

// CORRECT — entity class name
session.createQuery("SELECT u FROM User u WHERE u.name = :name");

// WRONG — mixed case
session.createQuery("FROM user WHERE name = :name");

// CORRECT — matches @Entity class exactly
session.createQuery("FROM User WHERE name = :name", User.class);
```

### Fix 2: Use correct property names

```java
@Entity
@Table(name = "users")
public class User {
    @Id private Long id;
    @Column(name = "full_name")
    private String name;  // HQL uses "name", not "full_name" or "fullName"
}

// WRONG — column name or incorrect property
session.createQuery("SELECT u.full_name FROM User u");

// CORRECT — Java field name
session.createQuery("SELECT u.name FROM User u");

// Use @AttributeOverride if needed
@Entity
@AttributeOverride(name = "name", column = @Column(name = "full_name"))
public class User { ... }
```

### Fix 3: Use correct parameter binding

```java
// WRONG — positional parameter mismatch
session.createQuery("SELECT u FROM User u WHERE u.name = ?1 AND u.age = ?2")
    .setParameter(1, "John")
    // Missing parameter 2
    .list();

// CORRECT — all parameters provided
session.createQuery("SELECT u FROM User u WHERE u.name = :name AND u.age = :age")
    .setParameter("name", "John")
    .setParameter("age", 30)
    .list();

// Use setParameterList for IN clauses
session.createQuery("SELECT u FROM User u WHERE u.id IN :ids")
    .setParameterList("ids", List.of(1L, 2L, 3L))
    .list();
```

### Fix 4: Use Spring Data JPA @Query correctly

```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {

    // CORRECT — JPQL with entity class and field names
    @Query("SELECT u FROM User u WHERE u.name = :name")
    Optional<User> findByName(@Param("name") String name);

    // CORRECT — native SQL uses table/column names
    @Query(value = "SELECT * FROM users WHERE full_name = :name", nativeQuery = true)
    Optional<User> findByNameNative(@Param("name") String name);

    // CORRECT — aggregate query
    @Query("SELECT u.department, COUNT(u) FROM User u GROUP BY u.department")
    List<Object[]> countByDepartment();
}
```

### Fix 5: Handle entity joins properly

```java
// CORRECT — join with explicit association path
session.createQuery(
    "SELECT u FROM User u JOIN u.orders o WHERE o.total > :minTotal", User.class)
    .setParameter("minTotal", 100.0)
    .list();

// CORRECT — left join for optional associations
session.createQuery(
    "SELECT u FROM User u LEFT JOIN FETCH u.address WHERE u.id = :id", User.class)
    .setParameter("id", 1L)
    .uniqueResult();

// CORRECT — subquery
session.createQuery(
    "SELECT u FROM User u WHERE u.id IN (SELECT o.userId FROM Order o WHERE o.total > :total)")
    .setParameter("total", 500.0)
    .list();
```

## Prevention Checklist

- Use entity class names (not table names) in HQL/JPQL queries
- Reference Java field names (not column names) in HQL
- Provide all required named parameters before executing queries
- Use `@Param` annotations with Spring Data JPA `@Query`
- Validate query syntax at startup with `spring.jpa.show-sql=true`
- Test queries with sample data to catch mapping issues early

## Related Errors

- [Hibernate TypeMismatchException](/languages/java/hibernate-type-mismatch/)
- [Hibernate ConstraintViolationException](/languages/java/hibernate-constraint-violation/)
- [Hibernate MappingException](/languages/java/hibernate-mapping/)
