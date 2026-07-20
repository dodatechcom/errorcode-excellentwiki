---
title: "[Solution] PHP 8.0 Union Type Error — Type Declaration Doesn't Accept Union Types"
description: "Fix PHP 8.0 Union Type Error by updating type declarations to use proper union syntax. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 301
---

# PHP 8.0 Union Type Error — Type Declaration Doesn't Accept Union Types

A Union Type Error occurs when a type declaration doesn't accept union types or the syntax is incorrect. PHP 8.0 introduced union types (e.g., `int|string`) allowing parameters, return types, and properties to accept multiple types. Before PHP 8.0, you had to use PHPDoc annotations instead.

## Common Causes

```php
<?php
// Cause 1: Using pre-PHP 8.0 syntax for multiple types
function process(int string $value) { // Fatal error — invalid syntax
    return $value;
}

// Cause 2: Union type with incompatible types (e.g., class and scalar together improperly)
function setData(array|int|string $value) { // Valid in PHP 8.0, but usage may cause issues
    return $value;
}

// Cause 3: Mismatched union type in child class
class Base {
    public int|string $id;
}
class Child extends Base {
    public int|float $id; // Error — cannot change type in child
}

// Cause 4: Returning wrong type from union-typed function
function getId(): int|string {
    return true; // TypeError — bool not in union
}

// Cause 5: Passing wrong type to union-typed parameter
function store(int|string $id): void {
    echo $id;
}
store([]); // TypeError — array not accepted
?>
```

## How to Fix

### Fix 1: Update function signatures to use proper union syntax

```php
<?php
// Before: PHPDoc only (no runtime enforcement)
/**
 * @param int|string $id
 */
function process($id) {
    return $id;
}

// After: Proper union type in PHP 8.0+
function process(int|string $id): int|string {
    return $id;
}
?>
```

### Fix 2: Use matching types in child classes

```php
<?php
class Base {
    public int|string $id;
}

class Child extends Base {
    // Correct — must include all types from parent
    public int|string $id;

    // Or remove the type declaration entirely if flexible typing is needed
}
?>
```

### Fix 3: Validate input before passing to union-typed functions

```php
<?php
function store(int|string $id): void {
    echo $id;
}

function processInput(mixed $input): void {
    if (is_int($input) || is_string($input)) {
        store($input);
    } else {
        throw new InvalidArgumentException(
            'Expected int or string, got ' . get_debug_type($input)
        );
    }
}

processInput(42);       // OK
processInput("abc");    // OK
processInput([]);       // InvalidArgumentException
?>
```

### Fix 4: Use proper return type checking

```php
<?php
function getId(): int|string {
    $value = someExternalCall();

    if (is_int($value) || is_string($value)) {
        return $value;
    }

    // Fallback to a valid type
    return 0;
}
?>
```

## Examples

```php
<?php
// Union types with classes
class User {
    public function __construct(
        private int|string $identifier,
        private string|null $nickname,
    ) {}

    public function getIdentifier(): int|string {
        return $this->identifier;
    }

    public function getNickname(): string|null {
        return $this->nickname ?? 'Anonymous';
    }
}

$user1 = new User(1, null);
$user2 = new User('abc123', 'Bob');

echo $user1->getIdentifier(); // 1
echo $user2->getNickname();   // Bob

// Union types with enum (PHP 8.1+)
// function setStatus(Status|BackupStatus $status): void { ... }
?>
```

## Related Errors

- [PHP 8.0 Union Type Declaration Error](/languages/php/php80-union-type-declaration/) — Union type syntax errors
- [PHP 8.1 Intersection Type Error](/languages/php/php81-intersection-types/) — Using `&` instead of `|`
- [PHP 8.0 Typed Property Error](/languages/php/php80-typed-property-error/) — Typed property initialization issues
