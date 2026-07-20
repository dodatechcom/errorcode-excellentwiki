---
title: "[Solution] PHP 8.0 Match Expression Error — Non-Exhaustive Match Cases"
description: "Fix PHP 8.0 Match Expression Error by adding default arms, covering all cases, and using proper syntax. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 302
---

# PHP 8.0 Match Expression Error — Non-Exhaustive Match Cases

The Match Expression Error occurs when a `match` expression doesn't cover all possible values or is missing a default arm. PHP 8.0 introduced the `match` expression as a strict, type-safe alternative to `switch`. Unlike `switch`, `match` uses strict comparison (`===`) and should handle every possible case.

## Common Causes

```php
<?php
// Cause 1: Missing default arm and not all cases covered
$status = getStatus(); // Returns 0, 1, or 2
$message = match($status) {
    0 => 'Pending',
    1 => 'Active',
    // Error — 2 is not covered and no default arm
};

// Cause 2: Loose vs strict comparison mismatch
$flag = match($input) {
    '0' => 'string zero',
    0 => 'int zero',
    // Unexpected behavior — match uses ===, not ==
};

// Cause 3: Non-exhaustive enum match (PHP 8.1+)
enum Status { case Active; case Inactive; case Pending; }
$s = Status::Active;
$result = match($s) {
    Status::Active => 'Active',
    // Error — missing Inactive and Pending
};

// Cause 4: Return type mismatch in match arms
function getCode(): int|string {
    return match(rand(0, 1)) {
        0 => 'zero',
        1 => 1,
        // TypeError — arms return different types
    };
}

// Cause 5: Match with void expression
match($value) {
    'save' => saveData(),   // void return
    'load' => loadData(),   // void return — match result unused but inconsistent
};
?>
```

## How to Fix

### Fix 1: Add a default arm to cover all remaining cases

```php
<?php
$status = getStatus();
$message = match($status) {
    0 => 'Pending',
    1 => 'Active',
    default => 'Unknown', // Catches all other values
};
?>
```

### Fix 2: Cover every possible value explicitly

```php
<?php
$direction = getDirection(); // 'north', 'south', 'east', or 'west'
$delta = match($direction) {
    'north' => [0, -1],
    'south' => [0, 1],
    'east'  => [1, 0],
    'west'  => [-1, 0],
};
?>
```

### Fix 3: Handle enum exhaustiveness with all cases

```php
<?php
enum Status {
    case Active;
    case Inactive;
    case Pending;
}

$s = getStatus();
$result = match($s) {
    Status::Active   => 'Active',
    Status::Inactive => 'Inactive',
    Status::Pending  => 'Pending',
};
?>
```

### Fix 4: Ensure consistent return types

```php
<?php
function getCode(): int|string {
    return match(rand(0, 1)) {
        0 => 'zero',
        1 => 'one',
    };
}

// Or keep consistent types
function getStatusCode(): int {
    return match(getInput()) {
        'ok'    => 200,
        'error' => 500,
        default => 404,
    };
}
?>
```

## Examples

```php
<?php
// Match with multiple conditions per arm
$code = match(true) {
    $x > 0 && $y > 0  => 1,
    $x < 0 && $y > 0  => 2,
    $x < 0 && $y < 0  => 3,
    default            => 4,
};

// Match with function calls
$result = match($action) {
    'create' => createUser($data),
    'update' => updateUser($data),
    'delete' => deleteUser($data),
    default  => throw new InvalidArgumentException("Unknown action: $action"),
};

// Match returning different types (valid if return type allows it)
function describe(int|string $value): string {
    return match(true) {
        is_int($value)    => "Integer: $value",
        is_string($value) => "String: \"$value\"",
    };
}
?>
```

## Related Errors

- [PHP 8.0 Named Argument Error](/languages/php/php80-named-argument/) — Incorrect named arguments in function calls
- [PHP 8.1 Enum Error](/languages/php/php81-enums/) — Invalid enum definition or usage
- [PHP 8.0 Match Expression Exhaustiveness](/languages/php/php80-match-expression/) — Ensuring all cases are covered
