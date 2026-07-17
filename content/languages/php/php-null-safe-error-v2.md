---
title: "[Solution] PHP Null Safe Operator: On Null Error Fix"
description: "Fix PHP null safe operator errors. Learn how the ?-> operator works and when it returns null."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Null Safe Operator: On Null Error Fix

A PHP null safe error occurs when the null safe operator (`?->`) is used incorrectly or when a method call on null still triggers side effects.

## What This Error Means

PHP 8.0 introduced the null safe operator (`?->`), which chains method calls that return null early. If the left side is null, the entire chain returns null without calling subsequent methods. Errors occur when developers misunderstand this behavior or use it in contexts where null is unexpected.

## Common Causes

- Chaining methods on a null object without null safe operator
- Using null safe operator but not handling null return
- Misunderstanding that null safe stops at the first null
- Using null safe with functions that have side effects

## How to Fix

### 1. Use null safe operator for optional chaining

```php
<?php
class Address {
    public ?City $city = null;
}

class City {
    public string $name = "Unknown";
}

$address = new Address();

// WRONG: Without null safe — throws Error
// echo $address->city->name;

// CORRECT: Use null safe operator
echo $address?->city?->name ?? 'No city';
?>
```

### 2. Handle null return from null safe chain

```php
<?php
class User {
    public ?Address $address = null;
}

function getCityName(?User $user): string {
    // null safe returns null if any link is null
    $city = $user?->address?->city?->name;

    // CORRECT: Handle null result
    return $city ?? 'Unknown city';
}
?>
```

### 3. Don't use null safe with side effects

```php
<?php
// WRONG: Side effects may not execute if null
// $user?->logAccess(); // Skipped if $user is null

// CORRECT: Be explicit about side effects
if ($user !== null) {
    $user->logAccess();
}
?>
```

### 4. Combine with null coalescing for defaults

```php
<?php
class Order {
    public ?string $discountCode = null;
}

function getDiscount(?Order $order): string {
    return $order?->discountCode ?? 'NONE';
}

$order = new Order();
echo getDiscount($order); // "NONE"

$order->discountCode = 'SAVE20';
echo getDiscount($order); // "SAVE20"
?>
```

## Related Errors

- [PHP Notice: Undefined Index]({{< relref "/languages/php/notice-undefined-index" >}})
- [PHP Fatal Error]({{< relref "/languages/php/fatal-out-of-memory" >}})
- [PHP Parse error]({{< relref "/languages/php/parse-error" >}})
