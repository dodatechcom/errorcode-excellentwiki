---
title: "AccessDeniedException - access denied"
description: "Spring throws AccessDeniedException when a user lacks the required permissions to access a resource"
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["security", "access-denied", "authorization", "spring-security", "role"]
weight: 5
---

This error occurs when an authenticated user attempts to access a resource they do not have permission for. Spring Security throws `AccessDeniedException` and returns a 403 Forbidden response.

## Common Causes

- User does not have the required role or authority
- `@PreAuthorize` or `@Secured` annotation denies access
- CSRF token validation failure in Spring Security
- Method-level security constraint violated
- Missing security configuration for the endpoint

## How to Fix

1. Configure role-based access in SecurityConfig:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/admin/**").hasRole("ADMIN")
                .requestMatchers("/api/**").hasAuthority("SCOPE_read")
                .anyRequest().authenticated()
            );
        return http.build();
    }
}
```

2. Use method-level security annotations:

```java
@Service
public class DocumentService {

    @PreAuthorize("hasRole('ADMIN') or #document.owner == authentication.name")
    public Document getDocument(Document document) {
        return document;
    }
}
```

3. Handle AccessDeniedException globally:

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(AccessDeniedException.class)
    public ResponseEntity<Map<String, String>> handleAccessDenied(AccessDeniedException ex) {
        return ResponseEntity.status(HttpStatus.FORBIDDEN)
            .body(Map.of("error", "Access denied", "message", ex.getMessage()));
    }
}
```

## Examples

```java
@PreAuthorize("hasRole('ADMIN')")
public void deleteUser(Long id) { ... }
// AccessDeniedException: Forbidden — user does not have role ADMIN
```

## Related Errors

- [Bean not found]({{< relref "/frameworks/spring/spring-bean-not-found" >}})
- [Security config error]({{< relref "/frameworks/spring/spring-security-error" >}})
