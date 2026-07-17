---
title: "[Solution] Jackson UnknownPropertyException Fix"
description: "Fix Jackson unknown property error. Configure ObjectMapper to ignore, fail on, or handle unexpected JSON fields."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Jackson UnknownPropertyException Fix

A `UnrecognizedPropertyException` is thrown when Jackson encounters a JSON property that does not exist in the target Java class during deserialization.

## What This Error Means

Common messages:

- `UnrecognizedPropertyException: Unrecognized field "extra_field"`
- `UnrecognizedPropertyException: not marked as ignorable`
- `JSON parse error: Unrecognized field "unknown"`

The JSON contains a key that has no corresponding field or setter in the Java class. By default, Jackson fails on unknown properties for type safety.

## Common Causes

```java
// Cause 1: JSON has extra fields not in the model
public class User {
    private String name;
    private String email;
}
// JSON: {"name": "Alice", "email": "a@b.com", "role": "admin"}

// Cause 2: Field name mismatch (camelCase vs snake_case)
public class UserProfile {
    private String firstName;
    private String lastName;
}
// JSON: {"first_name": "Alice", "last_name": "Smith"}

// Cause 3: API response version mismatch
// API v2 adds "created_at" field but client has v1 model
```

## How to Fix

### Fix 1: Ignore unknown properties globally

```java
ObjectMapper mapper = new ObjectMapper();
mapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
```

### Fix 2: Use @JsonIgnoreProperties on the class

```java
@JsonIgnoreProperties(ignoreUnknown = true)
public class User {
    private String name;
    private String email;
}
```

### Fix 3: Map snake_case JSON to camelCase Java

```java
ObjectMapper mapper = new ObjectMapper();
mapper.setPropertyNamingStrategy(PropertyNamingStrategies.SNAKE_CASE);

public class UserProfile {
    private String firstName;
    private String lastName;
}
// JSON: {"first_name": "Alice", "last_name": "Smith"} — maps correctly
```

### Fix 4: Use @JsonProperty for explicit mapping

```java
public class User {
    @JsonProperty("name")
    private String name;

    @JsonProperty("email_address")
    private String email;
}
```

### Fix 5: Use @JsonAnySetter for dynamic properties

```java
public class User {
    private String name;
    private Map<String, Object> extraFields = new HashMap<>();

    @JsonAnySetter
    public void setExtra(String key, Object value) {
        extraFields.put(key, value);
    }
}
```

### Fix 6: Use JsonNode for fully dynamic JSON

```java
JsonNode node = mapper.readTree(jsonString);
String name = node.get("name").asText();
JsonNode unknown = node.get("extra_field"); // Access any field
```

## Related Errors

- {{< relref "jackson-deserialization" >}} — Jackson deserialization type mismatch.
- {{< relref "jackson-nullable" >}} — Jackson null key for Map.
