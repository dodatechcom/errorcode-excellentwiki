---
title: "[Solution] Deprecated Function Migration: manual hashCode to Objects.hash"
description: "Migrate from deprecated manual hashCode to Objects.hash."
deprecated_function: "Manual hashCode"
replacement_function: "Objects.hash()"
languages: ["java"]
deprecated_since: "Java 7+"
---

# [Solution] Deprecated Function Migration: manual hashCode to Objects.hash

The `Manual hashCode` has been deprecated in favor of `Objects.hash()`.

## Migration Guide

Objects.hash is concise and correct

Manual hashCode implementations are error-prone.

## Before (Deprecated)

```java
@Override
public int hashCode() {
    int r = name != null ? name.hashCode() : 0;
    r = 31 * r + (age != null ? age.hashCode() : 0);
    return r;
}
```

## After (Modern)

```java
@Override
public int hashCode() {
    return Objects.hash(name, age);
}
```

## Key Differences

- Objects.hash is concise
- Handles null values
- Less error-prone
