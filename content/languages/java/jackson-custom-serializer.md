---
title: "[Solution] JsonGenerationException — Jackson Custom Serializer Fix"
description: "Fix JsonGenerationException in Jackson custom serializers. Resolve 'Can not write JSON field' errors in custom serialization logic."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# JsonGenerationException — Jackson Custom Serializer Fix

A `JsonGenerationException` with the message "Can not write JSON field" is thrown when a custom Jackson serializer encounters an error while writing a field to the JSON output. This typically happens when the serializer tries to write a field name that conflicts with the current write state.

## What This Error Means

Common messages:

- `com.fasterxml.jackson.core.JsonGenerationException: Can not write JSON field "name"`
- `JsonGenerationException: Can not write a field name, expecting field value`
- `JsonGenerationException: Broken surrogate pair`

## Common Causes

```java
// Cause 1: Writing a field name inside writeValue without writeStartObject
public class CustomSerializer extends JsonSerializer<User> {
    @Override
    public void serialize(User user, JsonGenerator gen, SerializerProvider sp)
            throws IOException {
        gen.writeFieldName("name"); // ERROR: no object context!
        gen.writeString(user.getName());
    }
}

// Cause 2: Writing duplicate field names
gen.writeStartObject();
gen.writeStringField("name", "Alice");
gen.writeStringField("name", "Bob"); // Duplicate field name

// Cause 3: Calling writeFieldName twice before a value
gen.writeFieldName("key");
gen.writeFieldName("key2"); // Missing value for "key"
```

## How to Fix

### Fix 1: Use writeStartObject/writeEndObject correctly

Wrap field writes in writeStartObject and writeEndObject calls to ensure the JsonGenerator is in the correct write state.

```java
public class UserSerializer extends JsonSerializer<User> {

    @Override
    public void serialize(User user, JsonGenerator gen,
            SerializerProvider provider) throws IOException {
        gen.writeStartObject();
        gen.writeStringField("name", user.getName());
        gen.writeNumberField("age", user.getAge());
        gen.writeStringField("email", user.getEmail());
        gen.writeEndObject();
    }
}

// Register the serializer
public class UserMixin {
    @JsonSerialize(using = UserSerializer.class)
    private String name;
}
```

### Fix 2: Use BeanSerializerModifier for systematic field filtering

Instead of a fully custom serializer, use BeanSerializerModifier to selectively skip fields and avoid field-name conflicts.

```java
public class NullFieldFilter extends BeanSerializerModifier {

    @Override
    public List<BeanPropertyWriter> changeProperties(
            SerializationConfig config, BeanDescription beanDesc,
            List<BeanPropertyWriter> beanProperties) {

        return beanProperties.stream()
            .filter(prop -> {
                // Skip properties that would fail
                return prop.getType().isPrimitive()
                    || !prop.getType().isReferenceType();
            })
            .collect(Collectors.toList());
    }
}

ObjectMapper mapper = new ObjectMapper();
mapper.setSerializerFactory(mapper.getSerializerFactory()
    .withModifier(new NullFieldFilter()));
```

### Fix 3: Catch and wrap JsonGenerationException with context

Wrap the exception with additional context to make debugging easier when serialization fails in production.

```java
public class SafeUserSerializer extends JsonSerializer<User> {

    @Override
    public void serialize(User user, JsonGenerator gen,
            SerializerProvider provider) throws IOException {
        try {
            gen.writeStartObject();
            gen.writeStringField("name", user.getName());
            gen.writeNumberField("id", user.getId());
            gen.writeEndObject();
        } catch (JsonGenerationException e) {
            throw new IOException(
                "Failed to serialize User{id=" + user.getId() + "}", e);
        }
    }
}
```

## Related Errors

- {{< relref "jackson-mix-in" >}} — InvalidDefinitionException — MixIn Conflict
- {{< relref "jackson-unwrap" >}} — InvalidDefinitionException — @JsonUnwrapped
