---
title: "[Solution] PHP 8.1 Return Type Declaration Deprecation"
description: "Fix PHP 8.1 missing return type declaration deprecations. Add void, never, and proper return types to functions."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1102
---

# PHP 8.1 Return Type Declaration Deprecation

PHP 8.1 introduced deprecation notices for internal functions and methods that lack return type declarations. This is part of PHP's ongoing effort to add strict types across the standard library and encourage best practices in user code.

## Common Causes

```php
<?php
// Cause 1: Missing return type on function
function calculateTotal($items) {
    return array_reduce($items, fn($sum, $item) => $sum + $item, 0);
}

// Cause 2: Built-in function without return type (PHP 8.1 deprecation)
// PHP 8.1 deprecates calling internal functions with null for non-nullable parameters
strlen(null); // Deprecated: null passed to non-nullable parameter

// Cause 3: Method missing return type in interface implementation
class MyIterator implements Iterator {
    public function current() { // Missing return type
        return $this->current;
    }
}

// Cause 4: Recursive function with no explicit return type
function factorial(int $n) {
    if ($n <= 1) return 1;
    return $n * factorial($n - 1);
}
```

## How to Fix

### Fix 1: Add scalar return type declarations

```php
<?php
// Bad: no return type
function calculateTotal(array $items): int|float {
    return array_reduce($items, fn($sum, $item) => $sum + $item, 0);
}

// Good: explicit return type
function calculateTotal(array $items): float {
    return array_reduce($items, fn($sum, $item) => $sum + (float) $item, 0.0);
}

function getCount(array $items): int {
    return count($items);
}
```

### Fix 2: Use void for functions that return nothing

```php
<?php
// Bad: no return type on void function
function logMessage(string $message) {
    error_log($message);
}

// Good: explicit void return type
function logMessage(string $message): void {
    error_log($message);
}
```

### Fix 3: Use never for functions that always throw

```php
<?php
// Bad: unclear intent
function throwError(string $message) {
    throw new \RuntimeException($message);
}

// Good: never return type (PHP 8.1+)
function throwError(string $message): never {
    throw new \RuntimeException($message);
}
```

### Fix 4: Handle nullable return types properly

```php
<?php
// Bad: ambiguous nullable without type
function findUser(int $id) {
    $user = $this->db->query("SELECT * FROM users WHERE id = $id")->fetch();
    return $user ?: null;
}

// Good: explicit nullable return type
function findUser(int $id): ?array {
    $user = $this->db->query("SELECT * FROM users WHERE id = $id")->fetch();
    return $user ?: null;
}
```

## Examples

```php
<?php
// Full example with proper return types

class UserRepository
{
    public function findById(int $id): ?array
    {
        // Returns array or null
        return $this->db->find($id);
    }

    public function findAll(): array
    {
        // Returns array
        return $this->db->findAll();
    }

    public function delete(int $id): bool
    {
        // Returns bool
        return $this->db->delete($id);
    }

    public function logDeletion(int $id): void
    {
        // Returns nothing
        error_log("Deleted user $id");
    }

    public function fail(string $reason): never
    {
        // Never returns — always throws
        throw new \RuntimeException($reason);
    }
}
```

## Related Errors

- [PHP 8.1 Never Return Type]({{< relref "/languages/php/php81-never-return-type" >}}) — never type details
- [PHP 8.1 Enums]({{< relref "/languages/php/php81-enums" >}}) — enum implementation
- [PHP Deprecated]({{< relref "/languages/php/php-deprecated" >}}) — general deprecation warnings
