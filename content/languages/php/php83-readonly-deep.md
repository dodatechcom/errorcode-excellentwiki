---
title: "[Solution] PHP Deep Readonly Property Modification Error Fix"
description: "Fix 'Cannot modify readonly property' deep copy errors in PHP 8.3+. Understand nested readonly semantics and deep cloning."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "php83", "readonly-properties", "deep-clone", "immutability"]
severity: "error"
---

# Cannot Modify Readonly Property (Deep Readonly)

## Error Message

```
Uncaught Error: Cannot modify readonly property OrderItem::$product->name in /path/to/file.php:25
```

## Common Causes

- Attempting to modify a property of an object that is itself a readonly property
- Deep cloning readonly objects without implementing __clone recursively
- Trying to mutate nested readonly objects retrieved from a readonly parent property
- Using readonly properties that hold references to other objects with mutable sub-properties

## Solutions

### Solution 1: Use value objects with static factory methods for deep updates

When a readonly property holds an object, create a new object with the desired changes instead of mutating.

```php
<?php
readonly class Address {
    public function __construct(
        public string $street,
        public string $city,
        public string $zipCode,
    ) {}
}

readonly class Customer {
    public function __construct(
        public string $name,
        public Address $address,
    ) {}

    public function withCity(string $newCity): self {
        return new self(
            $this->name,
            new Address(
                $this->address->street,
                $newCity,
                $this->address->zipCode,
            ),
        );
    }
}

$customer = new Customer(
    'Alice',
    new Address('123 Main St', 'Portland', '97201'),
);

$updated = $customer->withCity('Seattle');
echo $updated->address->city; // 'Seattle'
echo $customer->address->city; // 'Portland' (unchanged)
?>
```

### Solution 2: Implement __clone for deep readonly object copying

When using clone on objects with readonly properties that hold mutable references, handle the deep copy in __clone.

```php
<?php
class Settings {
    public function __construct(
        public readonly string $theme,
        public readonly array $options,
    ) {}
}

readonly class Profile {
    public function __construct(
        public string $name,
        public Settings $settings,
    ) {}

    public function __clone(): void {
        // Clone the nested Settings object so modifications don't affect original
        $this->settings = clone $this->settings;
    }
}

$original = new Profile('Alice', new Settings('dark', ['notifications' => true]));
$copy = clone $original;

// $copy->settings is a deep clone — modifying it won't affect $original
echo $copy->name; // 'Alice'
?>
```

### Solution 3: Redesign with shallow readonly and mutable containers

When deep mutation is needed, keep the container mutable and only make leaf properties readonly.

```php
<?php
class OrderItem {
    public string $name;
    public int $quantity;

    public function __construct(string $name, int $quantity) {
        $this->name = $name;
        $this->quantity = $quantity;
    }
}

class Order {
    /** @var OrderItem[] */
    private array $items = [];

    public function addItem(string $name, int $quantity): void {
        $this->items[] = new OrderItem($name, $quantity);
    }

    public function updateQuantity(int $index, int $newQty): void {
        if (isset($this->items[$index])) {
            $this->items[$index]->quantity = $newQty;
        }
    }

    public function getItems(): array {
        return $this->items;
    }
}

$order = new Order();
$order->addItem('Widget', 2);
$order->updateQuantity(0, 5);
echo $order->getItems()[0]->quantity; // 5
?>
```

## Prevention Tips

- PHP 8.2+ readonly objects cannot be cloned and modified — treat them as truly immutable
- Use the with*() pattern (e.g., withName(), withCity()) to create modified copies of readonly objects
- Avoid storing mutable objects inside readonly properties unless you never need to change them
- Run PHPStan at level 8+ to detect deep readonly modification attempts at analysis time

## Related Errors

- [PHP Readonly Property Error]({{< relref "/languages/php/php81-readonly-property" >}})
- [PHP Readonly Class Error]({{< relref "/languages/php/php82-readonly-class" >}})
- [PHP Deep Readonly Error]({{< relref "/languages/php/php83-readonly-deep" >}})
