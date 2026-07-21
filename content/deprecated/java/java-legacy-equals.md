---
title: "[Solution] Deprecated Function Migration: manual null-safe equals to Objects.equals"
description: "Migrate from deprecated manual null-safe equals to Objects.equals."
deprecated_function: "a != null && a.equals(b)"
replacement_function: "Objects.equals(a, b)"
languages: ["java"]
deprecated_since: "Java 7+"
---

# [Solution] Deprecated Function Migration: manual null-safe equals to Objects.equals

The `a != null && a.equals(b)` has been deprecated in favor of `Objects.equals(a, b)`.

## Migration Guide

Objects.equals handles null values safely

Manual null checks before equals are verbose.

## Before (Deprecated)

```java
if (a != null && a.equals(b)) { }
```

## After (Modern)

```java
if (Objects.equals(a, b)) { }
```

## Key Differences

- Objects.equals handles nulls
- Much more concise
