---
title: "[Solution] Java ClassCastException — casting to Comparable where object doesn't implement it"
description: "Fix Java ClassCastException when casting to comparable where object doesn't implement it with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ClassCastException — casting to Comparable where object doesn't implement it

A `ClassCastException` occurs when Object obj = new Object();
Comparable c = (Comparable) obj;  // ClassCastException.

## Common Causes

```java
Object obj = new Object();
Comparable c = (Comparable) obj;  // ClassCastException
```

## Solutions

```java
// Fix: instanceof check
if (obj instanceof Comparable) { Comparable c = (Comparable) obj; }

// Fix: nullsLast
numbers.sort(Comparator.nullsLast(Comparator.naturalOrder()));

// Fix: safe sort
public static <T> void safeSort(List<T> list, Comparator<T> comp) { list.sort(comp); }
```

## Prevention Checklist

- Use instanceof Comparable before casting.
- Use Comparator.naturalOrder() for known types.
- Use Comparator.nullsFirst/Last for null safety.

## Related Errors

ClassCastException, ClassCastException
