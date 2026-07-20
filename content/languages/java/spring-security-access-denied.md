---
title: "[Solution] Java AccessDeniedException — Spring Security authorization failure"
description: "Fix Java AccessDeniedException by checking @PreAuthorize annotations, verifying roles, and configuring security rules. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 104
---

# AccessDeniedException — Spring Security authorization failure

An `AccessDeniedException` is thrown by Spring Security when an authenticated user attempts to access a resource they do not have the required permissions or roles for. Unlike authentication errors, the user is logged in but lacks authorization.

## Description

Spring Security evaluates authorization rules after successful authentication. When the access decision voter denies access, the `AccessDeniedHandler` is invoked and the exception is thrown. Common message variants include:

- `Access is denied`
- `Forbidden`
- `403 Forbidden`
- `org.springframework.security.access.AccessDeniedException: Access is denied`

## Common Causes

```java
// Cause 1: Missing @PreAuthorize or role check
@RestController
@RequestMapping("/admin")
public class AdminController {
    @GetMapping("/users")
    public List<User> getUsers() { ... }  // No role restriction — or wrong config
}

// Cause 2: Overly restrictive security configuration
http.authorizeHttpRequests(auth -> auth
    .anyRequest().hasRole("ADMIN")  // All requests require ADMIN
);

// Cause 3: @PreAuthorize expression evaluates to false
@PreAuthorize("hasRole('ADMIN') and #id == authentication.principal.id")
public User getUser(Long id) { ... }  // User is not ADMIN

// Cause 4: CSRF token missing or invalid on state-changing request
@PostMapping("/transfer")
public void transfer(@RequestBody TransferRequest req) { ... }

// Cause 5: Method-level security not enabled
// Missing @EnableMethodSecurity on configuration class
```

## Solutions

### Fix 1: Add role-based access control annotations

```java
@RestController
@RequestMapping("/api/users")
public class UserController {

    @GetMapping("/{id}")
    @PreAuthorize("hasAnyRole('USER', 'ADMIN')")
    public User getUser(@PathVariable Long id) {
        return userService.findById(id);
    }

    @DeleteMapping("/{id}")
    @PreAuthorize("hasRole('ADMIN')")
    public void deleteUser(@PathVariable Long id) {
        userService.delete(id);
    }
}
```

### Fix 2: Configure security rules properly

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/public/**").permitAll()
                .requestMatchers("/api/admin/**").hasRole("ADMIN")
                .requestMatchers("/api/user/**").hasAnyRole("USER", "ADMIN")
                .anyRequest().authenticated()
            )
            .csrf(csrf -> csrf
                .ignoringRequestMatchers("/api/**")  // Disable for REST APIs
            )
            .exceptionHandling(ex -> ex
                .accessDeniedHandler((request, response, accessDeniedException) -> {
                    response.setStatus(HttpServletResponse.SC_FORBIDDEN);
                    response.getWriter().write("{\"error\": \"Access denied\"}");
                })
            );
        return http.build();
    }
}
```

### Fix 3: Enable method security

```java
@Configuration
@EnableMethodSecurity  // Enables @PreAuthorize, @PostAuthorize
public class MethodSecurityConfig {}

// Now method-level annotations work
@Service
public class OrderService {
    @PreAuthorize("#order.userId == authentication.principal.id")
    public void cancelOrder(Order order) {
        // Only the order owner can cancel
    }
}
```

### Fix 4: Use SpEL expressions for fine-grained access

```java
@PreAuthorize("hasRole('ADMIN') or #username == authentication.name")
public UserProfile getProfile(String username) {
    return userService.getProfile(username);
}

@PostAuthorize("returnObject.owner == authentication.name")
public Document getDocument(Long id) {
    return documentRepository.findById(id);
}

@PreAuthorize("hasAuthority('documents:write') and @securityChecker.isOwner(#id, authentication)")
public void updateDocument(Long id, Document doc) {
    documentRepository.save(doc);
}
```

### Fix 5: Configure custom access denied handler

```java
@Component
public class CustomAccessDeniedHandler implements AccessDeniedHandler {

    @Override
    public void handle(HttpServletRequest request,
                       HttpServletResponse response,
                       AccessDeniedException accessDeniedException) {
        if (isAjax(request)) {
            response.setStatus(HttpServletResponse.SC_FORBIDDEN);
            response.setContentType("application/json");
            response.getWriter().write("{\"error\": \"Insufficient permissions\"}");
        } else {
            response.sendRedirect("/access-denied");
        }
    }

    private boolean isAjax(HttpServletRequest request) {
        return "XMLHttpRequest".equals(request.getHeader("X-Requested-With"));
    }
}
```

## Prevention Checklist

- Enable `@EnableMethodSecurity` for method-level authorization
- Use `@PreAuthorize` with clear role and ownership expressions
- Test authorization rules for every endpoint with different roles
- Configure `AccessDeniedHandler` for consistent error responses
- Verify CSRF configuration matches your API type (REST vs. form-based)
- Log access denied events for security auditing

## Related Errors

- [AuthenticationException](/languages/java/spring-security-authentication-failed/)
- [InsufficientAuthenticationException](/languages/java/spring-security-authentication-failed/)
- [SecurityException](/languages/java/securityexception/)
