---
title: "[Solution] Java IllegalFormatCodePointException — Invalid Unicode Code Point Fix"
description: "Fix Java IllegalFormatCodePointException by validating code points, using Character.isValidCodePoint(), and handling supplementary characters."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 436
---

# IllegalFormatCodePointException — Invalid Unicode Code Point Fix

An `IllegalFormatCodePointException` is thrown when an invalid Unicode code point is passed to a `Formatter` via the `c` conversion. This covers code points that are not valid Unicode characters.

## Description

`java.util.IllegalFormatCodePointException` extends `java.util.IllegalFormatException`. It is thrown when the character argument to the `c` conversion is not a valid Unicode code point (i.e., not in the range 0x0000 to 0x10FFFF, or is a surrogate code point in the range 0xD800-0xDFFF).

Common message variants:

- `IllegalFormatCodePointException: c = 0xD800`
- `IllegalFormatCodePointException: Invalid code point`
- `IllegalFormatCodePointException: c = -1`

## Common Causes

```java
// Cause 1: Passing a negative value to %c conversion
int invalidCode = -1;
String result = String.format("%c", invalidCode);
// Throws IllegalFormatCodePointException

// Cause 2: Passing a surrogate code point (reserved for UTF-16 encoding)
int surrogate = 0xD800;  // High surrogate — not a valid standalone code point
String result = String.format("%c", surrogate);
// Throws IllegalFormatCodePointException

// Cause 3: Passing a value beyond Unicode range
int beyondUnicode = 0x110000;  // Beyond max Unicode code point (0x10FFFF)
String result = String.format("%c", beyondUnicode);
// Throws IllegalFormatCodePointException

// Cause 4: Incorrect byte-to-int conversion
byte[] bytes = {(byte) 0xFF, (byte) 0xFE};
int invalidInt = ((bytes[0] & 0xFF) << 8) | (bytes[1] & 0xFF);
String result = String.format("%c", invalidInt);  // May be invalid code point

// Cause 5: Extracting code point from malformed string
String str = "Hello";
int badIndex = str.codePointCount(0, str.length()) + 1;  // Out of range
int cp = str.codePointAt(badIndex);  // Could be -1 or invalid
String result = String.format("%c", cp);
```

## Solutions

### Fix 1: Validate code points before formatting

```java
public static String safeFormatChar(int codePoint) {
    if (!Character.isValidCodePoint(codePoint)) {
        throw new IllegalArgumentException("Invalid code point: 0x" + Integer.toHexString(codePoint));
    }
    return String.format("%c", codePoint);
}

// Usage
try {
    System.out.println(safeFormatChar(0x0041));  // 'A' — OK
    System.out.println(safeFormatChar(0xD800));  // Surrogate — throws
} catch (IllegalArgumentException e) {
    System.err.println(e.getMessage());
}
```

### Fix 2: Use Character.isValidCodePoint() check

```java
public static String formatCodePointSafely(int codePoint) {
    if (Character.isValidCodePoint(codePoint)) {
        return String.format("%c", codePoint);
    } else {
        System.err.println("Skipping invalid code point: 0x" + Integer.toHexString(codePoint));
        return "";  // Return empty or replacement
    }
}

// Usage
int[] codePoints = {0x0041, 0xD800, 0x00E9, 0x10FFFF, -1};
for (int cp : codePoints) {
    String formatted = formatCodePointSafely(cp);
    System.out.println("Code point 0x" + Integer.toHexString(cp) + " -> '" + formatted + "'");
}
```

### Fix 3: Handle supplementary characters correctly

```java
public static String formatStringWithCodePoints(String str) {
    StringBuilder sb = new StringBuilder();
    str.codePoints().forEach(cp -> {
        if (Character.isValidCodePoint(cp)) {
            sb.append(String.format("%c", cp));
        } else {
            sb.append('?');  // Replace invalid code points
        }
    });
    return sb.toString();
}

// Usage
String input = "Hello \uD800 World";  // Contains surrogate
String result = formatStringWithCodePoints(input);
System.out.println(result);
```

### Fix 4: Safely extract and format code points from strings

```java
public static void printCodePoints(String str) {
    int offset = 0;
    while (offset < str.length()) {
        int codePoint = str.codePointAt(offset);
        if (Character.isValidCodePoint(codePoint)) {
            System.out.printf("Code point: 0x%04X = %c%n", codePoint, codePoint);
        } else {
            System.err.printf("Invalid code point at offset %d: 0x%04X%n", offset, codePoint);
        }
        offset += Character.charCount(codePoint);
    }
}
```

## Prevention Checklist

- Always validate code points with `Character.isValidCodePoint()` before using `%c` conversion.
- Never pass surrogate code points (0xD800-0xDFFF) as standalone values.
- Handle supplementary characters (above U+FFFF) using `codePointAt()` and `charCount()`.
- Check for negative values before passing to format conversions.
- Use `codePoints()` stream for safe iteration over string code points.

## Related Errors

- [IllegalFormatException](../illegalformatexception) — base class for format exceptions.
- [StringIndexOutOfBoundsException](../stringindexoutofboundsexception) — invalid string index.
- [IllegalArgumentException](../illegalargumentexception) — invalid argument value.
