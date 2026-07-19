---
title: "[Solution] Java NullPointerException"
description: "Annotation Processor Generated Code"
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# generated code from Lombok or MapStruct missing null handling

A `generated` is thrown when @data.

## Common Causes

```java
@Data
public class User {
    private String name;
    private Address address;
}
```

## Solutions

```java
// Fix: add @NonNull
@Data @NonNull
public class User {
    @NonNull private String name;
    private Address address;
}

// Fix: MapStruct default value
@Mapping(source="name", target="displayName", defaultValue="Unknown")
```

## Prevention Checklist

- Review generated source code periodically.
- Use @NonNull/@Nullable annotations.
- Add tests for null scenarios with generated code.

## Related Errors

[NullPointerException](nullpointerexception), [IllegalArgumentException](illegalargumentexception)
