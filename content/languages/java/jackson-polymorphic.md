---
title: "[Solution] InvalidTypeIdException — Jackson Polymorphic Deserialization Fix"
description: "Fix InvalidTypeIdException when Jackson cannot resolve a type ID during polymorphic deserialization. Configure @JsonTypeInfo correctly."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# InvalidTypeIdException — Jackson Polymorphic Deserialization Fix

An `InvalidTypeIdException` is thrown when Jackson encounters a type ID in JSON that it cannot map to any registered subtype during polymorphic deserialization. This is common in REST APIs that use inheritance-based type hierarchies.

## What This Error Means

Common messages:

- `com.fasterxml.jackson.databind.exc.InvalidTypeIdException: Could not resolve type id 'order' as a subtype of [simple type, class com.example.BaseEvent]`
- `InvalidTypeIdException: Could not resolve type id 'discount'`
- `InvalidTypeIdException: No such type id 'payment'`

## Common Causes

```java
// Cause 1: Missing @JsonSubTypes on the base class
public abstract class BaseEvent {
    private String type;
    // No @JsonSubTypes annotation!
}

// Cause 2: Type ID in JSON does not match any registered subtype
// JSON: {"type": "order_event", ...}
@JsonSubTypes({
    @JsonSubTypes.Type(value = OrderEvent.class, name = "order") // "order_event" won't match "order"
})

// Cause 3: Subtype class not on the classpath at deserialization time
@JsonSubTypes({
    @JsonSubTypes.Type(value = ExternalEvent.class, name = "external")
})
```

## How to Fix

### Fix 1: Add @JsonSubTypes with correct type IDs

Annotate the base class with @JsonTypeInfo and @JsonSubTypes, ensuring each name matches the value serialized in your JSON payloads.

```java
@JsonTypeInfo(
    use = JsonTypeInfo.Id.NAME,
    include = JsonTypeInfo.As.PROPERTY,
    property = "type"
)
@JsonSubTypes({
    @JsonSubTypes.Type(value = OrderEvent.class, name = "order"),
    @JsonSubTypes.Type(value = PaymentEvent.class, name = "payment"),
    @JsonSubTypes.Type(value = RefundEvent.class, name = "refund")
})
public abstract class BaseEvent {
    private Instant timestamp;
}
```

### Fix 2: Use a custom TypeResolverBuilder for dynamic type resolution

When type IDs are not known at compile time, implement a custom TypeResolverBuilder that resolves subtypes dynamically from a registry.

```java
public class DynamicTypeResolverBuilder extends DefaultTypeResolverBuilder {

    private final Map<String, Class<?>> typeRegistry;

    public DynamicTypeResolverBuilder(Map<String, Class<?>> registry) {
        super ObjectMapper.DefaultTyping.OBJECT_AND_NON_CONCRETE);
        this.typeRegistry = registry;
    }

    @Override
    public TypeDeserializer buildTypeDeserializer(
            DeserializationConfig config, JavaType baseType,
            BeanDescription baseDesc) {
        // Look up subtype from dynamic registry
        // ...
    }
}

// Registration
Map<String, Class<?>> registry = Map.of(
    "order", OrderEvent.class,
    "payment", PaymentEvent.class
);
mapper.setDefaultTyping(new DynamicTypeResolverBuilder(registry));
```

### Fix 3: Enable FAIL_ON_INVALID_SUBTYPE to fail fast

Configure the ObjectMapper to raise an error immediately when an unknown type ID is encountered, rather than silently returning null.

```java
ObjectMapper mapper = new ObjectMapper();
mapper.configure(
    DeserializationFeature.FAIL_ON_INVALID_SUBTYPE, true
);

// This ensures that unknown type IDs throw immediately
// instead of being silently ignored or defaulting to null
try {
    BaseEvent event = mapper.readValue(json, BaseEvent.class);
} catch (InvalidTypeIdException e) {
    log.error("Unknown event type in payload: {}", json, e);
}
```

## Related Errors

- {{< relref "jackson-deserialization" >}} — MismatchedInputException
- {{< relref "jackson-mix-in" >}} — InvalidDefinitionException — MixIn Conflict
