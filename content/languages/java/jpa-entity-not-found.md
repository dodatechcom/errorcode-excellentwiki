---
title: "[Solution] Java EntityNotFoundException — JPA entity not found in database"
description: "Fix Java EntityNotFoundException by choosing find() vs getReference(), verifying IDs, and handling persistence context correctly. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 111
---

# EntityNotFoundException — JPA entity not found in database

An `EntityNotFoundException` is thrown when JPA cannot locate an entity by its identifier in the persistence context or database. This differs from a null result — it indicates the entity was expected but does not exist.

## Description

JPA provides multiple ways to retrieve entities, each with different failure modes. `find()` returns null when not found, while `getReference()` and `EntityManager.find()` can throw `EntityNotFoundException` when the entity does not exist. Common message variants include:

- `Entity not found`
- `No entity found for query`
- `javax.persistence.EntityNotFoundException`
- `Unable to find entity with id: X`
- `Entity was not found in the database`

## Common Causes

```java
// Cause 1: Using getReference() for non-existent entity
User user = entityManager.getReference(User.class, 999L);  // ID 999 doesn't exist
user.getName();  // EntityNotFoundException when proxy is accessed

// Cause 2: Wrong ID type or value
User user = entityManager.find(User.class, "999");  // ID is Long, not String

// Cause 3: Entity deleted between lookup and use
User user = userRepository.findById(1L).orElseThrow();
// Another transaction deletes user
userService.update(user);  // EntityNotFoundException on flush

// Cause 4: Wrong entity class in find
Order order = entityManager.find(Order.class, userId);  // Should be User.class

// Cause 5: JPQL query returns no results when one is expected
User user = entityManager.createQuery("SELECT u FROM User u WHERE u.id = :id", User.class)
    .setParameter("id", 999L)
    .getSingleResult();  // NoResultException — similar to EntityNotFoundException
```

## Solutions

### Fix 1: Use findById() with proper error handling

```java
@Service
public class UserService {

    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public User getUser(Long id) {
        return userRepository.findById(id)
            .orElseThrow(() -> new ResourceNotFoundException("User not found with id: " + id));
    }

    public Optional<User> findUser(Long id) {
        return userRepository.findById(id);  // Returns Optional.empty() if not found
    }
}

@RestControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleNotFound(ResourceNotFoundException ex) {
        return ResponseEntity.status(HttpStatus.NOT_FOUND)
            .body(new ErrorResponse("NOT_FOUND", ex.getMessage()));
    }
}
```

### Fix 2: Use find() instead of getReference() when you need to check existence

```java
@Service
public class UserService {

    private final EntityManager entityManager;

    public UserService(EntityManager entityManager) {
        this.entityManager = entityManager;
    }

    // find() — returns null if not found (no exception)
    public User findUser(Long id) {
        return entityManager.find(User.class, id);  // null if not found
    }

    // getReference() — creates proxy, throws on access if not found
    public User getReference(Long id) {
        User user = entityManager.getReference(User.class, id);
        return user;  // Safe — but access later may throw
    }
}
```

### Fix 3: Verify IDs before operations

```java
@Service
public class OrderService {

    private final UserRepository userRepository;
    private final OrderRepository orderRepository;

    public OrderService(UserRepository userRepository, OrderRepository orderRepository) {
        this.userRepository = userRepository;
        this.orderRepository = orderRepository;
    }

    @Transactional
    public Order createOrder(Long userId, CreateOrderRequest request) {
        User user = userRepository.findById(userId)
            .orElseThrow(() -> new ResourceNotFoundException("User not found"));

        Order order = new Order();
        order.setUser(user);
        order.setTotal(request.total());
        return orderRepository.save(order);
    }
}
```

### Fix 4: Handle persistence context correctly

```java
@Service
public class UserService {

    private final EntityManager entityManager;

    public UserService(EntityManager entityManager) {
        this.entityManager = entityManager;
    }

    @Transactional
    public User updateUser(Long id, UserUpdateRequest request) {
        User user = entityManager.find(User.class, id);
        if (user == null) {
            throw new ResourceNotFoundException("User not found: " + id);
        }
        user.setName(request.name());
        // No explicit save needed — dirty checking handles update
        return user;
    }

    @Transactional
    public void deleteUser(Long id) {
        User user = entityManager.find(User.class, id);
        if (user != null) {
            entityManager.remove(user);
        }
    }
}
```

### Fix 5: Use named queries with proper exception handling

```java
@Entity
@NamedQuery(name = "User.findByEmail",
    query = "SELECT u FROM User u WHERE u.email = :email")
public class User { ... }

@Repository
public class UserRepositoryImpl {

    private final EntityManager entityManager;

    public UserRepositoryImpl(EntityManager entityManager) {
        this.entityManager = entityManager;
    }

    public Optional<User> findByEmail(String email) {
        try {
            User user = entityManager.createNamedQuery("User.findByEmail", User.class)
                .setParameter("email", email)
                .getSingleResult();
            return Optional.of(user);
        } catch (NoResultException e) {
            return Optional.empty();
        }
    }
}
```

## Prevention Checklist

- Prefer `findById()` over `getReference()` when you need to verify existence
- Use `Optional` return types and handle empty results gracefully
- Validate entity IDs before performing operations in service methods
- Define custom `ResourceNotFoundException` for consistent error handling
- Add `@ExceptionHandler` for `EntityNotFoundException` in a global handler
- Never assume an entity exists — always check and handle the not-found case

## Related Errors

- [NoResultException](/languages/java/nosuchelementexception/)
- [TransactionRequiredException](/languages/java/jpa-transaction-required/)
- [Hibernate ConstraintViolationException](/languages/java/hibernate-constraint-violation/)
