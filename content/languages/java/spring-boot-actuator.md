---
title: "[Solution] Actuator Endpoint Error — Spring Boot Actuator Fix"
description: "Fix Spring Boot Actuator endpoint errors. Resolve endpointServletWebServerFactoryCustomizer issues and actuator configuration problems."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Actuator Endpoint Error — Spring Boot Actuator Fix

Actuator endpoint errors occur when Spring Boot's monitoring and management endpoints fail to initialize or respond correctly. The `EndpointServletWebServerFactoryCustomizer` error indicates a conflict in the web server factory configuration caused by actuator auto-configuration.

## What This Error Means

Common messages:

- `org.springframework.boot.actuate.autoconfigure.endpoint.EndpointServletWebServerFactoryCustomizer`
- `NoSuchBeanDefinitionException: No qualifying bean of type 'EndpointServletWebServerFactoryCustomizer'`
- `Actuator endpoint 'health' is not available`

## Common Causes

```java
// Cause 1: Actuator on a different port without proper config
management:
  server:
    port: 8081
  endpoints:
    web:
      exposure:
        include: health,info,metrics

// Cause 2: Custom WebServerFactory conflicting with actuator
@Bean
public ServletWebServerFactory servletWebServerFactory() {
    return new TomcatServletWebServerFactory(); // May conflict
}

// Cause 3: Security blocking actuator endpoints
// Spring Security configured without actuator endpoint rules
```

## How to Fix

### Fix 1: Configure actuator endpoints properly

Define which endpoints to expose and on which port to avoid conflicts with the main application.

```java
# application.yml
management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics,env,beans
      base-path: /actuator
  endpoint:
    health:
      show-details: when-authorized
    env:
      enabled: true
  server:
    port: 8081  # Separate port for actuator

# Allow actuator on same port with specific paths
management:
  endpoints:
    web:
      base-path: /manage
  server:
    port: ${server.port:8080}
```

### Fix 2: Add actuator Spring Security configuration

Secure actuator endpoints by allowing only authorized access to sensitive endpoints like env and beans.

```java
@Configuration
@EnableWebSecurity
public class ActuatorSecurityConfig {

    @Bean
    public SecurityFilterChain actuatorFilterChain(
            HttpSecurity http) throws Exception {
        http
            .securityMatcher("/actuator/**")
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/actuator/health").permitAll()
                .requestMatchers("/actuator/info").permitAll()
                .anyRequest().hasRole("ADMIN")
            )
            .httpBasic(Customizer.withDefaults());
        return http.build();
    }
}
```

### Fix 3: Create a custom actuator endpoint

Extend Spring Boot Actuator by creating a custom endpoint for application-specific health checks or operations.

```java
@Component
@Endpoint(id = "cache")
public class CacheEndpoint {

    private final CacheManager cacheManager;

    public CacheEndpoint(CacheManager cacheManager) {
        this.cacheManager = cacheManager;
    }

    @ReadOperation
    public Map<String, Object> cacheInfo() {
        Map<String, Object> info = new HashMap<>();
        cacheManager.getCacheNames().forEach(name -> {
            Cache cache = cacheManager.getCache(name);
            info.put(name, cache != null ? "active" : "null");
        });
        return info;
    }

    @WriteOperation
    public void evictAll() {
        cacheManager.getCacheNames().forEach(name -> {
            Objects.requireNonNull(cacheManager.getCache(name)).clear();
        });
    }
}
```

## Related Errors

- {{< relref "spring-boot-autoconfig-error" >}} — Auto-Configuration Failed
- {{< relref "spring-security" >}} — Spring Security Configuration Error
