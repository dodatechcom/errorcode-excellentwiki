---
title: "[Solution] Java unchecked cast warning — Fix Unchecked Type Cast"
description: "Fix Java compiler warning 'unchecked cast' by using @SuppressWarnings, adding runtime checks, or using wildcards. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["warning"]
error_types: ["compile"]
weight: 412
---

# Java Compiler Warning: unchecked cast

This compile-time warning (not an error by default) occurs when you cast a raw type to a parameterized type. The compiler cannot verify at compile time that the cast is safe because of type erasure — generic type information is erased at runtime.

## Error Message

```
warning: [unchecked] unchecked cast
        List<String> list = (List<String>) rawList;
                             ^
  required: List<String>
  found:    List
```

Other variants:

```
warning: [unchecked] unchecked cast to parameterized type
warning: [unchecked] unchecked cast from Object to Comparable
```

## Common Causes

### Cause 1: Casting Raw Type to Parameterized Type

```java
List rawList = new ArrayList(); // raw type
List<String> strings = (List<String>) rawList; // WARNING: unchecked cast
```

### Cause 2: Casting from Collection with get()

```java
Object obj = getFromStorage();
List<String> strings = (List<String>) obj; // WARNING: unchecked cast
```

### Cause 3: Casting from Deserialized Data

```java
ObjectInputStream ois = new ObjectInputStream(inputStream);
List<String> data = (List<String>) ois.readObject(); // WARNING: unchecked cast
```

### Cause 4: Casting Generic Array

```java
Object[] array = new Object[10];
String[] strings = (String[]) array; // WARNING: unchecked cast
```

### Cause 5: Casting with Generics in Wildcards

```java
List<?> wildcardList = getList();
List<String> strings = (List<String>) wildcardList; // WARNING: unchecked cast
```

### Cause 6: Casting in Utility Methods

```java
public static <T> T deserialize(byte[] data) {
    // WARNING: unchecked cast from Object to T
    return (T) deserializeObject(data);
}
```

## Solutions

### Fix 1: Use @SuppressWarnings

Suppress the warning when you've verified the cast is safe.

```java
@SuppressWarnings("unchecked")
List<String> strings = (List<String>) rawList; // Warning suppressed
```

### Fix 2: Use Class Type Token for Runtime Checking

Pass the Class object to verify the type at runtime.

```java
public static <T> T safeCast(Object obj, Class<T> type) {
    if (type.isInstance(obj)) {
        return type.cast(obj);
    }
    throw new ClassCastException("Cannot cast " + obj.getClass() + " to " + type);
}

List<String> strings = safeCast(rawList, List.class);
```

### Fix 3: Use Wildcards Correctly

```java
// Instead of:
List<String> strings = (List<String>) rawList;

// Use:
@SuppressWarnings("unchecked")
List<? extends Object> safe = (List<? extends Object>) rawList;
```

### Fix 4: Use instanceof Check Before Cast

```java
if (rawList instanceof List) {
    // Still unchecked, but at least we know it's a List
    @SuppressWarnings("unchecked")
    List<String> strings = (List<String>) rawList;
}
```

### Fix 5: Use Type-safe Heterogeneous Container

```java
public class TypeSafeContainer {
    private Map<Class<?>, Object> map = new HashMap<>();

    public <T> void put(Class<T> type, T value) {
        map.put(type, value);
    }

    public <T> T get(Class<T> type) {
        return type.cast(map.get(type)); // safe cast, no unchecked warning
    }
}
```

### Fix 6: Use Proper Generic Methods

```java
// Instead of casting in a utility method:
public static <T> T unsafeDeserialize(byte[] data) {
    return (T) deserializeObject(data); // unchecked
}

// Use a type-safe approach:
public static <T> T safeDeserialize(byte[] data, Class<T> type) {
    return type.cast(deserializeObject(data));
}
```

## Prevention Checklist

- Always check `instanceof` before casting when type safety cannot be guaranteed
- Use `@SuppressWarnings("unchecked")` only after verifying the cast is safe
- Prefer type-safe methods like `Class.cast()` over direct casting
- Avoid raw types — always parameterize generic types
- Use type tokens (passing `Class<T>`) for runtime type checking
- Consider using the Checker Framework for compile-time type safety
- Document why the cast is safe with a comment near `@SuppressWarnings`

## Related Errors

- [X is a raw type (raw-type)](/languages/java/raw-type)
- [incompatible types (incompatible-types)](/languages/java/incompatible-types)
- [incompatible types: possible lossy conversion (incompatible-types-assignment)](/languages/java/incompatible-types-assignment)
