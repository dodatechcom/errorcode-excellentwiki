---
title: "ResponseStatusException - gateway error"
description: "Spring Cloud Gateway throws ResponseStatusException when a route cannot be resolved or the downstream service is unavailable"
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["gateway", "cloud-gateway", "routing", "proxy", "downstream"]
weight: 5
---

This error occurs when Spring Cloud Gateway fails to route a request to a downstream service or when the downstream service returns an error status. It throws `ResponseStatusException`.

## Common Causes

- Downstream service is unreachable or returns 5xx
- Route predicate does not match the incoming request
- Circuit breaker has tripped for the target service
- Rate limiting exceeded on the gateway
- Load balancer cannot find any available instances

## How to Fix

1. Configure routes with fallback in `application.yml`:

```yaml
spring:
  cloud:
    gateway:
      routes:
        - id: user-service
          uri: lb://user-service
          predicates:
            - Path=/api/users/**
          filters:
            - name: CircuitBreaker
              args:
                fallbackUri: forward:/fallback/users
```

2. Add retry and timeout configuration:

```yaml
spring:
  cloud:
    gateway:
      routes:
        - id: order-service
          uri: lb://order-service
          predicates:
            - Path=/api/orders/**
          filters:
            - name: Retry
              args:
                retries: 3
                backoff:
                  firstBackoff: 100ms
                  maxBackoff: 1s
```

3. Handle gateway errors globally:

```java
@RestControllerAdvice
public class GatewayExceptionHandler {

    @ExceptionHandler(ResponseStatusException.class)
    public ResponseEntity<Map<String, String>> handleGatewayError(
            ResponseStatusException ex) {
        return ResponseEntity.status(ex.getStatusCode())
            .body(Map.of("error", ex.getReason()));
    }
}
```

## Examples

```text
ResponseStatusException: 502 BAD_GATEWAY — Unable to connect to downstream service
```

## Related Errors

- [REST client error]({{< relref "/frameworks/spring/rest-client-error" >}})
- [Config error]({{< relref "/frameworks/spring/spring-cloud-config-error" >}})
