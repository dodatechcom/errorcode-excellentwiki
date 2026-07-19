---
title: "[Solution] Java NumberFormatException — parsing hex or octal strings with wrong radix"
description: "Fix Java NumberFormatException when parsing hex or octal strings with wrong radix with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# NumberFormatException — parsing hex or octal strings with wrong radix

A `NumberFormatException` occurs when String hex = "0xFF";
int v = Integer.parseInt(hex);  // NFE — not decimal.

## Common Causes

```java
String hex = "0xFF";
int v = Integer.parseInt(hex);  // NFE — not decimal
```

## Solutions

```java
// Fix: correct radix
int v = Integer.parseInt(hex, 16);  // 255

// Fix: Integer.decode handles 0x, #, 0
int v = Integer.decode("0xFF");  // 255
int v2 = Integer.decode("#FF");  // 255

// Fix: validate hex
if (input.matches("^0[xX][0-9a-fA-F]+$")) {
    int v = Integer.parseInt(input.substring(2), 16);
}
```

## Prevention Checklist

- Use Integer.decode() for prefixed strings.
- Always specify radix explicitly.
- Use BigInteger for arbitrary-precision hex.

## Related Errors

IllegalArgumentException, ArithmeticException
