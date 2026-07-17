---
title: "ExhaustedRetryException - retry failed"
description: "Spring Retry throws ExhaustedRetryException when all retry attempts have been exhausted"
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Spring Retry exhausts all configured retry attempts and the operation still fails. It throws `ExhaustedRetryException` indicating the retry policy has been fully consumed.

## Common Causes

- Transient error persists beyond retry window
- Retry policy configured with too few attempts
- No backoff delay causing rapid retry exhaustion
- `@Recover` method not defined for fallback
- Retry on non-retryable exception type

## How to Fix

1. Configure retry with exponential backoff:

```java
@Retryable(
    retryFor = {ResourceAccessException.class, DataAccessException.class},
    maxAttempts = 3,
    backoff = @Backoff(delay = 1000, multiplier = 2.0, maxDelay = 10000)
)
public void callExternalService(String request) {
    restTemplate.postForObject("/api/external", request, String.class);
}
```

2. Implement a `@Recover` method:

```java
@Recover
public void callExternalServiceFallback(ResourceAccessException ex, String request) {
    log.warn("External service unavailable, using fallback for: {}", request);
    // Fallback logic — cache the request for later retry
}
```

3. Use `RetryTemplate` for more control:

```java
@Bean
public RetryTemplate retryTemplate() {
    return RetryTemplate.builder()
        .maxAttempts(3)
        .exponentialBackoff(1000, 2.0, 10000)
        .retryOn(ResourceAccessException.class)
        .build();
}
```

## Examples

```java
@Retryable(maxAttempts = 2)
public void connect() { throw new ConnectionException("refused"); }
// ExhaustedRetryException: Retry exhausted after 2 attempts
```

## Related Errors

- [REST client error]({{< relref "/frameworks/spring/rest-client-error" >}})
- [Batch error]({{< relref "/frameworks/spring/spring-batch-error" >}})
