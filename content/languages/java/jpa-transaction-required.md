---
title: "[Solution] Java TransactionRequiredException — JPA operation requires an active transaction"
description: "Fix Java TransactionRequiredException by starting a transaction, using @Transactional, and checking persistence context. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 112
---

# TransactionRequiredException — JPA operation requires an active transaction

A `TransactionRequiredException` is thrown when a JPA persistence operation is attempted without an active transaction. JPA requires transactions for all data modification operations (insert, update, delete) and sometimes for reads depending on configuration.

## Description

JPA's EntityManager delegates all write operations to the underlying database within a transaction. Without an active transaction, the operation cannot proceed. Common message variants include:

- `Transaction required for entity manager operation`
- `javax.persistence.TransactionRequiredException: no transaction in progress`
- `Cannot perform this operation without an active transaction`
- `Entity manager must be joined to a transaction`

## Common Causes

```java
// Cause 1: Calling persist/merge/remove without transaction
@Service
public class UserService {
    private final EntityManager entityManager;

    public void saveUser(User user) {
        entityManager.persist(user);  // TransactionRequiredException!
    }
}

// Cause 2: Missing @Transactional annotation
@Service
public class OrderService {
    private final OrderRepository orderRepository;

    public void createOrder(Order order) {
        orderRepository.save(order);  // Spring Data needs @Transactional for writes
    }
}

// Cause 3: Calling repository method from outside Spring proxy
@Service
public class UserService {
    private final UserRepository userRepository;

    public void processUser() {
        this.updateUserInternal();  // Calls through this — bypasses proxy
    }

    @Transactional
    public void updateUserInternal() {
        // @Transactional doesn't work — called via this, not the proxy
    }
}

// Cause 4: EntityManager in application-managed mode without manual transaction
EntityManager em = entityManagerFactory.createEntityManager();
em.persist(user);  // TransactionRequiredException

// Cause 5: Read-only query with strict transaction requirement
User user = entityManager.find(User.class, 1L);  // May fail if JTA configured strictly
```

## Solutions

### Fix 1: Add @Transactional to service methods

```java
@Service
public class UserService {

    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Transactional
    public User createUser(CreateUserRequest request) {
        User user = new User();
        user.setName(request.name());
        user.setEmail(request.email());
        return userRepository.save(user);
    }

    @Transactional
    public User updateUser(Long id, UserUpdateRequest request) {
        User user = userRepository.findById(id).orElseThrow();
        user.setName(request.name());
        return userRepository.save(user);
    }

    @Transactional
    public void deleteUser(Long id) {
        userRepository.deleteById(id);
    }
}
```

### Fix 2: Use @Transactional(readOnly = true) for reads

```java
@Service
public class UserService {

    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Transactional(readOnly = true)
    public Optional<User> findById(Long id) {
        return userRepository.findById(id);
    }

    @Transactional(readOnly = true)
    public List<User> findAll() {
        return userRepository.findAll();
    }
}
```

### Fix 3: Fix self-invocation issue

```java
@Service
public class UserService {

    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    // WRONG — self-invocation bypasses proxy, no transaction
    public void processAll() {
        this.saveUser(new User());  // No transaction!
    }

    // CORRECT — inject self proxy
    @Lazy @Autowired private UserService self;

    public void processAll() {
        self.saveUser(new User());  // Transaction works
    }

    @Transactional
    public void saveUser(User user) {
        userRepository.save(user);
    }
}
```

### Fix 4: Use application-managed transactions explicitly

```java
@Service
public class LegacyService {

    private final EntityManagerFactory entityManagerFactory;

    public LegacyService(EntityManagerFactory entityManagerFactory) {
        this.entityManagerFactory = entityManagerFactory;
    }

    public void manualTransaction() {
        EntityManager em = entityManagerFactory.createEntityManager();
        EntityTransaction tx = em.getTransaction();
        try {
            tx.begin();
            User user = new User();
            user.setName("John");
            em.persist(user);
            tx.commit();
        } catch (Exception e) {
            if (tx.isActive()) {
                tx.rollback();
            }
            throw e;
        } finally {
            em.close();
        }
    }
}
```

### Fix 5: Configure Spring transaction manager

```java
@Configuration
@EnableTransactionManagement
public class TransactionConfig {

    @Bean
    public PlatformTransactionManager transactionManager(
            EntityManagerFactory entityManagerFactory) {
        JpaTransactionManager transactionManager = new JpaTransactionManager();
        transactionManager.setEntityManagerFactory(entityManagerFactory);
        return transactionManager;
    }
}
```

## Prevention Checklist

- Add `@Transactional` to all service methods that perform writes
- Use `@Transactional(readOnly = true)` for read-only operations
- Never call `@Transactional` methods from within the same class (self-invocation)
- Configure `PlatformTransactionManager` with the correct `EntityManagerFactory`
- Ensure all repository save/update/delete operations happen inside a transaction
- Use `@EnableTransactionManagement` in your configuration class

## Related Errors

- [EntityNotFoundException](/languages/java/jpa-entity-not-found/)
- [Hibernate SessionException](/languages/java/hibernate-session-closed-error/)
- [PersistenceException](/languages/java/persistenceexception/)
