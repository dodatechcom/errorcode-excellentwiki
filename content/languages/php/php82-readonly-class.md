---
title: "[Solution] PHP Readonly Class Reassignment Error Fix"
description: "Fix 'Cannot reassign readonly property' errors in PHP 8.2 readonly classes. All properties become readonly automatically."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "php82", "readonly-class", "immutability", "runtime-error"]
severity: "error"
---

# Cannot Reassign Readonly Property in Readonly Class

## Error Message

```
Uncaught Error: Cannot reassign readonly property Point::$x in /path/to/file.php:18
```

## Common Causes

- Declaring a class as readonly and then attempting to modify any of its properties after construction
- Using a readonly class in a mutable context like a builder pattern
- Cloning a readonly class and trying to change property values on the clone
- Forgetting that a readonly class makes ALL properties implicitly readonly

## Solutions

### Solution 1: Design readonly classes as immutable value objects

Readonly classes are meant for data objects that never change after creation — design accordingly.

```php
<?php
readonly class Point {
    public function __construct(
        public float $x,
        public float $y,
        public float $z,
    ) {}

    public function distanceTo(Point $other): float {
        return sqrt(
            ($this->x - $other->x) ** 2 +
            ($this->y - $other->y) ** 2 +
            ($this->z - $other->z) ** 2
        );
    }
}

$origin = new Point(0, 0, 0);
$point = new Point(3, 4, 0);
echo $origin->distanceTo($point); // 5.0
// $point->x = 10; // Error: readonly property
?>
```

### Solution 2: Use static factory methods for alternative constructors

Since readonly classes cannot be mutated, use static factory methods to create variants.

```php
<?php
readonly class Money {
    public function __construct(
        public int $amount,
        public string $currency,
    ) {}

    public static function fromCents(int $cents, string $currency): self {
        return new self($cents, $currency);
    }

    public function withAmount(int $newAmount): self {
        return new self($newAmount, $this->currency);
    }

    public function add(Money $other): self {
        if ($this->currency !== $other->currency) {
            throw new \InvalidArgumentException('Currency mismatch');
        }
        return new self($this->amount + $other->amount, $this->currency);
    }
}

$price = Money::fromCents(1500, 'USD');
$tax = new Money(200, 'USD');
$total = $price->add($tax);
echo $total->amount; // 1700
?>
```

### Solution 3: Use a mutable alternative when properties need changing

If your class needs to be modified after creation, use a regular class instead of a readonly class.

```php
<?php
// Regular class when mutability is needed
class ShoppingCart {
    private array $items = [];

    public function addItem(string $name, int $quantity): void {
        $this->items[$name] = $quantity;
    }

    public function removeItem(string $name): void {
        unset($this->items[$name]);
    }

    public function getItems(): array {
        return $this->items;
    }
}

$cart = new ShoppingCart();
$cart->addItem('Widget', 2);
$cart->addItem('Gadget', 1);
print_r($cart->getItems());
?>
```

## Prevention Tips

- A readonly class makes ALL declared properties implicitly readonly — no need for individual readonly keywords
- Readonly classes cannot have dynamic properties and are automatically non-extensible
- Use readonly classes for DTOs, value objects, and configuration objects that should never change
- Combine readonly classes with constructor promotion for extremely concise immutable definitions

## Related Errors

- [PHP Readonly Property Error]({{< relref "/languages/php/php81-readonly-property" >}})
- [PHP Deep Readonly Error]({{< relref "/languages/php/php83-readonly-deep" >}})
- [PHP Dynamic Property Deprecated Error]({{< relref "/languages/php/php-dynamic-property-error-v2" >}})
