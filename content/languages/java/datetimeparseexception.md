---
title: "[Solution] Java DateTimeParseException — Date-Time Parsing Fix"
description: "Fix Java DateTimeParseException by using correct format patterns, handling optional sections, and validating input before parsing."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 51
---

# DateTimeParseException — Date-Time Parsing Fix

A `DateTimeParseException` is thrown when a date-time string cannot be parsed according to the specified format. This is one of the most common exceptions when working with `java.time` APIs and user-provided date strings.

## Description

`java.time.format.DateTimeParseException` extends `DateTimeException`. Common variants include:

- `java.time.format.DateTimeParseException: Text '2024/03/15' could not be parsed at index 4`
- `java.time.format.DateTimeParseException: Unable to obtain LocalDate from TemporalAccessor`
- `java.time.format.DateTimeParseException: Trailing text found`

The exception provides the `parsedString()` and `getErrorIndex()` methods to help diagnose exactly where parsing failed.

## Common Causes

```java
// Cause 1: Format pattern doesn't match the input string
DateTimeFormatter fmt = DateTimeFormatter.ofPattern("yyyy-MM-dd");
LocalDate.parse("03/15/2024", fmt);  // DateTimeParseException: wrong format

// Cause 2: Case sensitivity mismatch
DateTimeFormatter fmt = DateTimeFormatter.ofPattern("MMM dd, yyyy");
LocalDate.parse("mar 15, 2024", fmt);  // DateTimeParseException: expected "Mar"

// Cause 3: Trailing or leading text
DateTimeFormatter fmt = DateTimeFormatter.ofPattern("yyyy-MM-dd");
LocalDate.parse("2024-03-15T00:00:00", fmt);  // DateTimeParseException: trailing text

// Cause 4: Null input
DateTimeFormatter fmt = DateTimeFormatter.ISO_LOCAL_DATE;
LocalDate.parse(null, fmt);  // NullPointerException (not DateTimeParseException)

// Cause 5: Ambiguous patterns
DateTimeFormatter fmt = DateTimeFormatter.ofPattern("dd/MM/yyyy");
LocalDate.parse("1/1/2024", fmt);  // DateTimeParseException: expects two digits for day and month
```

## Solutions

### Fix 1: Match the format pattern to the actual input

```java
// Input: "March 15, 2024"
DateTimeFormatter fmt = DateTimeFormatter.ofPattern("MMMM d, yyyy");
LocalDate date = LocalDate.parse("March 15, 2024", fmt);

// Input: "2024/03/15"
DateTimeFormatter fmt = DateTimeFormatter.ofPattern("yyyy/MM/dd");
LocalDate date = LocalDate.parse("2024/03/15", fmt);
```

### Fix 2: Handle optional or variable-length sections

```java
DateTimeFormatter fmt = new DateTimeFormatterBuilder()
    .appendPattern("yyyy-MM-dd")
    .optionalStart()
    .appendPattern("'T'HH:mm:ss")
    .optionalEnd()
    .toFormatter();

String input1 = "2024-03-15";
String input2 = "2024-03-15T10:30:00";
LocalDate.parse(input1, fmt);   // works
LocalDate.parse(input2, fmt);   // also works
```

### Fix 3: Validate input format before parsing

```java
public static LocalDate parseDateSafe(String input) {
    if (input == null || input.isBlank()) {
        return LocalDate.now();
    }
    // Quick regex check before attempting parse
    if (!input.matches("\\d{4}-\\d{2}-\\d{2}")) {
        throw new IllegalArgumentException("Expected format yyyy-MM-dd, got: " + input);
    }
    return LocalDate.parse(input);
}
```

### Fix 4: Use parseDefaulting for missing components

```java
DateTimeFormatter fmt = DateTimeFormatter.ofPattern("yyyy-MM-dd")
    .withDefaultLocale(Locale.US);

// Or use withChronology to set defaults
DateTimeFormatter fmt = DateTimeFormatter.ofPattern("dd MMM yyyy")
    .withChronology(IsoChronology.INSTANCE);
```

## Prevention Checklist

- Always match the `DateTimeFormatter` pattern exactly to the expected input format
- Use `.optionalStart()` / `.optionalEnd()` for parts that may or may not be present
- Test parsing with all expected input variations (different months, single-digit days, etc.)
- Validate input strings with a quick regex or length check before parsing
- Always handle `DateTimeParseException` in user-facing input parsing

## Related Errors

- [DateTimeException](/languages/java/datetimeexception/) — Thrown by invalid date-time values after successful parsing
- [NumberFormatException](/languages/java/numberformatexception/) — Thrown when numeric components cannot be parsed
- [IllegalArgumentException](/languages/java/illegal-argument/) — Thrown by invalid format pattern strings
