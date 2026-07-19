---
title: "[Solution] Java NumberFormatException — parsing numbers with locale-specific formatting"
description: "Fix Java NumberFormatException when parsing numbers with locale-specific formatting with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# NumberFormatException — parsing numbers with locale-specific formatting

A `NumberFormatException` occurs when String input = "1.234,56";
double v = Double.parseDouble(input);  // NFE.

## Common Causes

```java
String input = "1.234,56";
double v = Double.parseDouble(input);  // NFE
```

## Solutions

```java
// Fix: NumberFormat
NumberFormat f = NumberFormat.getInstance(Locale.GERMAN);
Number n = f.parse("1.234,56");

// Fix: strip non-numeric
String c = input.replaceAll("[^\\d.\\-]", "");
double v = Double.parseDouble(c);
```

## Prevention Checklist

- Use NumberFormat.getInstance(locale).
- Strip separators before parseDouble.
- Use BigDecimal for financial calculations.

## Related Errors

ParseException, IllegalArgumentException
