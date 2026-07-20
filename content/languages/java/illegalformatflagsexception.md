---
title: "[Solution] Java IllegalFormatFlagsException — Illegal Format Flag Combination Fix"
description: "Fix Java IllegalFormatFlagsException by checking flag compatibility, using valid flag combinations, and consulting format specifier docs."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 430
---

# IllegalFormatFlagsException — Illegal Format Flag Combination Fix

An `IllegalFormatFlagsException` is thrown when an illegal or incompatible combination of format flags is given to a `Formatter`. This occurs when flags that cannot coexist are used together in the same format specifier.

## Description

`java.util.IllegalFormatFlagsException` extends `java.util.IllegalFormatException` and is an unchecked exception. It is thrown when format flags are mutually exclusive or when the combination is otherwise invalid for the given conversion.

Common message variants:

- `IllegalFormatFlagsException: Flags = '+' and '-'`
- `IllegalFormatFlagsException: Illegal combination of flags`
- `IllegalFormatFlagsException: Duplicate flags`

## Common Causes

```java
// Cause 1: Using both '+' and '-' flags together (mutually exclusive)
String result = String.format("%+-10d", 42);
// '+' requires sign, '-' left-aligns — illegal combination

// Cause 2: Using '#' with 'd' conversion (flag not applicable)
String result = String.format("%#d", 42);
// '#' is only valid for floating-point and hex/octal conversions

// Cause 3: Using ',' with 's' conversion
String result = String.format("%,s", "hello");
// ',' (locale-specific grouping) is only valid for numeric conversions

// Cause 4: Using '0' with '-' flag (zero padding requires right-alignment)
String result = String.format("%-010d", 42);
// '-' (left-align) and '0' (zero-pad) are incompatible

// Cause 5: Using '^' with unsupported conversion
String result = String.format("%^10s", "hello");
// '^' is an extension flag not supported in standard Java
```

## Solutions

### Fix 1: Avoid using mutually exclusive flags together

```java
// Instead of both '+' and '-' (which are incompatible):
// String result = String.format("%+-10d", 42);  // ERROR

// Use one or the other:
String withSign = String.format("%+10d", 42);   // Forces sign display
String aligned = String.format("%-10d", 42);    // Left-aligns

System.out.println(withSign);  // "       +42"
System.out.println(aligned);   // "42        "
```

### Fix 2: Use only flags that apply to the conversion type

```java
// For 'd' (decimal integer) conversion, only these flags are valid: '-', '+', ' ', '0', ','
String valid = String.format("%,010d", 1234567);  // Comma grouping + zero-pad

// For 's' (string) conversion, only '-' is valid as a flag
String validStr = String.format("%-20s", "hello");  // Left-aligned string

// For 'f' (float) conversion, '-', '+', ' ', '0', '#' are valid
String validFloat = String.format("%+,10.2f", 3.14);  // Sign, comma grouping, width, precision
```

### Fix 3: Validate flags programmatically before formatting

```java
public class FormatValidator {
    private static final Map<Character, Set<Character>> VALID_FLAGS_PER_CONVERSION = Map.of(
        'd', Set.of('-', '+', ' ', '0', ','),
        'f', Set.of('-', '+', ' ', '0', '#', ','),
        'e', Set.of('-', '+', ' ', '0', '#'),
        's', Set.of('-'),
        'c', Set.of('-'),
        'b', Set.of('-')
    );

    public static void validateFormatFlags(char conversion, char... flags) {
        Set<Character> validFlags = VALID_FLAGS_PER_CONVERSION.get(conversion);
        if (validFlags == null) {
            throw new IllegalArgumentException("Unknown conversion: %" + conversion);
        }

        Set<Character> seen = new HashSet<>();
        for (char flag : flags) {
            if (!validFlags.contains(flag)) {
                throw new IllegalFormatFlagsException(
                    "Flag '" + flag + "' is not valid for conversion '%" + conversion + "'", flag);
            }
            if (!seen.add(flag)) {
                throw new IllegalFormatFlagsException(
                    "Duplicate flag '" + flag + "' for conversion '%" + conversion + "'", flag);
            }
        }
    }
}

// Usage
FormatValidator.validateFormatFlags('d', '+', '0');  // OK
FormatValidator.validateFormatFlags('d', '+', '-');   // Throws IllegalFormatFlagsException
```

### Fix 4: Use safe formatting wrapper

```java
public class SafeFormatter {
    public static String format(String format, Object... args) {
        try {
            return String.format(format, args);
        } catch (IllegalFormatFlagsException e) {
            System.err.println("Invalid format flags: " + e.getMessage());
            // Return formatted string without flags
            String simpleFormat = format.replaceAll("[%][+- #,0]*", "%");
            return String.format(simpleFormat, args);
        }
    }
}

// Usage
String result = SafeFormatter.format("%+-10d", 42);  // Falls back to safe format
```

## Prevention Checklist

- Never combine '+' and '-' flags in the same format specifier.
- Only use flags that are valid for the specific conversion type.
- Use '0' padding only with numeric conversions and without '-'.
- Use '#' only with floating-point and hex/octal conversions.
- Test format strings with various inputs to catch flag errors early.

## Related Errors

- [DuplicateFormatFlagsException](../duplicateformatflagsexception) — duplicate flag in format specifier.
- [FormatFlagsConversionMismatchException](../formatflagsconversionmismatchexception) — flag incompatible with conversion.
- [UnknownFormatFlagsException](../unknownformatflagsexception) — unknown flag character.
