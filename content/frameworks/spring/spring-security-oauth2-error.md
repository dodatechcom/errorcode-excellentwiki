---
title: "[Solution] Spring Security OAuth2 Error"
description: "Fix Spring Security OAuth2 errors when token validation, resource server configuration, or client authentication fails."
frameworks: ["spring"]
error-types: ["security-error"]
severities: ["error"]
---

OAuth2 errors in Spring Security occur when token validation fails, client configuration is incorrect, or resource server cannot verify tokens.

## Common Causes

- JWT issuer URL not configured correctly
- JWK endpoint not accessible
- Client ID or secret misconfigured
- Token not included in Authorization header
- Scopes do not match required permissions

## How to Fix

### Configure Resource Server

```java
@Configuration
@EnableResourceServer
public class ResourceServerConfig extends ResourceServerConfigurerAdapter {
    @Override
    public void configure(HttpSecurity http) throws Exception {
        http.authorizeRequests()
            .antMatchers("/api/public/**").permitAll()
            .antMatchers("/api/**").authenticated()
            .and().cors();
    }

    @Override
    public void configure(ResourceServerSecurityConfigurer resources) {
        resources.resourceId("my-api");
    }
}
```

### Configure JWT Validation

```yaml
# application.yml
security:
  oauth2:
    resourceserver:
      jwt:
        issuer-uri: https://auth.example.com/
        jwk-set-uri: https://auth.example.com/.well-known/jwks.json
```

### Handle Token Errors

```java
@RestControllerAdvice
public class OAuth2ErrorHandler {
    @ExceptionHandler(AccessDeniedException.class)
    public ResponseEntity<Map<String, String>> handleAccessDenied(AccessDeniedException e) {
        return ResponseEntity.status(HttpStatus.FORBIDDEN)
            .body(Map.of("error", "access_denied", "message", e.getMessage()));
    }
}
```

## Examples

```java
@Configuration
public class SecurityConfig {
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/public/**").permitAll()
                .anyRequest().authenticated()
            )
            .oauth2ResourceServer(oauth2 -> oauth2
                .jwt(jwt -> jwt.jwtAuthenticationConverter(jwtAuthConverter()))
            );
        return http.build();
    }
}
```

Common error: `Invalid JWT signature` -- ensure the JWK URI is correct and the signing key matches.
