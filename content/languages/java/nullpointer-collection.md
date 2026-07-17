---
title: "[Solution] Java NullPointerException on Collection Operations Fix"
description: "Fix Java NullPointerException when working with collections: List, Map, Set. Handle null collections, null elements, and use Optional and Collections.emptyList()."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# NullPointerException on Collection Operations

A `NullPointerException` during collection operations is one of the most common Java runtime errors. It occurs when you call methods like `.size()`, `.get()`, `.contains()`, `.add()`, or `.stream()` on a collection reference that is `null`, or when collection elements are `null` and you dereference them.

## Description

Collections in Java are reference types. A `List`, `Map`, or `Set` variable can be `null`, and calling any method on it will throw NPE. Additionally, the collection itself may be non-null but contain `null` elements that cause NPE when accessed and dereferenced.

Common variants:

- `NullPointerException: Cannot invoke "java.util.List.size()" because "list" is null`
- `NullPointerException: Cannot invoke "java.lang.Object.hashCode()" because "key" is null`
- `NullPointerException: Cannot invoke "java.util.stream.Stream.filter()" because the return value of "..." is null`

## Common Causes

```java
// Cause 1: Null collection variable
List<String> list = null;
int size = list.size();  // NPE

// Cause 2: Map.get() returns null
Map<String, String> map = new HashMap<>();
String value = map.get("missing-key");  // null
int len = value.length();  // NPE

// Cause 3: Stream on null collection
List<String> items = getItems();  // returns null
items.stream().filter(s -> s.length() > 3);  // NPE

// Cause 4: Collections.emptyList() vs null
List<String> results = search(query);  // returns null instead of empty list
for (String result : results) {  // NPE
    process(result);
}

// Cause 5: Null element in collection
List<String> list = Arrays.asList("a", null, "c");
list.get(1).toUpperCase();  // NPE on null element
```

## How to Fix

### Fix 1: Initialize collections to empty instead of null

```java
// Wrong
public List<String> findUsers(String query) {
    List<String> results = null;
    if (query != null) {
        results = db.search(query);
    }
    return results;  // May return null
}

// Correct
public List<String> findUsers(String query) {
    if (query == null) {
        return Collections.emptyList();
    }
    return db.search(query);
}
```

### Fix 2: Use null-safe collection operations

```java
// Wrong
List<String> list = getList();
for (String item : list) {  // NPE if list is null
    process(item);
}

// Correct — check first
List<String> list = getList();
if (list != null) {
    for (String item : list) {
        process(item);
    }
}

// Or use default empty list
List<String> list = getList() != null ? getList() : Collections.emptyList();
```

### Fix 3: Handle null values from Map.get()

```java
// Wrong
Map<String, User> userMap = buildMap();
User user = userMap.get(userId);
String name = user.getName();  // NPE if userId not in map

// Correct
User user = userMap.get(userId);
if (user != null) {
    String name = user.getName();
}

// Or use Optional
Optional.ofNullable(userMap.get(userId))
    .map(User::getName)
    .ifPresent(this::processName);
```

### Fix 4: Use Objects.requireNonNull for method entry

```java
import java.util.Objects;
import java.util.List;

public void processItems(List<String> items) {
    Objects.requireNonNull(items, "items list must not be null");
    items.stream()
        .filter(Objects::nonNull)
        .forEach(this::process);
}
```

### Fix 5: Use nullable stream operations safely

```java
// Wrong
List<String> items = getItems();
items.stream().filter(s -> s.length() > 3).toList();  // NPE if items is null

// Correct
List<String> items = getItems();
Optional.ofNullable(items)
    .orElse(Collections.emptyList())
    .stream()
    .filter(Objects::nonNull)
    .filter(s -> s.length() > 3)
    .toList();
```

## Examples

This error commonly occurs when:

- A database query returns `null` instead of an empty collection
- A method returns `null` when the caller expects an empty collection
- Using `Map.get()` without checking for `null` before dereferencing
- Streaming over a collection that was not initialized

## Related Errors

- [NullPointerException](nullpointerexception) — general null reference access
- [NoSuchElementException](#) — calling `.get()` on empty Optional
- [UnsupportedOperationException](#) — modifying an unmodifiable collection
