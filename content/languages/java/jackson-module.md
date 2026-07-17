---
title: "[Solution] UnresolvedTypeVariableException — Jackson Module Fix"
description: "Fix UnresolvedTypeVariableException when Jackson cannot resolve generic type variables. Register type modules."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# UnresolvedTypeVariableException — Jackson Module Fix

An `UnresolvedTypeVariableException` is thrown when Jackson encounters a generic type variable that it cannot resolve. This typically happens with complex generic hierarchies or when the `jackson-module-parameter-names` module is missing.

## What This Error Means

Common message:

- `Unresolved type variable [T]`

## Common Causes

```java
// Cause 1: Generic type not resolvable
public abstract class BaseResponse<T> {
    private T data;
}
public class UserResponse extends BaseResponse<User> { }

// Cause 2: Missing jackson-datatype-jdk8 module
Optional<String> optionalField;  // Jackson doesn't know Optional
```

## How to Fix

### Fix 1: Register required Jackson modules

```java
ObjectMapper mapper = new ObjectMapper();
mapper.registerModule(new JavaTimeModule());
mapper.registerModule(new Jdk8Module());
mapper.registerModule(new ParameterNamesModule());
```

### Fix 2: Use @JsonTypeInfo for generic types

```java
@JsonTypeInfo(use = JsonTypeInfo.Id.CLASS)
public abstract class BaseResponse<T> { }
```

### Fix 3: Add Jackson dependencies (Maven)

```xml
<dependency>
    <groupId>com.fasterxml.jackson.datatype</groupId>
    <artifactId>jackson-datatype-jdk8</artifactId>
</dependency>
<dependency>
    <groupId>com.fasterxml.jackson.datatype</groupId>
    <artifactId>jackson-datatype-jsr310</artifactId>
</dependency>
<dependency>
    <groupId>com.fasterxml.jackson.module</groupId>
    <artifactId>jackson-module-parameter-names</artifactId>
</dependency>
```

## Related Errors

- {{< relref "jackson-deserialization" >}} — MismatchedInputException
- {{< relref "jackson-unknown" >}} — UnrecognizedPropertyException
