---
title: "[Solution] Spring Actuator Error"
description: "Fix Spring Actuator errors when health checks, metrics, or management endpoints fail."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Actuator errors occur when management endpoints are not accessible, health checks fail, or metrics are not properly exposed.

## Common Causes

- Actuator dependency not in classpath
- Endpoints not enabled in configuration
- Security blocks management endpoints
- Health indicator not properly configured
- Custom health check throws exception

## How to Fix

### Add Actuator Dependency

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
```

### Configure Endpoints

```yaml
# application.yml
management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics,prometheus
  endpoint:
    health:
      show-details: when-authorized
  health:
    db:
      enabled: true
```

### Expose Endpoints Securely

```java
@Configuration
public class ActuatorConfig {
    @Bean
    public SecurityFilterChain actuatorSecurity(HttpSecurity http) throws Exception {
        http
            .securityMatcher(EndpointRequest.toAnyEndpoint())
            .authorizeHttpRequests(auth -> auth
                .requestMatchers(EndpointRequest.to("health", "info")).permitAll()
                .anyRequest().authenticated()
            );
        return http.build();
    }
}
```

### Create Custom Health Indicator

```java
@Component
public class RedisHealthIndicator implements HealthIndicator {
    @Autowired
    private RedisConnectionFactory redisConnectionFactory;

    @Override
    public Health health() {
        try {
            redisConnectionFactory.getConnection().ping();
            return Health.up().withDetail("redis", "reachable").build();
        } catch (Exception e) {
            return Health.down().withDetail("redis", e.getMessage()).build();
        }
    }
}
```

## Examples

```yaml
# Bug -- no endpoints exposed
management:
  endpoints:
    web:
      exposure:
        include: ""  # No endpoints!

# Fix -- expose desired endpoints
management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics
```
