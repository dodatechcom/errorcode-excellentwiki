---
title: "[Solution] UnrecognizedPropertyException — Unknown JSON Property Fix"
description: "Fix Jackson UnrecognizedPropertyException when JSON contains fields not mapped in Java."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# UnrecognizedPropertyException — Unknown JSON Property Fix

An `UnrecognizedPropertyException` is thrown when Jackson encounters a JSON field that does not correspond to any property in the target Java class. By default, Jackson fails on unknown properties.

## What This Error Means

Common message:

- `Unrecognized field "xyz" (class com.example.User), not marked as ignorable`

## Common Causes

```java
// Cause 1: JSON has extra fields not in Java class
public class User {
    private String name;
    private String email;
}
// JSON: {"name": "John", "email": "john@test.com", "age": 30}

// Cause 2: Field name mismatch (case sensitivity)
public class User {
    private String firstName;
}
// JSON: {"first_name": "John"}  // Snake case vs camelCase
```

## How to Fix

### Fix 1: Ignore unknown properties globally

```java
ObjectMapper mapper = new ObjectMapper();
mapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
```

```properties
spring.jackson.deserialization.fail-on-unknown-properties=false
```

### Fix 2: Add @JsonIgnoreProperties on the class

```java
@JsonIgnoreProperties(ignoreUnknown = true)
public class User {
    private String name;
    private String email;
}
```

### Fix 3: Use @JsonProperty for name mapping

```java
public class User {
    @JsonProperty("first_name")
    private String firstName;

    @JsonProperty("last_name")
    private String lastName;
}
```

### Fix 4: Use @JsonAlias for multiple possible names

```java
public class User {
    @JsonAlias({"first_name", "firstName", "fname"})
    private String firstName;
}
```

## Related Errors

- {{< relref "jackson-deserialization" >}} — MismatchedInputException
- {{< relref "jackson-nullable" >}} — Null key for Map
- {{< relref "jackson-token" >}} — JsonProcessingException
