---
title: "PHP Warning: round() mode parameter deprecated"
description: "Fix PHP Warning: round() mode parameter deprecated. Learn to use proper RoundingMode constants, check PHP version, and handle the mode parameter correctly."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: round() mode parameter deprecated

This warning occurs when using the deprecated `mode` parameter of `round()` as an integer constant. PHP 8.1+ requires `RoundingMode` enum values instead.

## Common Causes

- Using integer constants like `PHP_ROUND_HALF_UP` directly
- Passing non-enum values to the mode parameter
- Running PHP 8.1 or later without updating the mode argument

## How to Fix

### Use Proper RoundingMode Constants

```php
<?php
// Wrong — deprecated integer constant
$result = round(1.5, 0, PHP_ROUND_HALF_UP);

// Correct — use RoundingMode enum (PHP 8.1+)
$result = round(1.5, 0, RoundingMode::HalfAwayFromZero);
?>
```

### Check PHP Version

```php
<?php
// Wrong — deprecated usage on PHP 8.1+
$result = round(1.5, 0, PHP_ROUND_HALF_DOWN);

// Correct — conditional approach
if (PHP_VERSION_ID >= 80100) {
    $result = round(1.5, 0, RoundingMode::HalfDown);
} else {
    $result = round(1.5, 0, PHP_ROUND_HALF_DOWN);
}
?>
```

### Handle Mode Parameter

```php
<?php
// Wrong — integer mode is deprecated
$result = round(1.5, 0, 3);

// Correct — use named arguments or enum
$result = round(1.5, mode: RoundingMode::HalfEven);
?>
```

## Examples

```php
<?php
// This triggers the warning
$result = round(1.25, 1, PHP_ROUND_HALF_UP);
// Deprecated: round(): Passing non-enum value to mode parameter

// Correct
$result = round(1.25, 1, RoundingMode::HalfAwayFromZero); // 1.3
?>
```

## Related Errors

- [PHP Deprecated: implode()]({{< relref "/languages/php/warning-deprecated-nullable" >}})
- [PHP Warning: number_format()]({{< relref "/languages/php/warning-number-format" >}})
- [PHP Warning: intdiv()]({{< relref "/languages/php/warning-in-intdiv" >}})
