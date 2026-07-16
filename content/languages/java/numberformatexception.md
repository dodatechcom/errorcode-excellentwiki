---
title: "[Solution] Java NumberFormatException — Safe String-to-Number Parsing"
description: "Fix Java NumberFormatException by validating input before parsing, using try-catch blocks, and regex checks for safe string-to-number conversion."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
tags: ["numberformatexception", "parsing", "input-validation", "integer"]
date: 2026-07-15
---

# Java NumberFormatException

A `NumberFormatException` is thrown when you attempt to convert a `String` that does not contain a parsable number into a numeric type such as `Integer`, `Long`, `Double`, or `Float`. It is an unchecked exception and is one of the most common runtime errors in Java applications that handle user input.

## Common Causes

```java
// Cause 1: Empty string
int num = Integer.parseInt("");  // NFE

// Cause 2: Non-numeric characters
int num = Integer.parseInt("abc");  // NFE

// Cause 3: Null string
int num = Integer.parseInt(null);  // NFE: null argument

// Cause 4: Leading/trailing whitespace
int num = Integer.parseInt("  42  ");  // NFE in strict parsers

// Cause 5: Number exceeds type range
int num = Integer.parseInt("9999999999999");  // NFE: overflow
```

## Solutions

### Fix 1: Wrap parsing in a try-catch block

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
    number = 0; // default value
}
```

### Fix 2: Validate input with a regex before parsing

```java
public static int safeParseInt(String input, int defaultValue) {
    if (input == null || !input.matches("-?\\d+")) {
        return defaultValue;
    }
    return Integer.parseInt(input);
}

// Usage
int result = safeParseInt("abc", 0);   // returns 0
int result2 = safeParseInt("42", 0);   // returns 42
```

### Fix 3: Use `Integer.valueOf()` with a fallback

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

### Fix 4: Trim and validate user input

```java
String rawInput = "  42  ";

// Trim whitespace before parsing
String cleaned = rawInput.trim();
if (!cleaned.isEmpty() && cleaned.matches("-?\\d+")) {
    int number = Integer.parseInt(cleaned);
    System.out.println("Parsed: " + number);
} else {
    System.out.println("Invalid input");
}
```

### Fix 5: Use `BigDecimal` for large or decimal values

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

## Prevention Tips

- Always validate external input (form fields, CSV data, API responses) before parsing
- Use `Optional<Integer>` to signal that a parse result may be absent
- Set clear error messages so users know what input format is expected
- Prefer `BigDecimal` for financial or precision-critical calculations

## Related Errors

- [IllegalArgumentException](../illegalargumentexception) — invalid method argument at runtime
- [ArithmeticException](../arithmeticexception) — divide by zero or overflow
- [NullPointerException](../nullpointerexception) — null reference access
