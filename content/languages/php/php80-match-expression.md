---
title: "[Solution] PHP Unhandled Match Value Error Fix"
description: "Fix 'Unhandled match value' errors in PHP 8.0+. Learn exhaustive matching and default arms in match expressions."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "php80", "match-expression", "exhaustiveness", "runtime-error"]
severity: "error"
---

# Unhandled Match Value

## Error Message

```
Uncaught ValueError: Unhandled match value of type string in /path/to/file.php:10
```

## Common Causes

- The match expression does not cover all possible input values and has no default arm
- Passing an unexpected type to a match expression that only handles specific enum cases
- Refactoring code that uses switch without default to match without adding a default arm
- Using match with a typed enum but forgetting a case for one of its values

## Solutions

### Solution 1: Add a default arm to the match expression

Include a default arm (using the underscore syntax) to catch any unhandled values gracefully.

```php
<?php
$status = getOrderStatus($orderId);

$result = match($status) {
    'pending'   => 'Order is pending',
    'shipped'   => 'Order has shipped',
    'delivered' => 'Order delivered',
    default     => 'Unknown status: ' . $status,
};

echo $result;
?>
```

### Solution 2: Cover all possible values explicitly

When working with enums or known value sets, list every possible case so no value slips through.

```php
<?php
enum Color {
    case Red;
    case Green;
    case Blue;
}

function colorHex(Color $c): string {
    return match($c) {
        Color::Red   => '#FF0000',
        Color::Green => '#00FF00',
        Color::Blue  => '#0000FF',
    }; // Safe: all cases covered, no default needed
}

echo colorHex(Color::Red); // '#FF0000'
?>
```

### Solution 3: Use default with a thrown exception for strict validation

When unhandled values indicate a bug, throw an exception in the default arm to fail fast.

```php
<?php
function handlePayment(string $method): string {
    return match($method) {
        'credit_card' => 'Processing credit card',
        'paypal'      => 'Redirecting to PayPal',
        'crypto'      => 'Processing crypto payment',
        default       => throw new InvalidArgumentException(
            "Unsupported payment method: $method"
        ),
    };
}

handlePayment('wire'); // throws InvalidArgumentException
?>
```

## Prevention Tips

- Always add a default arm unless you are 100% certain all values are covered
- Use enums with match for type-safe exhaustive matching in PHP 8.1+
- Match uses strict comparison (===), unlike switch which uses loose comparison — be aware of type differences
- PHPStan can detect non-exhaustive match expressions when using enums

## Related Errors

- [PHP Match Expression Error]({{< relref "/languages/php/php-match-error" >}})
- [PHP Enum Error]({{< relref "/languages/php/php81-enum-error" >}})
- [PHP Fatal Error]({{< relref "/languages/php/fatal-error" >}})
