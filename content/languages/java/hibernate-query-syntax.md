---
title: "[Solution] Hibernate QueryException — HQL/JPQL Syntax Error"
description: "Fix org.hibernate.QueryException unexpected char. Resolve HQL and JPQL syntax errors in Hibernate queries."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# QueryException — HQL/JPQL Syntax Error

A `QueryException` with message `unexpected char` or similar syntax error occurs when Hibernate cannot parse an HQL (Hibernate Query Language) or JPQL query. This is caused by invalid syntax, incorrect entity/field references, or using SQL-specific syntax in HQL.

## What This Error Means

HQL/JPQL is an object-oriented query language that operates on entity classes and their properties, not database tables and columns. Syntax that works in SQL may not work in HQL. Common issues include using SQL functions not available in HQL, incorrect JOIN syntax, or referencing fields that do not exist on the entity.

## Common Causes

```java
// Cause 1: Using SQL syntax instead of HQL
Query query = session.createQuery("SELECT * FROM User u WHERE u.name = 'John'");
// HQL does not use * or table names

// Cause 2: Incorrect JOIN syntax
Query query = session.createQuery(
    "SELECT u FROM User u INNER JOIN orders o ON u.id = o.user_id");
// HQL JOINs use entity relationships, not ON clauses

// Cause 3: Referencing non-existent field
Query query = session.createQuery("SELECT u.username FROM User u");
// Entity has field "name", not "username"

// Cause 4: Using database-specific functions in HQL
Query query = session.createQuery("SELECT CONCAT(u.first_name, ' ', u.last_name) FROM User u");
// HQL does not have CONCAT — use || or + depending on dialect
```

## How to Fix

### Fix 1: Use proper HQL syntax

```java
// Instead of SELECT *, select the entity
Query<User> query = session.createQuery("FROM User u WHERE u.name = :name", User.class);
query.setParameter("name", "John");

// Or with explicit select
Query<User> query = session.createQuery("SELECT u FROM User u WHERE u.name = :name", User.class);
```

### Fix 2: Use HQL JOIN syntax with entity relationships

```java
// Correct HQL JOIN using entity relationship
Query<Object[]> query = session.createQuery(
    "SELECT u, o FROM User u JOIN u.orders o WHERE u.name = :name",
    Object[].class);

// Or with LEFT JOIN FETCH
@Query("SELECT u FROM User u LEFT JOIN FETCH u.orders WHERE u.id = :id")
User findByIdWithOrders(@Param("id") Long id);
```

### Fix 3: Reference entity fields, not column names

```java
@Entity
@Table(name = "app_users")  // Table name is "app_users"
public class User {
    @Id
    private Long id;

    @Column(name = "user_name")  // Column is "user_name"
    private String name;          // Use "name" in HQL
}

// Correct HQL
Query<User> query = session.createQuery("FROM User u WHERE u.name = :name", User.class);
```

### Fix 4: Use Criteria API for complex dynamic queries

```java
CriteriaBuilder cb = session.getCriteriaBuilder();
CriteriaQuery<User> cq = cb.createQuery(User.class);
Root<User> root = cq.from(User.class);

List<Predicate> predicates = new ArrayList<>();
if (name != null) predicates.add(cb.equal(root.get("name"), name));
if (minAge != null) predicates.add(cb.greaterThanOrEqualTo(root.get("age"), minAge));

cq.select(root).where(predicates.toArray(new Predicate[0]));
List<User> results = session.createQuery(cq).getResultList();
```

### Fix 5: Validate HQL at startup or with tests

```java
@Test
void testHqlSyntax() {
    // This will throw QueryException if syntax is wrong
    session.createQuery("FROM User u WHERE u.name = :name", User.class)
        .setParameter("name", "test");
}
```

## Prevention Tips

- Always use entity field names in HQL, never database column names.
- Use JPQL over native HQL for better portability.
- Write unit tests for all HQL/JPQL queries to catch syntax errors early.
- Use the JPA static metamodel with Criteria API for type-safe dynamic queries.

## Related Errors

- {{< relref "hibernate-unknown-entity" >}} — Unknown entity mapping
- {{< relref "hibernate-type-error" >}} — Type mapping errors
- {{< relref "jpa-criteria-api" >}} — Criteria API errors
