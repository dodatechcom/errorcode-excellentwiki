---
title: "[Solution] Deprecated Function Migration: Iterator.remove to removeIf"
description: "Migrate from deprecated Iterator.remove pattern to removeIf."
deprecated_function: "Iterator.remove()"
replacement_function: "list.removeIf()"
languages: ["java"]
deprecated_since: "Java 8+"
---

# [Solution] Deprecated Function Migration: Iterator.remove to removeIf

The `Iterator.remove()` has been deprecated in favor of `list.removeIf()`.

## Migration Guide

removeIf is more concise.

## Before (Deprecated)

```java
Iterator<Item> it = list.iterator();
while (it.hasNext()) {
    if (it.next().isExpired()) {
        it.remove();
    }
}
```

## After (Modern)

```java
list.removeIf(Item::isExpired);
```

## Key Differences

- removeIf is a one-liner
