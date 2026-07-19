---
title: "[Solution] JPA Detached Entity Passed to Persist"
description: "Fix javax.persistence.PersistenceException detached entity passed to persist. Resolve JPA detached entity issues."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Detached Entity Passed to Persist

A `PersistenceException` with message `detached entity passed to persist` occurs when a JPA entity that is no longer associated with the current persistence context (session) is passed to `persist()`. This happens when the entity was loaded in a previous transaction or was explicitly detached.

## What This Error Means

When a persistence context (EntityManager/Session) is closed, all entities it managed become "detached." Detached entities retain their data and ID but are no longer tracked by JPA. Attempting to persist a detached entity fails because JPA cannot distinguish between "save new" and "update existing" without context.

## Common Causes

```java
// Cause 1: Entity loaded in one transaction, persisted in another
@Transactional
public User getUser(Long id) {
    return entityManager.find(User.class, id);
    // Transaction ends, entity becomes detached
}

@Transactional
public void updateUser(User user) {
    user.setName("New Name");
    entityManager.persist(user);  // Detached entity — fails
}

// Cause 2: Entity deserialized from HTTP request
// Controller receives User JSON, entity is detached
@PostMapping("/users/{id}")
public User update(@PathVariable Long id, @RequestBody User user) {
    entityManager.persist(user);  // Detached — not managed
}

// Cause 3: Entity removed from one context, persisted in another
entityManager.remove(entity);
entityManager.persist(entity);  // May fail depending on state
```

## How to Fix

### Fix 1: Use merge() for detached entities

```java
@Transactional
public User updateUser(Long id, String newName) {
    User user = entityManager.find(User.class, id);
    entityManager.detach(user);
    user.setName(newName);
    return entityManager.merge(user);  // Reattaches and updates
}
```

### Fix 2: Use @Transactional to keep entity managed

```java
@Transactional
public User updateUser(User user) {
    // If user is detached, merge first
    User managed = entityManager.merge(user);
    managed.setName("Updated");
    return managed;
    // Transaction commits, changes are persisted
}
```

### Fix 3: Load entity fresh within the transaction

```java
@PostMapping("/users/{id}")
public ResponseEntity<User> update(@PathVariable Long id, @RequestBody UserUpdateDto dto) {
    User existing = userRepository.findById(id).orElseThrow();
    existing.setName(dto.getName());
    existing.setEmail(dto.getEmail());
    userRepository.save(existing);  // save() handles detached correctly
    return ResponseEntity.ok(existing);
}
```

### Fix 4: Use @Transactional(REQUIRES_NEW) carefully

```java
@Service
public class UserService {
    @Transactional
    public void processUser(Long id) {
        User user = entityManager.find(User.class, id);
        auditService.logAccess(user);  // Calls separate transaction
        user.setStatus(Status.PROCESSED);
        entityManager.merge(user);
    }
}

@Service
public class AuditService {
    @Transactional(REQUIRES_NEW)
    public void logAccess(User user) {
        // user may be detached in this new transaction
        AuditLog log = new AuditLog();
        log.setUserId(user.getId());
        auditLogRepository.save(log);
    }
}
```

## Prevention Tips

- Always use `merge()` when the entity may be detached.
- Keep entity loading and modification within the same `@Transactional` boundary.
- Use DTOs for API boundaries to avoid passing entities across transaction boundaries.
- Prefer Spring Data `save()` which automatically handles persist vs merge.

## Related Errors

- {{< relref "jpa-entity-exists" >}} — EntityExistsException
- {{< relref "hibernate-proxy-init" >}} — LazyInitializationException
- {{< relref "jpa-optimistic-lock" >}} — Optimistic lock failure
