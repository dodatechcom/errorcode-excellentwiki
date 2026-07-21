---
title: "[Solution] Deprecated Function Migration: Arrays.sort with Comparator to parallelSort"
description: "Migrate from deprecated Arrays.sort for large arrays to parallelSort."
deprecated_function: "Arrays.sort(arr, comparator)"
replacement_function: "Arrays.parallelSort(arr, comparator)"
languages: ["java"]
deprecated_since: "Java 8+"
---

# [Solution] Deprecated Function Migration: Arrays.sort with Comparator to parallelSort

The `Arrays.sort(arr, comparator)` has been deprecated in favor of `Arrays.parallelSort(arr, comparator)`.

## Migration Guide

parallelSort uses multiple threads.

## Before (Deprecated)

```java
Arrays.sort(largeArray, comparator);
```

## After (Modern)

```java
Arrays.parallelSort(largeArray, comparator);
```

## Key Differences

- parallelSort uses multiple threads
