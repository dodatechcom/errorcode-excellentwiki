---
title: "[Solution] Spring Security CORS Error"
description: "Fix Spring Security CORS errors when cross-origin requests are blocked by security configuration."
frameworks: ["spring"]
error-types: ["security-error"]
severities: ["error"]
---

CORS errors in Spring Security occur when the security configuration does not include CORS headers or the preflight request is not handled.

## Common Causes

- CORS configuration not added to SecurityFilterChain
- Preflight OPTIONS request blocked by security
- Origins list does not include the requesting origin
- Credentials not allowed for wildcard origins
- Security headers interfere with CORS

## How to Fix

### Configure CORS with Security

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .cors(cors -> cors.configurationSource(corsConfigurationSource()))
            .authorizeHttpRequests(auth -> auth
                .anyRequest().authenticated()
            );
        return http.build();
    }

    @Bean
    public CorsConfigurationSource corsConfigurationSource() {
        CorsConfiguration config = new CorsConfiguration();
        config.setAllowedOrigins(List.of("https://myapp.com", "https://admin.myapp.com"));
        config.setAllowedMethods(List.of("GET", "POST", "PUT", "DELETE", "OPTIONS"));
        config.setAllowedHeaders(List.of("Authorization", "Content-Type"));
        config.setAllowCredentials(true);

        UrlBasedCorsConfigurationSource source = new UrlBasedCorsConfigurationSource();
        source.registerCorsConfiguration("/**", config);
        return source;
    }
}
```

### Handle OPTIONS Request

```java
http
    .cors(cors -> cors.configurationSource(corsConfigurationSource()))
    .csrf(csrf -> csrf.ignoringRequestMatchers("/api/**"))
    .authorizeHttpRequests(auth -> auth
        .requestMatchers(HttpMethod.OPTIONS, "/**").permitAll()
        .anyRequest().authenticated()
    );
```

## Examples

```java
// Bug -- no CORS in security config
http.authorizeHttpRequests(auth -> auth.anyRequest().authenticated());
// CORS headers not added

// Fix -- add CORS
http.cors(cors -> cors.configurationSource(corsConfigurationSource()));
```
