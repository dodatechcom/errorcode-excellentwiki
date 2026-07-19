---
title: "[Solution] PHP Readonly Property Modification Error Fix"
description: "Fix 'Cannot modify readonly property' errors in PHP 8.1+. Learn proper readonly initialization and immutability patterns."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "php81", "readonly-properties", "immutability", "runtime-error"]
severity: "error"
---

# Cannot Modify Readonly Property

## Error Message

```
Uncaught Error: Cannot modify readonly property User::$id in /path/to/file.php:22
```

## Common Causes

- Attempting to reassign a readonly property after it has been initialized in the constructor
- Using a readonly property as a return value and then trying to modify it from a method
- Cloning or unserializing an object with readonly properties without proper __clone implementation
- Trying to modify a readonly property from outside the class scope

## Solutions

### Solution 1: Initialize readonly properties only in the constructor or declaration

Readonly properties can only be set once — ensure the constructor assigns all values.

```php
<?php
class User {
    public function __construct(
        public readonly int $id,
        public readonly string $name,
        public readonly string $email,
    ) {}
}

$user = new User(1, 'Alice', 'alice@example.com');
echo $user->name; // 'Alice'

// WRONG: This will throw an error
// $user->name = 'Bob';
?>
```

### Solution 2: Use private setters with initialization logic

When you need conditional initialization, use a private property alongside the readonly one.

```php
<?php
class Config {
    private readonly string $cachedPath;

    public function __construct(
        public readonly string $environment,
        string $cacheDir = '/tmp/cache',
    ) {
        $this->cachedPath = $cacheDir . '/' . $this->environment . '.json';
    }

    public function getCachedPath(): string {
        return $this->cachedPath;
    }
}

$config = new Config('production');
echo $config->getCachedPath(); // '/tmp/cache/production.json'
// $config->environment = 'dev'; // Error: readonly
?>
```

### Solution 3: Implement __clone for readonly properties that need copying

When cloning objects with readonly properties, you must provide a __clone method if modification is needed.

```php
<?php
class Entity {
    public function __construct(
        public readonly int $id,
        public string $label,
    ) {}

    public function __clone(): void {
        // readonly $id is automatically copied during clone — no issue
        // Only non-readonly properties need manual handling
    }
}

$original = new Entity(1, 'First');
$copy = clone $original;
$copy->label = 'Updated'; // Allowed: $label is not readonly
// $copy->id = 2; // Error: readonly

echo $copy->label; // 'Updated'
echo $copy->id;    // 1 (unchanged)
?>
```

## Prevention Tips

- Readonly properties can only be initialized once — either at declaration or in the constructor
- Use readonly promoted properties (PHP 8.1+) for clean, immutable value objects
- readonly properties are not compatible with __clone unless the clone is in the same scope
- Combine readonly with union types for flexible yet immutable design patterns

## Related Errors

- [PHP Readonly Class Error]({{< relref "/languages/php/php82-readonly-class" >}})
- [PHP Deep Readonly Error]({{< relref "/languages/php/php83-readonly-deep" >}})
- [PHP Typed Property Error]({{< relref "/languages/php/php80-typed-property-error" >}})
