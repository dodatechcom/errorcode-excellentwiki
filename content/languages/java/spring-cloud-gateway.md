---
title: "[Solution] ResponseStatusException 502 — Spring Cloud Gateway Fix"
description: "Fix ResponseStatusException 502 Bad Gateway in Spring Cloud Gateway. Resolve upstream service connectivity issues."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["spring-cloud", "gateway", "502", "bad-gateway", "load-balancer"]
weight: 5
---

# ResponseStatusException 502 — Spring Cloud Gateway Fix

A `ResponseStatusException` with status 502 (Bad Gateway) occurs when Spring Cloud Gateway cannot reach the upstream service. The gateway received an invalid response or no response from the target service.

## What This Error Means

Common message:

- `502 Bad Gateway`
- `ResponseStatusException: 502 Bad Gateway`

## Common Causes

```yaml
# Cause 1: Upstream service not running
spring:
  cloud:
    gateway:
      routes:
        - id: user-service
          uri: http://user-service:8080
          predicates:
            - Path=/api/users/**

# Cause 2: Service discovery not configured
spring:
  cloud:
    gateway:
      routes:
        - id: user-service
          uri: lb://user-service  # Load balanced but service not registered
```

## How to Fix

### Fix 1: Check upstream service

```bash
curl -v http://user-service:8080/actuator/health
netstat -tlnp | grep 8080
```

### Fix 2: Configure timeouts

```yaml
spring:
  cloud:
    gateway:
      httpclient:
        connect-timeout: 5000
        response-timeout: 10s
```

### Fix 3: Add fallback handling

```java
@RestController
public class FallbackController {

    @RequestMapping("/fallback/user-service")
    public ResponseEntity<String> userServiceFallback() {
        return ResponseEntity.status(HttpStatus.SERVICE_UNAVAILABLE)
            .body("User service is currently unavailable");
    }
}
```

### Fix 4: Configure retry filter

```yaml
spring:
  cloud:
    gateway:
      routes:
        - id: user-service
          filters:
            - name: Retry
              args:
                retries: 3
                backoff:
                  firstBackoff: 100ms
                  maxBackoff: 500ms
```

## Related Errors

- {{< relref "spring-cloud-config" >}} — ConfigDataException
- {{< relref "resttemplate" >}} — RestClientResponseException
- {{< relref "webclient" >}} — WebClientResponseException
