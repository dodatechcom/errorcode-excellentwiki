---
title: "[Solution] PHP UnhandledMatchError — Match Expression Failed"
description: "Fix PHP UnhandledMatchError by adding default cases, covering all possible values, and using enum matching."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 61
---

# UnhandledMatchError — Match Expression Failed

UnhandledMatchError is thrown when a `match` expression has no matching case and no default (`default:`) branch. Introduced in PHP 8.0, this ensures exhaustive matching is enforced at runtime.

## Common Causes

```php
<?php
// Cause 1: Missing default case
$value = 3;
$result = match($value) {
    1 => 'one',
    2 => 'two',
}; // UnhandledMatchError: no match for 3

// Cause 2: Enum not covering all cases
enum Color { case Red; case Green; case Blue; }
$color = Color::Blue;
$result = match($color) {
    Color::Red => 'Red',
    Color::Green => 'Green',
}; // UnhandledMatchError

// Cause 3: String match with unexpected value
$status = 'pending';
$result = match($status) {
    'active' => 'Active',
    'inactive' => 'Inactive',
}; // UnhandledMatchError

// Cause 4: Mixed type match without exhaustive cases
$multi = 42;
$result = match($multi) {
    0 => 'zero',
    1 => 'one',
    '1' => 'one string',
}; // UnhandledMatchError: 42 not matched
?>
```

## How to Fix

### Fix 1: Add a default case

```php
<?php
$value = 3;
$result = match($value) {
    1 => 'one',
    2 => 'two',
    default => 'unknown',
};

echo $result; // "unknown"
?>
```

### Fix 2: Cover all possible enum values

```php
<?php
enum Color { case Red; case Green; case Blue; }

$color = Color::Blue;
$result = match($color) {
    Color::Red => 'Red',
    Color::Green => 'Green',
    Color::Blue => 'Blue',
};

echo $result; // "Blue"

// Or use a default for future-proofing
$result = match($color) {
    Color::Red => 'Red',
    Color::Green => 'Green',
    default => 'Other',
};
?>
```

### Fix 3: Use wildcard with default

```php
<?php
function classify(int $value): string {
    return match (true) {
        $value < 0 => 'negative',
        $value === 0 => 'zero',
        $value > 0 => 'positive',
        default => 'impossible',
    };
}

// Or simpler pattern
function describe(string $status): string {
    return match ($status) {
        'active' => 'Currently active',
        'inactive' => 'Currently inactive',
        'pending' => 'Awaiting activation',
        default => "Unknown status: $status",
    };
}
?>
```

## Examples

```php
<?php
// Exhaustive enum matching with sealed classes
enum PaymentMethod: string {
    case CreditCard = 'credit_card';
    case PayPal = 'paypal';
    case BankTransfer = 'bank_transfer';
}

function getProcessingTime(PaymentMethod $method): string {
    return match ($method) {
        PaymentMethod::CreditCard => 'Instant',
        PaymentMethod::PayPal => '1-2 days',
        PaymentMethod::BankTransfer => '3-5 days',
        // No default needed — PHP enforces exhaustiveness for pure enums
    };
}

// Using match with complex conditions
function getDiscount(string $tier, int $years): int {
    return match (true) {
        $tier === 'premium' && $years >= 5 => 20,
        $tier === 'premium' => 15,
        $tier === 'standard' && $years >= 3 => 10,
        $tier === 'standard' => 5,
        default => 0,
    };
}
?>
```

## Related Errors

- [PHP ValueError]({{< relref "/languages/php/valueerror" >}}) — invalid value
- [PHP TypeError]({{< relref "/languages/php/typeerror" >}}) — type mismatch
- [PHP Fatal Error]({{< relref "/languages/php/fatal-error" >}}) — fatal error
