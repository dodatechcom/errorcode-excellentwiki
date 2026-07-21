---
title: "[Solution] Deprecated Function Migration: Comparator anonymous class to lambda"
description: "Migrate from deprecated Comparator anonymous class to lambda expressions in Java."
deprecated_function: "new Comparator<T>() {}"
replacement_function: "(a, b) -> ..."
languages: ["java"]
deprecated_since: "Java 8+"
---

# [Solution] Deprecated Function Migration: Comparator anonymous class to lambda

The `new Comparator<T>() {}` has been deprecated in favor of `(a, b) -> ...`.

## Migration Guide

Lambda expressions and Comparator.comparing make sorting much more concise.

## Before (Deprecated)

```java
Collections.sort(names, new Comparator<String>() {
    @Override
    public int compare(String a, String b) {
        return a.compareTo(b);
    }
});
```

## After (Modern)

```java
// Lambda
names.sort((a, b) -> a.compareTo(b));

// Method reference
names.sort(String::compareTo);

// Comparator.comparing
names.sort(Comparator.comparing(String::length));

// Then chaining
users.sort(
    Comparator.comparing(User::getLastName)
              .thenComparing(User::getFirstName)
);
```

## Key Differences

- Lambda is more concise than anonymous class
- Comparator.comparing for key extraction
- thenComparing for multi-field sorting
- Method references for simple cases
