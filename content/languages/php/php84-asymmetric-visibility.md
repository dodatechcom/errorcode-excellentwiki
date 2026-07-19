---
title: "[Solution] PHP Asymmetric Visibility Error Fix"
description: "Fix asymmetric visibility errors in PHP 8.4. Learn public-read/private-write property patterns and proper access control."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "php84", "asymmetric-visibility", "access-control", "runtime-error"]
severity: "error"
---

# Asymmetric Visibility Error

## Error Message

```
Fatal error: Asymmetric visibility is not supported for static properties in /path/to/file.php:8
```

## Common Causes

- Using asymmetric visibility on static properties, which is not allowed in PHP 8.4
- Combining asymmetric visibility with readonly properties in an incompatible way
- Trying to use asymmetric visibility in an interface or abstract class with incorrect syntax
- Using public(set) visibility modifier which is not a valid PHP visibility keyword

## Solutions

### Solution 1: Use public-read, private-write for immutable external state

Asymmetric visibility lets consumers read a property while restricting writes to the class itself.

```php
<?php
class User {
    public private(set) string $name;
    public private(set) string $email;
    public private(set) string $createdAt;

    public function __construct(string $name, string $email) {
        $this->name = $name;
        $this->email = $email;
        $this->createdAt = date('Y-m-d H:i:s');
    }

    public function updateEmail(string $newEmail): void {
        $this->email = $newEmail;
    }
}

$user = new User('Alice', 'alice@example.com');
echo $user->email; // 'alice@example.com'
// $user->email = 'bob@example.com'; // Error: cannot set
$user->updateEmail('alice@newdomain.com'); // Allowed via method
echo $user->email; // 'alice@newdomain.com'
?>
```

### Solution 2: Use protected-read, private-write for framework entities

In framework contexts, use protected-read to allow subclass access while keeping writes private.

```php
<?php
abstract class Entity {
    protected private(set) int $id;
    protected private(set) string $createdAt;

    public function __construct() {
        $this->createdAt = date('Y-m-d H:i:s');
    }

    public function getId(): int {
        return $this->id;
    }
}

class User extends Entity {
    public function __construct(
        public private(set) string $name,
    ) {
        parent::__construct();
    }

    // Only the class itself can set the ID (e.g., from ORM)
    public function setId(int $id): void {
        $this->id = $id;
    }
}

$user = new User('Bob');
$user->setId(42);
echo $user->getId(); // 42
echo $user->name;    // 'Bob'
// $user->name = 'X'; // Error: private(set)
?>
```

### Solution 3: Combine asymmetric visibility with constructor promotion

PHP 8.4 allows asymmetric visibility with promoted properties for concise, clean constructors.

```php
<?php
class Product {
    public function __construct(
        public private(set) string $sku,
        public private(set) string $name,
        public private(set) float $price,
        private int $stock = 0,
    ) {}

    public function restock(int $quantity): void {
        if ($quantity < 0) {
            throw new \InvalidArgumentException('Quantity must be positive');
        }
        $this->stock += $quantity;
    }

    public function isAvailable(): bool {
        return $this->stock > 0;
    }
}

$product = new Product('W-001', 'Widget', 9.99);
$product->restock(10);

echo $product->name; // 'Widget' (public read)
// $product->name = 'Other'; // Error: private(set)
echo $product->isAvailable() ? 'In stock' : 'Out of stock'; // 'In stock'
?>
```

## Prevention Tips

- Asymmetric visibility replaces the need for getter methods in many simple cases
- public(private(set)) is the most common pattern — public read, private write
- Asymmetric visibility is not supported on static properties or constants
- Combine with readonly for fully immutable properties that are initialized at construction time

## Related Errors

- [PHP Readonly Property Error]({{< relref "/languages/php/php81-readonly-property" >}})
- [PHP Property Hook Error]({{< relref "/languages/php/php84-property-hook" >}})
- [PHP Typed Property Error]({{< relref "/languages/php/php80-typed-property-error" >}})
