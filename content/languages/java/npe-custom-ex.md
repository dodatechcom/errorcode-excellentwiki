---
title: "[Solution] Java NullPointerException"
description: "Custom Exception Null Message"
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# custom exception getMessage() returns null causing NPE in callers

A `custom` is thrown when public class validationexception extends runtimeexception {.

## Common Causes

```java
public class ValidationException extends RuntimeException {
    public ValidationException() { super(); }  // message is null
}
String msg = e.getMessage().toUpperCase();  // NPE
```

## Solutions

```java
// Fix: always provide message
public ValidationException(String field) {
    super("Validation failed: " + field);
}

// Fix: null-check message
String msg = Objects.toString(e.getMessage(), "No message");

// Fix: Optional
String msg = Optional.ofNullable(e.getMessage()).map(String::toUpperCase).orElse("ERROR");
```

## Prevention Checklist

- Always provide message when constructing exceptions.
- Use Objects.toString for safe access.
- Configure logging to handle null messages.

## Related Errors

[NullPointerException](nullpointerexception), [IllegalArgumentException](illegalargumentexception)
