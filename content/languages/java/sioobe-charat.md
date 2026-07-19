---
title: "[Solution] Java StringIndexOutOfBoundsException — calling charAt() with index >= length or negative"
description: "Fix Java StringIndexOutOfBoundsException when calling charat() with index >= length or negative with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# StringIndexOutOfBoundsException — calling charAt() with index >= length or negative

A `StringIndexOutOfBoundsException` occurs when String s = "hello";
char c = s.charAt(5);  // SIOOBE.

## Common Causes

```java
String s = "hello";
char c = s.charAt(5);  // SIOOBE
```

## Solutions

```java
// Fix: bounds check
if (!s.isEmpty() && index >= 0 && index < s.length()) {
    char c = s.charAt(index);
}

// Fix: toCharArray
for (char c : s.toCharArray()) { process(c); }
```

## Prevention Checklist

- Validate charAt() index within [0, length()).
- Use enhanced for-loops.
- Handle empty strings explicitly.

## Related Errors

IndexOutOfBoundsException, ArrayIndexOutOfBoundsException
