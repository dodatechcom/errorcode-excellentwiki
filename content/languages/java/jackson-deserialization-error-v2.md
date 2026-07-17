---
title: "[Solution] Jackson Deserialization Mismatch Fix"
description: "Fix Jackson deserialization mismatch when JSON structure does not match expected Java type. Handle type mismatches and polymorphic types."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Jackson Deserialization Mismatch Fix

A `MismatchedInputException` or `InvalidDefinitionException` is thrown when Jackson encounters JSON that does not match the expected Java type during deserialization.

## What This Error Means

Common messages:

- `MismatchedInputException: Cannot deserialize instance of X out of VALUE_STRING`
- `InvalidDefinitionException: Cannot construct instance of X`
- `InvalidDefinitionException: No creator (like @JsonCreator) defined`

Jackson receives JSON data whose structure or types differ from the Java class definition. This can involve type mismatches, missing constructors, or polymorphic type resolution failures.

## Common Causes

```java
// Cause 1: Type mismatch — String where Integer expected
public class Product {
    private Integer price;
}
// JSON: {"price": "29.99"}  // String instead of Integer

// Cause 2: JSON array where object expected (or vice versa)
public class Config {
    private Map<String, String> settings;
}
// JSON: {"settings": [{"key": "val"}]}  // Array instead of Map

// Cause 3: Abstract type without @JsonTypeInfo
public abstract class Event { }
public class ClickEvent extends Event { }
// JSON: {"type": "click", "x": 100}  // Jackson doesn't know the subclass

// Cause 4: Enum from JSON string without matching constant
public enum Status { ACTIVE, INACTIVE }
// JSON: {"status": "enabled"}  // No matching enum constant
```

## How to Fix

### Fix 1: Use @JsonCreator for custom deserialization

```java
public class Product {
    private Double price;

    @JsonCreator
    public Product(@JsonProperty("price") String price) {
        this.price = Double.parseDouble(price);
    }
}
```

### Fix 2: Add @JsonTypeInfo for polymorphic types

```java
@JsonTypeInfo(use = JsonTypeInfo.Id.NAME, property = "type")
@JsonSubTypes({
    @JsonSubTypes.Type(value = ClickEvent.class, name = "click"),
    @JsonSubTypes.Type(value = ScrollEvent.class, name = "scroll")
})
public abstract class Event { }
```

### Fix 3: Handle enum deserialization with @JsonCreator

```java
public enum Status {
    ACTIVE, INACTIVE;

    @JsonCreator
    public static Status fromString(String value) {
        return switch (value.toLowerCase()) {
            case "enabled", "active" -> ACTIVE;
            case "disabled", "inactive" -> INACTIVE;
            default -> throw new IllegalArgumentException("Unknown status: " + value);
        };
    }
}
```

### Fix 4: Add default constructor for Jackson

```java
public class Product {
    private String name;
    private Double price;

    @JsonCreator
    public Product(@JsonProperty("name") String name,
                   @JsonProperty("price") Double price) {
        this.name = name;
        this.price = price;
    }
}
```

### Fix 5: Configure ObjectMapper to be more lenient

```java
ObjectMapper mapper = new ObjectMapper();
mapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
mapper.configure(DeserializationFeature.FAIL_ON_NULL_FOR_PRIMITIVES, false);
```

## Related Errors

- {{< relref "jackson-unknown" >}} — Unrecognized property error.
- {{< relref "jackson-token" >}} — JSON token processing error.
