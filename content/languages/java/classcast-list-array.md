---
title: "[Solution] Java ClassCastException — toArray returns Object[], casting to typed array fails"
description: "Fix Java ClassCastException when toarray returns object[], casting to typed array fails with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ClassCastException — toArray returns Object[], casting to typed array fails

A `ClassCastException` occurs when List<String> list = List.of("a","b");
String[] arr = (String[]) list.toArray();  // ClassCastException.

## Common Causes

```java
List<String> list = List.of("a","b");
String[] arr = (String[]) list.toArray();  // ClassCastException
```

## Solutions

```java
// Fix: toArray(String[]::new)
String[] arr = list.toArray(String[]::new);

// Fix: streams
String[] arr = list.stream().toArray(String[]::new);

// Fix: toArray with type token
String[] arr = list.toArray(new String[0]);
```

## Prevention Checklist

- Use toArray(String[]::new).
- Never cast Object[] to typed array.
- Prefer streams for conversion.

## Related Errors

ClassCastException, ArrayStoreException
