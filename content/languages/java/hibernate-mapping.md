---
title: "[Solution] Hibernate MappingException — Entity Mapping Fix"
description: "Fix Hibernate MappingException when entity mapping is invalid. Check @Column, @Table, @JoinColumn, and type mismatches."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# MappingException — Hibernate Entity Mapping Fix

A `MappingException` is thrown when Hibernate detects an invalid mapping configuration. This can happen during startup (schema generation) or at runtime when persisting entities.

## What This Error Means

Common messages:

- `could not determine type of parameter`
- `Repeated column in mapping for entity`
- `Unable to find column with logical name`

## Common Causes

```java
// Cause 1: Repeated column mapping
@Entity
public class User {
    @Column(name = "email")
    private String email;

    @Column(name = "email")
    private String secondaryEmail;  // MappingException: Repeated column
}

// Cause 2: Missing @JoinColumn on @ManyToOne
@Entity
public class Order {
    @ManyToOne
    private User user;  // Missing @JoinColumn
}

// Cause 3: Type mismatch between Java type and database column
@Entity
public class Product {
    @Column(columnDefinition = "VARCHAR(255)")
    private Integer price;  // Type mismatch
}
```

## How to Fix

### Fix 1: Ensure unique column names

```java
@Entity
public class User {
    @Column(name = "email")
    private String email;

    @Column(name = "secondary_email")
    private String secondaryEmail;
}
```

### Fix 2: Add @JoinColumn for relationships

```java
@Entity
public class Order {
    @ManyToOne
    @JoinColumn(name = "user_id")
    private User user;
}
```

### Fix 3: Match Java types to database types

```java
@Entity
public class Product {
    @Column(columnDefinition = "DECIMAL(10,2)")
    private BigDecimal price;
}
```

### Fix 4: Use schema validation

```properties
spring.jpa.hibernate.ddl-auto=validate
spring.jpa.show-sql=true
```

## Related Errors

- {{< relref "hibernate-lazy" >}} — LazyInitializationException
- {{< relref "hibernate-dialect" >}} — SQLDialect not found
- {{< relref "jpa-entity" >}} — EntityNotFoundException
