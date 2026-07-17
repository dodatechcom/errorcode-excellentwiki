---
title: "[Solution] Java ArithmeticException — Divide by Zero and Precision Fix"
description: "Fix Java ArithmeticException by checking the divisor before dividing, using BigDecimal for precision, and handling integer division carefully."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
date: 2026-07-15
---

# Java ArithmeticException

An `ArithmeticException` is thrown when an illegal arithmetic operation is attempted, most commonly integer division by zero. It can also occur with `BigDecimal` scale operations and integer overflow in certain contexts. This exception is unchecked and is a frequent result of missing divisor validation.

## Common Causes

```java
// Cause 1: Integer division by zero
int result = 10 / 0;  // ArithmeticException

// Cause 2: BigDecimal divide with non-terminating result
BigDecimal a = new BigDecimal("1");
BigDecimal b = new BigDecimal("3");
a.divide(b);  // ArithmeticException: non-terminating decimal expansion

// Cause 3: Modulo by zero
int mod = 10 % 0;  // ArithmeticException

// Cause 4: Integer overflow (unchecked in some contexts)
int max = Integer.MAX_VALUE;
int overflow = max + 1;  // wraps to Integer.MIN_VALUE, no exception
// but explicit checks can throw ArithmeticException
```

## Solutions

### Fix 1: Check the divisor before dividing

```java
// Wrong — no check for zero divisor
public int divide(int numerator, int denominator) {
    return numerator / denominator;
}

// Correct
public int divide(int numerator, int denominator) {
    if (denominator == 0) {
        throw new ArithmeticException("Cannot divide by zero");
    }
    return numerator / denominator;
}
```

### Fix 2: Use `BigDecimal` with a rounding mode

```java
import java.math.BigDecimal;
import java.math.RoundingMode;

// Wrong — throws ArithmeticException for non-terminating results
BigDecimal a = new BigDecimal("1");
BigDecimal b = new BigDecimal("3");
BigDecimal result = a.divide(b);  // ArithmeticException

// Correct — specify scale and rounding mode
BigDecimal result = a.divide(b, 10, RoundingMode.HALF_UP);
// result = 0.3333333333
```

### Fix 3: Use floating-point division when appropriate

```java
// Integer division truncates and can throw on zero
int intResult = 10 / 0;  // ArithmeticException

// Floating-point division returns Infinity, no exception
double doubleResult = 10.0 / 0;  // Infinity
double result = 10.0 / 3;        // 3.3333...

// Cast to double when you need fractional results
int a = 10, b = 3;
double result = (double) a / b;  // 3.3333...
```

### Fix 4: Guard against zero in a reusable utility

```java
public class MathUtils {
    public static int safeDivide(int numerator, int denominator, int fallback) {
        if (denominator == 0) {
            return fallback;
        }
        return numerator / denominator;
    }

    public static BigDecimal safeDivide(BigDecimal a, BigDecimal b, int scale) {
        if (b.compareTo(BigDecimal.ZERO) == 0) {
            return BigDecimal.ZERO;
        }
        return a.divide(b, scale, RoundingMode.HALF_UP);
    }
}

// Usage
int result = MathUtils.safeDivide(10, 0, -1);  // returns -1
BigDecimal result2 = MathUtils.safeDivide(
    new BigDecimal("1"), new BigDecimal("3"), 10
);
```

### Fix 5: Use `Math.floorDiv()` for signed integer division

```java
// Math.floorDiv handles negative divisors correctly
// and throws ArithmeticException for zero divisor
int result = Math.floorDiv(10, 0);  // ArithmeticException

// Safe pattern with try-catch
try {
    int result = Math.floorDiv(numerator, denominator);
} catch (ArithmeticException e) {
    System.err.println("Division by zero or overflow");
}
```

## Prevention Tips

- Always validate that a divisor is non-zero before division in integer contexts
- Use `BigDecimal` with explicit `RoundingMode` for financial and precision-critical calculations
- Prefer `double` division when fractional results are expected and zero results should be `Infinity`
- Write unit tests that include zero-divisor edge cases

## Related Errors

- [NumberFormatException](../numberformatexception) — invalid string-to-number conversion
- [IllegalArgumentException](../illegalargumentexception) — invalid method argument
- [ArithmeticException](#) — integer overflow (BigInteger)
