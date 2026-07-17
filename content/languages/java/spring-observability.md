---
title: "[Solution] ObservabilityException — Spring Observability Fix"
description: "Fix ObservabilityException when span creation fails in Spring Observability. Configure Micrometer and tracing properly."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["spring", "observability", "tracing", "micrometer", "span"]
weight: 5
---

# ObservabilityException — Spring Observability Fix

An `ObservabilityException` is thrown when Spring Observability (Micrometer Tracing) fails to create a span. This typically occurs when the tracing backend is unavailable or misconfigured.

## What This Error Means

Common message:

- `ObservabilityException: Span creation failed`
- `ObservabilityException: No tracer configured`

## Common Causes

```java
// Cause 1: No tracing backend configured
// Micrometer Tracing needs Brave or OpenTelemetry

// Cause 2: Tracing backend unavailable
// Zipkin/Jaeger not running

// Cause 3: Configuration mismatch
```

## How to Fix

### Fix 1: Add Micrometer Tracing dependencies

```xml
<dependency>
    <groupId>io.micrometer</groupId>
    <artifactId>micrometer-tracing-bridge-brave</artifactId>
</dependency>
<dependency>
    <groupId>io.zipkin.reporter2</groupId>
    <artifactId>zipkin-reporter-brave</artifactId>
</dependency>
```

### Fix 2: Configure tracing

```yaml
management:
  tracing:
    sampling:
      probability: 1.0
  zipkin:
    tracing:
      endpoint: http://localhost:9411/api/v2/spans
```

### Fix 3: Disable tracing if not needed

```yaml
management:
  tracing:
    enabled: false
```

## Related Errors

- {{< relref "spring-cloud-config" >}} — ConfigDataException
- {{< relref "spring-bean" >}} — NoSuchBeanDefinitionException
- {{< relref "spring-cloud-gateway" >}} — ResponseStatusException: 502
