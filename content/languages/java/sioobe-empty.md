---
title: "[Solution] Java StringIndexOutOfBoundsException — performing operations on empty strings where index access fails"
description: "Fix Java StringIndexOutOfBoundsException when performing operations on empty strings where index access fails with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# StringIndexOutOfBoundsException — performing operations on empty strings where index access fails

A `StringIndexOutOfBoundsException` occurs when String s = "";
char c = s.charAt(0);  // SIOOBE.

## Common Causes

```java
String s = "";
char c = s.charAt(0);  // SIOOBE
```

## Solutions

```java
// Fix: check isEmpty
if (!s.isEmpty()) { char c = s.charAt(0); }

// Fix: safe access
public static Character firstChar(String s) {
    return (s != null && !s.isEmpty()) ? s.charAt(0) : null;
}

// Fix: isBlank
if (!s.isBlank()) { char c = s.trim().charAt(0); }
```

## Prevention Checklist

- Check isEmpty()/isBlank() before character ops.
- Validate lastIndexOf() return before use.
- Test with empty, null, whitespace inputs.

## Related Errors

ArrayIndexOutOfBoundsException, NullPointerException
