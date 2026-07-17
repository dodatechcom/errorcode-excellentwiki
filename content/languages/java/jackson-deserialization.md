---
title: "[Solution] MismatchedInputException — Jackson Deserialization Fix"
description: "Fix Jackson MismatchedInputException when JSON structure does not match the expected Java type."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# MismatchedInputException — Jackson Deserialization Fix

A `MismatchedInputException` is thrown when Jackson encounters JSON that does not match the expected Java type during deserialization. This typically happens with polymorphic types, type mismatches, or unexpected JSON structures.

## What This Error Means

Common messages:

- `Cannot deserialize instance of ... out of VALUE_STRING`
- `Cannot deserialize instance of java.lang.Integer out of VALUE_STRING`
- `Expected START_ARRAY but got VALUE_STRING`

## Common Causes

```java
// Cause 1: Type mismatch
public class User {
    private Integer age;
}
// JSON: {"age": "twenty-five"}  // String instead of Integer

// Cause 2: Missing @JsonTypeInfo for polymorphic types
public abstract class Vehicle { }
public class Car extends Vehicle { }
// JSON: {"type": "car", "wheels": 4}  // Jackson doesn't know which subclass
```

## How to Fix

### Fix 1: Match JSON types to Java types

```java
public class User {
    @JsonProperty("age")
    private Integer age;
}
```

### Fix 2: Add @JsonTypeInfo for polymorphic deserialization

```java
@JsonTypeInfo(use = JsonTypeInfo.Id.NAME, property = "type")
@JsonSubTypes({
    @JsonSubTypes.Type(value = Car.class, name = "car"),
    @JsonSubTypes.Type(value = Truck.class, name = "truck")
})
public abstract class Vehicle { }
```

### Fix 3: Use @JsonCreator for custom deserialization

```java
public class User {
    private Integer age;

    @JsonCreator
    public User(@JsonProperty("age") String age) {
        this.age = Integer.parseInt(age);
    }
}
```

## Related Errors

- {{< relref "jackson-unknown" >}} — UnrecognizedPropertyException
- {{< relref "jackson-nullable" >}} — Null key for Map
- {{< relref "jackson-token" >}} — JsonProcessingException
