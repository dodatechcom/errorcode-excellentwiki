---
title: "[Solution] Deprecated Function Migration: SimpleDateFormat to DateTimeFormatter"
description: "Migrate from deprecated SimpleDateFormat to DateTimeFormatter."
deprecated_function: "SimpleDateFormat"
replacement_function: "DateTimeFormatter"
languages: ["java"]
deprecated_since: "Java 8+"
---

# [Solution] Deprecated Function Migration: SimpleDateFormat to DateTimeFormatter

The `SimpleDateFormat` has been deprecated in favor of `DateTimeFormatter`.

## Migration Guide

DateTimeFormatter is thread-safe.

## Before (Deprecated)

```java
SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
```

## After (Modern)

```java
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
```

## Key Differences

- DateTimeFormatter is thread-safe
