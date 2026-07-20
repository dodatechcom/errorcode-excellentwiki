---
title: "PHP Warning: intdiv() division by zero"
description: "Fix PHP Warning: intdiv() division by zero. Learn to check the divisor before dividing, validate input, and use bcmath for high precision."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: intdiv() division by zero

This warning occurs when `intdiv()` is called with a divisor of zero. Integer division by zero is mathematically undefined and results in a warning or error.

## Common Causes

- Accepting user input without validation
- Dividing by a variable that may be zero
- Off-by-one errors in loops

## How to Fix

### Check Divisor Before Division

```php
<?php
// Wrong — divisor may be zero
$result = intdiv($dividend, $divisor);

// Correct — guard with condition
if ($divisor != 0) {
    $result = intdiv($dividend, $divisor);
} else {
    $result = 0;
}
?>
```

### Validate Input

```php
<?php
// Wrong — no input validation
$result = intdiv($numerator, $denominator);

// Correct — validate and sanitize
$denominator = max(1, (int) $denominator);
$result = intdiv((int) $numerator, $denominator);
?>
```

### Use bcmul/bcdiv for Precision

```php
<?php
// Wrong — intdiv truncates
$result = intdiv(10, 3); // 3

// Correct — use bcmath for exact division
$result = bcdiv(10, 3, 2); // '3.33'
$result = (int) bcpow(10, 1); // bcpow for power, bcdiv for division
?>
```

## Examples

```php
<?php
// This triggers the warning
$divisor = 0;
$result = intdiv(10, $divisor);
// Warning: intdiv(): Division by zero

// Correct — check for zero
$result = $divisor != 0 ? intdiv(10, $divisor) : 0;

// Using coercion
$result = intdiv(10, max(1, $divisor));
?>
```

## Related Errors

- [PHP Warning: Division by zero]({{< relref "/languages/php/warning-div-by-zero" >}})
- [PHP Warning: number_format()]({{< relref "/languages/php/warning-number-format" >}})
- [PHP ValueError: intdiv()]({{< relref "/languages/php/valueerror" >}})
