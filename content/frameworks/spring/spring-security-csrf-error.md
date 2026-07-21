---
title: "[Solution] Spring Security CSRF Error"
description: "Fix Spring Security CSRF errors when form submissions or API requests are rejected by CSRF protection."
frameworks: ["spring"]
error-types: ["security-error"]
severities: ["error"]
---

CSRF errors in Spring Security occur when the CSRF token is missing, invalid, or the request does not include the expected token format.

## Common Causes

- CSRF token not included in form submission
- AJAX request missing CSRF token header
- Token expired or session rotated
- API endpoints requiring CSRF tokens
- Thymeleaf form not using `th:action`

## How to Fix

### Configure CSRF for Web Applications

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .csrf(csrf -> csrf
                .csrfTokenRepository(CookieCsrfTokenRepository.withHttpOnlyFalse())
            )
            .authorizeHttpRequests(auth -> auth
                .anyRequest().authenticated()
            );
        return http.build();
    }
}
```

### Include CSRF Token in Forms

```html
<form th:action="@{/submit}" method="post">
    <input type="hidden" th:name="${_csrf.parameterName}" th:value="${_csrf.token}"/>
    <input type="text" name="data"/>
    <button type="submit">Submit</button>
</form>
```

### Add CSRF Token to AJAX

```javascript
fetch("/api/data", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        "X-XSRF-TOKEN": getCookie("XSRF-TOKEN"),
    },
    body: JSON.stringify({data: "value"}),
});
```

### Disable CSRF for API Endpoints

```java
http
    .csrf(csrf -> csrf
        .ignoringRequestMatchers("/api/**")
    )
    .authorizeHttpRequests(auth -> auth
        .requestMatchers("/api/**").authenticated()
        .anyRequest().authenticated()
    );
```

## Examples

```java
// Bug -- CSRF enabled for REST API
http.csrf().disable();  // Too permissive

// Fix -- disable only for API routes
http
    .csrf(csrf -> csrf
        .ignoringRequestMatchers("/api/**")
    );
```

For stateless REST APIs, CSRF is typically not needed. Disable it for `/api/**` paths.
