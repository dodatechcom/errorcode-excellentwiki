---
title: "[Solution] JPA EntityExistsException — Detached Entity Passed to Persist"
description: "Fix javax.persistence.EntityExistsException detached entity passed to persist. Handle JPA entity persistence conflicts."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# EntityExistsException — Detached Entity Passed to Persist

An `EntityExistsException` with message `detached entity passed to persist` occurs when `EntityManager.persist()` is called on an entity that already exists in the database but is not managed by the current persistence context.

## What This Error Means

In JPA, an entity can be in one of four states: new (transient), managed, detached, or removed. `persist()` only works on new entities. If an entity has a primary key that already exists in the database, or was previously managed and then detached, calling `persist()` will fail.

## Common Causes

```java
// Cause 1: Entity with pre-set ID passed to persist
User user = new User();
user.setId(1L);  // ID already exists in database
entityManager.persist(user);  // EntityExistsException

// Cause 2: Detached entity re-persisted
User user = entityManager.find(User.class, 1L);
entityManager.detach(user);
// ... some code ...
entityManager.persist(user);  // EntityExistsException — already exists

// Cause 3: Merge vs persist confusion
// Using persist() when merge() should be used
User user = new User();
user.setId(existingId);
entityManager.persist(user);  // Fails — should use merge()
```

## How to Fix

### Fix 1: Use merge() instead of persist() for existing entities

```java
User user = entityManager.find(User.class, 1L);
entityManager.detach(user);
user.setName("Updated Name");
User merged = entityManager.merge(user);  // Updates existing entity
```

### Fix 2: Check existence before persisting

```java
public void createUser(User user) {
    if (user.getId() != null && entityManager.find(User.class, user.getId()) != null) {
        throw new EntityExistsException("User with ID " + user.getId() + " already exists");
    }
    entityManager.persist(user);
}
```

### Fix 3: Let JPA generate the ID and use persist() correctly

```java
@Entity
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;  // Do not set manually

    @Column(unique = true)
    private String email;
}

// Let the database assign the ID
User user = new User();
user.setEmail("john@example.com");
// Do NOT call user.setId() — let @GeneratedValue handle it
entityManager.persist(user);
```

### Fix 4: Use Spring Data JPA save() which handles both cases

```java
@Service
public class UserService {
    @Autowired
    private UserRepository userRepository;

    public User saveUser(User user) {
        // save() calls persist() for new, merge() for existing
        return userRepository.save(user);
    }
}
```

## Prevention Tips

- Do not set `@Id` manually unless you are certain the entity is new.
- Prefer `merge()` over `persist()` when the entity state is uncertain.
- Use Spring Data `save()` which abstracts persist vs merge.
- Use `@GeneratedValue` for auto-generated primary keys.

## Related Errors

- {{< relref "jpa-detached-entity" >}} — Detached entity persistence error
- {{< relref "jpa-constraint" >}} — ConstraintViolationException
- {{< relref "jpa-optimistic-lock" >}} — Optimistic lock failure
