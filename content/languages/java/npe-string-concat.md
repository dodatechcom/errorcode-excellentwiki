---
title: "[Solution] Java NullPointerException"
description: "String Concatenation Arithmetic with Null"
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# auto-unboxing null Integer in arithmetic before string concatenation

A `auto-unboxing` is thrown when integer a = null; int b = 5;.

## Common Causes

```java
Integer a = null; int b = 5;
String msg = "" + (a + b);  // NPE — a+b unboxes null
```

## Solutions

```java
// Fix: use String.valueOf
String msg = "Count: " + String.valueOf(count);

// Fix: Objects.toString with default
String msg = "Count: " + Objects.toString(count, "0");

// Fix: Optional
String msg = "Count: " + Optional.ofNullable(count).map(String::valueOf).orElse("N/A");

// Fix: guard arithmetic
String msg = "Result: " + ((a != null ? a : 0) + b);
```

## Prevention Checklist

- Use String.valueOf() for null-safe concatenation.
- Avoid auto-unboxing nullable types in arithmetic.
- Use Optional.map().orElse() for controlled presentation.

## Related Errors

[NullPointerException](nullpointerexception), [NumberFormatException](numberformatexception)
