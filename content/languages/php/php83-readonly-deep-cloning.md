---
title: "[Solution] PHP 8.3 Deep Cloning Readonly Error — Cloning Readonly Objects"
description: "Fix PHP 8.3 Deep Cloning Readonly Error by implementing __clone(), understanding readonly limitations, and using proper cloning. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 314
---

# PHP 8.3 Deep Cloning Readonly Error — Cloning Readonly Objects

The Deep Cloning Readonly Error occurs when attempting to clone objects with `readonly` properties, especially in deep object graphs. PHP 8.3 improved readonly property handling, but cloning readonly properties requires special consideration — you cannot modify readonly properties in `__clone()`, and the default shallow clone may not work as expected for nested objects.

## Common Causes

```php
<?php
// Cause 1: Trying to modify readonly property in __clone()
class User {
    public function __construct(
        public readonly string $name,
        public readonly Address $address,
    ) {}

    public function __clone(): void {
        $this->name = 'Copy'; // Error — readonly property cannot be modified
    }
}

// Cause 2: Shallow clone shares nested object references
class Order {
    public function __construct(
        public readonly string $id,
        public readonly User $user,
    ) {}
}

$order = new Order('1', new User('Alice', new Address('NY')));
$cloned = clone $order;
// $cloned->user is the SAME object as $order->user

// Cause 3: Cloning objects without considering immutability
class ImmutableConfig {
    public function __construct(
        public readonly string $host,
        public readonly int $port,
    ) {}
}

$config = new ImmutableConfig('localhost', 3306);
$copy = clone $config;
// $copy === $config is false, but properties are identical
// You can't modify $copy either

// Cause 4: Deep copy attempt fails with readonly
class Node {
    public function __construct(
        public readonly ?Node $next = null,
    ) {}

    public function withNext(Node $next): self {
        return new self($this->host, $next);
    }
}

// Cause 5: Serialization/deserialization issues with readonly
$serialized = serialize($config);
$unserialized = unserialize($serialized); // May fail in some PHP versions
?>
```

## How to Fix

### Fix 1: Use constructor-based copying instead of cloning

```php
<?php
class User {
    public function __construct(
        public readonly string $name,
        public readonly Address $address,
    ) {}

    public function withName(string $newName): self {
        return new self($newName, clone $this->address);
    }

    public function withAddress(Address $newAddress): self {
        return new self($this->name, $newAddress);
    }
}

$original = new User('Alice', new Address('New York', '10001'));
$copy = $original->withName('Bob');
// Original is unchanged, copy has new name
?>
```

### Fix 2: Implement deep clone via factory method

```php
<?php
class Address {
    public function __construct(
        public readonly string $city,
        public readonly string $zip,
    ) {}

    public function clone(): self {
        return new self($this->city, $this->zip);
    }
}

class User {
    public function __construct(
        public readonly string $name,
        public readonly Address $address,
    ) {}

    public function deepClone(): self {
        return new self($this->name, $this->address->clone());
    }
}

$original = new User('Alice', new Address('NYC', '10001'));
$copy = $original->deepClone();
// $copy->address is a new object, not shared
?>
```

### Fix 3: Use immutable pattern with fluent interface

```php
<?php
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

    public function withAmount(int $amount): self {
        return new self($amount, $this->currency);
    }
}

$price = new Money(1000, 'USD');
$discounted = $price->withAmount(800);
// Both are separate objects
?>
```

### Fix 4: Handle nested readonly objects in arrays

```php
<?php
class UserList {
    public function __construct(
        public readonly array $users, // Array of User objects
    ) {}

    public function deepClone(): self {
        return new self(
            array_map(
                fn(User $u) => new User($u->name, new Address($u->address->city, $u->address->zip)),
                $this->users
            )
        );
    }
}

$list = new UserList([
    new User('Alice', new Address('NYC', '10001')),
    new User('Bob', new Address('LA', '90001')),
]);

$copy = $list->deepClone();
// All nested objects are properly cloned
?>
```

## Examples

```php
<?php
// Practical deep clone pattern
class TreeNode {
    public function __construct(
        public readonly string $value,
        public readonly array $children = [],
    ) {}

    public function clone(): self {
        return new self(
            $this->value,
            array_map(
                fn(TreeNode $child) => $child->clone(),
                $this->children
            )
        );
    }

    public function withValue(string $newValue): self {
        return new self($newValue, $this->children);
    }
}

$tree = new TreeNode('root', [
    new TreeNode('child1', [
        new TreeNode('grandchild1'),
        new TreeNode('grandchild2'),
    ]),
    new TreeNode('child2'),
]);

$copy = $tree->clone();
$modified = $copy->withValue('new-root');
echo $tree->value;      // root (unchanged)
echo $modified->value;  // new-root
?>
```

## Related Errors

- [PHP 8.1 Readonly Property Error](/languages/php/php81-readonly-properties/) — Readonly property basics
- [PHP 8.2 Readonly Class Error](/languages/php/php82-readonly-classes/) — Readonly classes
- [PHP 8.4 Property Hook Error](/languages/php/php84-property-hooks/) — Property hooks
