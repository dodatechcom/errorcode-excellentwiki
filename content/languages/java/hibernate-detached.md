---
title: "[Solution] DetachedEntityPassivationException — Hibernate Detached Entity Fix"
description: "Fix DetachedEntityPassivationException when passing detached entities across conversations. Reattach or merge entities properly."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["hibernate", "jpa", "detached-entity", "passivation", "merge"]
weight: 5
---

# DetachedEntityPassivationException — Hibernate Detached Entity Fix

A `DetachedEntityPassivationException` is thrown when Hibernate encounters a detached entity that cannot be serialized or passed across persistence contexts. This is common in web applications with session-per-request patterns.

## What This Error Means

Common messages:

- `DetachedEntityPassivationException: detached entity passed to persist`
- `org.hibernate.TransientPropertyValueException`

## Common Causes

```java
// Cause 1: Detached entity passed to persist instead of merge
@Entity
public class User {
    @Id
    @GeneratedValue
    private Long id;
}

User user = entityManager.find(User.class, 1L);
// Session closes
entityManager.persist(user);  // DetachedEntityPassivationException

// Cause 2: Cascade persist on detached entity
@Entity
public class Order {
    @ManyToOne(cascade = CascadeType.PERSIST)
    private User user;  // User is detached
}
```

## How to Fix

### Fix 1: Use merge instead of persist

```java
@Transactional
public User updateUser(User detachedUser) {
    return entityManager.merge(detachedUser);
}
```

### Fix 2: Use CascadeType.MERGE

```java
@Entity
public class Order {
    @ManyToOne(cascade = CascadeType.MERGE)
    private User user;
}
```

### Fix 3: Reattach entity

```java
@Transactional
public User reattachUser(Long id) {
    User user = entityManager.find(User.class, id);
    return user;
}
```

### Fix 4: Use DTO pattern

```java
public class UserDTO {
    private Long id;
    private String name;

    public static UserDTO fromEntity(User user) {
        UserDTO dto = new UserDTO();
        dto.id = user.getId();
        dto.name = user.getName();
        return dto;
    }
}
```

## Related Errors

- {{< relref "hibernate-lazy" >}} — LazyInitializationException
- {{< relref "hibernate-mapping" >}} — MappingException
- {{< relref "jpa-entity" >}} — EntityNotFoundException
