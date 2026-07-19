---
title: "[Solution] Java IllegalArgumentException — Enum.valueOf() with string not matching any constant"
description: "Fix Java IllegalArgumentException when enum.valueof() with string not matching any constant with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# IllegalArgumentException — Enum.valueOf() with string not matching any constant

A `IllegalArgumentException` occurs when public enum Color { RED, GREEN, BLUE }
Color c = Color.valueOf("red");  // IAE.

## Common Causes

```java
public enum Color { RED, GREEN, BLUE }
Color c = Color.valueOf("red");  // IAE
```

## Solutions

```java
// Fix: case-insensitive lookup
public static <E extends Enum<E>> E fromString(Class<E> c, String v) {
    for (E e : c.getEnumConstants()) {
        if (e.name().equalsIgnoreCase(v)) return e;
    }
    throw new IAE("No "+c.getSimpleName()+" for: "+v);
}

// Fix: EnumUtils
Color c = EnumUtils.getEnum(Color.class, input, null);

// Fix: graceful fallback
try { Color c = Color.valueOf(input); }
catch (IllegalArgumentException e) { c = Color.RED; }
```

## Prevention Checklist

- Normalize input before enum lookup.
- Use case-insensitive comparison.
- Provide default values for invalid input.

## Related Errors

NullPointerException, NoSuchElementException
