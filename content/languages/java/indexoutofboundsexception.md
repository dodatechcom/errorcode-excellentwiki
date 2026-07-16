---
title: "[Solution] Java IndexOutOfBoundsException — List and Array Bounds Fix"
description: "Fix Java IndexOutOfBoundsException by checking list.size(), using safe iteration, and validating index bounds before accessing elements."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
tags: ["indexoutofboundsexception", "bounds-checking", "list", "array", "iteration"]
date: 2026-07-15
---

# Java IndexOutOfBoundsException

An `IndexOutOfBoundsException` is thrown when you attempt to access an element at an index that is outside the valid range of a list, array, or string. The valid index range is always `0` to `size() - 1`. This exception is unchecked and almost always signals a logic error in index management or loop boundaries.

## Common Causes

```java
// Cause 1: Off-by-one error in a loop
List<String> items = Arrays.asList("a", "b", "c");
for (int i = 0; i <= items.size(); i++) {  // <= is wrong, should be <
    System.out.println(items.get(i));
}

// Cause 2: Accessing an empty list
List<String> empty = new ArrayList<>();
String first = empty.get(0);  // IOOBE

// Cause 3: Hardcoded index without size check
String[] colors = {"red", "green"};
String third = colors[2];  // IOOBE

// Cause 4: Using last() on an empty LinkedList
LinkedList<String> queue = new LinkedList<>();
String head = queue.getFirst();  // IOOBE on empty list
```

## Solutions

### Fix 1: Always check list size before accessing by index

```java
// Wrong — assumes list has at least one element
public String getFirstItem(List<String> list) {
    return list.get(0);
}

// Correct
public String getFirstItem(List<String> list) {
    if (list.isEmpty()) {
        return null; // or throw NoSuchElementException
    }
    return list.get(0);
}
```

### Fix 2: Use enhanced for-loop to avoid index management

```java
// Wrong — manual index can go out of bounds
List<String> items = getItems();
for (int i = 0; i <= items.size(); i++) {
    process(items.get(i));
}

// Correct — iterator handles bounds internally
for (String item : items) {
    process(item);
}
```

### Fix 3: Use `List.get()` with bounds validation

```java
public static <T> T safeGet(List<T> list, int index, T defaultValue) {
    if (list == null || index < 0 || index >= list.size()) {
        return defaultValue;
    }
    return list.get(index);
}

// Usage
List<String> names = Arrays.asList("Alice", "Bob");
String name = safeGet(names, 5, "Unknown");  // returns "Unknown"
```

### Fix 4: Use stream API for safe element access

```java
List<String> items = Arrays.asList("a", "b", "c");

// Safe — stream handles empty lists gracefully
String first = items.stream()
    .findFirst()
    .orElse("default");

// Safe — get element at index using stream
String element = IntStream.range(0, items.size())
    .filter(i -> i == 2)
    .mapToObj(items::get)
    .findFirst()
    .orElse("not found");
```

### Fix 5: Use `Collections.emptyList()` checks for defensive code

```java
import java.util.Collections;

public void processItems(List<String> items) {
    if (items == null || items.isEmpty()) {
        return;
    }
    // Safe to access index 0 here
    String first = items.get(0);
    // ... process remaining items
}
```

## Prevention Tips

- Prefer enhanced for-loops and stream operations over indexed access when possible
- Use IDE warnings and static analysis to detect potential out-of-bounds access
- Write unit tests that include empty collections and boundary indices
- Never use `<=` in index-based for-loops — always use `< list.size()`

## Related Errors

- [NullPointerException](../nullpointerexception) — null reference access
- [IllegalArgumentException](../illegalargumentexception) — invalid method argument
- [UnsupportedOperationException](../unsupportedoperationexception) — unsupported operation on collection
