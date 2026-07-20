---
title: "[Solution] PHP Warning: Division by Zero"
description: "Fix PHP Warning: Division by zero. Check divisor before division, validate input, use bcmath for precision."
languages: ["php"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 111
---

# PHP Warning: Division by Zero

A division by zero error occurs when you attempt to divide a number by zero. In PHP 8, this produces a warning and returns `INF` (or `NAN` for `0/0`). In PHP 7, it returned `false` with a warning. Always validate the divisor before performing division.

## Common Causes

```php
// Cause 1: Direct division by zero
<?php
$result = 10 / 0;
// Warning: Division by zero
?>
```

```php
// Cause 2: Variable becomes zero from user input
<?php
$divisor = (int) $_GET['divisor'];
$result = 100 / $divisor; // User might send 0
?>
```

```php
// Cause 3: Division after array count
<?php
$items = [];
$average = array_sum($items) / count($items);
// Warning: Division by zero — empty array
?>
```

```php
// Cause 4: Modulo by zero
<?php
$result = 10 % 0;
// Warning: Division by zero
?>
```

```php
// Cause 5: Float precision issues
<?php
$a = 0.1 + 0.2;
$b = $a - 0.3;
$result = 1 / $b; // $b is effectively 0 due to float precision
?>
```

## How to Fix

### Fix 1: Check Divisor Before Division

Always verify the divisor is non-zero before dividing.

```php
<?php
function safeDivide(float $dividend, float $divisor): float|false
{
    if ($divisor == 0) {
        return false;
    }
    return $dividend / $divisor;
}

$result = safeDivide(10, 0);
if ($result === false) {
    echo "Cannot divide by zero";
} else {
    echo $result;
}
?>
```

### Fix 2: Validate User Input

Sanitize and validate all user-provided values before using them in calculations.

```php
<?php
function calculateAverage(array $numbers): float
{
    if (empty($numbers)) {
        return 0.0;
    }
    return array_sum($numbers) / count($numbers);
}

// Safe usage with user input
$divisor = (int) ($_POST['divisor'] ?? 0);
if ($divisor === 0) {
    $result = 0; // or handle the error appropriately
} else {
    $result = 100 / $divisor;
}

echo "Result: {$result}";
?>
```

### Fix 3: Use bcmath for Precise Arithmetic

For financial or precision-critical calculations, use the BC Math extension.

```php
<?php
// bcmath handles zero division properly
function safeBcDiv(string $dividend, string $divisor, int $scale = 2): string
{
    if (bccomp($divisor, '0') === 0) {
        throw new \InvalidArgumentException("Division by zero");
    }
    return bcdiv($dividend, $divisor, $scale);
}

try {
    $result = safeBcDiv('10.50', '3.00', 2);
    echo $result; // 3.50
} catch (\InvalidArgumentException $e) {
    echo $e->getMessage();
}

// Check before dividing
$a = '100';
$b = '0';
if (bccomp($b, '0') !== 0) {
    echo bcdiv($a, $b, 2);
} else {
    echo "Cannot divide by zero";
}
?>
```

### Fix 4: Handle Float Precision Issues

Be aware of floating-point precision when dividing.

```php
<?php
// Problem: float precision
$a = 0.1 + 0.2;
$b = $a - 0.3;
// $b is approximately 5.551115123125783e-17, not exactly 0

// Solution 1: Use epsilon comparison
function isEffectivelyZero(float $value, float $epsilon = 1e-10): bool
{
    return abs($value) < $epsilon;
}

$result = isEffectivelyZero($b) ? '0' : (string) (1 / $b);

// Solution 2: Use bcmath for exact decimal math
$b = bcsub(bcadd('0.1', '0.2', 20), '0.3', 20);
if (bccomp($b, '0') !== 0) {
    echo bcdiv('1', $b, 10);
} else {
    echo "0";
}
?>
```

## Examples

```php
<?php
// Complete safe division utility
class MathHelper
{
    public static function divide(float $a, float $b): float
    {
        if (self::isZero($b)) {
            throw new \DivisionByZeroError("Cannot divide {$a} by zero");
        }
        return $a / $b;
    }

    public static function modulo(int $a, int $b): int
    {
        if ($b === 0) {
            throw new \DivisionByZeroError("Cannot modulo {$a} by zero");
        }
        return $a % $b;
    }

    public static function average(array $numbers): float
    {
        if (empty($numbers)) {
            return 0.0;
        }
        return array_sum($numbers) / count($numbers);
    }

    private static function isZero(float $value, float $epsilon = 1e-10): bool
    {
        return abs($value) < $epsilon;
    }
}

try {
    echo MathHelper::divide(10, 3) . "\n";    // 3.3333...
    echo MathHelper::modulo(10, 3) . "\n";    // 1
    echo MathHelper::average([10, 20, 30]) . "\n"; // 20.0
} catch (\DivisionByZeroError $e) {
    echo "Math error: " . $e->getMessage();
}
?>
```

```php
<?php
// Safe percentage calculation
function percentage(float $part, float $total): float
{
    if (abs($total) < 1e-10) {
        return 0.0;
    }
    return ($part / $total) * 100;
}

echo percentage(25, 100);  // 25.0
echo percentage(0, 0);     // 0.0 (safe)
?>
```

## Related Errors

- [PHP Warning: pow() Invalid Base or Exponent](/languages/php/warning-power-modulus)
- [PHP Fatal Error: Out of Memory](/languages/php/fatal-out-of-memory)
- [PHP Memory Limit Error](/languages/php/memory-limit-error)
