---
title: "[Solution] Java NumberFormatException — invalid exponent, multiple decimals, or trailing chars"
description: "Fix Java NumberFormatException when invalid exponent, multiple decimals, or trailing chars with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# NumberFormatException — invalid exponent, multiple decimals, or trailing chars

A `NumberFormatException` occurs when String s = "1.23e";
double v = Double.parseDouble(s);  // NFE.

## Common Causes

```java
String s = "1.23e";
double v = Double.parseDouble(s);  // NFE
```

## Solutions

```java
// Fix: validate format
if (s.matches("-?\\d+(\\.\\d+)?(e[+-]?\\d+)?")) {
    double v = Double.parseDouble(s);
}

// Fix: NumberFormat
NumberFormat f = NumberFormat.getInstance();
ParsePosition pos = new ParsePosition(0);
Number n = f.parse(s, pos);
if (pos.getIndex() == s.length()) { double v = n.doubleValue(); }
```

## Prevention Checklist

- Validate format before parsing.
- Use BigDecimal for precision.
- Strip non-numeric chars before parsing.

## Related Errors

ArithmeticException, IllegalArgumentException
