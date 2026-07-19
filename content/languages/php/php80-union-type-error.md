---
title: "[Solution] PHP Union Type Declaration Error Fix"
description: "Fix 'Declaration of X must be compatible with Y' union type errors in PHP 8.0+. Ensure correct override signatures."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "php80", "union-types", "lsp", "declaration-error"]
severity: "error"
---

# Union Type Declaration Error

## Error Message

```
Declaration of ChildClass::process(mixed $input): int|string must be compatible with ParentClass::process(string $input): string|int
```

## Common Causes

- A child class method uses a union return type that is not compatible with the parent class signature
- Overriding a method with a wider or narrower union type than the parent declaration
- Mixing PHP 8.0 union types with older non-union type hints in an inheritance hierarchy
- Third-party libraries compiled against a different PHP version with incompatible union types

## Solutions

### Solution 1: Match the parent class method signature exactly

Ensure child class overrides use the same union types as the parent class declaration.

```php
<?php
class Repository {
    public function find(int $id): string|int {
        return $id > 0 ? "item-$id" : 0;
    }
}

class UserRepository extends Repository {
    // WRONG: return type too narrow
    // public function find(int $id): string { ... }

    // CORRECT: same signature as parent
    public function find(int $id): string|int {
        return $id > 0 ? "user-$id" : 0;
    }
}
?>
```

### Solution 2: Use covariant return types safely

PHP 8.0 allows covariant return types — a child may return a more specific type, but not a wider one.

```php
<?php
class Shape {
    public function describe(): string|array {
        return 'shape';
    }
}

class Circle extends Shape {
    // CORRECT: returning a narrower type (string) is allowed
    public function describe(): string {
        return 'circle';
    }
}
?>
```

### Solution 3: Update the parent class to use union types

If the parent class uses non-union types, modernize it with union types so children can override freely.

```php
<?php
// BEFORE (PHP 7.x style):
class Base {
    public function convert(string|int $value): string {
        return (string) $value;
    }
}

// AFTER (PHP 8.0+ union types):
class Base {
    public function convert(string|int $value): string|float {
        return is_numeric($value) ? (float) $value : 0.0;
    }
}
?>
```

## Prevention Tips

- Always run your test suite after upgrading PHP to catch signature incompatibilities
- Use PHPStan at level 6+ to detect union type mismatches at static analysis time
- Be cautious with vendor libraries — check their PHP version requirements before upgrading
- Document union type contracts clearly in your API documentation

## Related Errors

- [PHP Intersection Type Error]({{< relref "/languages/php/php81-intersection-type" >}})
- [PHP Typed Property Error]({{< relref "/languages/php/php80-typed-property-error" >}})
- [PHP Parse Error]({{< relref "/languages/php/parse-error" >}})
