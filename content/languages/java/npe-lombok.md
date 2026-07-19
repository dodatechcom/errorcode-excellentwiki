---
title: "[Solution] Java NullPointerException"
description: "Lombok Generated Methods Null"
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# Lombok-generated equals/hashCode/toString encountering null fields

A `Lombok-generated` is thrown when @data.

## Common Causes

```java
@Data
public class Order {
    private String id;
    private Customer customer;
    // toString() calls customer.toString() — NPE
}
```

## Solutions

```java
// Fix: @ToString.Exclude
@Data
public class Order {
    private String id;
    @ToString.Exclude private Customer customer;
}

// Fix: @NonNull on required builder fields
@Builder public class Config {
    @NonNull private final String host;
    private final int port;
}
```

## Prevention Checklist

- Review Lombok-generated code.
- Add @NonNull to required @Builder fields.
- Use @ToString.Exclude on nullable fields.

## Related Errors

[NullPointerException](nullpointerexception), [IllegalArgumentException](illegalargumentexception)
