---
title: "[Solution] PHP Readonly: Modification Error Fix"
description: "Fix PHP readonly property modification errors. Learn how readonly properties work in PHP 8.1+."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Readonly: Modification Error Fix

A PHP readonly error occurs when you try to modify a readonly property after it has been initialized. Readonly properties can only be written to once.

## What This Error Means

PHP 8.1 introduced readonly properties and PHP 8.2 introduced readonly classes. Once a readonly property is assigned a value in the constructor (or declared inline), any subsequent attempt to modify it throws an `Error`.

## Common Causes

- Trying to reassign a readonly property after construction
- Unsetting a readonly property
- Using clone on an object with readonly properties incorrectly
- Attempting double initialization in constructor

## How to Fix

### 1. Only assign readonly properties once

```php
<?php
class User {
    public function __construct(
        public readonly string $name,
        public readonly string $email,
    ) {}
}

$user = new User('Alice', 'alice@example.com');

// WRONG: Reassigning readonly property
// $user->name = 'Bob'; // Error: cannot modify readonly property

// CORRECT: Create a new instance instead
$newUser = new User('Bob', 'bob@example.com');
?>
```

### 2. Handle readonly in clone scenarios

```php
<?php
class Config {
    public function __construct(
        public readonly string $host,
        public readonly int $port,
    ) {}
}

$config = new Config('localhost', 3306);

// WRONG: Clone + modify readonly
// $newConfig = clone $config;
// $newConfig->port = 5432; // Error

// CORRECT: Use a factory method
function withPort(Config $config, int $port): Config {
    return new Config($config->host, $port);
}
$newConfig = withPort($config, 5432);
?>
```

### 3. Don't double-initialize in constructor

```php
<?php
class Service {
    public readonly string $name;

    public function __construct(string $name) {
        // WRONG: Double assignment
        // $this->name = $name;
        // $this->name = strtoupper($name); // Error

        // CORRECT: Single assignment
        $this->name = strtoupper($name);
    }
}
?>
```

### 4. Use readonly classes carefully

```php
<?php
// PHP 8.2+: readonly class — all properties are readonly
readonly class Point {
    public function __construct(
        public float $x,
        public float $y,
    ) {}
}

$point = new Point(1.0, 2.0);
// $point->x = 3.0; // Error: cannot modify readonly property
?>
```

## Related Errors

- [PHP Parse error]({{< relref "/languages/php/parse-error" >}})
- [PHP Dynamic property error]({{< relref "/languages/php/php-dynamic-property-error-v2" >}})
- [PHP Deprecated function]({{< relref "/languages/php/php-deprecated-error-v2" >}})
