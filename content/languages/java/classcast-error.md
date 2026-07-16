---
title: "[Solution] Java ClassCastException: Cannot Be Cast To Fix"
description: "Fix Java ClassCastException when an object cannot be cast. Use generics, instanceof checks, pattern matching, and avoid raw type collections."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
tags: ["classcastexception", "casting", "instanceof", "generics", "type-safety"]
weight: 5
---

# ClassCastException: Cannot Be Cast To

A `ClassCastException` is thrown when you attempt to cast an object to a type it is not an instance of at runtime. Despite Java's compile-time type checking, casts on `Object` references, raw collections, and generic type erasure can produce invalid casts that only fail at runtime.

## Description

Java enforces type safety at compile time, but some casts bypass the compiler and are validated at runtime. When the actual object type doesn't match the target type, the JVM throws `ClassCastException`.

Common variants:

- `ClassCastException: class java.lang.String cannot be cast to class java.lang.Integer`
- `ClassCastException: java.util.HashMap cannot be cast to java.util.List`
- `ClassCastException: class [Ljava.lang.Object; cannot be cast to class [Ljava.lang.String;`

## Common Causes

```java
// Cause 1: Casting Object to wrong type
Object obj = "hello";
Integer num = (Integer) obj;  // ClassCastException

// Cause 2: Raw type collection with mixed types
List list = new ArrayList();
list.add("string");
list.add(42);
String item = (String) list.get(1);  // Integer cannot be cast to String

// Cause 3: Generic type erasure causing unexpected runtime types
List<Integer> numbers = new ArrayList<>();
Object[] arr = numbers.toArray();
String s = (String) arr[0];  // ClassCastException

// Cause 4: Wrong generic type in method chain
Map<String, Object> map = new HashMap<>();
map.put("users", List.of("Alice", "Bob"));
List<Integer> users = (List<Integer>) map.get("users");  // ClassCastException at iteration
```

## How to Fix

### Fix 1: Check type before casting with instanceof

```java
// Wrong
Object obj = getFromMap("key");
String value = (String) obj;

// Correct
Object obj = getFromMap("key");
if (obj instanceof String) {
    String value = (String) obj;
    process(value);
} else {
    log.warn("Expected String, got {}", obj.getClass().getName());
}
```

### Fix 2: Use generics to avoid raw type casts

```java
// Wrong — raw type forces manual casting
Map map = new HashMap();
map.put("name", "Alice");
String name = (String) map.get("name");

// Correct — generic type eliminates the cast
Map<String, String> map = new HashMap<>();
map.put("name", "Alice");
String name = map.get("name");
```

### Fix 3: Use pattern matching for instanceof (Java 16+)

```java
// Traditional
if (obj instanceof String) {
    String s = (String) obj;
    process(s);
}

// Java 16+ — pattern matching eliminates the manual cast
if (obj instanceof String s) {
    process(s);
}

// Combined with null check
if (obj instanceof String s && s.length() > 5) {
    processLongString(s);
}
```

### Fix 4: Use Optional with type-safe methods

```java
// Wrong
User user = (User) session.getAttribute("user");

// Correct
Optional<User> user = Optional.ofNullable(session.getAttribute("user"))
    .filter(u -> u instanceof User)
    .map(u -> (User) u);
user.ifPresent(u -> processOrder(u));
```

### Fix 5: Avoid toArray() followed by unsafe casting

```java
// Wrong
List<Integer> numbers = List.of(1, 2, 3);
Object[] arr = numbers.toArray();
String first = (String) arr[0];  // ClassCastException

// Correct
Integer[] arr = numbers.toArray(new Integer[0]);
List<String> strings = numbers.stream()
    .map(String::valueOf)
    .collect(Collectors.toList());
```

## Examples

This error commonly occurs when:

- Retrieving objects from a session or cache without type checking
- Using raw `ArrayList` or `HashMap` without generics
- Deserializing objects where the class definition has changed
- Casting between unrelated types in a polymorphic hierarchy

## Related Errors

- [NullPointerException](nullpointerexception) — dereferencing a null reference after cast
- [ArrayStoreException](#) — storing wrong type in a typed array
- [UnsupportedClassVersionError](#) — class compiled with newer JVM version
