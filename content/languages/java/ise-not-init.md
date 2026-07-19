---
title: "[Solution] Java IllegalStateException — methods called on objects not fully constructed or initialized"
description: "Fix Java IllegalStateException when methods called on objects not fully constructed or initialized with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# IllegalStateException — methods called on objects not fully constructed or initialized

A `IllegalStateException` occurs when MyService service = new MyService();
service.process();  // ISE — init() not called.

## Common Causes

```java
MyService service = new MyService();
service.process();  // ISE — init() not called
```

## Solutions

```java
// Fix: validate state
public void process() {
    if (!initialized) throw new ISE("Not initialized — call init() first");
}

// Fix: PostConstruct
@PostConstruct
public void init() { this.initialized = true; }

// Fix: immutable construction
public final class Config {
    private final String host;
    public Config(String host) { this.host = Objects.requireNonNull(host); }
}
```

## Prevention Checklist

- Use final fields and constructor validation.
- Implement InitializingBean/DisposableBean.
- Validate state at method start.

## Related Errors

NullPointerException, IllegalArgumentException
