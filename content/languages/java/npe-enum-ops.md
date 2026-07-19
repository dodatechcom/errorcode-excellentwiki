---
title: "[Solution] Java NullPointerException"
description: "Enum Operations on Null"
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# calling methods on null enum references or switch on null enum

A `calling` is thrown when color color = getcolor();.

## Common Causes

```java
Color color = getColor();
String name = color.name();  // NPE if null
switch (color) { ... }  // NPE if null
```

## Solutions

```java
// Fix: null check
if (color != null) { color.name(); }

// Fix: Optional
Optional.ofNullable(getColor()).ifPresent(c -> System.out.println(c.name()));

// Fix: safe lookup
public static <E extends Enum<E>> E safeValueOf(Class<E> c, String n) {
    try { return Enum.valueOf(c, n); }
    catch (IllegalArgumentException e) { return null; }
}
```

## Prevention Checklist

- Null-check enum refs before .name() or switch.
- Use EnumMap only with non-null keys.
- Filter nulls from enum collections.

## Related Errors

[NullPointerException](nullpointerexception), [IllegalArgumentException](illegalargumentexception)
