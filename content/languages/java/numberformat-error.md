---
title: "[Solution] Java NumberFormatException: For Input String Fix"
description: "Fix Java NumberFormatException when parsing strings to numbers. Validate input, use try-catch, and handle empty strings and locale-specific formats."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# NumberFormatException: For Input String

A `NumberFormatException` is thrown when you attempt to parse a `String` into a numeric type (`Integer`, `Long`, `Double`, etc.) but the string does not contain a parsable number. This is one of the most common runtime exceptions when handling user input, CSV data, or API responses.

## Description

Java's numeric parsing methods (`Integer.parseInt`, `Long.parseLong`, `Double.parseDouble`) are strict — they reject empty strings, null strings, non-numeric characters, and numbers exceeding the type's range.

Common variants:

- `NumberFormatException: For input string: ""`
- `NumberFormatException: For input string: "abc"`
- `NumberFormatException: For input string: "9999999999999"` (overflow)
- `NumberFormatException: For input string: "3.14"` (when parsing Integer)

## Common Causes

```java
// Cause 1: Empty string
int num = Integer.parseInt("");  // NumberFormatException

// Cause 2: Non-numeric characters
int num = Integer.parseInt("abc");  // NumberFormatException

// Cause 3: Null string
int num = Integer.parseInt(null);  // NumberFormatException: null argument

// Cause 4: Leading/trailing whitespace
int num = Integer.parseInt("  42  ");  // NumberFormatException

// Cause 5: Number exceeds type range
int num = Integer.parseInt("9999999999999");  // NumberFormatException: overflow

// Cause 6: Decimal in integer parser
int num = Integer.parseInt("3.14");  // NumberFormatException
```

## How to Fix

### Fix 1: Wrap parsing in try-catch

```java
// Wrong — no error handling
String input = "abc";
int number = Integer.parseInt(input);  // NumberFormatException

// Correct
String input = "abc";
int number;
try {
    number = Integer.parseInt(input);
} catch (NumberFormatException e) {
    System.err.println("Invalid number: " + input);
    number = 0;  // default
}
```

### Fix 2: Validate input with regex before parsing

```java
public static int safeParseInt(String input, int defaultValue) {
    if (input == null || input.trim().isEmpty() || !input.trim().matches("-?\\d+")) {
        return defaultValue;
    }
    return Integer.parseInt(input.trim());
}

// Usage
int result = safeParseInt("abc", 0);   // returns 0
int result2 = safeParseInt("42", 0);   // returns 42
int result3 = safeParseInt("", 0);     // returns 0
```

### Fix 3: Use Integer.valueOf with a fallback

```java
public static Integer tryParse(String input) {
    try {
        return Integer.valueOf(input);
    } catch (NumberFormatException e) {
        return null;
    }
}

// Usage
Integer value = tryParse("123");
if (value != null) {
    System.out.println("Parsed: " + value);
}
```

### Fix 4: Trim whitespace before parsing

```java
String rawInput = "  42  ";

// Trim before parsing
String cleaned = rawInput.trim();
if (!cleaned.isEmpty() && cleaned.matches("-?\\d+")) {
    int number = Integer.parseInt(cleaned);
    System.out.println("Parsed: " + number);
}
```

### Fix 5: Use BigDecimal for large or decimal values

```java
import java.math.BigDecimal;

String input = "999999999999.99";
try {
    BigDecimal value = new BigDecimal(input);
    System.out.println("Parsed: " + value);
} catch (NumberFormatException e) {
    System.err.println("Cannot parse: " + input);
}
```

### Fix 6: Use NumberFormat for locale-aware parsing

```java
import java.text.NumberFormat;
import java.text.ParseException;
import java.util.Locale;

NumberFormat format = NumberFormat.getInstance(Locale.US);
try {
    Number number = format.parse("1,234.56");
    double value = number.doubleValue();
} catch (ParseException e) {
    System.err.println("Cannot parse: " + e.getMessage());
}
```

## Examples

This error commonly occurs when:

- Parsing user input from forms without validation
- Reading CSV files where numeric columns contain empty cells
- Converting API response strings to numbers
- Parsing locale-specific numbers (e.g., "1.234,56" vs "1,234.56")

## Related Errors

- [IllegalArgumentException](illegal-argument) — invalid method argument at runtime
- [ArithmeticException](#) — divide by zero or overflow after parsing
- [NullPointerException](nullpointerexception) — null passed to parseInt
