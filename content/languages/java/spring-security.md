---
title: "[Solution] AccessDeniedException — Spring Security Authorization Fix"
description: "Fix Spring Security AccessDeniedException when a user lacks required permissions. Configure roles, @PreAuthorize, and security expressions."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# AccessDeniedException — Spring Security Authorization Fix

An `AccessDeniedException` is thrown when an authenticated user attempts to access a resource they do not have permission for. Spring Security throws this exception when the authorization rules deny access.

## What This Error Means

The exception is thrown by the security filter chain after authentication succeeds but authorization fails. Common message formats:

- `Access is denied`
- `Forbidden`
- `403 Forbidden`

## Common Causes

```java
// Cause 1: Missing role annotation
@RestController
@RequestMapping("/admin")
public class AdminController {
    @GetMapping("/users")
    public List<User> getUsers() { ... }  // No role check
}

// Cause 2: Overly restrictive security config
http.authorizeHttpRequests(auth -> auth
    .anyRequest().hasRole("ADMIN")  // All requests need ADMIN
);

// Cause 3: @PreAuthorize expression evaluates to false
@PreAuthorize("hasRole('ADMIN') and #id == authentication.principal.id")
public User getUser(Long id) { ... }

// Cause 4: CSRF token missing or invalid
```

## How to Fix

### Fix 1: Add role-based access control

```java
@RestController
@RequestMapping("/admin")
@PreAuthorize("hasRole('ADMIN')")
public class AdminController {

    @GetMapping("/users")
    @PreAuthorize("hasAnyRole('ADMIN', 'SUPERVISOR')")
    public List<User> getUsers() { ... }
}
```

### Fix 2: Configure security properly

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http.authorizeHttpRequests(auth -> auth
            .requestMatchers("/public/**").permitAll()
            .requestMatchers("/admin/**").hasRole("ADMIN")
            .anyRequest().authenticated()
        );
        return http.build();
    }
}
```

### Fix 3: Handle AccessDeniedException globally

```java
@ControllerAdvice
public class SecurityExceptionHandler {

    @ExceptionHandler(AccessDeniedException.class)
    public ResponseEntity<String> handleAccessDenied(AccessDeniedException ex) {
        return ResponseEntity.status(HttpStatus.FORBIDDEN)
            .body("You do not have permission to access this resource");
    }
}
```

## Related Errors

- {{< relref "spring-bean" >}} — NoSuchBeanDefinitionException
- {{< relref "spring-aop" >}} — BeanCreationException in AOP
- {{< relref "spring-cloud-gateway" >}} — ResponseStatusException: 502
