---
title: "ObservabilityException - trace error"
description: "Spring throws ObservabilityException when tracing or metrics collection fails"
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Spring's observability infrastructure fails to create or propagate tracing spans, or when metrics collection encounters an error. It throws `ObservabilityException`.

## Common Causes

- Tracing backend (Zipkin, Jaeger) is unreachable
- Micrometer registry configuration is invalid
- Span context propagation headers are malformed
- Circular span creation in interceptors
- OpenTelemetry SDK not properly initialized

## How to Fix

1. Configure Micrometer tracing properly:

```yaml
management:
  tracing:
    sampling:
      probability: 1.0
  zipkin:
    tracing:
      endpoint: http://localhost:9411/api/v2/spans
```

2. Add fallback when tracing is unavailable:

```java
@Configuration
public class ObservabilityConfig {

    @Bean
    public ObservationRegistry observationRegistry() {
        return ObservationRegistry.create();
    }

    @Bean
    public MeterRegistryCustomizer<MeterRegistry> metricsCommonTags() {
        return registry -> registry.config()
            .commonTags("application", "my-service");
    }
}
```

3. Handle tracing errors gracefully:

```java
@Service
public class TracedService {

    @Observed(name = "service.operation")
    public String performOperation(String input) {
        try {
            return process(input);
        } catch (ObservabilityException e) {
            log.warn("Tracing failed, continuing without trace: {}", e.getMessage());
            return process(input);
        }
    }
}
```

## Examples

```java
// Tracing backend unreachable
@Observed(name = "user.create")
public User createUser(CreateUserRequest request) { ... }
// ObservabilityException: Failed to report span to Zipkin
```

## Related Errors

- [Observability config error]({{< relref "/frameworks/spring/observability-error" >}})
- [REST client error]({{< relref "/frameworks/spring/rest-client-error" >}})
