---
title: "[Solution] Java IllegalArgumentException — null passed to methods that explicitly reject it via Objects.requireNonNull"
description: "Fix Java IllegalArgumentException when null passed to methods that explicitly reject it via objects.requirenonnull with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# IllegalArgumentException — null passed to methods that explicitly reject it via Objects.requireNonNull

A `IllegalArgumentException` occurs when public void process(String input) {
    Objects.requireNonNull(input, "input must not be null");
}.

## Common Causes

```java
public void process(String input) {
    Objects.requireNonNull(input, "input must not be null");
}
```

## Solutions

```java
// Fix: validate at method entry
public void process(String input) {
    Objects.requireNonNull(input, "input must not be null");
}

// Fix: Guava Preconditions
Preconditions.checkNotNull(input, "input must not be null");

// Fix: Optional at call site
String input = Optional.ofNullable(raw).orElseThrow(() -> new IAE("input required"));
```

## Prevention Checklist

- Validate all parameters at method entry.
- Use Objects.requireNonNull for mandatory params.
- Document null-acceptance in Javadoc.

## Related Errors

NullPointerException, IllegalStateException
