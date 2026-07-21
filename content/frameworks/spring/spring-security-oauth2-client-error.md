---
title: "[Solution] Spring Security OAuth2 Client Error"
description: "Fix Spring Security OAuth2 client errors when login with external providers fails or tokens are not obtained."
frameworks: ["spring"]
error-types: ["authentication-error"]
severities: ["error"]
---

OAuth2 client errors occur when the application cannot obtain tokens from the authorization server or the callback fails.

## Common Causes

- Client ID or secret incorrect
- Redirect URI does not match registered URI
- Authorization server URL wrong
- Scope not requested correctly
- PKCE challenge not configured for public clients

## How to Fix

### Configure OAuth2 Client

```yaml
# application.yml
spring:
  security:
    oauth2:
      client:
        registration:
          google:
            client-id: your-client-id
            client-secret: your-client-secret
            scope:
              - openid
              - profile
              - email
          github:
            client-id: your-github-client-id
            client-secret: your-github-client-secret
        provider:
          google:
            issuer-uri: https://accounts.google.com
          github:
            authorization-uri: https://github.com/login/oauth/authorize
            token-uri: https://github.com/login/oauth/access_token
            user-info-uri: https://api.github.com/user
```

### Configure Security for OAuth2 Login

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests(auth -> auth
                .anyRequest().authenticated()
            )
            .oauth2Login(oauth2 -> oauth2
                .loginPage("/login")
                .defaultSuccessUrl("/dashboard")
            );
        return http.build();
    }
}
```

### Handle OAuth2 Errors

```java
@ControllerAdvice
public class OAuth2ExceptionHandler {
    @ExceptionHandler(OAuth2AuthenticationException.class)
    public ResponseEntity<Map<String, String>> handleOAuth2Error(OAuth2AuthenticationException e) {
        return ResponseEntity.badRequest()
            .body(Map.of("error", e.getError().getErrorCode(), "description", e.getError().getDescription()));
    }
}
```

## Examples

```yaml
# Bug -- wrong redirect URI
spring:
  security:
    oauth2:
      client:
        registration:
          google:
            redirect-uri: "{baseUrl}/login/oauth2/code/google"
            # Must match registered URI in Google Console

# Fix -- correct redirect URI
spring:
  security:
    oauth2:
      client:
        registration:
          google:
            redirect-uri: "{baseUrl}/login/oauth2/code/{registrationId}"
```
