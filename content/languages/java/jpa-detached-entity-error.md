---
title: "[Solution] Java detached entity error — JPA entity not associated with persistence context"
description: "Fix Java detached entity error by merging entities, reattaching to context, and handling stale data. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 113
---

# Detached entity error — JPA entity not associated with persistence context

A detached entity error occurs when you attempt to perform operations on an entity that was once managed by a persistence context but is no longer. The entity has been serialized, returned from a method whose transaction has ended, or explicitly detached.

## Description

JPA entities exist in three states: managed, detached, and removed. When a transaction ends, all managed entities become detached. Operations on detached entities fail because they are no longer tracked by the persistence context. Common message variants include:

- `javax.persistence.PersistenceException: detached entity passed to persist`
- `org.hibernate.TransientPropertyValueException: object references an unsaved transient instance`
- `org.hibernate.NonUniqueObjectException: a different object with the same identifier value was already associated with the session`
- `detached entity passed to merge`
- `No row with the given identifier exists`

## Common Causes

```java
// Cause 1: Persisting a detached entity
User user = userRepository.findById(1L).orElseThrow();
// Transaction ends, user becomes detached
userRepository.save(user);  // Trying to persist detached entity

// Cause 2: Two entities with same ID in persistence context
User user1 = entityManager.find(User.class, 1L);
User user2 = new User();
user2.setId(1L);  // Same ID as user1
entityManager.persist(user2);  // NonUniqueObjectException

// Cause 3: Entity references unsaved transient instance
@Entity
public class Order {
    @ManyToOne
    private Customer customer;  // customer is new and not persisted
}

Order order = new Order();
order.setCustomer(new Customer());  // Transient customer — not saved
orderRepository.save(order);  // TransientPropertyValueException

// Cause 4: Entity detached after serialization (e.g., REST API round-trip)
// Controller receives JSON, deserializes to entity with ID — entity is detached
```

## Solutions

### Fix 1: Use merge() for detached entities

```java
@Service
public class UserService {

    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Transactional
    public User updateUser(User detachedUser) {
        // Detach detected — use merge to reattach
        return userRepository.save(detachedUser);
        // Spring Data's save() calls merge for entities with non-null ID
    }

    @Transactional
    public User mergeUser(User detachedUser) {
        return entityManager.merge(detachedUser);
    }
}
```

### Fix 2: Persist related entities before referencing

```java
@Entity
public class Order {
    @ManyToOne(cascade = CascadeType.PERSIST)
    private Customer customer;
}

@Service
public class OrderService {

    @Transactional
    public Order createOrder(Long customerId) {
        Customer customer = customerRepository.findById(customerId)
            .orElseThrow(() -> new ResourceNotFoundException("Customer not found"));

        Order order = new Order();
        order.setCustomer(customer);  // customer is managed
        return orderRepository.save(order);
    }

    @Transactional
    public Order createOrderWithNewCustomer(String customerName) {
        Customer customer = new Customer();
        customer.setName(customerName);
        customerRepository.save(customer);  // Persist first

        Order order = new Order();
        order.setCustomer(customer);  // customer now managed
        return orderRepository.save(order);
    }
}
```

### Fix 3: Avoid multiple managed copies of same entity

```java
@Service
public class UserService {

    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Transactional
    public User updateUser(Long id, UserUpdateRequest request) {
        // Use single find — don't create another instance
        User user = userRepository.findById(id).orElseThrow();
        user.setName(request.name());
        return userRepository.save(user);
        // Works correctly — only one managed copy
    }

    // WRONG — creates two managed instances of same entity
    @Transactional
    public void badUpdate(Long id) {
        User user1 = userRepository.findById(id).orElseThrow();
        User user2 = userRepository.findById(id).orElseThrow();
        user1.setName("A");
        user2.setName("B");  // NonUniqueObjectException — two managed copies
    }
}
```

### Fix 4: Handle detached entities in controllers

```java
@RestController
@RequestMapping("/api/users")
public class UserController {

    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    @PutMapping("/{id}")
    public ResponseEntity<User> updateUser(@PathVariable Long id,
                                           @RequestBody UserUpdateRequest request) {
        // DON'T pass deserialized entity directly to service
        // Service re-fetches to ensure managed state
        User updated = userService.updateUser(id, request);
        return ResponseEntity.ok(updated);
    }
}

@Service
public class UserService {
    @Transactional
    public User updateUser(Long id, UserUpdateRequest request) {
        User user = userRepository.findById(id).orElseThrow();
        // user is managed — safe to modify
        user.setName(request.name());
        user.setEmail(request.email());
        return user;  // Return managed entity — dirty checking handles save
    }
}
```

### Fix 5: Use @DynamicUpdate for partial updates

```java
@Entity
@DynamicUpdate
public class User {
    @Id @GeneratedValue
    private Long id;
    private String name;
    private String email;
    private String bio;
}

@Service
public class UserService {
    @Transactional
    public User updateName(Long id, String name) {
        User user = userRepository.findById(id).orElseThrow();
        user.setName(name);
        // @DynamicUpdate generates SQL with only changed columns
        return user;
    }
}
```

## Prevention Checklist

- Never call `persist()` on an entity with a pre-existing ID — use `merge()` instead
- Always persist related entities before referencing them in other entities
- Avoid having two managed instances of the same entity in one persistence context
- Re-fetch entities from the database in service methods instead of operating on detached ones
- Use `CascadeType.ALL` or `CascadeType.PERSIST` for owned relationships
- Use `@DynamicUpdate` for partial updates to avoid overwriting unchanged fields

## Related Errors

- [EntityNotFoundException](/languages/java/jpa-entity-not-found/)
- [NonUniqueObjectException](/languages/java/hibernate-query-exception/)
- [Hibernate LazyInitializationException](/languages/java/hibernate-lazy-loading-error/)
