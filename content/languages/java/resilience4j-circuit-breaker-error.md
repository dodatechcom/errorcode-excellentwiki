---
title: "[Solution] Java Resilience4j CircuitBreaker error — circuit breaker state or configuration issue"
description: "Fix Java Resilience4j CircuitBreaker error by checking state, configuring thresholds, and handling fallbacks. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 120
---

# Resilience4j CircuitBreaker error — circuit breaker state or configuration issue

A Resilience4j CircuitBreaker error occurs when the circuit breaker transitions to the OPEN state, its configuration is invalid, or the fallback mechanism fails. This covers state transitions, threshold violations, and exception handling within the circuit breaker pattern.

## Description

Resilience4j CircuitBreaker monitors calls and trips the circuit when failure rates exceed thresholds. When the circuit is OPEN, all calls are rejected with `CallNotPermittedException`. Errors also occur from invalid configuration or misconfigured fallback methods. Common message variants include:

- `io.github.resilience4j.circuitbreaker.CallNotPermittedException: CircuitBreaker 'X' is OPEN`
- `CircuitBreaker 'X' is in state OPEN`
- `CircuitBreaker 'X' is in state HALF_OPEN`
- `IllegalArgumentException: Invalid threshold percentage`
- `Bulkhead full` (when used with Bulkhead)

## Common Causes

```java
// Cause 1: Circuit OPEN due to high failure rate
@CircuitBreaker(name = "paymentService", fallbackMethod = "fallbackPayment")
public PaymentResult processPayment(PaymentRequest request) {
    // Failing repeatedly — circuit opened after threshold exceeded
    return paymentGateway.charge(request);
}

public PaymentResult fallbackPayment(PaymentRequest request, Exception ex) {
    throw new RuntimeException("Fallback also failed");  // Fallback error
}

// Cause 2: Invalid configuration
CircuitBreakerConfig.custom()
    .failureRateThreshold(150)  // Must be 0-100
    .waitDurationInOpenState(Duration.ofSeconds(-1))  // Must be positive
    .build();

// Cause 3: Missing fallback method signature
@CircuitBreaker(name = "service", fallbackMethod = "fallback")
public String callExternalService(String input) {
    return externalService.call(input);
}

// Fallback has wrong parameter list
public String fallback(String input) {
    // Missing the exception parameter — Resilience4j expects it
    return "fallback";
}

// Cause 4: Circuit never recovers from OPEN state
// No successful calls in HALF_OPEN to close the circuit
```

## Solutions

### Fix 1: Configure circuit breaker thresholds properly

```yaml
resilience4j:
  circuitbreaker:
    instances:
      paymentService:
        slidingWindowSize: 10
        slidingWindowType: COUNT_BASED
        minimumNumberOfCalls: 5
        failureRateThreshold: 50
        waitDurationInOpenState: 30s
        permittedNumberOfCallsInHalfOpenState: 3
        automaticTransitionFromOpenToHalfOpenEnabled: true
        recordExceptions:
          - java.io.IOException
          - java.net.SocketTimeoutException
          - com.example.PaymentException
        ignoreExceptions:
          - com.example.InvalidPaymentDataException
        slowCallRateThreshold: 80
        slowCallDurationThreshold: 2s
```

### Fix 2: Implement proper fallback methods

```java
@Service
public class PaymentService {

    @CircuitBreaker(name = "paymentService", fallbackMethod = "fallbackPayment")
    @Retry(name = "paymentService")
    public PaymentResult processPayment(PaymentRequest request) {
        return paymentGateway.charge(request);
    }

    // Fallback signature: same return type + exception type as last param
    public PaymentResult fallbackPayment(PaymentRequest request, Exception ex) {
        log.warn("Payment circuit open, using fallback: {}", ex.getMessage());

        // Use alternative payment processor
        if (ex instanceof CallNotPermittedException) {
            return alternativePaymentGateway.charge(request);
        }

        // Queue for retry later
        paymentQueue.enqueue(request);
        return PaymentResult.pending("Payment queued for retry");
    }

    @CircuitBreaker(name = "inventoryService", fallbackMethod = "fallbackInventory")
    public InventoryCheck checkInventory(String productId) {
        return inventoryClient.check(productId);
    }

    public InventoryCheck fallbackInventory(String productId, Exception ex) {
        log.warn("Inventory check failed, returning cached data: {}", ex.getMessage());
        return cachedInventory.get(productId);
    }
}
```

### Fix 3: Monitor circuit breaker state

```java
@Component
public class CircuitBreakerMonitor {

    private final CircuitBreakerRegistry registry;

    public CircuitBreakerMonitor(CircuitBreakerRegistry registry) {
        this.registry = registry;

        // Listen for state transitions
        registry.getEventPublisher()
            .onEvent(event -> {
                log.info("Circuit breaker event: {} - {} - state={}",
                    event.getCircuitBreakerName(),
                    event.getEventType(),
                    event.getStateTransition());
            });

        // Register specific circuit breaker listener
        CircuitBreaker cb = registry.circuitBreaker("paymentService");
        cb.getEventPublisher()
            .onStateTransition(event -> {
                log.warn("CircuitBreaker '{}' state: {} -> {}",
                    event.getCircuitBreakerName(),
                    event.getStateTransition().getFromState(),
                    event.getStateTransition().getToState());
            });
    }

    // Expose circuit state via actuator endpoint
    @GetMapping("/actuator/circuitbreakers")
    public Map<String, Object> getCircuitStates() {
        Map<String, Object> states = new HashMap<>();
        registry.getAllCircuitBreakers().forEach(cb -> {
            states.put(cb.getName(), Map.of(
                "state", cb.getState().name(),
                "failureRate", cb.getMetrics().getFailureRate(),
                "successRate", cb.getMetrics().getSuccessRate(),
                "notPermittedCalls", cb.getMetrics().getNumberOfNotPermittedCalls()
            ));
        });
        return states;
    }
}
```

### Fix 4: Handle HALF_OPEN state gracefully

```java
@Service
public class ResilientPaymentService {

    private final CircuitBreakerRegistry registry;

    public ResilientPaymentService(CircuitBreakerRegistry registry) {
        this.registry = registry;
    }

    public PaymentResult processPayment(PaymentRequest request) {
        CircuitBreaker cb = registry.circuitBreaker("paymentService");

        return CircuitBreaker.decorateSupplier(cb, () -> {
            // This call is permitted in HALF_OPEN state
            // If it succeeds, circuit closes; if it fails, circuit opens again
            return paymentGateway.charge(request);
        }).recover(CallNotPermittedException.class, ex -> {
            // Circuit is OPEN — use fallback
            log.warn("Circuit open, falling back to alternative payment");
            return alternativePaymentGateway.charge(request);
        }).get();
    }
}
```

### Fix 5: Use Retry with CircuitBreaker for resilience

```java
@Service
public class ExternalServiceClient {

    @CircuitBreaker(name = "externalService", fallbackMethod = "fallback")
    @Retry(name = "externalService")
    @TimeLimiter(name = "externalService")
    public CompletableFuture<String> callExternal(String request) {
        return CompletableFuture.supplyAsync(() -> {
            return externalApiClient.call(request);
        });
    }

    public CompletableFuture<String> fallback(String request, Exception ex) {
        return CompletableFuture.completedFuture(
            "Service unavailable, using cached response"
        );
    }
}
```

```yaml
resilience4j:
  retry:
    instances:
      externalService:
        maxAttempts: 3
        waitDuration: 500ms
        enableExponentialBackoff: true
        exponentialBackoffMultiplier: 2
        retryExceptions:
          - java.io.IOException
          - java.net.SocketTimeoutException
  timelimiter:
    instances:
      externalService:
        timeoutDuration: 3s
        cancelRunningFuture: true
```

## Prevention Checklist

- Configure `failureRateThreshold`, `waitDurationInOpenState`, and `minimumNumberOfCalls` based on expected traffic
- Always implement fallback methods that return a degraded response instead of propagating errors
- Monitor circuit state transitions with event listeners and expose via actuator
- Use `ignoreExceptions` for client errors that should not count as circuit failures
- Combine CircuitBreaker with Retry and TimeLimiter for layered resilience
- Test circuit breaker behavior with chaos engineering tools (Chaos Monkey, ToxiProxy)

## Related Errors

- [CallNotPermittedException](/languages/java/rejectedexecutionexception/)
- [TimeoutException](/languages/java/timeoutexception/)
- [Retry exceeded errors](/languages/java/spring-retry/)
