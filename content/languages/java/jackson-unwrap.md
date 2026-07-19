---
title: "[Solution] InvalidDefinitionException — Jackson @JsonUnwrapped Fix"
description: "Fix InvalidDefinitionException 'No serializer found' when using @JsonUnwrapped in Jackson. Resolve flattening conflicts."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# InvalidDefinitionException — Jackson @JsonUnwrapped Fix

An `InvalidDefinitionException` with the message "No serializer found" is thrown when Jackson cannot serialize a property annotated with `@JsonUnwrapped`. This happens when the unwrapped class has properties that conflict with the parent class or when the unwrapped object is null.

## What This Error Means

Common messages:

- `com.fasterxml.jackson.databind.exc.InvalidDefinitionException: No serializer found for class com.example.Address`
- `InvalidDefinitionException: No serializer found for class com.example.Metadata`
- `InvalidDefinitionException: Cannot handle managed/back reference`

## Common Causes

```java
// Cause 1: Property name conflict between parent and unwrapped child
public class User {
    private String name;

    @JsonUnwrapped
    private Address address;
}
public class Address {
    private String name; // CONFLICT: "name" already exists in User!
}

// Cause 2: Unwrapped object is null and no default value configured
public class User {
    @JsonUnwrapped
    private Address address; // null — Jackson tries to serialize null unwrapped
}

// Cause 3: Unwrapped class has no accessible properties
public class EmptyClass {
    // No fields or getters
}
```

## How to Fix

### Fix 1: Resolve property name conflicts with @JsonProperty

Prefix the conflicting property names in the unwrapped class to avoid collisions with parent class fields.

```java
public class Address {
    @JsonProperty("addressName")
    private String name;

    @JsonProperty("addressStreet")
    private String street;
}

public class User {
    private String name; // No conflict now — address fields are prefixed

    @JsonUnwrapped
    private Address address;
}

// Output: {"name": "Alice", "addressName": "123 Main St", "addressStreet": "Springfield"}
```

### Fix 2: Use @JsonInclude to handle null unwrapped objects

Configure the ObjectMapper or class-level annotation to skip null unwrapped objects during serialization.

```java
public class User {
    private String name;

    @JsonUnwrapped
    @JsonInclude(JsonInclude.Include.NON_NULL)
    private Address address;
}

// Or configure globally
ObjectMapper mapper = new ObjectMapper();
mapper.setSerializationInclusion(JsonInclude.Include.NON_NULL);
```

### Fix 3: Create a custom serializer for @JsonUnwrapped classes

When @JsonUnwrapped causes persistent issues, write a custom serializer that handles the flattening explicitly.

```java
public class UserSerializer extends JsonSerializer<User> {

    @Override
    public void serialize(User user, JsonGenerator gen,
            SerializerProvider provider) throws IOException {
        gen.writeStartObject();
        gen.writeStringField("name", user.getName());

        if (user.getAddress() != null) {
            gen.writeStringField("street", user.getAddress().getStreet());
            gen.writeStringField("city", user.getAddress().getCity());
        }

        gen.writeEndObject();
    }
}

@JsonSerialize(using = UserSerializer.class)
public class User { ... }
```

## Related Errors

- {{< relref "jackson-mix-in" >}} — InvalidDefinitionException — MixIn Conflict
- {{< relref "jackson-custom-serializer" >}} — JsonGenerationException
