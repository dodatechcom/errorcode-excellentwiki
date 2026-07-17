---
title: "[Solution] StreamConstraintsException — Jackson Oversized Payload Fix"
description: "Fix Jackson StreamConstraintsException when JSON exceeds configured size limits. Adjust stream constraints for large payloads."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# StreamConstraintsException — Jackson Oversized Payload Fix

A `StreamConstraintsException` is thrown when a JSON payload exceeds the configured size limits in Jackson. This is a security feature to prevent DoS attacks via oversized payloads.

## What This Error Means

Common messages:

- `Number of field names (50001) exceeds the maximum allowed (50000)`
- `Document nesting depth (1001) exceeds the maximum allowed (1000)`

## Common Causes

```java
// Cause 1: Large JSON array
// JSON: {"items": [1, 2, 3, ..., 100000]}

// Cause 2: Deep nesting
// JSON: {"a": {"b": {"c": {"d": ...}}}}

// Cause 3: Many field names
// JSON: {"field1": "...", "field2": "...", ..., "field50001": "..."}
```

## How to Fix

### Fix 1: Increase stream constraints

```java
ObjectMapper mapper = new ObjectMapper();
mapper.getFactory()
    .setStreamReadConstraints(StreamReadConstraints.builder()
        .maxStringLength(10_000_000)
        .maxNestingDepth(1000)
        .maxNumberLength(20)
        .build());
```

### Fix 2: Configure via Spring Boot

```properties
spring.jackson.stream-constraints.max-string-length=10000000
spring.jackson.stream-constraints.max-number-length=20
spring.jackson.stream-constraints.max-nesting-depth=1000
```

### Fix 3: Process in chunks for very large payloads

```java
try (JsonParser parser = mapper.getFactory().createParser(inputStream)) {
    while (parser.nextToken() != null) {
        // Process token by token
    }
}
```

## Related Errors

- {{< relref "jackson-deserialization" >}} — MismatchedInputException
- {{< relref "jackson-token" >}} — JsonProcessingException
- {{< relref "outofmemoryerror" >}} — OutOfMemoryError
