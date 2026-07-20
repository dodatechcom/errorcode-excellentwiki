---
title: "[Solution] Java DateTimeException — Invalid Date-Time Calculation Fix"
description: "Fix Java DateTimeException by validating date ranges, using DateTimeFormatter for parsing, and leveraging TemporalAdjusters for safe date operations."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# DateTimeException — Invalid Date-Time Calculation Fix

A `DateTimeException` is thrown when a date-time calculation or access operation fails because the value is outside the valid range or is semantically invalid. For example, requesting day 32 of January, or month 13 of a year.

## Description

`java.time.DateTimeException` is an unchecked exception from the `java.time` package. Common variants include:

- `java.time.DateTimeException: Invalid int value for MonthDay: 13`
- `java.time.DateTimeException: Invalid value for MonthDay (MonthDay must be between 1 - 12 and Day must be between 1 - 29/30/31)`
- `java.time.DateTimeException: Field DayOfWeek cannot be set to 10`
- `java.time.DateTimeException: Unable to obtain TemporalField from TemporalAccessor`

This exception is thrown by most `java.time` classes when you attempt to create or query a date-time object with impossible values.

## Common Causes

```java
// Cause 1: Invalid day for the given month
LocalDate date = LocalDate.of(2024, 2, 30);  // DateTimeException: Feb has 29 days max in leap year

// Cause 2: Invalid month number
Month month = Month.of(13);  // DateTimeException: invalid month

// Cause 3: Invalid hour/minute/second values
LocalTime time = LocalTime.of(25, 0);  // DateTimeException: hour must be 0-23

// Cause 4: Querying a field that is not supported
LocalDate date = LocalDate.now();
date.get(ChronoField.CLOCK_HOUR_OF_AMPM);  // DateTimeException: field not supported

// Cause 5: Parsing produces out-of-range value
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
LocalDate.parse("2024-13-01", formatter);  // DateTimeException: invalid month
```

## Solutions

### Fix 1: Validate ranges before creating date-time objects

```java
public static LocalDate safeLocalDate(int year, int month, int day) {
    Month m = Month.of(month);  // throws if invalid, but gives clear message
    int maxDay = m.length(Year.isLeap(year));
    if (day < 1 || day > maxDay) {
        throw new DateTimeException("Day " + day + " is out of range for " + m + " " + year);
    }
    return LocalDate.of(year, m, day);
}
```

### Fix 2: Use DateTimeFormatter with resolverStyle for parsing

```java
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("uuuu-MM-dd")
    .withResolverStyle(ResolverStyle.STRICT);

try {
    LocalDate date = LocalDate.parse("2024-02-30", formatter);
} catch (DateTimeException e) {
    System.err.println("Invalid date: " + e.getMessage());
}
```

### Fix 3: Use TemporalAdjusters for safe date navigation

```java
// Instead of manually adding days/months, use TemporalAdjusters
LocalDate today = LocalDate.now();
LocalDate lastDayOfMonth = today.with(TemporalAdjusters.lastDayOfMonth());
LocalDate nextMonday = today.with(TemporalAdjusters.nextOrSame(DayOfWeek.MONDAY));

// Safe month addition that handles overflow
LocalDate threeMonthsLater = today.plusMonths(3)
    .with(TemporalAdjusters.lastDayOfMonth());
```

### Fix 4: Catch and handle with fallback values

```java
public LocalDate parseDateSafe(String input) {
    try {
        return LocalDate.parse(input);
    } catch (DateTimeException e) {
        return LocalDate.now(); // fallback to current date
    }
}
```

## Prevention Checklist

- Always validate date components (year, month, day) before constructing `LocalDate` or `LocalDateTime`
- Use `ResolverStyle.STRICT` when parsing date strings to reject invalid combinations
- Prefer `TemporalAdjusters` over manual arithmetic for date navigation
- Handle leap years explicitly when dealing with February dates
- Wrap date parsing in try-catch blocks and provide meaningful error messages

## Related Errors

- [DateTimeParseException](/languages/java/datetimeparseexception/) — Thrown when parsing a date-time string fails
- [IllegalArgumentException](/languages/java/illegal-argument/) — Thrown by some date-time constructors with invalid arguments
- [ArithmeticException](/languages/java/arithmeticexception/) — Thrown when arithmetic operations overflow
