---
title: "[Solution] Java ClassCastException — JSON structure doesn't match expected Java type"
description: "Fix Java ClassCastException when json structure doesn't match expected java type with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ClassCastException — JSON structure doesn't match expected Java type

A `ClassCastException` occurs when Map map = mapper.readValue(json, Map.class);
List<String> names = (List<String>) map.get("names");  // ClassCastException.

## Common Causes

```java
Map map = mapper.readValue(json, Map.class);
List<String> names = (List<String>) map.get("names");  // ClassCastException
```

## Solutions

```java
// Fix: typed deserialization
Map<String,List<String>> map = mapper.readValue(json, new TypeReference<>(){}});

// Fix: @JsonSubTypes for polymorphism
@JsonSubTypes({@JsonSubTypes.Type(value=Dog.class,name="dog")})
public abstract class Animal {}
```

## Prevention Checklist

- Use typed deserialization.
- Use @JsonSubTypes for polymorphic types.
- Validate JSON structure.

## Related Errors

ClassCastException, JsonProcessingException
