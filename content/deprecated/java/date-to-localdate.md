---
title: "[Solution] Deprecated Function Migration: java.util.Date to java.time"
description: "Migrate from deprecated java.util.Date to java.time.LocalDate and related classes in Java."
deprecated_function: "java.util.Date / Calendar"
replacement_function: "java.time (LocalDate, LocalDateTime)"
languages: ["java"]
deprecated_since: "Java 8+"
---

# [Solution] Deprecated Function Migration: java.util.Date to java.time

The `java.util.Date / Calendar` has been deprecated in favor of `java.time (LocalDate, LocalDateTime)`.

## Migration Guide

java.util.Date is mutable, not thread-safe, and has a confusing API. The java.time package provides immutable, thread-safe date/time classes.

## Before (Deprecated)

```java
import java.util.Date;
import java.util.Calendar;
import java.text.SimpleDateFormat;

Date date = new Date();
Calendar cal = Calendar.getInstance();
SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
String formatted = sdf.format(date);
```

## After (Modern)

```java
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

LocalDate today = LocalDate.now();
LocalDate nextWeek = today.plusWeeks(1);
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
String formatted = today.format(formatter);
```

## Key Differences

- LocalDate for date-only, LocalDateTime for date+time
- Immutable -- all methods return new instances
- Thread-safe by design
- Built-in formatting with DateTimeFormatter
