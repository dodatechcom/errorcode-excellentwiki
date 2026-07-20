---
title: "[Solution] PHP DivisionByZeroError — Division By Zero"
description: "Fix PHP DivisionByZeroError by checking divisors, using match/case for zero handling, and validating input."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 55
---

# DivisionByZeroError — Division By Zero

DivisionByZeroError is thrown when a division or modulo operation is performed with a divisor of zero. In PHP 8.0+, this is a proper Error subclass instead of a warning. Division by zero on integers throws `DivisionByZeroError`, while floating-point division by zero produces `INF` or `NAN`.

## Common Causes

```php
<?php
// Cause 1: Direct integer division by zero
$result = 10 / 0; // DivisionByZeroError (integer)

// Cause 2: Modulo with zero
$result = 10 % 0; // DivisionByZeroError

// Cause 3: Unvalidated user input
$divisor = $_GET['divisor'] ?? 0;
$result = 100 / $divisor; // DivisionByZeroError if $divisor is 0

// Cause 4: Zero from calculation used as divisor
$offset = $max - $max; // 0
$page = $total / $offset; // DivisionByZeroError

// Cause 5: Match expression with intdiv()
$a = 5;
$b = 0;
$result = intdiv($a, $b); // DivisionByZeroError
?>
```

## How to Fix

### Fix 1: Check divisor before division

```php
<?php
function safeDivide(int $a, int $b): int|float {
    if ($b === 0) {
        throw new ValueError("Cannot divide $a by zero");
    }
    return $a / $b;
}

try {
    $result = safeDivide(10, 0);
} catch (ValueError $e) {
    echo "Error: " . $e->getMessage();
}
?>
```

### Fix 2: Use match/case with default for zero handling

```php
<?php
function calculate(int $a, int $b): string {
    return match (true) {
        $b === 0 => 'Cannot divide by zero',
        default => (string)($a / $b),
    };
}

echo calculate(10, 0); // "Cannot divide by zero"
echo calculate(10, 2); // "5"
?>
```

### Fix 3: Use float division to avoid the error

```php
<?php
// Float division by zero returns INF, no error
$a = 10.0;
$b = 0.0;
$result = $a / $b; // INF (not an error)

// Check for INF result
if (!is_finite($result)) {
    echo "Result is infinite — division by zero";
}
?>
```

### Fix 4: Validate input before processing

```php
<?php
function calculateAverage(array $numbers): float {
    $count = count($numbers);
    if ($count === 0) {
        return 0.0;
    }
    return array_sum($numbers) / $count;
}
?>
```

## Examples

```php
<?php
// Safe division pattern
function divideWithRemainder(int $dividend, int $divisor): array {
    if ($divisor === 0) {
        throw new \DivisionByZeroError("Divisor cannot be zero");
    }

    return [
        'quotient' => intdiv($dividend, $divisor),
        'remainder' => $dividend % $divisor,
    ];
}

try {
    $result = divideWithRemainder(10, 3);
    echo "Quotient: {$result['quotient']}, Remainder: {$result['remainder']}";
} catch (\DivisionByZeroError $e) {
    echo "Error: " . $e->getMessage();
}
?>
```

## Related Errors

- [PHP ArithmeticError]({{< relref "/languages/php/arithmeticerror" >}}) — arithmetic operation failed
- [PHP ValueError]({{< relref "/languages/php/valueerror" >}}) — invalid value
- [PHP Fatal Error]({{< relref "/languages/php/fatal-error" >}}) — fatal error
