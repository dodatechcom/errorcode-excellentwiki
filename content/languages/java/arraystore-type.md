---
title: "[Solution] Java ArrayStoreException — storing incompatible type in covariant array"
description: "Fix Java ArrayStoreException when storing incompatible type in covariant array with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ArrayStoreException — storing incompatible type in covariant array

A `ArrayStoreException` occurs when Object[] arr = new String[10];
arr[0] = Integer.valueOf(42);  // ArrayStoreException.

## Common Causes

```java
Object[] arr = new String[10];
arr[0] = Integer.valueOf(42);  // ArrayStoreException
```

## Solutions

```java
// Fix: create correct array type
Object[] arr = new Object[10];
arr[0] = Integer.valueOf(42);  // OK

// Fix: use List<Object>
List<Object> list = new ArrayList<>();
list.add(42);

// Fix: clone array with correct type
String[] src = {"a","b"};
String[] dest = src.clone();  // String[] not Object[]
```

## Prevention Checklist

- Don't rely on array covariance.
- Use List<Object> for heterogeneous collections.
- Clone arrays to preserve type information.

## Related Errors

ClassCastException, ArrayIndexOutOfBoundsException
