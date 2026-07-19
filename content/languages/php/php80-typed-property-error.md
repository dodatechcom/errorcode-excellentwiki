---
title: "[Solution] PHP Typed Property Initialization Error Fix"
description: "Fix 'Typed property must not be accessed before initialization' errors in PHP 8.0+. Learn proper initialization and null safety."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "php80", "typed-properties", "initialization", "fatal-error"]
severity: "error"
---

# Typed Property Must Not Be Accessed Before Initialization

## Error Message

```
Uncaught Error: Typed property User::$email must not be accessed before initialization
```

## Common Causes

- Accessing a typed property before assigning a value to it in the constructor or declaration
- Declaring a typed property without a default value and then reading it before assignment
- Using a subclass that forgets to call the parent constructor which initializes properties
- Returning an object from a factory method where some properties were never set

## Solutions

### Solution 1: Initialize typed properties with default values

Provide a default value for every typed property so it is never uninitialized when accessed.

```php
<?php
class User {
    public string $name = '';
    public string $email = '';
    public int $age = 0;
}

$user = new User();
echo $user->email; // '' instead of fatal error
?>
```

### Solution 2: Initialize all properties in the constructor

Assign values to all typed properties inside __construct() to guarantee they are set before use.

```php
<?php
class Order {
    public float $total;
    public string $status;

    public function __construct(float $total, string $status) {
        $this->total = $total;
        $this->status = $status;
    }
}

$order = new Order(99.99, 'pending');
echo $order->status; // 'pending'
?>
```

### Solution 3: Use nullable types for optional properties

When a property may legitimately be unset, use a nullable type (?Type) and check for null before use.

```php
<?php
class Product {
    public string $name;
    public ?string $discountCode = null;

    public function __construct(string $name) {
        $this->name = $name;
    }

    public function applyDiscount(): string {
        if ($this->discountCode === null) {
            return 'No discount applied';
        }
        return "Discount code: {$this->discountCode}";
    }
}

$product = new Product('Widget');
echo $product->applyDiscount(); // 'No discount applied'
?>
```

## Prevention Tips

- Always assign every typed property a value before reading it — PHP 8.0 does not allow reading uninitialized typed properties
- Use ?Type (nullable) for properties that may intentionally be unset
- Run PHPStan or Psalm in your CI to catch uninitialized property access at static analysis time
- Consider using constructor promotion (PHP 8.0+) to enforce property initialization at instantiation

## Related Errors

- [PHP Union Type Error]({{< relref "/languages/php/php80-union-type-error" >}})
- [PHP Readonly Property Error]({{< relref "/languages/php/php81-readonly-property" >}})
- [PHP Deprecated Function Usage]({{< relref "/languages/php/php-deprecated" >}})
