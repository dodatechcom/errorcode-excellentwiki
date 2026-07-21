---
title: "[Solution] Spring Security Method Security Error"
description: "Fix Spring Security method-level security errors when @PreAuthorize or @Secured annotations are not enforced."
frameworks: ["spring"]
error-types: ["security-error"]
severities: ["error"]
---

Method security errors occur when `@PreAuthorize`, `@PostAuthorize`, or `@Secured` annotations are not enforced due to missing configuration.

## Common Causes

- `@EnableMethodSecurity` annotation missing
- AOP proxy not created for the bean
- SpEL expression has syntax errors
- Security context not propagated to method
- Custom permission evaluator not configured

## How to Fix

### Enable Method Security

```java
@Configuration
@EnableMethodSecurity
public class SecurityConfig {
}
```

### Use Method Security Annotations

```java
@Service
public class UserService {
    @PreAuthorize("hasRole('ADMIN')")
    public User deleteUser(Long id) {
        return userRepository.deleteById(id);
    }

    @PreAuthorize("#userId == authentication.principal.id")
    public User getUser(Long userId) {
        return userRepository.findById(userId).orElse(null);
    }

    @PostAuthorize("returnObject.id == authentication.principal.id")
    public User getOwnProfile(Long id) {
        return userRepository.findById(id).orElse(null);
    }

    @Secured({"ROLE_ADMIN", "ROLE_MANAGER"})
    public List<User> getAllUsers() {
        return userRepository.findAll();
    }
}
```

### Configure Custom Permission Evaluator

```java
@Component
public class CustomPermissionEvaluator implements PermissionEvaluator {
    @Override
    public boolean hasPermission(Authentication auth, Object target, Object permission) {
        return checkPermission(auth, target, permission.toString());
    }

    @Override
    public boolean hasPermission(Authentication auth, Serializable targetId, String targetType, Object permission) {
        return checkPermission(auth, targetType, permission.toString());
    }

    private boolean checkPermission(Authentication auth, Object target, String permission) {
        // Custom permission logic
        return true;
    }
}
```

## Examples

```java
// Bug -- no @EnableMethodSecurity
@Service
public class UserService {
    @PreAuthorize("hasRole('ADMIN')")
    public void adminOnly() {
        // Not enforced -- any user can call
    }
}

// Fix -- add annotation
@Configuration
@EnableMethodSecurity
public class SecurityConfig {}
```
