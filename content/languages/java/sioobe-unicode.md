---
title: "[Solution] Java StringIndexOutOfBoundsException — char-based indexing doesn't match code point boundaries for emoji"
description: "Fix Java StringIndexOutOfBoundsException when char-based indexing doesn't match code point boundaries for emoji with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# StringIndexOutOfBoundsException — char-based indexing doesn't match code point boundaries for emoji

A `StringIndexOutOfBoundsException` occurs when String emoji = "\uD83D\uDE00";
char c = emoji.charAt(0);  // high surrogate, not 😀
int len = emoji.length();  // 2, not 1.

## Common Causes

```java
String emoji = "\uD83D\uDE00";
char c = emoji.charAt(0);  // high surrogate, not 😀
int len = emoji.length();  // 2, not 1
```

## Solutions

```java
// Fix: codePointAt
int cp = emoji.codePointAt(0);  // 128512
int chars = Character.charCount(cp);  // 2

// Fix: codePoints stream
s.codePoints().mapToObj(cp -> new String(Character.toChars(cp))).forEach(System.out::print);

// Fix: offsetByCodePoints
int idx = s.offsetByCodePoints(0, 7);
```

## Prevention Checklist

- Use codePointAt() instead of charAt().
- Use codePoints() stream for iteration.
- length() returns char count, not visible chars.

## Related Errors

IndexOutOfBoundsException, UnsupportedOperationException
