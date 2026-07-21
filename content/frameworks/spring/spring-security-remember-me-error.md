---
title: "[Solution] Spring Security Remember Me Error"
description: "Fix Spring Security remember-me errors when persistent login tokens fail to authenticate or are not created."
frameworks: ["spring"]
error-types: ["authentication-error"]
severities: ["error"]
---

Remember-me errors occur when persistent login tokens are not properly generated, stored, or validated.

## Common Causes

- Token repository not configured
- Secret key for token generation not set
- Token table not created in database
- Token expired but not cleaned up
- Cookie domain or path incorrect

## How to Fix

### Configure Remember-Me

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .rememberMe(remember -> remember
                .key("unique-key")
                .tokenValiditySeconds(86400 * 30)  // 30 days
                .userDetailsService(userDetailsService)
            );
        return http.build();
    }
}
```

### Use Persistent Token Repository

```java
@Bean
public PersistentTokenRepository persistentTokenRepository() {
    JdbcTokenRepositoryImpl tokenRepository = new JdbcTokenRepositoryImpl();
    tokenRepository.setDataSource(dataSource);
    tokenRepository.setCreateTableOnStartup(false);
    return tokenRepository;
}
```

### Create Token Table

```sql
CREATE TABLE persistent_logins (
    username VARCHAR(64) NOT NULL,
    series VARCHAR(64) PRIMARY KEY,
    token VARCHAR(64) NOT NULL,
    last_used TIMESTAMP NOT NULL
);
```

### Handle Token Errors

```java
http
    .rememberMe(remember -> remember
        .tokenRepository(persistentTokenRepository())
        .authenticationSuccessHandler((request, response, authentication) -> {
            response.sendRedirect("/dashboard");
        })
    );
```

## Examples

```java
// Bug -- no token repository
http.rememberMe(remember -> remember.key("secret"));
// Tokens stored in memory, lost on restart

// Fix -- use database repository
http.rememberMe(remember -> remember
    .tokenRepository(persistentTokenRepository())
    .key("secret")
);
```
