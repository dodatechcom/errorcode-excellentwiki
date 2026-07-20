---
title: "[Solution] Java UnsupportedOperationException — Stream Operations Fix"
description: "Fix Java UnsupportedOperationException in Stream operations by using proper collector, implementing custom collector, and avoiding terminal operations on unmodifiable collections."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 8
---

# UnsupportedOperationException — Stream Operations Fix

An `UnsupportedOperationException` in Stream operations is thrown when a terminal or intermediate operation tries to modify a collection that does not support the requested mutation — typically an unmodifiable collection returned by `List.of()`, `Set.of()`, `Map.of()`, or `Collections.unmodifiable*()`.

## Description

Java 9+ factory methods (`List.of()`, `Set.of()`, `Map.of()`) and `Collections.unmodifiable*()` return views that throw `UnsupportedOperationException` on any mutation attempt. When a Stream's terminal operation (like `collect()`) or intermediate operation (like `sorted()`) internally tries to modify the source collection, this exception occurs.

Message variants:

- `java.lang.UnsupportedOperationException`
- `java.lang.UnsupportedOperationException: null`
- `java.lang.UnsupportedOperationException: add operation not supported`

## Common Causes

```java
// Cause 1: Collecting into an unmodifiable list
List<String> result = List.of("a", "b").stream()
    .collect(Collectors.toList());  // Returns ArrayList — OK
// But this fails:
List<String> result = Stream.of("a", "b")
    .collect(Collectors.toUnmodifiableList());  // creates unmodifiable
// Then trying to modify result.add("c") → UnsupportedOperationException

// Cause 2: In-place sort on unmodifiable list
List<String> list = List.of("c", "a", "b");
list.stream().sorted().collect(Collectors.toList());  // OK — returns new list
list.sort(Comparator.naturalOrder());  // UnsupportedOperationException

// Cause 3: Stream.concat modifying the source
List<String> a = List.of("1", "2");
List<String> b = List.of("3", "4");
Stream.concat(a.stream(), b.stream())...  // may try to modify underlying

// Cause 4: toList() terminal operation on unmodifiable source (Java 16+)
List<String> source = List.of("a", "b");
List<String> result = source.stream().toList();  // returns unmodifiable copy
result.add("c");  // UnsupportedOperationException

// Cause 5: Collectors.toMap with merge function on unmodifiable map
Map<String, Integer> map = Map.of("a", 1);
Map<String, Integer> result = map.entrySet().stream()
    .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
```

## Solutions

### Fix 1: Use a mutable collector

```java
// Wrong — Collectors.toUnmodifiableList creates unmodifiable result
List<String> result = stream.collect(Collectors.toUnmodifiableList());
result.add("oops");  // UnsupportedOperationException

// Right — Collectors.toList creates a mutable ArrayList
List<String> result = stream.collect(Collectors.toList());
result.add("ok");  // works

// Right — collect into a specific mutable collection
List<String> result = stream.collect(Collectors.toCollection(ArrayList::new));
```

### Fix 2: Implement a custom collector when needed

```java
import java.util.stream.Collector;
import java.util.function.Supplier;
import java.util.function.BiConsumer;
import java.util.function.BinaryOperator;
import java.util.Collections;

public class UnmodifiableListCollector {
    public static <T> Collector<T, ?, List<T>> toUnmodifiableList() {
        return Collector.of(
            ArrayList::new,          // mutable accumulator
            List::add,               // add element
            (left, right) -> { left.addAll(right); return left; },  // combine
            Collections::unmodifiableList  // finisher — make unmodifiable
        );
    }
}

// Usage
List<String> result = stream.collect(UnmodifiableListCollector.toUnmodifiableList());
```

### Fix 3: Create a new mutable list from unmodifiable source

```java
// Source is unmodifiable
List<String> source = List.of("a", "b", "c");

// Wrong — trying to modify source directly
source.add("d");  // UnsupportedOperationException

// Right — create a mutable copy
List<String> mutable = new ArrayList<>(source);
mutable.add("d");

// Right — stream and collect into mutable list
List<String> result = source.stream()
    .collect(Collectors.toCollection(ArrayList::new));
result.add("d");
```

### Fix 4: Use Stream.toList() carefully (Java 16+)

```java
// Stream.toList() returns an unmodifiable list
List<String> result = source.stream()
    .filter(s -> s.length() > 2)
    .toList();  // unmodifiable
// result.add("x");  // UnsupportedOperationException

// If you need mutability, use collect(Collectors.toList())
List<String> mutable = source.stream()
    .filter(s -> s.length() > 2)
    .collect(Collectors.toList());  // mutable ArrayList
mutable.add("new");
```

### Fix 5: Use mapToObj to transform without modifying source

```java
// Instead of modifying the source collection
List<String> source = List.of("a", "b", "c");

// Wrong
source.stream().forEach(s -> { /* can't add/remove */ });

// Right — transform and collect
List<String> transformed = source.stream()
    .map(String::toUpperCase)
    .collect(Collectors.toCollection(ArrayList::new));
```

## Prevention Checklist

- Know the difference between `toList()` (mutable) and `toUnmodifiableList()` (immutable).
- Always collect into `ArrayList::new` or `Collectors.toList()` when mutability is needed.
- Never assume `Stream.toList()` returns a mutable list.
- Create mutable copies of unmodifiable collections before modifying them.
- Use `Collectors.toCollection()` to control the exact collection type.
- Document whether returned collections are mutable or immutable.

## Related Errors

- [UnsupportedOperationException](../unsupportedoperationexception) — general operation not supported
- [UnsupportedOperationException Immutable List](../uoe-immutable-list) — modification on `List.of()` result
- [UnsupportedOperationException Immutable Map](../uoe-immutable-map) — modification on `Map.of()` result
- [UnsupportedOperationException Immutable Set](../uoe-immutable-set) — modification on `Set.of()` result
