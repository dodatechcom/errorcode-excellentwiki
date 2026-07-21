---
title: "[Solution] Deprecated Function Migration: ordinal-based switch to enum-based switch"
description: "Migrate from deprecated ordinal-based switch to enum-based switch."
deprecated_function: "switch (ordinal) { case 0: }"
replacement_function: "switch (enumValue) { case VALUE: }"
languages: ["java"]
deprecated_since: "Java 5+"
---

# [Solution] Deprecated Function Migration: ordinal-based switch to enum-based switch

The `switch (ordinal) { case 0: }` has been deprecated in favor of `switch (enumValue) { case VALUE: }`.

## Migration Guide

Enum-based switch is safer.

## Before (Deprecated)

```java
switch (ordinal) {
    case 0: break;
    case 1: break;
}
```

## After (Modern)

```java
switch (color) {
    case RED: break;
    case GREEN: break;
}
```

## Key Differences

- Enum-based switch is safer
