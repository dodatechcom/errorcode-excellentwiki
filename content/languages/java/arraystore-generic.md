---
title: "[Solution] Java ArrayStoreException — storing wrong type in typed array due to generic type erasure"
description: "Fix Java ArrayStoreException when storing wrong type in typed array due to generic type erasure with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ArrayStoreException — storing wrong type in typed array due to generic type erasure

A `ArrayStoreException` occurs when Object[] arr = new String[10];
arr[0] = 42;  // ArrayStoreException.

## Common Causes

```java
Object[] arr = new String[10];
arr[0] = 42;  // ArrayStoreException
```

## Solutions

```java
// Fix: proper array creation
String[] arr = new String[10];
arr[0] = "hello";  // OK

// Fix: use List instead
List<String> list = new ArrayList<>();
list.add("hello");

// Fix: check type before store
if (obj instanceof String) {
    arr[0] = (String) obj;
}
```

## Prevention Checklist

- Use proper typed arrays.
- Prefer List over arrays for type safety.
- Check type before storing in arrays.
- Use List.of() or Arrays.asList() for initialization.

## Related Errors

ClassCastException, ArrayIndexOutOfBoundsException
