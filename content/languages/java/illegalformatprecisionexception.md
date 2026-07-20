---
title: "[Solution] Java IllegalFormatPrecisionException — Illegal Format Precision Fix"
description: "Fix Java IllegalFormatPrecisionException by using non-negative precision, checking conversion type, and removing precision for unsupported conversions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 431
---

# IllegalFormatPrecisionException — Illegal Format Precision Fix

An `IllegalFormatPrecisionException` is thrown when a negative precision is given, or when the conversion does not support a precision specifier. Precision is specified after the `.` in a format string.

## Description

`java.util.IllegalFormatPrecisionException` extends `java.util.IllegalFormatException`. Precision is only supported for certain conversions: `f`, `e`, `E`, `g`, `G` (floating-point), and `s` (string). Using precision with `d`, `o`, `x`, `b`, `c`, or `h` conversions throws this exception.

Common message variants:

- `IllegalFormatPrecisionException: -1`
- `IllegalFormatPrecisionException: Conversion = d, Precision = 3`
- `IllegalFormatPrecisionException: Precision not supported for conversion`

## Common Causes

```java
// Cause 1: Negative precision value
String result = String.format("%.-1.3s", "hello");
// Precision cannot be negative — throws IllegalFormatPrecisionException

// Cause 2: Using precision with decimal integer conversion
String result = String.format("%.3d", 42);
// 'd' conversion does not support precision — throws IllegalFormatPrecisionException

// Cause 3: Using precision with octal conversion
String result = String.format("%.5o", 255);
// 'o' conversion does not support precision

// Cause 4: Using precision with boolean conversion
String result = String.format("%.2b", true);
// 'b' conversion does not support precision

// Cause 5: Using precision with hexadecimal conversion
String result = String.format("%.4x", 255);
// 'x' conversion does not support precision
```

## Solutions

### Fix 1: Only use precision with supported conversions

```java
// Precision is supported for these conversions:
// f, e, E, g, G — floating-point (controls decimal places)
// s — string (controls max length)
// c — character (in some cases)

// For floating-point:
String result = String.format("%.2f", 3.14159);  // "3.14"

// For strings (truncation):
String result = String.format("%.5s", "Hello World");  // "Hello"

// For integers (NO precision — use width instead):
String result = String.format("%10d", 42);  // "        42"
// NOT: String.format("%.3d", 42);  // ERROR
```

### Fix 2: Use width instead of precision for integer formatting

```java
// Width controls total minimum characters — works with all conversions
String padded = String.format("%010d", 42);    // "0000000042"
String paddedSpace = String.format("%10d", 42);  // "        42"

// For string truncation, use precision:
String truncated = String.format("%.10s", "A very long string");  // "A very lon"
```

### Fix 3: Validate precision before formatting

```java
public class PrecisionValidator {
    private static final Set<Character> PRECISION_SUPPORTED = Set.of('f', 'e', 'E', 'g', 'G', 's');

    public static String safeFormat(String format, Object... args) {
        try {
            return String.format(format, args);
        } catch (IllegalFormatPrecisionException e) {
            System.err.println("Precision error: " + e.getMessage());
            // Remove precision from format string
            String fixed = format.replaceAll("%.\\d+", "%");
            return String.format(fixed, args);
        }
    }
}

// Usage
String result = PrecisionValidator.safeFormat("%.3d", 42);  // Falls back to "%d"
```

### Fix 4: Use conditional precision based on conversion type

```java
public static String formatNumber(double value, char conversion, int precision) {
    if (conversion != 'f' && conversion != 'e' && conversion != 'E' &&
        conversion != 'g' && conversion != 'G') {
        // Precision not supported — use width only
        return String.format("%10" + conversion, value);
    }
    return String.format("%." + precision + conversion, value);
}

// Usage
System.out.println(formatNumber(3.14159, 'f', 2));  // "      3.14"
System.out.println(formatNumber(3.14159, 'd', 2));  // Falls back to width only
```

## Prevention Checklist

- Only use precision with floating-point conversions (`f`, `e`, `E`, `g`, `G`) and `s`.
- Use width (not precision) for controlling minimum character count in integers.
- Always use non-negative precision values.
- Test format strings with various conversion types to catch precision errors.
- Document precision requirements in format string comments.

## Related Errors

- [IllegalFormatWidthException](../illegalformatwidthexception) — illegal format width.
- [IllegalFormatFlagsException](../illegalformatflagsexception) — illegal flag combination.
- [UnknownFormatConversionException](../unknownformatconversionexception) — unknown conversion character.
