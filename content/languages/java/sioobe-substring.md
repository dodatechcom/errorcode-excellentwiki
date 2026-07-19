---
title: "[Solution] Java StringIndexOutOfBoundsException — substring with beginIndex or endIndex exceeding string length"
description: "Fix Java StringIndexOutOfBoundsException when substring with beginindex or endindex exceeding string length with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# StringIndexOutOfBoundsException — substring with beginIndex or endIndex exceeding string length

A `StringIndexOutOfBoundsException` occurs when String s = "hello";
String sub = s.substring(0, 6);  // SIOOBE.

## Common Causes

```java
String s = "hello";
String sub = s.substring(0, 6);  // SIOOBE
```

## Solutions

```java
// Fix: clamp indices
int begin = Math.max(0, Math.min(beginIdx, s.length()));
int end = Math.max(begin, Math.min(endIdx, s.length()));
String sub = s.substring(begin, end);

// Fix: Apache StringUtils
String sub = StringUtils.substring(s, begin, end);
```

## Prevention Checklist

- Validate beginIndex and endIndex.
- Use Math.min()/max() to clamp.
- Use Apache Commons for null-safe ops.

## Related Errors

IndexOutOfBoundsException, NullPointerException
