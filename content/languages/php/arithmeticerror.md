---
title: "[Solution] PHP ArithmeticError — Arithmetic Operation Failed"
description: "Fix PHP ArithmeticError by validating operands, checking shift amounts, and using bcmath for large numbers."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 53
---

# ArithmeticError — Arithmetic Operation Failed

ArithmeticError is thrown when an arithmetic operation fails. Common triggers include bitwise shift by a negative number or integer overflow beyond PHP_INT_MAX. This was introduced in PHP 7.0 as a base class for math-related errors.

## Common Causes

```php
<?php
// Cause 1: Bitwise shift by negative number
$value = 1 << -1; // ArithmeticError

// Cause 2: Bitwise shift exceeding platform integer size
$value = 1 << 64; // ArithmeticError on 64-bit systems

// Cause 3: Division that causes integer overflow
$a = PHP_INT_MAX;
$b = -1;
$result = $a / $b; // ArithmeticError (integer overflow)

// Cause 4: Bitwise NOT on invalid type
$result = ~(1 << -1); // ArithmeticError

// Cause 5: Bitwise shift on very large computed value
$shift = PHP_INT_MAX + 1; // Becomes float
$result = 1 << $shift; // ArithmeticError
?>
```

## How to Fix

### Fix 1: Validate shift amount before bitwise operations

```php
<?php
function safeShiftLeft(int $value, int $shift): int {
    if ($shift < 0 || $shift >= PHP_INT_SIZE * 8) {
        throw new InvalidArgumentException("Shift amount must be between 0 and " . (PHP_INT_SIZE * 8 - 1));
    }
    return $value << $shift;
}

try {
    $result = safeShiftLeft(1, -1);
} catch (ArithmeticError $e) {
    echo "Arithmetic error: " . $e->getMessage();
} catch (InvalidArgumentException $e) {
    echo "Invalid argument: " . $e->getMessage();
}
?>
```

### Fix 2: Use bcmath for large number arithmetic

```php
<?php
// Instead of native integer arithmetic for large numbers:
// $result = PHP_INT_MAX * 2; // ArithmeticError

// Use bcmath functions:
$a = '9223372036854775807'; // PHP_INT_MAX as string
$b = '2';
$result = bcmul($a, $b); // Returns string "18446744073709551614"

echo $result; // No overflow

// Also for division:
$result = bcdiv('100', '3', 10); // "33.3333333333"
?>
```

### Fix 3: Check for overflow before operations

```php
<?php
function safeMultiply(int $a, int $b): int {
    if ($a !== 0 && abs($b) > PHP_INT_MAX / abs($a)) {
        throw new ArithmeticError('Integer overflow detected');
    }
    return $a * $b;
}

try {
    $result = safeMultiply(PHP_INT_MAX, 2);
} catch (ArithmeticError $e) {
    echo "Overflow: " . $e->getMessage();
}
?>
```

## Examples

```php
<?php
// Handling ArithmeticError in a calculator
function calculate(string $operation, int $a, int $b): int|string {
    try {
        return match ($operation) {
            'shift_left' => $a << $b,
            'shift_right' => $a >> $b,
            default => throw new \InvalidArgumentException("Unknown operation"),
        };
    } catch (ArithmeticError $e) {
        return "Error: " . $e->getMessage();
    }
}

echo calculate('shift_left', 1, -1); // Error: Bit shift by negative number
echo calculate('shift_left', 1, 3);  // 8
?>
```

## Related Errors

- [PHP DivisionByZeroError]({{< relref "/languages/php/divisionbyzeroerror" >}}) — division by zero
- [PHP AssertionError]({{< relref "/languages/php/assertionerror" >}}) — assertion failure
- [PHP Fatal Error]({{< relref "/languages/php/fatal-error" >}}) — fatal error
