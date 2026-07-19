---
title: "[Solution] Java ClassNotFoundException — test framework classes (JUnit, Mockito) used in production code"
description: "Fix Java ClassNotFoundException when test framework classes (junit, mockito) used in production code with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ClassNotFoundException — test framework classes (JUnit, Mockito) used in production code

A `ClassNotFoundException` occurs when import org.junit.jupiter.api.Assertions;
Assertions.assertNotNull(user);  // works in test, ClassNotFoundException in production.

## Common Causes

```java
import org.junit.jupiter.api.Assertions;
Assertions.assertNotNull(user);  // works in test, ClassNotFoundException in production
```

## Solutions

```java
// Fix: remove test imports
Objects.requireNonNull(user, "User must not be null");

// Fix: create production utility
public class Preconditions {
    public static <T> T checkNotNull(T o, String n) {
        if (o==null) throw new IAE(n+" must not be null");
        return o;
    }
}
```

## Prevention Checklist

- Never import test frameworks in main source.
- Use @VisibleForTesting for test-only methods.
- Run integration tests in clean environment.

## Related Errors

ClassNotFoundException, NoClassDefFoundError
