---
title: "[Solution] Java ConcurrentModificationException — modifying HashMap during keySet/values/entrySet iteration"
description: "Fix Java ConcurrentModificationException when modifying hashmap during keyset/values/entryset iteration with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ConcurrentModificationException — modifying HashMap during keySet/values/entrySet iteration

A `ConcurrentModificationException` occurs when Map<String,Integer> map = new HashMap<>();
for (String key : map.keySet()) {
    if (map.get(key)==1) map.remove(key);  // CME
}.

## Common Causes

```java
Map<String,Integer> map = new HashMap<>();
for (String key : map.keySet()) {
    if (map.get(key)==1) map.remove(key);  // CME
}
```

## Solutions

```java
// Fix: Iterator.remove()
Iterator<Map.Entry<String,Integer>> it = map.entrySet().iterator();
while (it.hasNext()) {
    if (it.next().getValue()==1) it.remove();
}

// Fix: removeIf
map.entrySet().removeIf(e -> e.getValue()==1);

// Fix: collect keys to remove
List<String> toRemove = new ArrayList<>();
for (var e : map.entrySet()) { if (e.getValue()==1) toRemove.add(e.getKey()); }
toRemove.forEach(map::remove);
```

## Prevention Checklist

- Use Iterator.remove() or removeIf().
- Collect items to remove, then remove.
- Use ConcurrentHashMap for concurrent.

## Related Errors

UnsupportedOperationException, NullPointerException
