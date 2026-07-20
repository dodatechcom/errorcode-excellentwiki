---
title: "[Solution] PHP 8.4 Nullable Type Error — Invalid Nullable Type Declaration"
description: "Fix PHP 8.4 Nullable Type Error by using correct syntax (?Type), checking type compatibility, and understanding PHP 8.4 requirements. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 318
---

# PHP 8.4 Nullable Type Error — Invalid Nullable Type Declaration

A Nullable Type Error occurs when the nullable type syntax is incorrect, used with incompatible types, or when nullable types conflict with other PHP features like readonly or enums. PHP has supported `?Type` syntax since PHP 7.1, but PHP 8.0+ added union types (`Type|null`) and PHP 8.4 may enforce stricter rules on nullable declarations.

## Common Causes

```php
<?php
// Cause 1: Using ? on compound types (intersection, union)
function handle(?int|string $value) { // Error — can't use ? with union
}

// Cause 2: ?void is not valid
function process(?void $value) { // Error — void is already null-equivalent
}

// Cause 3: Nullable type on readonly with default null
class Config {
    public readonly ?string $host = null; // Valid, but may cause confusion
}

// Cause 4: Using ? on a class that can't be null
class User {
    public ?User $parent; // Valid but requires careful initialization
}

// Cause 5: Conflicting nullable declarations
function store(string|null|null $value) { // Redundant null
}
?>
```

## How to Fix

### Fix 1: Use `?Type` or `Type|null` — not both together

```php
<?php
// These are equivalent in PHP 8.0+
function find(int $id): ?string { // ?Type syntax
    return null; // Returns string or null
}

function findById(int $id): string|null { // Union syntax
    return null;
}

// Wrong — don't combine both
// function bad(?int|string $value) { }
?>
```

### Fix 2: Never use ?void

```php
<?php
// Wrong
// function process(?void $value) { }

// Correct — use Type|null for nullable return
function process(mixed $input): ?int {
    if ($input === null) {
        return null;
    }
    return (int)$input;
}

// Or return null explicitly
function doWork(): ?string {
    $result = performAction();
    return $result !== false ? $result : null;
}
?>
```

### Fix 3: Handle nullable initialization properly

```php
<?php
class User {
    private ?string $nickname;

    public function __construct(?string $nickname = null) {
        $this->nickname = $nickname;
    }

    public function getDisplayName(): string {
        // Always check before using nullable
        return $this->nickname ?? $this->getDefaultName();
    }

    private function getDefaultName(): string {
        return 'Anonymous';
    }
}

$user1 = new User();        // nickname = null
$user2 = new User('Alice'); // nickname = 'Alice'
echo $user1->getDisplayName(); // Anonymous
echo $user2->getDisplayName(); // Alice
?>
```

### Fix 4: Use union types for multiple non-null types

```php
<?php
// For multiple types including null, use union
function process(int|string|null $value): int|string|null {
    return $value;
}

// Or use nullable with single type
function findById(int $id): ?array {
    return findInDatabase($id) ?: null;
}
?>
```

## Examples

```php
<?php
// Nullable types in class hierarchy
class BaseRepository {
    protected function find(int $id): ?array {
        return $this->db->select('WHERE id = ?', [$id]);
    }
}

class UserRepository extends BaseRepository {
    public function findUser(int $id): ?User {
        $data = parent::find($id);
        return $data !== null ? new User($data) : null;
    }
}

// Nullable with type coercion
function normalize(mixed $value): string {
    return match(true) {
        is_string($value)  => $value,
        is_int($value)     => (string)$value,
        is_float($value)   => number_format($value, 2),
        $value === null    => '',
        default            => throw new TypeError('Unsupported type'),
    };
}

// Nullable in PHPDoc for backward compatibility
/**
 * @param int|string|null $id
 * @return User|null
 */
function findUser($id) {
    if ($id === null) {
        return null;
    }
    return User::find($id);
}
?>
```

## Related Errors

- [PHP 8.0 Union Type Error](/languages/php/php80-union-type-error/) — Union type vs nullable
- [PHP 8.0 Union Type Declaration Error](/languages/php/php80-union-type-declaration/) — Union type syntax
- [PHP 8.4 Asymmetric Visibility Error](/languages/php/php84-asymmetric-visibility/) — Visibility with types
