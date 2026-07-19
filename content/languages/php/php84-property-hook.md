---
title: "[Solution] PHP Property Hook Error Fix"
description: "Fix property hook errors in PHP 8.4. Learn proper hook syntax, virtual properties, and backed vs non-backed hooks."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "php84", "property-hooks", "syntax-error", "fatal-error"]
severity: "error"
---

# Property Hook Error

## Error Message

```
Fatal error: Uncaught Error: Cannot use non-backed property 'name' in a virtual property context in /path/to/file.php:12
```

## Common Causes

- Using a property hook on a readonly property, which is not supported in PHP 8.4
- Trying to define both get/set hooks and a default value on a non-backed property
- Calling $this->name inside a get hook on a virtual (non-backed) property causing infinite recursion
- Using hooks in an interface or abstract class without proper syntax

## Solutions

### Solution 1: Use backed properties with get/set hooks

A backed property stores its value internally and can have hooks that run before/after access.

```php
<?php
class User {
    public string $name {
        get {
            return $this->name;
        }
        set (string $value) {
            $this->name = ucfirst(strtolower($value));
        }
    }
}

$user = new User();
$user->name = 'alice';
echo $user->name; // 'Alice'
?>
```

### Solution 2: Use virtual properties for computed values

Virtual properties have no backing storage — the get hook computes the value on the fly.

```php
<?php
class Circle {
    public function __construct(
        private float $radius,
    ) {}

    public float $area {
        get {
            return pi() * $this->radius ** 2;
        }
    }

    public float $circumference {
        get {
            return 2 * pi() * $this->radius;
        }
    }
}

$circle = new Circle(5.0);
echo $circle->area;          // 78.5398...
echo $circle->circumference; // 31.4159...
// $circle->area = 10; // Error: virtual property is read-only
?>
```

### Solution 3: Combine hooks with validation logic

Use set hooks to validate, transform, or constrain property values before they are stored.

```php
<?php
class Product {
    private float $discount = 0.0;

    public float $price {
        get {
            return $this->price * (1 - $this->discount);
        }
        set (float $value) {
            if ($value < 0) {
                throw new \InvalidArgumentException('Price cannot be negative');
            }
            $this->price = $value;
        }
    }

    public function setDiscount(float $percent): void {
        if ($percent < 0 || $percent > 100) {
            throw new \InvalidArgumentException('Discount must be 0-100');
        }
        $this->discount = $percent / 100;
    }
}

$product = new Product();
$product->price = 100.0;
$product->setDiscount(20);
echo $product->price; // 80.0
?>
```

## Prevention Tips

- Property hooks are only available in PHP 8.4+ — do not use them in code that must run on older versions
- You cannot combine property hooks with readonly properties
- Virtual properties (no backing storage) cannot have a set hook — they are inherently read-only
- Use hooks instead of __get/__set magic methods for cleaner, type-safe property access control

## Related Errors

- [PHP Readonly Property Error]({{< relref "/languages/php/php81-readonly-property" >}})
- [PHP Asymmetric Visibility Error]({{< relref "/languages/php/php84-asymmetric-visibility" >}})
- [PHP Typed Property Error]({{< relref "/languages/php/php80-typed-property-error" >}})
