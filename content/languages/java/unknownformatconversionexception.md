---
title: "[Solution] Java UnknownFormatConversionException — Unknown Conversion Character Fix"
description: "Fix Java UnknownFormatConversionException by checking conversion characters, using valid conversions (%s, %d, %f, etc.), and escaping % with %%."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 438
---

# UnknownFormatConversionException — Unknown Conversion Character Fix

An `UnknownFormatConversionException` is thrown when an unknown or invalid conversion character is encountered in a format string. Conversion characters follow the `%` in format specifiers.

## Description

`java.util.UnknownFormatConversionException` extends `java.util.IllegalFormatException`. It occurs when the character after `%` (after any flags, width, and precision) is not a valid conversion character.

Valid conversions: `b`, `B`, `h`, `H`, `s`, `S`, `c`, `C`, `d`, `o`, `x`, `X`, `e`, `E`, `f`, `g`, `G`, `t`, `T`, `%`, `n`.

Common message variants:

- `UnknownFormatConversionException: Conversion = q`
- `UnknownFormatConversionException: Unknown conversion`

## Common Causes

```java
// Cause 1: Typo in conversion character
String result = String.format("%q", "hello");
// 'q' is not a valid conversion — throws UnknownFormatConversionException

// Cause 2: Unescaped '%' in format string
String result = String.format("100% done");
// '%' is followed by 'd', making it interpret as integer format
// With different next char: "100%xyz" — throws for 'x' after '%'

// Cause 3: Using format characters from other languages
String result = String.format("%@", "test");  // '@' is not valid
String result = String.format("%i", 42);      // 'i' is not valid (use 'd')
String result = String.format("%D", 42);      // 'D' is not valid (use 'd')

// Cause 4: Accidental conversion in string concatenation
String user = "admin";
String sql = String.format("SELECT * FROM users WHERE role = '%s'", user);
// If user input contains '%', it may be interpreted as format specifier

// Cause 5: Copy-paste from C/C++ printf format strings
String result = String.format("%lld", 42L);  // 'lld' is not valid Java format
String result = String.format("%llu", 42L);  // 'llu' is not valid Java format
```

## Solutions

### Fix 1: Use valid Java conversion characters

```java
// Valid conversions and their types:
// %s  — String, Object (any toString())
// %d  — byte, short, int, long, Integer, etc.
// %f  — float, double, Float, Double
// %e  — scientific notation (float/double)
// %c  — char, Character
// %b  — boolean, Boolean
// %x  — hexadecimal integer
// %o  — octal integer
// %n  — platform-specific line separator
// %%  — literal percent sign

// Examples:
String s = String.format("Name: %s", "Alice");      // String
String d = String.format("Count: %d", 42);           // Decimal integer
String f = String.format("Pi: %f", 3.14159);         // Float
String x = String.format("Hex: %x", 255);            // Hex integer
String b = String.format("Active: %b", true);         // Boolean
String c = String.format("Char: %c", 'A');            // Character
```

### Fix 2: Escape '%' when it's literal text

```java
// Wrong: unescaped '%'
String result = String.format("100% complete");
// Tries to interpret '%c' — UnknownFormatConversionException if next char invalid

// Correct: escape as '%%'
String result = String.format("100%% complete");
System.out.println(result);  // "100% complete"

// In SQL strings with user input — escape user content
String userInput = "50%";
String safe = userInput.replace("%", "%%");
String sql = String.format("SELECT * FROM products WHERE discount = '%s'", safe);
```

### Fix 3: Validate format strings dynamically

```java
public class FormatValidator {
    private static final String VALID_CONVERSIONS = "bBhHsScCdDofFeEgGtT%n";

    public static void checkFormatString(String format) {
        for (int i = 0; i < format.length(); i++) {
            if (format.charAt(i) == '%' && i + 1 < format.length()) {
                char next = format.charAt(i + 1);
                if (!VALID_CONVERSIONS.contains(String.valueOf(next))) {
                    throw new UnknownFormatConversionException(
                        "Conversion = " + next, next);
                }
                i++;  // Skip conversion character
            }
        }
    }
}

// Usage
FormatValidator.checkFormatString("Hello %s, count: %d");  // OK
FormatValidator.checkFormatString("Hello %q");              // Throws
```

### Fix 4: Use String.replace to prevent format injection

```java
public static String safeFormat(String template, Map<String, String> values) {
    String result = template;
    for (Map.Entry<String, String> entry : values.entrySet()) {
        // Escape any '%' in user values
        String escapedValue = entry.getValue().replace("%", "%%");
        result = result.replace("{" + entry.getKey() + "}", escapedValue);
    }
    return result;
}

// Usage
String template = "Hello {name}, your balance is {balance}%";
Map<String, String> values = Map.of("name", "Alice", "balance", "100");
String result = safeFormat(template, values);
System.out.println(result);  // "Hello Alice, your balance is 100%"
```

## Prevention Checklist

- Only use valid Java format conversion characters (`%s`, `%d`, `%f`, `%c`, `%b`, `%x`, `%o`, `%e`, `%g`, `%t`, `%%`, `%n`).
- Always escape `%` as `%%` when it represents a literal percent sign.
- Escape user input before inserting into format strings.
- Validate format strings at application startup.
- Don't copy format strings from C/C++ `printf` — Java has different valid conversions.

## Related Errors

- [IllegalFormatException](../illegalformatexception) — base class for format exceptions.
- [IllegalFormatFlagsException](../illegalformatflagsexception) — illegal flag combination.
- [UnknownFormatFlagsException](../unknownformatflagsexception) — unknown flag character.
