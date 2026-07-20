---
title: "[Solution] PHP 8.2 Readonly Class Error — Invalid Readonly Class Usage"
description: "Fix PHP 8.2 Readonly Class Error by defining readonly classes correctly, understanding limitations, and using appropriately. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 311
---

# PHP 8.2 Readonly Class Error — Invalid Readonly Class Usage

A Readonly Class Error occurs when a `readonly` class is defined incorrectly or violates readonly class constraints. PHP 8.2 introduced `readonly` classes — a shorthand that makes all declared properties implicitly `readonly`. This eliminates the need to add `readonly` to each individual property.

## Common Causes

```php
<?php
// Cause 1: Readonly class with non-promoted properties
readonly class User {
    public string $name; // Error — readonly class properties must be promoted
    public int $age;

    public function __construct(string $name, int $age) {
        $this->name = $name; // Won't work as expected
        $this->age = $age;
    }
}

// Cause 2: Readonly class extending another class
readonly class Child extends ParentClass { // Error — readonly classes cannot extend non-readonly classes
}

// Cause 3: Non-readonly class extending readonly class
class Mutable extends ReadOnlyClass { // Error — non-readonly cannot extend readonly
}

// Cause 4: Readonly class with dynamic properties
readonly class Config {
    public function __construct(
        public string $host,
    ) {}
}

$config = new Config('localhost');
$config->port = 3306; // Error — readonly + dynamic properties not allowed

// Cause 5: Readonly class with static properties
readonly class StaticExample {
    public static int $count = 0; // Error — static properties not allowed
}
?>
```

## How to Fix

### Fix 1: Use constructor promotion for all properties

```php
<?php
readonly class User {
    public function __construct(
        public string $name,
        public int $age,
        public string $email,
    ) {}
}

$user = new User('Alice', 25, 'alice@example.com');
echo $user->name; // Alice
// $user->name = 'Bob'; // Error — readonly
?>
```

### Fix 2: Only extend readonly classes

```php
<?php
readonly class Base {
    public function __construct(
        public string $id,
    ) {}
}

// Correct — readonly extending readonly
readonly class Child extends Base {
    public function __construct(
        string $id,
        public string $name,
    ) {
        parent::__construct($id);
    }
}

// Wrong — non-readonly extending readonly
// class Mutable extends Base { }
?>
```

### Fix 3: Use readonly class for value objects

```php
<?php
readonly class Coordinates {
    public function __construct(
        public float $latitude,
        public float $longitude,
    ) {}

    public function distanceTo(Coordinates $other): float {
        $latDiff = deg2rad($other->latitude - $this->latitude);
        $lonDiff = deg2rad($other->longitude - $this->longitude);

        $a = sin($latDiff / 2) ** 2
            + cos(deg2rad($this->latitude))
            * cos(deg2rad($other->latitude))
            * sin($lonDiff / 2) ** 2;

        return 6371000 * 2 * atan2(sqrt($a), sqrt(1 - $a));
    }
}

$origin = new Coordinates(0.0, 0.0);
$dest = new Coordinates(40.7128, -74.0060);
echo $origin->distanceTo($dest) . " meters\n";
?>
```

### Fix 4: Use interface instead of readonly for flexibility

```php
<?php
interface Immutable {
    // Marker interface for immutable objects
}

readonly class StrictUser {
    public function __construct(
        public string $name,
    ) {}
}

class FlexibleUser implements Immutable {
    public function __construct(
        private string $name,
    ) {}

    public function getName(): string { return $this->name; }
    public function setName(string $name): void { $this->name = $name; }
}
?>
```

## Examples

```php
<?php
// Readonly class with enum-like behavior
readonly class Money {
    public function __construct(
        public int $amount,
        public string $currency,
    ) {}

    public function add(Money $other): self {
        if ($this->currency !== $other->currency) {
            throw new InvalidArgumentException('Currency mismatch');
        }
        return new self($this->amount + $other->amount, $this->currency);
    }

    public function __toString(): string {
        return number_format($this->amount / 100, 2) . ' ' . $this->currency;
    }
}

$price = new Money(1999, 'USD');
$tax = new Money(150, 'USD');
$total = $price->add($tax);
echo $total; // 21.49 USD
?>
```

## Related Errors

- [PHP 8.1 Readonly Property Error](/languages/php/php81-readonly-properties/) — Individual readonly properties
- [PHP 8.3 Deep Cloning Readonly Error](/languages/php/php83-readonly-deep-cloning/) — Cloning readonly objects
- [PHP 8.4 Asymmetric Visibility Error](/languages/php/php84-asymmetric-visibility/) — Visibility modifiers with readonly
