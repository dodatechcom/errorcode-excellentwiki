---
title: "[Solution] Java LazyInitializationException — Hibernate lazy collection access outside session"
description: "Fix Java LazyInitializationException by using JOIN FETCH, open session in view, or @Transactional. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 106
---

# LazyInitializationException — Hibernate lazy collection access outside session

A `LazyInitializationException` is thrown when you attempt to access a lazily-loaded collection or proxy after the Hibernate Session has been closed. Hibernate uses proxies for lazy loading and requires an active session to fetch data from the database.

## Description

When an entity is loaded, lazily-associated collections are not immediately fetched. Instead, Hibernate creates a proxy that queries the database on first access. If the Session is closed before this access, Hibernate cannot perform the query. Common message variants include:

- `could not initialize proxy - no Session`
- `No session currently active`
- `Session was already closed`
- `failed to lazily initialize a collection of role: X, could not initialize proxy - no Session`

## Common Causes

```java
// Cause 1: Accessing lazy collection after transaction ends
@Entity
public class User {
    @OneToMany(fetch = FetchType.LAZY)
    private List<Order> orders;
}

@Service
public class UserService {
    @Transactional
    public User getUser(Long id) {
        return userRepository.findById(id).orElseThrow();
        // Transaction ends, session closes
    }
}

// In controller — session is closed
@GetMapping("/users/{id}")
public User getUser(@PathVariable Long id) {
    User user = userService.getUser(id);
    user.getOrders().size();  // LazyInitializationException!
}

// Cause 2: Returning entity to serialization boundary (REST response)
// Cause 3: Accessing lazy field in a scheduled task or async method
// Cause 4: Accessing lazy association in equals/hashCode/toString
```

## Solutions

### Fix 1: Use JOIN FETCH in JPQL

```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {

    @Query("SELECT u FROM User u JOIN FETCH u.orders WHERE u.id = :id")
    Optional<User> findByIdWithOrders(@Param("id") Long id);

    @Query("SELECT u FROM User u LEFT JOIN FETCH u.orders LEFT JOIN FETCH u.address WHERE u.id = :id")
    Optional<User> findByIdWithAllAssociations(@Param("id") Long id);
}
```

### Fix 2: Use @EntityGraph

```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {

    @EntityGraph(attributePaths = {"orders", "address"})
    Optional<User> findByIdWithGraph(Long id);

    // Named entity graph defined on the entity
    // @NamedEntityGraph(name = "User.full", attributeNodes = {
    //     @NamedAttributeNode("orders"),
    //     @NamedAttributeNode("address")
    // })
}

@Entity
@NamedEntityGraph(name = "User.full", attributeNodes = {
    @NamedAttributeNode("orders"),
    @NamedAttributeNode("address")
})
public class User { ... }
```

### Fix 3: Use @Transactional on the calling method

```java
@Service
public class UserService {

    @Transactional(readOnly = true)
    public List<Order> getUserOrders(Long userId) {
        User user = userRepository.findById(userId).orElseThrow();
        // Session is still open in this method
        return user.getOrders();  // Works — lazy init within transaction
    }
}

// Or at the controller level (use with caution)
@RestController
public class UserController {

    @GetMapping("/users/{id}/orders")
    @Transactional(readOnly = true)
    public List<Order> getOrders(@PathVariable Long id) {
        User user = userService.getUser(id);
        return user.getOrders();  // Session open during request
    }
}
```

### Fix 4: Use FETCH in Criteria API

```java
@Service
public class UserQueryService {

    private final EntityManager entityManager;

    public UserQueryService(EntityManager entityManager) {
        this.entityManager = entityManager;
    }

    public User findByIdWithOrders(Long id) {
        CriteriaBuilder cb = entityManager.getCriteriaBuilder();
        CriteriaQuery<User> query = cb.createQuery(User.class);
        Root<User> root = query.from(User.class);
        root.fetch("orders", JoinType.LEFT);
        root.fetch("address", JoinType.LEFT);
        query.select(root).where(cb.equal(root.get("id"), id));
        return entityManager.createQuery(query).getSingleResult();
    }
}
```

### Fix 5: Use Hibernate.initialize()

```java
@Service
public class UserService {

    @Transactional(readOnly = true)
    public User getUserFull(Long id) {
        User user = userRepository.findById(id).orElseThrow();
        Hibernate.initialize(user.getOrders());     // Force load
        Hibernate.initialize(user.getAddress());     // Force load
        return user;
    }
}
```

## Prevention Checklist

- Design service methods to fetch all needed data within the transaction boundary
- Use `JOIN FETCH` or `@EntityGraph` to eagerly load required associations
- Add `@Transactional(readOnly = true)` to service methods that read lazy data
- Avoid returning entities with lazy collections directly from controllers
- Use `Hibernate.initialize()` when eager loading cannot be done via queries
- Enable `spring.jpa.open-in-view=false` and handle session boundaries explicitly

## Related Errors

- [SessionException](/languages/java/hibernate-session-closed-error/)
- [TransactionRequiredException](/languages/java/jpa-transaction-required/)
- [Hibernate QueryException](/languages/java/hibernate-query-exception/)
