---
title: "[Solution] Spring Security Memory Leak Error"
description: "Fix Spring Security memory leaks when SecurityContext is not properly released between requests."
frameworks: ["spring"]
error-types: ["performance-error"]
severities: ["error"]
---

Memory leaks in Spring Security occur when `SecurityContext` is not cleared after request processing, holding references to authentication objects.

## Common Causes

- `SecurityContextPersistenceFilter` not clearing context
- Custom filter not releasing SecurityContext
- Thread pool reuses threads with stale context
- Async processing not clearing SecurityContext
- Test context not properly cleaned up

## How to Fix

### Ensure Security Context is Cleared

```java
@Configuration
public class SecurityConfig {
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .securityContext(securityContext -> securityContext
                .requireExplicitSave(false)  // Auto-save and clear
            )
            .sessionManagement(session -> session
                .sessionCreationPolicy(SessionCreationPolicy.STATELESS)
            );
        return http.build();
    }
}
```

### Clear Context in Async Processing

```java
@Component
public class AsyncSecurityFilter implements Filter {
    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) {
        try {
            SecurityContextHolder.setContext(createSecurityContext(request));
            chain.doFilter(request, response);
        } finally {
            SecurityContextHolder.clearContext();
        }
    }
}
```

### Monitor Memory Usage

```java
@Component
public class SecurityContextMonitor {
    @Scheduled(fixedRate = 60000)
    public void monitorContexts() {
        log.info("Active SecurityContexts: {}", SecurityContextHolder.getContext());
    }
}
```

## Examples

```java
// Bug -- not clearing context
@Component
public class CustomFilter implements Filter {
    @Override
    public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain) {
        SecurityContextHolder.setContext(createContext(req));
        chain.doFilter(req, res);
        // Context not cleared!
    }
}

// Fix -- clear in finally block
@Component
public class CustomFilter implements Filter {
    @Override
    public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain) {
        try {
            SecurityContextHolder.setContext(createContext(req));
            chain.doFilter(req, res);
        } finally {
            SecurityContextHolder.clearContext();
        }
    }
}
```
