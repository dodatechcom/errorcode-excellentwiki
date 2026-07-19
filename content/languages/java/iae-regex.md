---
title: "[Solution] Java IllegalArgumentException — invalid regular expressions passed to Pattern.compile"
description: "Fix Java IllegalArgumentException when invalid regular expressions passed to pattern.compile with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# IllegalArgumentException — invalid regular expressions passed to Pattern.compile

A `IllegalArgumentException` occurs when Pattern.compile("(hello");  // PatternSyntaxException.

## Common Causes

```java
Pattern.compile("(hello");  // PatternSyntaxException
```

## Solutions

```java
// Fix: validate before compile
public static boolean isValidRegex(String p) {
    try { Pattern.compile(p); return true; }
    catch (PatternSyntaxException e) { return false; }
}

// Fix: Pattern.quote for user input
Pattern p = Pattern.compile(Pattern.quote(userInput));

// Fix: pre-compile and cache
private static final Pattern EMAIL = Pattern.compile("^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$");
```

## Prevention Checklist

- Use Pattern.quote() for user input.
- Pre-compile and cache patterns.
- Consider simpler string ops over regex.

## Related Errors

PatternSyntaxException, StackOverflowError
