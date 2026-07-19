---
title: "[Solution] Java NullPointerException"
description: "String Operations on Null"
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# calling methods like equals, length, or trim on a null String

A `calling` is thrown when string name = getname();.

## Common Causes

```java
String name = getName();
if (name.equals("admin")) { ... }  // NPE
```

## Solutions

```java
// Fix: literal-first equals
if ("admin".equals(name)) { ... }

// Fix: Objects.equals
if (Objects.equals(name, "admin")) { ... }

// Fix: Optional
String trimmed = Optional.ofNullable(userInput).map(String::trim).orElse("");
```

## Prevention Checklist

- Use literal-first `.equals()`.
- Use `Objects.equals()` for symmetric comparison.
- Use StringUtils from Apache Commons.

## Related Errors

[NullPointerException](nullpointerexception), [IllegalArgumentException](illegalargumentexception)
