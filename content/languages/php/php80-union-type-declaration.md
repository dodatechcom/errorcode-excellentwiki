---
title: "[Solution] PHP 8.0 Union Type Declaration Error — Invalid Union Type Syntax"
description: "Fix PHP 8.0 Union Type Declaration Error by using correct syntax (Type1|Type2), checking PHP version, and updating type hints. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 305
---

# PHP 8.0 Union Type Declaration Error — Invalid Union Type Syntax

A Union Type Declaration Error occurs when the syntax for union types is incorrect or when union types are used on PHP versions that don't support them. PHP 8.0 introduced union types using the `|` separator. Common mistakes include using commas, `|` with incompatible types, or using the syntax on PHP 7.x.

## Common Causes

```php
<?php
// Cause 1: Using comma instead of pipe
function process(int, string $value) { // Parse error
    return $value;
}

// Cause 2: Union type with two classes that share a common descendant
function handle(SplFileInfo|DirectoryIterator $item) { // May cause issues
    return $item->getPathname();
}

// Cause 3: Using union types on PHP 7.x
// function getId(): int|string { } // Fatal error on PHP 7

// Cause 4: Union type with void
function doWork(): void|int { // Error — cannot use void with other types
    return null;
}

// Cause 5: Nullable union type confusion
function find(int|null|false $id): int|null|false { // Valid but verbose
    return $id;
}
?>
```

## How to Fix

### Fix 1: Use pipe `|` separator for union types

```php
<?php
// Wrong — comma separator
// function process(int, string $value) { }

// Correct — pipe separator
function process(int|string $value): int|string {
    return $value;
}

// Also correct for properties
class Model {
    public int|string $id;
    public string|null $name;
}
?>
```

### Fix 2: Replace void + other types with nullable type

```php
<?php
// Wrong — void cannot be in a union
// function doWork(): void|int { }

// Correct — use null instead of void for return types
function doWork(): ?int {
    return null; // Use null to indicate no return value
}

// Or use separate functions
function doWork(): void { /* ... */ }
function getResult(): int { /* ... */ }
?>
```

### Fix 3: Use `?Type` shorthand for Type|null

```php
<?php
// These are equivalent in PHP 8.0+
function find(int|null $id): string|null { /* ... */ }
function find(?int $id): ?string { /* ... */ }

// For class types
function getUser(): User|null { /* ... */ }  // Union syntax
function getUser(): ?User { /* ... */ }       // Short nullable syntax
?>
```

### Fix 4: Check PHP version before using union types

```php
<?php
// Option A: Upgrade PHP to 8.0+
// Option B: Use PHPDoc for backward compatibility
/**
 * @param int|string $id
 * @return int|string|null
 */
function process($id) {
    return $id;
}

// Option C: Use type checking at runtime
function process($id) {
    if (!is_int($id) && !is_string($id)) {
        throw new TypeError('Expected int or string');
    }
    return $id;
}
?>
```

### Fix 5: Handle incompatible class unions with interfaces

```php
<?php
// If two classes are unrelated, create a common interface
interface HasPathname {
    public function getPathname(): string;
}

class MyFile extends SplFileInfo implements HasPathname { /* ... */ }
class MyDir extends SplFileInfo implements HasPathname { /* ... */ }

// Now use the interface type
function process(HasPathname $item): string {
    return $item->getPathname();
}
?>
```

## Examples

```php
<?php
// Full union type examples
class User {
    public function __construct(
        private int|string $id,
        private string|null $email,
        private float|int|false $balance,
    ) {}

    public function getId(): int|string {
        return $this->id;
    }

    public function getBalance(): float|int|false {
        return $this->balance;
    }
}

// Union types in method parameters
class Validator {
    public static function validate(int|string|float $value): bool {
        return match(true) {
            is_int($value)    => $value > 0,
            is_string($value) => strlen($value) > 0,
            is_float($value)  => $value > 0.0,
            default           => false,
        };
    }
}

Validator::validate(42);      // true
Validator::validate('hello'); // true
Validator::validate(3.14);    // true
?>
```

## Related Errors

- [PHP 8.0 Union Type Error](/languages/php/php80-union-type-error/) — Runtime type mismatch with union types
- [PHP 8.1 Intersection Type Error](/languages/php/php81-intersection-types/) — Using `&` for intersection types
- [PHP 8.2 DNF Type Error](/languages/php/php82-disjunctive-normal-form/) — Combining `&` and `|` in types
