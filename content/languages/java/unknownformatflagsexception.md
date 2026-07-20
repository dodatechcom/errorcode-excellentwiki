---
title: "[Solution] Java UnknownFormatFlagsException — Unknown Format Flag Fix"
description: "Fix Java UnknownFormatFlagsException by checking valid flags for conversion, consulting Java docs, and removing unknown flags."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 439
---

# UnknownFormatFlagsException — Unknown Format Flag Fix

An `UnknownFormatFlagsException` is thrown when an unknown flag character is used in a format specifier. Flags appear between `%` and the conversion character in a format string.

## Description

`java.util.UnknownFormatFlagsException` extends `java.util.IllegalFormatException`. It occurs when a character in the flags portion of a format specifier is not one of the recognized flag characters.

Valid flags: `-` (left-align), `+` (force sign), ` ` (space), `0` (zero-pad), `,` (grouping), `(` (parentheses), `#` (alternative form).

Common message variants:

- `UnknownFormatFlagsException: Flag = @`
- `UnknownFormatFlagsException: Unknown flag`

## Common Causes

```java
// Cause 1: Using an unrecognized flag character
String result = String.format("%@10d", 42);
// '@' is not a valid flag — throws UnknownFormatFlagsException

// Cause 2: Typo in flag specification
String result = String.format("%!10d", 42);
// '!' is not a valid flag

// Cause 3: Copying format flags from other programming languages
String result = String.format("%_10d", 42);
// '_' is not a valid Java format flag

// Cause 4: Dynamic format building with invalid characters
String flags = getUserFlags();  // Returns "abc"
String format = "%" + flags + "10d";
String result = String.format(format, 42);
// 'a', 'b', 'c' are not valid flags

// Cause 5: Using '#' with integer conversion (technically wrong conversion, but flag check may trigger first)
String result = String.format("%#10d", 42);
// '#' with 'd' — may trigger UnknownFormatFlagsException or FormatFlagsConversionMismatchException
```

## Solutions

### Fix 1: Use only valid flag characters

```java
// Valid flags for Java format specifiers:
// '-' : Left-align the output (default is right-align)
// '+' : Include sign for positive numbers (numeric only)
// ' ' : Prefix positive numbers with a space
// '0' : Pad with zeros instead of spaces (numeric only)
// ',' : Use locale-specific grouping separators (numeric only)
// '(' : Enclose negative numbers in parentheses
// '#' : Alternative form (floating-point: always show decimal; hex: show 0x prefix)

// Examples with valid flags:
String leftAlign = String.format("%-20s", "hello");    // Left-aligned string
String withSign = String.format("%+10d", 42);          // "+        42"
String zeroPad = String.format("%010d", 42);           // "0000000042"
String grouping = String.format("%,d", 1000000);       // "1,000,000"
String altForm = String.format("%#x", 255);            // "0xff"
```

### Fix 2: Validate flags before formatting

```java
public class FlagValidator {
    private static final Set<Character> VALID_FLAGS = Set.of('-', '+', ' ', '0', ',', '(', '#');

    public static void validateFlags(String formatString) {
        int i = 0;
        while (i < formatString.length()) {
            if (formatString.charAt(i) == '%') {
                i++;  // Skip '%'

                // Skip argument index if present
                while (i < formatString.length() && Character.isDigit(formatString.charAt(i))) {
                    i++;
                }

                // Check for '$' (argument index separator)
                if (i < formatString.length() && formatString.charAt(i) == '$') {
                    i++;
                }

                // Validate flags
                while (i < formatString.length() && VALID_FLAGS.contains(formatString.charAt(i))) {
                    i++;
                }

                // Skip width
                while (i < formatString.length() && Character.isDigit(formatString.charAt(i))) {
                    i++;
                }

                // Skip precision
                if (i < formatString.length() && formatString.charAt(i) == '.') {
                    i++;
                    while (i < formatString.length() && Character.isDigit(formatString.charAt(i))) {
                        i++;
                    }
                }

                // Check conversion character
                if (i < formatString.length()) {
                    char conversion = formatString.charAt(i);
                    if (!"bBhHsScCdDofFeEgGtT%n".contains(String.valueOf(conversion))) {
                        throw new UnknownFormatConversionException(
                            "Conversion = " + conversion, conversion);
                    }
                }
            } else {
                i++;
            }
        }
    }
}

// Usage
FlagValidator.validateFlags("%-+10.2f");  // OK
FlagValidator.validateFlags("%@10d");     // Throws if '@' somehow passes
```

### Fix 3: Strip unknown flags from format strings

```java
public static String cleanFormatFlags(String format) {
    Set<Character> validFlags = Set.of('-', '+', ' ', '0', ',', '(', '#');
    StringBuilder cleaned = new StringBuilder();
    boolean inSpec = false;

    for (int i = 0; i < format.length(); i++) {
        char c = format.charAt(i);

        if (c == '%') {
            inSpec = true;
            cleaned.append(c);
        } else if (inSpec && !validFlags.contains(c) && !Character.isDigit(c)
                   && c != '.' && c != '$' && !"bBhHsScCdDofFeEgGtT%n".contains(String.valueOf(c))) {
            // Skip unknown flag
            System.err.println("Removing unknown flag: '" + c + "'");
        } else {
            cleaned.append(c);
            if ("bBhHsScCdDofFeEgGtT%".contains(String.valueOf(c))) {
                inSpec = false;
            }
        }
    }

    return cleaned.toString();
}

// Usage
String cleaned = cleanFormatFlags("%@-+10d");
System.out.println(cleaned);  // "%-+10d" (@ removed)
```

### Fix 4: Map common mistakes to correct flags

```java
public class FlagMapper {
    public static String mapFlags(String flags) {
        Map<Character, Character> knownMappings = Map.of(
            '_', '-',    // Common mistake: underscore instead of dash
            '=', '0',    // Common mistake: equals instead of zero
            'P', '(',    // Common mistake: uppercase P for parentheses
            'g', ','     // Common mistake: 'g' for grouping instead of ','
        );

        StringBuilder mapped = new StringBuilder();
        for (char c : flags.toCharArray()) {
            Character correct = knownMappings.get(c);
            if (correct != null) {
                System.err.println("Mapping flag '" + c + "' to '" + correct + "'");
                mapped.append(correct);
            } else {
                mapped.append(c);
            }
        }
        return mapped.toString();
    }
}
```

## Prevention Checklist

- Only use valid flag characters: `-`, `+`, ` `, `0`, `,`, `(`, `#`.
- Validate format strings before execution to catch unknown flags.
- Don't copy format strings from other languages without converting.
- Use flag validation utilities when building format strings dynamically.
- Document the correct flags for each conversion type.

## Related Errors

- [IllegalFormatFlagsException](../illegalformatflagsexception) — illegal flag combination.
- [DuplicateFormatFlagsException](../duplicateformatflagsexception) — duplicate flag in specifier.
- [FormatFlagsConversionMismatchException](../formatflagsconversionmismatchexception) — flag incompatible with conversion.
