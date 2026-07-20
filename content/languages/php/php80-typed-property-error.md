---
title: "[Solution] PHP 8.0 Typed Property Error — Typed Property Accessed Before Initialization"
description: "Fix PHP 8.0 Typed Property Error by initializing in constructor, using nullable types, and checking initialization. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 319
---

# PHP 8.0 Typed Property Error — Typed Property Accessed Before Initialization

A Typed Property Error occurs when a typed property is accessed before it has been initialized. PHP 7.4 introduced typed properties, and PHP 8.0 refined the behavior. Accessing a typed property that hasn't been assigned a value throws a `TypeError: Typed property X::$y must not be accessed before initialization`.

## Common Causes

```php
<?php
// Cause 1: Accessing property without initializing
class User {
    public string $name; // Type declared, no default value
}

$user = new User();
echo $user->name; // TypeError — not initialized

// Cause 2: Missing constructor initialization
class Product {
    public float $price;
    public string $sku;

    public function __construct(string $name) {
        $this->name = $name; // Bug — $name is not a property
        // $this->price and $this->sku never initialized
    }
}

// Cause 3: Uninitialized property in conditional
class Config {
    public string $host;

    public function getHost(): string {
        if ($this->host !== 'localhost') { // TypeError
            return $this->host;
        }
        return 'localhost';
    }
}

// Cause 4: Property set only in some code paths
class Order {
    public string $trackingNumber;

    public function __construct(bool $shipped) {
        if ($shipped) {
            $this->trackingNumber = 'TRACK123';
        }
        // If !$shipped, trackingNumber is uninitialized
    }
}

// Cause 5: Accessing after clone (shallow copy of uninitialized)
class Entity {
    public int $id;
}
$entity = new Entity();
$entity->id = 1;
$clone = clone $entity; // OK if $entity->id was set
?>
```

## How to Fix

### Fix 1: Initialize all typed properties in the constructor

```php
<?php
class User {
    public function __construct(
        public string $name,
        public int $age,
        public string $email,
    ) {}
}

$user = new User('Alice', 25, 'alice@example.com');
echo $user->name; // OK — initialized via constructor promotion
?>
```

### Fix 2: Use nullable types when null is valid

```php
<?php
class User {
    public function __construct(
        public string $name,
        public ?string $nickname = null, // Nullable — null is valid initial state
        public ?Address $address = null,
    ) {}
}

$user = new User('Alice');
echo $user->nickname ?? 'No nickname'; // OK
?>
```

### Fix 3: Provide default values

```php
<?php
class Config {
    public string $host = 'localhost';
    public int $port = 3306;
    public bool $ssl = true;
    public int $timeout = 30;
}

$config = new Config();
echo $config->host; // OK — default value
?>
```

### Fix 4: Guard access with isSet or null checks

```php
<?php
class UserProfile {
    public string $bio;

    public function getBioOrFallback(): string {
        // Use reflection or a flag to check initialization
        if (!isset($this->bio)) {
            return 'No bio provided';
        }
        return $this->bio;
    }
}

// Or use property hooks (PHP 8.4+)
class ModernProfile {
    public string $bio {
        get { return $this->_bio ?? 'No bio provided'; }
        set { $this->_bio = $value; }
    }
    private ?string $_bio = null;
}
?>
```

## Examples

```php
<?php
// Proper initialization patterns
class Order {
    public function __construct(
        public string $id,
        public float $total,
        public string $status,
        public ?string $trackingNumber = null,
        public DateTimeImmutable $createdAt,
    ) {
        // Additional initialization if needed
    }

    public static function create(string $id, float $total): self {
        return new self(
            id: $id,
            total: $total,
            status: 'pending',
            createdAt: new DateTimeImmutable(),
        );
    }
}

$order = Order::create('ORD-001', 99.99);
echo $order->status;        // pending
echo $order->trackingNumber; // null (safe — nullable type)
echo $order->createdAt->format('Y-m-d'); // 2024-01-01

// Using readonly + typed properties (PHP 8.1+)
class Point {
    public function __construct(
        public readonly float $x,
        public readonly float $y,
    ) {}
}
?>
```

## Related Errors

- [PHP 8.1 Readonly Property Error](/languages/php/php81-readonly-properties/) — Readonly properties
- [PHP 8.0 Union Type Error](/languages/php/php80-union-type-error/) — Union types in properties
- [PHP 8.0 Null Safe Operator Error](/languages/php/php80-null-safe-operator/) — Null handling
