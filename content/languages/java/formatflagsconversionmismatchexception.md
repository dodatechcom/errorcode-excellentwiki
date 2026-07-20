---
title: "[Solution] Java FormatFlagsConversionMismatchException — Flag Conversion Mismatch Fix"
description: "Fix Java FormatFlagsConversionMismatchException by removing incompatible flag, checking conversion docs, and using correct flag combination."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 434
---

# FormatFlagsConversionMismatchException — Flag Conversion Mismatch Fix

A `FormatFlagsConversionMismatchException` is thrown when a format flag is incompatible with the given conversion. For example, using the `#` flag with the `d` conversion is invalid.

## Description

`java.util.FormatFlagsConversionMismatchException` extends `java.util.IllegalFormatException`. It occurs when a valid flag is used with a conversion that does not support it.

Common message variants:

- `FormatFlagsConversionMismatchException: Conversion = d, Flag = #`
- `FormatFlagsConversionMismatchException: Flag not applicable to conversion`

## Common Causes

```java
// Cause 1: Using '#' flag with decimal integer conversion
String result = String.format("%#d", 42);
// '#' is only for floating-point and hex/octal — throws mismatch exception

// Cause 2: Using ',' (grouping) flag with string conversion
String result = String.format("%,s", "hello");
// ',' is only for numeric conversions

// Cause 3: Using '0' flag with string conversion
String result = String.format("%020s", "hello");
// '0' is only for numeric conversions — use spaces for strings

// Cause 4: Using '+' flag with string conversion
String result = String.format("%+s", "hello");
// '+' is only for numeric conversions

// Cause 5: Using '#' flag with character conversion
String result = String.format("%#c", 'A');
// '#' doesn't apply to character conversion
```

## Solutions

### Fix 1: Match flags to the correct conversion types

```java
// For 'd' (decimal): only '-', '+', ' ', '0', ','
String d = String.format("%,010d", 1234567);  // "  1,234,567"

// For 'f' (float): '-', '+', ' ', '0', '#', ','
String f = String.format("%#,10.2f", 1234.5);  // "  1,234.50"

// For 's' (string): only '-'
String s = String.format("%-20s", "hello");  // "hello               "

// For 'x' (hex): only '-', '#', '0'
String x = String.format("%#010x", 255);  // "0x000000ff"

// For 'c' (char): only '-'
String c = String.format("%-5c", 'A');  // "A    "
```

### Fix 2: Check flag compatibility before formatting

```java
public class FlagCompatibilityChecker {
    private static final Map<Character, Set<Character>> VALID_FLAGS = Map.of(
        'd', Set.of('-', '+', ' ', '0', ','),
        'f', Set.of('-', '+', ' ', '0', '#', ','),
        'e', Set.of('-', '+', ' ', '0', '#'),
        'E', Set.of('-', '+', ' ', '0', '#'),
        'g', Set.of('-', '+', ' ', '0', '#'),
        'G', Set.of('-', '+', ' ', '0', '#'),
        'o', Set.of('-', '#', '0'),
        'x', Set.of('-', '#', '0'),
        'X', Set.of('-', '#', '0'),
        's', Set.of('-'),
        'S', Set.of('-'),
        'c', Set.of('-'),
        'C', Set.of('-'),
        'b', Set.of('-'),
        'B', Set.of('-'),
        'h', Set.of('-'),
        'H', Set.of('-')
    );

    public static void checkCompatibility(char conversion, String flags) {
        Set<Character> validFlags = VALID_FLAGS.get(conversion);
        if (validFlags == null) return;  // Unknown conversion

        for (char flag : flags.toCharArray()) {
            if (!validFlags.contains(flag)) {
                throw new FormatFlagsConversionMismatchException(
                    "Flag '" + flag + "' is incompatible with conversion '%" + conversion + "'",
                    flag, conversion);
            }
        }
    }
}

// Usage
FlagCompatibilityChecker.checkCompatibility('d', "+0,");  // OK
FlagCompatibilityChecker.checkCompatibility('d', "#");    // Throws exception
```

### Fix 3: Use safe formatting with automatic flag correction

```java
public static String safeFormat(String format, Object... args) {
    try {
        return String.format(format, args);
    } catch (FormatFlagsConversionMismatchException e) {
        System.err.println("Flag mismatch: " + e.getMessage() + " — removing incompatible flag");
        // Remove the problematic flag from the format string
        String fixed = format.replace(String.valueOf(e.getFlags()), "");
        return String.format(fixed, args);
    }
}

// Usage
String result = safeFormat("%#d", 42);  // Falls back to "%d"
System.out.println(result);  // "42"
```

## Prevention Checklist

- Only use flags that are documented as valid for the specific conversion type.
- Test format strings with various conversion types to catch mismatches.
- Use flag compatibility checkers when building format strings dynamically.
- Keep a reference table of valid flag/conversion combinations.
- Catch and handle `FormatFlagsConversionMismatchException` with informative messages.

## Related Errors

- [IllegalFormatFlagsException](../illegalformatflagsexception) — illegal flag combination.
- [DuplicateFormatFlagsException](../duplicateformatflagsexception) — duplicate flag in specifier.
- [UnknownFormatFlagsException](../unknownformatflagsexception) — unknown flag character.
