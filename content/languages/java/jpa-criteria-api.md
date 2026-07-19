---
title: "[Solution] JPA Criteria API — Unknown Attribute Path"
description: "Fix java.lang.IllegalArgumentException Unknown attribute path in Criteria API. Resolve JPA type mismatch errors."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Criteria API — Unknown Attribute Path

An `IllegalArgumentException` with message `Unknown attribute path` occurs in JPA Criteria API when the attribute name used in `root.get()`, `root.join()`, or path navigation does not match any field in the entity class.

## What This Error Means

The Criteria API is type-safe and resolves attribute paths at runtime by inspecting the entity's metamodel. If the attribute name string does not match a field name or `@AttributeOverride`, the API throws this exception. This typically happens due to typos, renamed fields, or incorrect path expressions.

## Common Causes

```java
// Cause 1: Typo in attribute name
CriteriaBuilder cb = entityManager.getCriteriaBuilder();
CriteriaQuery<User> cq = cb.createQuery(User.class);
Root<User> root = cq.from(User.class);
cq.select(root).where(cb.equal(root.get("userName"), "John"));
// Field is "name", not "userName" — IllegalArgumentException

// Cause 2: Attribute path through non-existent relationship
Root<User> root = cq.from(User.class);
Join<User, Order> join = root.join("orderss");  // Typo: should be "orders"

// Cause 3: Using database column name instead of Java field name
Root<User> root = cq.from(User.class);
cq.where(cb.equal(root.get("user_name"), "John"));
// DB column is "user_name" but Java field is "name"
```

## How to Fix

### Fix 1: Use the metamodel for type-safe attribute access

```java
// Generate metamodel: User_ class with static attribute descriptors
import static com.example.entity.User_;

CriteriaBuilder cb = entityManager.getCriteriaBuilder();
CriteriaQuery<User> cq = cb.createQuery(User.class);
Root<User> root = cq.from(User.class);

// Compile-time safe — no string typos possible
cq.select(root).where(cb.equal(root.get(User_.name), "John"));
```

### Fix 2: Verify attribute names match entity fields

```java
// Entity definition
@Entity
public class User {
    @Id
    private Long id;

    @Column(name = "user_name")
    private String name;  // Use "name" in Criteria, not "user_name"

    @ManyToOne
    private Department department;
}

// Correct usage
Root<User> root = cq.from(User.class);
cq.where(cb.equal(root.get("name"), "John"));  // Java field name
Join<User, Department> dept = root.join("department");  // Relationship name
```

### Fix 3: Use dynamic path with validation

```java
public <T, V> Path<V> safeGetPath(Root<T> root, String attributePath) {
    try {
        Path<V> path = root.get(attributePath);
        return path;
    } catch (IllegalArgumentException e) {
        throw new IllegalArgumentException(
            "Attribute '" + attributePath + "' not found in entity " +
            root.getModel().getName() + ". Check field names.", e);
    }
}

// Usage
Root<User> root = cq.from(User.class);
Path<String> namePath = safeGetPath(root, "name");
cq.where(cb.equal(namePath, "John"));
```

### Fix 4: Debug by listing entity attributes

```java
EntityType<User> entityModel = entityManager.getMetamodel().entity(User.class);
entityModel.getDeclaredAttributes().forEach(attr -> {
    System.out.println("Attribute: " + attr.getName() + " type: " + attr.getJavaType());
});
```

## Prevention Tips

- Always use the JPA static metamodel (`User_`) for Criteria API queries.
- Enable IDE support for metamodel generation.
- Validate Criteria queries with unit tests that exercise all query paths.
- Use `@AttributeOverride` carefully and update Criteria code when column mappings change.

## Related Errors

- {{< relref "hibernate-query-syntax" >}} — HQL/JPQL syntax errors
- {{< relref "hibernate-unknown-entity" >}} — Unknown entity mapping
- {{< relref "hibernate-type-error" >}} — Type mapping errors
