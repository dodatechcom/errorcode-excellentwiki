---
title: "[Solution] Deprecated Function Migration: Date.parse to LocalDate.parse"
description: "Migrate from deprecated Date.parse to LocalDate.parse."
deprecated_function: "Date.parse(dateString)"
replacement_function: "LocalDate.parse(dateString)"
languages: ["java"]
deprecated_since: "Java 8+"
---

# [Solution] Deprecated Function Migration: Date.parse to LocalDate.parse

The `Date.parse(dateString)` has been deprecated in favor of `LocalDate.parse(dateString)`.

## Migration Guide

LocalDate is immutable.

## Before (Deprecated)

```java
Date date = new Date(Date.parse("2024-01-15"));
```

## After (Modern)

```java
LocalDate date = LocalDate.parse("2024-01-15");
```

## Key Differences

- LocalDate is immutable
