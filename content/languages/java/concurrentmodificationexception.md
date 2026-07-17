---
title: "[Solution] Java ConcurrentModificationException — Iterator Fix"
description: "Fix Java ConcurrentModificationException by using iterators for removal, concurrent collections, or synchronized blocks when modifying collections during iteration."
languages: ["java"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# ConcurrentModificationException — Iterator Fix

A `ConcurrentModificationException` is thrown when a collection is modified while being iterated over, outside of the iterator's own `remove()` method. This is a checked exception that signals a structural modification to a collection during iteration.

## Description

The exception is part of Java's fail-fast iterator mechanism. When an iterator detects that the collection has been structurally modified (adding or removing elements) since iteration began, it throws this exception to prevent unpredictable behavior.

## Common Causes

```java
// Cause 1: Modifying collection during for-each loop
List<String> items = new ArrayList<>(Arrays.asList("a", "b", "c"));
for (String item : items) {
    if (item.equals("b")) {
        items.remove(item);  // ConcurrentModificationException
    }
}

// Cause 2: Adding elements during iteration
Map<String, Integer> map = new HashMap<>();
map.put("a", 1);
for (String key : map.keySet()) {
    map.put("b", 2);  // ConcurrentModificationException
}

// Cause 3: Multiple threads accessing non-synchronized collection
List<String> sharedList = new ArrayList<>();
// Thread 1: iterates
// Thread 2: adds element — ConcurrentModificationException

// Cause 4: Using removeIf on wrong collection
Set<String> set = new HashSet<>(Arrays.asList("a", "b", "c"));
for (String s : set) {
    set.removeIf(x -> x.equals("a"));  // modifies during iteration
}
```

## Solutions

```java
// Fix 1: Use Iterator.remove() instead of Collection.remove()
List<String> items = new ArrayList<>(Arrays.asList("a", "b", "c"));
Iterator<String> it = items.iterator();
while (it.hasNext()) {
    String item = it.next();
    if (item.equals("b")) {
        it.remove();  // safe removal via iterator
    }
}

// Fix 2: Use removeIf() (Java 8+)
List<String> items = new ArrayList<>(Arrays.asList("a", "b", "c"));
items.removeIf(item -> item.equals("b"));

// Fix 3: Use CopyOnWriteArrayList for concurrent iteration
List<String> items = new CopyOnWriteArrayList<>(Arrays.asList("a", "b", "c"));
for (String item : items) {
    if (item.equals("b")) {
        items.remove(item);  // safe — copy-on-write
    }
}

// Fix 4: Use ConcurrentHashMap for concurrent map operations
Map<String, Integer> map = new ConcurrentHashMap<>();
map.put("a", 1);
for (String key : map.keySet()) {
    map.computeIfAbsent("b", k -> 2);  // safe
}

// Fix 5: Collect items to remove, then remove after iteration
List<String> toRemove = new ArrayList<>();
for (String item : items) {
    if (item.equals("b")) {
        toRemove.add(item);
    }
}
items.removeAll(toRemove);
```

## Examples

```java
// Common pattern that triggers the exception
Map<String, User> userMap = new HashMap<>();
userMap.put("alice", new User("Alice"));
userMap.put("bob", new User("Bob"));

for (Map.Entry<String, User> entry : userMap.entrySet()) {
    if (entry.getValue().isActive()) {
        userMap.remove(entry.getKey());  // ConcurrentModificationException
    }
}
```

## Related Exceptions

- [IllegalStateException]({{< relref "/languages/java/illegalstateexception" >}}) — iterator already removed
- [UnsupportedOperationException](../unsupportedoperationexception) — collection is unmodifiable
- [NullPointerException](../nullpointerexception) — null key or value in collection
