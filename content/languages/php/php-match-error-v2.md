---
title: "[Solution] PHP Match: Unhandled Value Error Fix"
description: "Fix PHP match expression unhandled value errors. Learn how match differs from switch and how to handle all cases."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Match: Unhandled Value Error Fix

A PHP match error occurs when the match expression encounters a value that is not handled by any arm and has no `default` branch. Unlike `switch`, `match` is strict about exhaustive handling.

## What This Error Means

PHP 8.0 introduced the `match` expression as a strict alternative to `switch`. It uses strict comparison (`===`) and requires either all possible values to be covered or a `default` branch. If a value falls through without a match, PHP throws an `UnhandledMatchError`.

## Common Causes

- No `default` branch and an unexpected value is passed
- Using loose comparison expectations with strict `match`
- Numeric values that fall outside expected ranges
- Adding new enum cases or string values without updating match arms

## How to Fix

### 1. Add a default branch

```php
<?php
function describe(int $code): string {
    // WRONG: No default for unexpected codes
    // return match ($code) {
    //     200 => 'OK',
    //     404 => 'Not Found',
    //     500 => 'Server Error',
    // };

    // CORRECT: Include default
    return match ($code) {
        200 => 'OK',
        404 => 'Not Found',
        500 => 'Server Error',
        default => 'Unknown',
    };
}
?>
```

### 2. Use match for strict comparison

```php
<?php
$value = "1";

// WRONG: match uses strict comparison — "1" !== 1
$result = match ($value) {
    1 => 'integer one',
    "1" => 'string one',
    default => 'other',
};

// CORRECT: Match the actual type
$result = match ($value) {
    "1" => 'string one',
    default => 'other',
};
?>
```

### 3. Handle nullable values

```php
<?php
function resolve(?string $input): string {
    // WRONG: Will fail if $input is null
    // return match ($input) {
    //     'admin' => 'Administrator',
    //     'user' => 'Regular User',
    // };

    // CORRECT: Handle null case
    return match ($input) {
        'admin' => 'Administrator',
        'user' => 'Regular User',
        null => 'Anonymous',
        default => 'Unknown',
    };
}
?>
```

### 4. Use match as a return expression

```php
<?php
// CORRECT: match returns a value
$result = match ($action) {
    'create' => createItem(),
    'update' => updateItem(),
    'delete' => deleteItem(),
    default => throw new \InvalidArgumentException("Unknown action: $action"),
};
?>
```

## Related Errors

- [PHP Enum error]({{< relref "/languages/php/php-enumerator-error-v2" >}})
- [PHP Named argument error]({{< relref "/languages/php/php-named-arg-error-v2" >}})
- [PHP Parse error]({{< relref "/languages/php/parse-error" >}})
