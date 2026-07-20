---
title: "[Solution] Java ConcurrentModificationException — Generic Collection Fix"
description: "Fix Java ConcurrentModificationException in Iterator, Collection, and Map by using CopyOnWriteArrayList, ConcurrentHashMap, or iterator's remove()."
languages: ["java"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# ConcurrentModificationException — Generic Collection Fix

A `ConcurrentModificationException` is thrown when a collection is structurally modified while being iterated, outside of the iterator's own `remove()` method. This generic variant covers CME across Iterator, Collection, and Map interfaces.

## Description

The exception is part of Java's fail-fast iterator mechanism. When an iterator detects that the underlying collection has been structurally modified (elements added or removed) since iteration began, it throws this exception to prevent unpredictable behavior. This is different from thread-specific CME issues — this covers any modification during single-threaded iteration.

## Common Causes

```java
// Cause 1: Using for-each loop and removing from original collection
List<String> items = new ArrayList<>(Arrays.asList("a", "b", "c"));
for (String item : items) {
    if (item.equals("b")) {
        items.remove(item); // ConcurrentModificationException
    }
}

// Cause 2: Modifying Map during keySet/entrySet iteration
Map<String, Integer> map = new HashMap<>();
map.put("a", 1);
map.put("b", 2);
for (String key : map.keySet()) {
    if (key.equals("a")) {
        map.remove(key); // ConcurrentModificationException
    }
}

// Cause 3: Adding elements during Iterator traversal
List<Integer> numbers = new ArrayList<>(Arrays.asList(1, 2, 3));
Iterator<Integer> it = numbers.iterator();
while (it.hasNext()) {
    Integer num = it.next();
    if (num == 2) {
        numbers.add(4); // ConcurrentModificationException
    }
}

// Cause 4: Using removeIf during for-each loop
Set<String> set = new HashSet<>(Arrays.asList("x", "y", "z"));
for (String s : set) {
    set.removeIf(v -> v.equals("x")); // ConcurrentModificationException
}
```

## Solutions

### Fix 1: Use Iterator's remove() Method

```java
List<String> items = new ArrayList<>(Arrays.asList("a", "b", "c"));
Iterator<String> it = items.iterator();
while (it.hasNext()) {
    String item = it.next();
    if (item.equals("b")) {
        it.remove(); // safe — uses iterator's own remove
    }
}
```

### Fix 2: Use CopyOnWriteArrayList

```java
List<String> items = new CopyOnWriteArrayList<>(Arrays.asList("a", "b", "c"));
for (String item : items) {
    if (item.equals("b")) {
        items.remove(item); // safe — copy-on-write
    }
}
```

### Fix 3: Use ConcurrentHashMap for Map Operations

```java
Map<String, Integer> map = new ConcurrentHashMap<>();
map.put("a", 1);
map.put("b", 2);
for (String key : map.keySet()) {
    if (key.equals("a")) {
        map.remove(key); // safe — ConcurrentHashMap
    }
}
```

### Fix 4: Collect Items to Remove, Then Remove After Iteration

```java
List<String> items = new ArrayList<>(Arrays.asList("a", "b", "c"));
List<String> toRemove = new ArrayList<>();
for (String item : items) {
    if (item.equals("b")) {
        toRemove.add(item);
    }
}
items.removeAll(toRemove); // safe — done after iteration
```

### Fix 5: Use removeIf() (Java 8+)

```java
List<String> items = new ArrayList<>(Arrays.asList("a", "b", "c"));
items.removeIf(item -> item.equals("b")); // safe — internal iterator
```

## Prevention Checklist

- Never modify a collection directly during for-each or Iterator traversal
- Use `Iterator.remove()` for safe removal during iteration
- Prefer `CopyOnWriteArrayList` for read-heavy concurrent scenarios
- Use `ConcurrentHashMap` instead of `HashMap` for concurrent map operations
- Collect elements to remove in a separate list, then remove after iteration completes

## Related Errors

- [IllegalStateException]({{< relref "/languages/java/illegalstateexception" >}}) — iterator already removed element
- [UnsupportedOperationException]({{< relref "/languages/java/unsupportedoperationexception" >}}) — collection is unmodifiable
- [NullPointerException]({{< relref "/languages/java/nullpointerexception" >}}) — null key or value in collection
