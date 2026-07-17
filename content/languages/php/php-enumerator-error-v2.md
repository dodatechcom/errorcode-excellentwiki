---
title: "[Solution] PHP Enum Case Not Handled Error Fix"
description: "Fix PHP Enum errors when a case is not handled in a match or switch. Learn PHP 8.1 enum best practices."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["enum", "enum-case", "match", "php", "exhaustive"]
weight: 5
---

# PHP Enum: Case Not Handled Error Fix

A PHP Enum error occurs when a `match` expression or `switch` statement does not handle all possible enum cases. PHP enums are strict — you must handle every case or use a default.

## What This Error Means

PHP 8.1 introduced backed and non-backed enums. When using enums with `match`, PHP expects exhaustive handling of all cases unless a `default` branch is provided. Missing a case produces a runtime error when that unhandled case is encountered.

## Common Causes

- Forgetting to add a `default` case in a match expression
- Not handling all enum cases when the enum gains new values
- Using `switch` with an enum but not covering all cases
- New enum cases added later that existing code doesn't handle

## How to Fix

### 1. Add a default case for safety

```php
<?php
enum Status {
    case Active;
    case Inactive;
    case Pending;
}

function getStatusLabel(Status $status): string {
    // WRONG: Missing cases
    // return match ($status) {
    //     Status::Active => 'Active',
    //     Status::Inactive => 'Inactive',
    // };

    // CORRECT: Handle all cases or add default
    return match ($status) {
        Status::Active => 'Active',
        Status::Inactive => 'Inactive',
        Status::Pending => 'Pending',
        default => 'Unknown',
    };
}
?>
```

### 2. Use exhaustive matching for backed enums

```php
<?php
enum Color: string {
    case Red = 'red';
    case Green = 'green';
    case Blue = 'blue';
}

function hexCode(Color $color): string {
    return match ($color) {
        Color::Red => '#FF0000',
        Color::Green => '#00FF00',
        Color::Blue => '#0000FF',
    }; // Safe: all cases covered, no default needed
}
?>
```

### 3. Handle new enum cases gracefully

```php
<?php
enum Priority: int {
    case Low = 1;
    case Medium = 2;
    case High = 3;
}

function sortPriority(Priority $p): int {
    return match ($p) {
        Priority::Low => 1,
        Priority::Medium => 2,
        Priority::High => 3,
        // Adding default prevents errors when new cases are added
        default => 0,
    };
}
?>
```

### 4. Use enum method instead of match

```php
<?php
enum Status {
    case Active;
    case Inactive;
    case Pending;

    public function label(): string {
        return match ($this) {
            self::Active => 'Active',
            self::Inactive => 'Inactive',
            self::Pending => 'Pending',
        };
    }
}
?>
```

## Related Errors

- [PHP Match error]({{< relref "/languages/php/php-match-error-v2" >}})
- [PHP Parse error]({{< relref "/languages/php/parse-error" >}})
- [PHP Notice: Undefined Index]({{< relref "/languages/php/notice-undefined-index" >}})
