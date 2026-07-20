---
title: "[Solution] Java SessionException — Hibernate session closed during operation"
description: "Fix Java SessionException by checking session lifecycle, using current session, and handling transactions properly. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 107
---

# SessionException — Hibernate session closed during operation

A `SessionException` is thrown when Hibernate attempts to execute an operation on a Session that has already been closed. This typically occurs when code tries to interact with entities after the persistence context has ended.

## Description

Hibernate Sessions are bound to transactions. When a transaction completes, the Session is closed and any further database operations through that Session fail. Common message variants include:

- `Session was already closed`
- `Session is closed`
- `Could not open connection`
- `org.hibernate.SessionException: Session is closed`
- `org.hibernate.resource.jdbc.internal.LogicalConnectionManagedImpl: Connection is not available`

## Common Causes

```java
// Cause 1: Using session after transaction commits
Session session = sessionFactory.openSession();
Transaction tx = session.beginTransaction();
User user = session.get(User.class, 1L);
tx.commit();
session.close();

session.update(user);  // SessionException — session already closed

// Cause 2: Using open session outside transaction
Session session = sessionFactory.openSession();
// No transaction started
session.createQuery("FROM User").list();  // May fail

// Cause 3: Accessing entity after OpenEntityManagerInView filter closes
// In a long-running request with lazy loading outside the filter

// Cause 4: Multi-thread access to same session
// Sessions are not thread-safe — sharing between threads causes this

// Cause 5: SessionFactory is closed
sessionFactory.close();
sessionFactory.openSession();  // SessionFactory is already closed
```

## Solutions

### Fix 1: Use Spring's current session with @Transactional

```java
@Service
public class UserService {

    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Transactional
    public User updateUser(Long id, UserUpdateRequest request) {
        // Spring manages the session lifecycle
        User user = userRepository.findById(id).orElseThrow();
        user.setName(request.name());
        return userRepository.save(user);
        // Session closes after transaction completes
    }

    @Transactional(readOnly = true)
    public User getUser(Long id) {
        // Read-only transaction, session open during method
        return userRepository.findById(id).orElseThrow();
    }
}
```

### Fix 2: Use sessionFactory.openSession() with try-with-resources

```java
@Service
public class LegacyMigrationService {

    private final SessionFactory sessionFactory;

    public LegacyMigrationService(SessionFactory sessionFactory) {
        this.sessionFactory = sessionFactory;
    }

    public void migrateUsers() {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = session.beginTransaction();
            try {
                List<User> users = session.createQuery("FROM User", User.class).list();
                for (User user : users) {
                    // Process user
                }
                tx.commit();
            } catch (Exception e) {
                tx.rollback();
                throw e;
            }
        }  // Session auto-closed here
    }
}
```

### Fix 3: Use StatelessSession for batch operations

```java
@Service
public class BatchService {

    private final SessionFactory sessionFactory;

    public BatchService(SessionFactory sessionFactory) {
        this.sessionFactory = sessionFactory;
    }

    @Transactional
    public void batchUpdate(List<User> users) {
        StatelessSession statelessSession = sessionFactory.openStatelessSession();
        Transaction tx = statelessSession.beginTransaction();
        try {
            for (User user : users) {
                statelessSession.update(user);
            }
            tx.commit();
        } catch (Exception e) {
            tx.rollback();
            throw e;
        } finally {
            statelessSession.close();
        }
    }
}
```

### Fix 4: Prevent thread sharing

```java
// WRONG — sharing session between threads
@Service
public class BadService {
    private Session sharedSession;  // Not thread-safe

    @PostConstruct
    public void init() {
        sharedSession = sessionFactory.openSession();
    }
}

// CORRECT — create session per method
@Service
public class GoodService {

    @Transactional
    public User getUser(Long id) {
        // Each method gets its own session from Spring
        return userRepository.findById(id).orElseThrow();
    }
}
```

### Fix 5: Check SessionFactory status before opening

```java
@Service
public class ResilientSessionService {

    private final SessionFactory sessionFactory;

    public ResilientSessionService(SessionFactory sessionFactory) {
        this.sessionFactory = sessionFactory;
    }

    public void safeQuery() {
        if (!sessionFactory.isOpen()) {
            throw new IllegalStateException("SessionFactory is closed");
        }

        try (Session session = sessionFactory.openSession()) {
            List<User> users = session.createQuery("FROM User", User.class).list();
            // Process results
        }
    }
}
```

## Prevention Checklist

- Use `@Transactional` and let Spring manage the Session lifecycle
- Never share a Session between threads
- Use `try-with-resources` when manually opening Sessions
- Prefer `StatelessSession` for batch operations that do not need caching
- Check `SessionFactory.isOpen()` before creating Sessions in long-running processes
- Enable `spring.jpa.open-in-view=false` to avoid implicit sessions in controllers

## Related Errors

- [LazyInitializationException](/languages/java/hibernate-lazy-loading-error/)
- [TransactionRequiredException](/languages/java/jpa-transaction-required/)
- [PersistenceException](/languages/java/persistenceexception/)
