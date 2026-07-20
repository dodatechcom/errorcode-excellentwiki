---
title: "[Solution] PHP 8.4 Asymmetric Visibility Error — Invalid Visibility Modifier Combination"
description: "Fix PHP 8.4 Asymmetric Visibility Error by using correct syntax (public private(set)), checking access levels, and understanding PHP 8.4 requirements. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 315
---

# PHP 8.4 Asymmetric Visibility Error — Invalid Visibility Modifier Combination

An Asymmetric Visibility Error occurs when property visibility modifiers are combined incorrectly. PHP 8.4 introduced asymmetric visibility, allowing you to set different visibility levels for reading and writing a property — e.g., publicly readable but privately writable using the `public private(set)` syntax.

## Common Causes

```php
<?php
// Cause 1: Wrong syntax — missing "set" keyword
class User {
    public private string $name; // Error — invalid syntax
}

// Cause 2: Set visibility is more permissive than read visibility
class Config {
    private(set) public string $host; // Error — set can't be more visible than get
}

// Cause 3: Using asymmetric visibility with readonly
class User2 {
    public private(set) readonly string $name; // Error — readonly is already write-restricted
}

// Cause 4: Invalid visibility keywords
class Item {
    public protected(set) string $name; // Error — "protected(set)" not valid in some contexts
}

// Cause 5: Asymmetric visibility on static properties
class Counter {
    public private(set) static int $count = 0; // Error — not supported on static
}
?>
```

## How to Fix

### Fix 1: Use correct "visibility visibility(set)" syntax

```php
<?php
class User {
    public private(set) string $name;
    public private(set) int $age;
    protected private(set) string $email;

    public function __construct(string $name, int $age, string $email) {
        $this->name = $name;
        $this->age = $age;
        $this->email = $email;
    }

    // Public can read, only this class can write
}

$user = new User('Alice', 25, 'alice@example.com');
echo $user->name; // OK — public read
// $user->name = 'Bob'; // Error — private(set)
?>
```

### Fix 2: Ensure set visibility is same or more restrictive

```php
<?php
class Article {
    // Valid combinations
    public private(set) string $title;        // public read, private write
    public protected(set) string $slug;       // public read, protected write
    public protected(set) string $author;     // public read, protected write
    protected private(set) string $secret;    // protected read, private write

    // Invalid
    // private public(set) string $bad;       // private read, public write — ERROR
}

class BlogPost extends Article {
    public function updateSlug(string $newSlug): void {
        $this->slug = $newSlug; // OK — protected(set) allows child class
    }
}
?>
```

### Fix 3: Don't combine with readonly (use one or the other)

```php
<?php
// Option A: Use readonly for immutable properties
class ImmutableUser {
    public function __construct(
        public readonly string $name,
        public readonly int $age,
    ) {}
}

// Option B: Use asymmetric visibility for public-read, private-write
class MutableUser {
    public private(set) string $name;
    public private(set) int $age;

    public function __construct(string $name, int $age) {
        $this->name = $name;
        $this->age = $age;
    }

    public function updateName(string $name): void {
        $this->name = $name;
    }
}
?>
```

### Fix 4: Use PHPDoc for backward compatibility

```php
<?php
/**
 * @property-read string $name
 */
class UserBC {
    private string $name;

    public function __construct(string $name) {
        $this->name = $name;
    }

    public function getName(): string {
        return $this->name;
    }
}

$user = new UserBC('Alice');
echo $user->getName();
?>
```

## Examples

```php
<?php
class Product {
    public private(set) string $id;
    public private(set) string $name;
    public protected(set) float $price;
    public private(set) int $stock;

    public function __construct(string $name, float $price, int $stock) {
        $this->id = uniqid('prod_');
        $this->name = $name;
        $this->price = $price;
        $this->stock = $stock;
    }

    public function reduceStock(int $amount): void {
        if ($amount > $this->stock) {
            throw new InvalidArgumentException('Insufficient stock');
        }
        $this->stock -= $amount;
    }

    public function updatePrice(float $newPrice): void {
        if ($newPrice < 0) {
            throw new InvalidArgumentException('Price cannot be negative');
        }
        $this->price = $newPrice;
    }
}

$product = new Product('Widget', 9.99, 100);
echo $product->name;     // Widget (public read)
echo $product->price;    // 9.99 (public read)
// $product->price = 5.0; // Error — protected(set)

$product->updatePrice(7.99); // OK — via method
$product->reduceStock(10);   // OK — via method

class AdminProduct extends Product {
    public function adminUpdatePrice(float $newPrice): void {
        $this->price = $newPrice; // OK — protected(set) allows child access
    }
}
?>
```

## Related Errors

- [PHP 8.1 Readonly Property Error](/languages/php/php81-readonly-properties/) — Readonly as alternative to private(set)
- [PHP 8.2 Readonly Class Error](/languages/php/php82-readonly-classes/) — Full readonly classes
- [PHP 8.4 Property Hook Error](/languages/php/php84-property-hooks/) — Property hooks with visibility
