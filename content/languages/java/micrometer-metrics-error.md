---
title: "[Solution] Java Micrometer metrics error — metrics registration or publishing failure"
description: "Fix Java Micrometer metrics error by checking meter registry, verifying tags, and handling naming conventions. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 119
---

# Micrometer metrics error — metrics registration or publishing failure

A Micrometer metrics error occurs when metrics cannot be registered, collected, or published to an observability backend. This covers meter registry issues, tag problems, naming convention violations, and backend connectivity failures.

## Description

Micrometer provides a facade for application metrics across different monitoring systems. Errors occur when meters are registered with invalid names, duplicate registrations conflict, tags contain invalid characters, or the registry cannot publish metrics. Common message variants include:

- `MeterAlreadyExistsException: A meter named 'X' already exists`
- `IllegalStateException: MeterRegistry is closed`
- `MeterFilter rejected meter`
- `InvalidTagException: Tag value for 'X' must not be empty`
- `Failed to publish metrics to X`

## Common Causes

```java
// Cause 1: Duplicate meter registration with different types
meterRegistry.gauge("jvm.memory.used", tags, object, Obj::getSize);
meterRegistry.timer("jvm.memory.used", tags);  // Conflict — name already used as gauge

// Cause 2: Invalid tag characters
Tags tags = Tags.of("method", "GET /api/users/{id}");  // '/' is invalid
counter.increment(tags);

// Cause 3: Counter incremented with non-monotonic value
// Counter only goes up — using it for values that decrease
Counter counter = meterRegistry.counter("active.connections");
counter.increment(-1);  // Counter cannot decrease

// Cause 4: Timer with negative duration
Timer.builder("request.duration")
    .register(meterRegistry)
    .record(-100, TimeUnit.MILLISECONDS);  // Negative duration

// Cause 5: Registry closed during shutdown
// Publishing metrics after application context is closed
```

## Solutions

### Fix 1: Use consistent meter names and types

```java
@Configuration
public class MetricsConfig {

    @Bean
    public MeterBinder customMetrics() {
        return registry -> {
            // Use Gauge for values that go up and down
            Gauge.builder("app.connections.active", connectionPool, ConnectionPool::getActive)
                .description("Number of active connections")
                .tag("pool", "main")
                .register(registry);

            // Use Counter for monotonically increasing values
            Counter.builder("app.requests.total")
                .description("Total HTTP requests")
                .tag("method", "GET")
                .register(registry);

            // Use Timer for duration measurements
            Timer.builder("app.request.duration")
                .description("Request duration")
                .publishPercentiles(0.5, 0.95, 0.99)
                .register(registry);
        };
    }
}
```

### Fix 2: Sanitize tags

```java
@Component
public class MetricsHelper {

    private final MeterRegistry registry;

    public MetricsHelper(MeterRegistry registry) {
        this.registry = registry;
    }

    public void recordRequest(String method, String path) {
        // Sanitize path tags — remove dynamic segments
        String sanitizedPath = sanitizePath(path);
        Counter.builder("http.requests")
            .tag("method", method)
            .tag("path", sanitizedPath)
            .register(registry)
            .increment();
    }

    private String sanitizePath(String path) {
        return path.replaceAll("/\\d+", "/{id}")
                   .replaceAll("/[a-f0-9-]{36}", "/{uuid}")
                   .replaceAll("[^a-zA-Z0-9/_\\-]", "_");
    }
}
```

### Fix 3: Use appropriate metric types

```java
@Service
public class MetricsService {

    private final MeterRegistry registry;

    public MetricsService(MeterRegistry registry) {
        this.registry = registry;
    }

    // CORRECT — Gauge for values that fluctuate
    public void registerConnectionPoolGauge(ConnectionPool pool) {
        Gauge.builder("db.pool.active", pool, ConnectionPool::getActiveConnections)
            .description("Active database connections")
            .register(registry);
    }

    // CORRECT — Counter for monotonically increasing values
    public void recordQueryCount() {
        Counter.builder("db.queries.total")
            .description("Total database queries executed")
            .register(registry)
            .increment();
    }

    // CORRECT — Timer for durations
    public <T> T recordQueryDuration(String queryName, Supplier<T> query) {
        return Timer.builder("db.query.duration")
            .tag("query", queryName)
            .publishPercentiles(0.5, 0.95)
            .register(registry)
            .record(query);
    }

    // CORRECT — DistributionSummary for value distributions
    public void recordResponseSize(long bytes) {
        DistributionSummary.builder("http.response.size")
            .baseUnit("bytes")
            .publishPercentiles(0.5, 0.95)
            .register(registry)
            .record(bytes);
    }
}
```

### Fix 4: Configure registry properly

```yaml
# application.yml
management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics,prometheus
  metrics:
    export:
      prometheus:
        enabled: true
    tags:
      application: my-app
      environment: ${ENV:development}
    distribution:
      percentiles-histogram:
        http.server.requests: true
      percentiles:
        http.server.requests: 0.5,0.95,0.99
```

### Fix 5: Handle registry lifecycle

```java
@Component
public class MetricsLifecycle implements DisposableBean {

    private final MeterRegistry registry;
    private final AtomicBoolean published = new AtomicBoolean(true);

    public MetricsLifecycle(MeterRegistry registry) {
        this.registry = registry;
    }

    public void recordMetric(String name, double value) {
        if (published.get() && registry != null) {
            try {
                Gauge.builder(name, () -> value).register(registry);
            } catch (Exception e) {
                // Log but don't fail — metrics are non-critical
            }
        }
    }

    @Override
    public void destroy() {
        published.set(false);
    }
}
```

## Prevention Checklist

- Use `MeterBinder` beans for centralized metrics configuration
- Sanitize tag values — remove special characters and dynamic path segments
- Choose the correct meter type: Gauge for fluctuating values, Counter for monotonically increasing
- Set `publishPercentiles` on Timers for latency percentiles
- Use `@MeterFilter` to enforce naming conventions and sanitize tags globally
- Handle metric registration failures gracefully — metrics should not break application logic

## Related Errors

- [IllegalStateException from closed registry](/languages/java/illegalstateexception/)
- [ConcurrentModificationException in metrics](/languages/java/concurrentmodificationexception/)
- [Spring Boot Actuator errors](/languages/java/spring-boot-actuator/)
