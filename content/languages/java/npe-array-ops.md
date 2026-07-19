---
title: "[Solution] Java NullPointerException"
description: "Array Operations and Element Access"
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# accessing array elements or iterating arrays containing null values

A `accessing` is thrown when object[] data = new object[3];.

## Common Causes

```java
Object[] data = new Object[3];
data[0] = "hello";
String s = (String) data[1];  // null, then s.length() NPE
```

## Solutions

```java
// Fix: check for null
for (Object item : data) {
    if (item instanceof String s) process(s);
}

// Fix: filter nulls before streaming
String[] upper = Arrays.stream(arr).filter(Objects::nonNull)
    .map(String::toUpperCase).toArray(String[]::new);

// Fix: null-safe comparator
Arrays.sort(arr, Comparator.nullsLast(Comparator.naturalOrder()));
```

## Prevention Checklist

- Null-check array elements before use.
- Use Comparator.nullsFirst/Last for sorting.
- Use Arrays.stream().filter(Objects::nonNull).

## Related Errors

[NullPointerException](nullpointerexception), [ArrayIndexOutOfBoundsException](arrayindexoutofboundsexception)
