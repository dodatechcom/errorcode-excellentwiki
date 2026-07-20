---
title: "[Solution] PHP 8.1 Readonly Property Error — Modifying Readonly Property"
description: "Fix PHP 8.1 Readonly Property Error by initializing in constructor and not modifying after. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 307
---

# PHP 8.1 Readonly Property Error — Modifying Readonly Property

A Readonly Property Error occurs when you attempt to modify a `readonly` property after it has been initialized, or when you try to use `readonly` on properties that cannot be readonly. PHP 8.1 introduced `readonly` properties that can only be written to during initialization (in the constructor or declaration).

## Common Causes

```php
<?php
// Cause 1: Modifying readonly property after construction
class User {
    public function __construct(
        public readonly string $name,
        public readonly int $age,
    ) {}
}

$user = new User('Alice', 25);
$user->name = 'Bob'; // Error — readonly property

// Cause 2: Readonly on static properties
class Config {
    public static readonly string $version = '1.0'; // Error
}

// Cause 3: Readonly on dynamic/late static properties
class Model {
    public readonly string $table; // Error if not in constructor
}

// Cause 4: Multiple initialization attempts
class Entity {
    public readonly int $id;

    public function __construct() {
        $this->id = 1; // First initialization
    }

    public function reset(): void {
        $this->id = 0; // Error — second write
    }
}

// Cause 5: Readonly with default value and constructor init
class Item {
    public readonly int $count = 5; // Allowed in 8.1+

    public function __construct() {
        $this->count = 10; // Error if default was set? Actually allowed to override
    }
}
?>
```

## How to Fix

### Fix 1: Only initialize readonly properties in the constructor

```php
<?php
class User {
    public readonly string $name;
    public readonly int $age;
    public readonly string $email;

    public function __construct(string $name, int $age, string $email) {
        $this->name = $name;
        $this->age = $age;
        $this->email = $email;
    }

    // Wrong — cannot modify after construction
    // public function rename(string $newName): void {
    //     $this->name = $newName;
    // }
}
?>
```

### Fix 2: Use readonly with constructor promotion (PHP 8.0+)

```php
<?php
class Config {
    public function __construct(
        public readonly string $host = 'localhost',
        public readonly int $port = 3306,
        public readonly bool $ssl = true,
    ) {}
}

$config = new Config(host: 'db.example.com', port: 5432, ssl: false);
echo $config->host; // db.example.com
// $config->host = 'new'; // Error — readonly
?>
```

### Fix 3: For modifiable values, use regular properties

```php
<?php
class ShoppingCart {
    // Readonly — set once during construction
    public readonly string $id;
    public readonly DateTimeImmutable $createdAt;

    // Mutable — can be modified
    private array $items = [];
    private float $total = 0.0;

    public function __construct() {
        $this->id = uniqid('cart_');
        $this->createdAt = new DateTimeImmutable();
    }

    public function addItem(string $item, float $price): void {
        $this->items[] = $item;
        $this->total += $price;
    }
}
?>
```

### Fix 4: Use clones for modified copies instead of mutating

```php
<?php
class Settings {
    public function __construct(
        public readonly string $theme,
        public readonly string $language,
        public readonly int $fontSize,
    ) {}

    public function withTheme(string $newTheme): self {
        return new self(
            theme: $newTheme,
            language: $this->language,
            fontSize: $this->fontSize,
        );
    }
}

$original = new Settings('dark', 'en', 14);
$modified = $original->withTheme('light');
// Both are immutable
?>
```

## Examples

```php
<?php
class UserProfile {
    public function __construct(
        public readonly int $id,
        public readonly string $username,
        private readonly string $passwordHash,
    ) {}

    public function verifyPassword(string $password): bool {
        return password_verify($password, $this->passwordHash);
    }
}

$user = new UserProfile(1, 'alice', password_hash('secret', PASSWORD_DEFAULT));
echo $user->username; // alice
// $user->username = 'bob'; // Error — readonly

// Readonly with lazy initialization pattern
class CachedData {
    private readonly array $data;

    public function __construct(private callable $loader) {}

    public function getData(): array {
        // Note: readonly means we can't lazily init like this
        // Use a different pattern instead
        return ($this->loader)();
    }
}
?>
```

## Related Errors

- [PHP 8.2 Readonly Class Error](/languages/php/php82-readonly-classes/) — Entire classes as readonly
- [PHP 8.3 Deep Cloning Readonly Error](/languages/php/php83-readonly-deep-cloning/) — Cloning readonly objects
- [PHP 8.4 Property Hook Error](/languages/php/php84-property-hooks/) — Property hooks with readonly
