---
title: "[Solution] Java ClassNotFoundException — trying to load a generic type parameter erased at runtime"
description: "Fix Java ClassNotFoundException when trying to load a generic type parameter erased at runtime with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ClassNotFoundException — trying to load a generic type parameter erased at runtime

A `ClassNotFoundException` occurs when Type type = List.class.getTypeParameters()[0];
Class.forName(type.getTypeName());  // ClassNotFoundException.

## Common Causes

```java
Type type = List.class.getTypeParameters()[0];
Class.forName(type.getTypeName());  // ClassNotFoundException
```

## Solutions

```java
// Fix: TypeReference (Jackson)
List<MyDTO> list = mapper.readValue(json, new TypeReference<List<MyDTO>>(){});

// Fix: pass Class<T> explicitly
public <T> List<T> deserialize(String json, Class<T> c) {
    return mapper.readValue(json, mapper.getTypeFactory().constructCollectionType(List.class, c));
}

// Fix: store class ref in subclass
public abstract class GenericDao<T> {
    private final Class<T> entityClass;
    protected GenericDao() {
        this.entityClass = (Class<T>)((ParameterizedType)
            getClass().getGenericSuperclass()).getActualTypeArguments()[0];
    }
}
```

## Prevention Checklist

- Pass Class<T> for runtime type resolution.
- Use TypeReference/TypeToken for JSON.
- Store class refs in abstract class constructors.

## Related Errors

ClassNotFoundException, ClassCastException
