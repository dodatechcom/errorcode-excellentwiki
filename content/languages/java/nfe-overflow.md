---
title: "[Solution] Java NumberFormatException — parsing number strings exceeding Integer/Long max values"
description: "Fix Java NumberFormatException when parsing number strings exceeding integer/long max values with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# NumberFormatException — parsing number strings exceeding Integer/Long max values

A `NumberFormatException` occurs when String s = "2147483648";
int v = Integer.parseInt(s);  // NFE.

## Common Causes

```java
String s = "2147483648";
int v = Integer.parseInt(s);  // NFE
```

## Solutions

```java
// Fix: BigInteger
BigInteger big = new BigInteger(s);
if (big.compareTo(BigInteger.valueOf(Integer.MAX_VALUE)) > 0) { /* handle */ }

// Fix: Long intermediate
long lv = Long.parseLong(s);
if (lv > Integer.MAX_VALUE || lv < Integer.MIN_VALUE) throw new IAE("out of range");
int iv = (int) lv;

// Fix: Math.toIntExact
int iv = Math.toIntExact(lv);  // ArithmeticException on overflow
```

## Prevention Checklist

- Use BigInteger for large numbers.
- Check string length before parseInt.
- Use Math.toIntExact() for safe conversion.

## Related Errors

ArithmeticException, IllegalArgumentException
