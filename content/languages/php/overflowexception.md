---
title: "[Solution] PHP OverflowException — Arithmetic Overflow Occurred"
description: "Fix PHP OverflowException by checking numeric limits, using bcmath for large numbers, and validating before operations."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# OverflowException — Arithmetic Overflow Occurred

This exception is thrown when an arithmetic operation produces a result that is too large to be represented within the available numeric range. In PHP, this can occur with integer overflow on 32-bit systems, floating-point precision issues, or when working with values that exceed PHP_INT_MAX.

## Common Causes

- Integer exceeds PHP_INT_MAX (2147483647 on 32-bit, 9223372036854775807 on 64-bit)
- Arithmetic operations that produce results larger than the type can hold
- Adding positive numbers that together exceed the maximum
- Multiplying large integers without using arbitrary precision

## How to Fix

### Fix 1: Check Numeric Limits Before Operations

Validate that operations will not exceed type limits.

```php
<?php
function safeMultiply(int $a, int $b): int
{
    $result = $a * $b;

    // Check for overflow by verifying the result
    if ($a != 0 && intdiv($result, $a) !== $b) {
        throw new OverflowException(
            "Multiplication overflow: $a * $b exceeds integer range"
        );
    }

    return $result;
}
?>
```

### Fix 2: Use bcmath for Large Number Arithmetic

Use the BCMath extension for arbitrary precision math.

```php
<?php
function largeMultiply(string $a, string $b): string
{
    // bcmath handles arbitrary precision — no overflow possible
    return bcmul($a, $b);
}

// Usage
$result = largeMultiply('99999999999999999999', '99999999999999999999');
echo $result; // 9999999999999999999800000000000000000001
?>
```

### Fix 3: Validate Before Incrementing

Check bounds before incrementing counters or indices.

```php
<?php
function incrementCounter(int &$counter): void
{
    if ($counter >= PHP_INT_MAX) {
        throw new OverflowException("Counter cannot exceed PHP_INT_MAX");
    }
    $counter++;
}
?>
```

### Fix 4: Use GMP Extension for Very Large Numbers

For even larger numbers, use the GMP extension.

```php
<?php
function bigCalc(string $a, string $b): string
{
    $gmpA = gmp_init($a);
    $gmpB = gmp_init($b);

    $result = gmp_mul($gmpA, $gmpB);
    return gmp_strval($result);
}
?>
```

## Examples

```php
<?php
// Example 1: Integer overflow on 32-bit system
$value = 2147483647 + 1;
// On 32-bit: wraps to -2147483648 (overflow)
// Fix: check if $a > PHP_INT_MAX - $b before adding

// Example 2: Multiplication overflow
$a = PHP_INT_MAX;
$result = $a * 2;
// Overflow — result cannot be represented
// Fix: use bcmul((string)$a, '2')

// Example 3: Counter overflow
$counter = PHP_INT_MAX;
$counter++;
// OverflowException
// Fix: validate $counter < PHP_INT_MAX before incrementing
?>
```

## Related Errors

- [PHP UnderflowException]({{< relref "/languages/php/underflowexception" >}})
- [PHP RangeException]({{< relref "/languages/php/rangeexception" >}})
- [PHP Fatal Error: Allowed memory size exhausted]({{< relref "/languages/php/fatal-out-of-memory" >}})
