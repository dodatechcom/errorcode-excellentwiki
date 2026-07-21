---
title: "[Solution] Deprecated Function Migration: Comparator to Comparable with natural ordering"
description: "Migrate from deprecated Comparator pattern to natural ordering."
deprecated_function: "Collections.sort(list, comparator)"
replacement_function: "list.sort(null)"
languages: ["java"]
deprecated_since: "Java 8+"
---

# [Solution] Deprecated Function Migration: Comparator to Comparable with natural ordering

The `Collections.sort(list, comparator)` has been deprecated in favor of `list.sort(null)`.

## Migration Guide

list.sort(null) uses natural ordering.

## Before (Deprecated)

```java
Collections.sort(list, null);
```

## After (Modern)

```java
list.sort(null);

list.stream().sorted().collect(Collectors.toList());
```

## Key Differences

- list.sort(null) for natural ordering
