---
title: "[Solution] Deprecated Function Migration: Calendar to java.time in Java"
description: "Migrate from deprecated Calendar to java.time classes."
deprecated_function: "Calendar.getInstance()"
replacement_function: "LocalDateTime.now()"
languages: ["java"]
deprecated_since: "Java 8+"
---

# [Solution] Deprecated Function Migration: Calendar to java.time in Java

The `Calendar.getInstance()` has been deprecated in favor of `LocalDateTime.now()`.

## Migration Guide

java.time is immutable and thread-safe

Calendar is mutable and not thread-safe. java.time provides immutable, thread-safe alternatives.

## Before (Deprecated)

```java
import java.util.Calendar;
import java.text.SimpleDateFormat;

Calendar cal = Calendar.getInstance();
cal.add(Calendar.DAY_OF_MONTH, 7);
Date nextWeek = cal.getTime();
SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
```

## After (Modern)

```java
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

LocalDate today = LocalDate.now();
LocalDate nextWeek = today.plusWeeks(1);
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
String formatted = today.format(formatter);
```

## Key Differences

- LocalDate for date-only
- LocalDateTime for date+time
- Immutable -- thread-safe
- Better API for date arithmetic
