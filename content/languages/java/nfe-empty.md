---
title: "[Solution] Java NumberFormatException — parsing empty strings, null, or whitespace into numeric types"
description: "Fix Java NumberFormatException when parsing empty strings, null, or whitespace into numeric types with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# NumberFormatException — parsing empty strings, null, or whitespace into numeric types

A `NumberFormatException` occurs when String input = "";
int v = Integer.parseInt(input);  // NFE.

## Common Causes

```java
String input = "";
int v = Integer.parseInt(input);  // NFE
```

## Solutions

```java
// Fix: check before parse
if (input != null && !input.trim().isEmpty()) { int v = Integer.parseInt(input.trim()); }

// Fix: Optional
Optional<Integer> v = Optional.ofNullable(input).map(String::trim).filter(s->!s.isEmpty()).map(Integer::parseInt);

// Fix: tryParse
public static Optional<Integer> tryParseInt(String s) {
    try { return Optional.of(Integer.parseInt(s.trim())); }
    catch (NumberFormatException e) { return Optional.empty(); }
}
```

## Prevention Checklist

- Validate non-empty before parsing.
- Use trim() before checking.
- Provide defaults for missing input.

## Related Errors

NullPointerException, StringIndexOutOfBoundsException
