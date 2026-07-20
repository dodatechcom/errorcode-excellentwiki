---
title: "[Solution] Java DuplicateFormatFlagsException — Duplicate Format Flag Fix"
description: "Fix Java DuplicateFormatFlagsException by removing duplicate flags, using unique flags per specifier, and checking flag list."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 433
---

# DuplicateFormatFlagsException — Duplicate Format Flag Fix

A `DuplicateFormatFlagsException` is thrown when a format specifier contains the same flag character more than once. Each flag must be unique within a single format specifier.

## Description

`java.util.DuplicateFormatFlagsException` extends `java.util.IllegalFormatException`. It occurs when the same flag character is repeated in a format specifier, such as `"%-+10d"` being written as `"%--10d"`.

Common message variants:

- `DuplicateFormatFlagsException: Flags = '-'`
- `DuplicateFormatFlagsException: Duplicate flag in format specifier`

## Common Causes

```java
// Cause 1: Typo — repeating the same flag
String result = String.format("%--10d", 42);
// Double '-' flag — throws DuplicateFormatFlagsException

// Cause 2: Copy-paste error with multiple flags
String result = String.format("%++10.2f", 3.14);
// Double '+' flag — throws DuplicateFormatFlagsException

// Cause 3: Dynamic format string construction accidentally repeats flags
String flags = "-0";
String format = "%" + flags + flags + "10d";  // "%--0010d"
String result = String.format(format, 42);
// Duplicate '-' and '0' flags

// Cause 4: String concatenation error
String result = String.format("%" + "-" + "-10d", 42);
// Duplicate '-' from concatenation

// Cause 5: Programmatic format building with duplicate flags
StringBuilder sb = new StringBuilder("%");
sb.append('-');
sb.append('0');
sb.append('-');  // Duplicate '-'
sb.append("10d");
String result = String.format(sb.toString(), 42);
```

## Solutions

### Fix 1: Ensure each flag appears only once in the format string

```java
// Wrong: duplicate flags
// String result = String.format("%--10d", 42);

// Correct: unique flags
String result = String.format("%-10d", 42);  // Left-align, width 10
// OR
String result = String.format("%010d", 42);  // Zero-padded, width 10
// OR
String result = String.format("%+-10.2f", 3.14);  // Sign, left-align, width 10, precision 2
```

### Fix 2: Deduplicate flags when building format strings dynamically

```java
public static String buildFormatString(char... flags) {
    // Deduplicate flags
    Set<Character> uniqueFlags = new LinkedHashSet<>();
    for (char flag : flags) {
        if (!uniqueFlags.add(flag)) {
            System.err.println("Warning: Removing duplicate flag '" + flag + "'");
        }
    }

    StringBuilder sb = new StringBuilder("%");
    for (char flag : uniqueFlags) {
        sb.append(flag);
    }
    return sb.toString();
}

// Usage
String fmt = buildFormatString('-', '-', '0', '0', '+');
// Result: "%-0+" (duplicates removed)
```

### Fix 3: Validate flag uniqueness before formatting

```java
public static void validateNoDuplicateFlags(String formatString) {
    Pattern pattern = Pattern.compile("%([-+# ,0]*)");
    Matcher matcher = pattern.matcher(formatString);

    while (matcher.find()) {
        String flags = matcher.group(1);
        Set<Character> seen = new HashSet<>();
        for (char c : flags.toCharArray()) {
            if (!seen.add(c)) {
                throw new DuplicateFormatFlagsException(
                    "Duplicate flag '" + c + "' in format specifier", c);
            }
        }
    }
}

// Usage
validateNoDuplicateFlags("%--10d");  // Throws DuplicateFormatFlagsException
validateNoDuplicateFlags("%-10d");   // OK
```

### Fix 4: Use enum or constants for flags to prevent duplication

```java
public enum FormatFlag {
    LEFT_ALIGN('-'),
    SIGN('+'),
    SPACE(' '),
    ZERO_PAD('0'),
    GROUP(','),
    PARENTHESES('('),
    HASH('#');

    private final char character;

    FormatFlag(char character) {
        this.character = character;
    }

    public char getCharacter() { return character; }
}

public static String formatWithFlags(int value, FormatFlag... flags) {
    Set<FormatFlag> uniqueFlags = EnumSet.copyOf(Arrays.asList(flags));
    StringBuilder sb = new StringBuilder("%");
    for (FormatFlag flag : uniqueFlags) {
        sb.append(flag.getCharacter());
    }
    sb.append("d");
    return String.format(sb.toString(), value);
}

// Usage
String result = formatWithFlags(42, FormatFlag.LEFT_ALIGN, FormatFlag.LEFT_ALIGN);
// Duplicates automatically removed by EnumSet
```

## Prevention Checklist

- Ensure each flag character appears only once per format specifier.
- Use `LinkedHashSet` or `EnumSet` to automatically deduplicate flags when building format strings.
- Validate format strings for duplicate flags before execution.
- Avoid string concatenation for building complex format strings.
- Use constants or enums for flag characters instead of raw character literals.

## Related Errors

- [IllegalFormatFlagsException](../illegalformatflagsexception) — illegal flag combination.
- [FormatFlagsConversionMismatchException](../formatflagsconversionmismatchexception) — flag incompatible with conversion.
- [UnknownFormatFlagsException](../unknownformatflagsexception) — unknown flag character.
