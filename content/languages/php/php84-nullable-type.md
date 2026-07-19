---
title: "[Solution] PHP Implicitly Nullable Parameter Deprecation Fix"
description: "Fix 'Deprecated: Implicitly nullable parameter' warnings in PHP 8.4. Use explicit nullable type declarations."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "php84", "nullable-types", "deprecation", "e-deprecated"]
severity: "error"
---

# Deprecated: Implicitly Nullable Parameter Declaration

## Error Message

```
Deprecated: Implicitly marking parameter $name as nullable is deprecated, the explicit nullable type must be used instead in /path/to/file.php:5
```

## Common Causes

- Using a default value of null on a non-nullable type hint (e.g., function foo(string $s = null))
- Legacy PHP code written before the explicit nullable syntax (?Type) was recommended
- Third-party libraries that haven't been updated for PHP 8.4 compatibility
- Copy-pasting old PHP examples that use the implicit nullable pattern

## Solutions

### Solution 1: Use explicit nullable type syntax (?Type)

Replace 'Type $param = null' with '?Type $param = null' to explicitly mark parameters as nullable.

```php
<?php
// WRONG: Implicit nullable — deprecated in PHP 8.4
function greet(string $name = null): string {
    return $name ? "Hello, $name" : 'Hello, stranger';
}

// CORRECT: Explicit nullable
function greet(?string $name = null): string {
    return $name ? "Hello, $name" : 'Hello, stranger';
}

echo greet('Alice');  // 'Hello, Alice'
echo greet();         // 'Hello, stranger'
?>
```

### Solution 2: Audit and fix all implicit nullable parameters

Search your codebase for the deprecated pattern and update every instance systematically.

```php
<?php
// WRONG: All three parameters use implicit nullable
function createUser(
    string $name,
    string $email = null,
    int $age = null,
): array {
    return compact('name', 'email', 'age');
}

// CORRECT: All three use explicit nullable
function createUser(
    string $name,
    ?string $email = null,
    ?int $age = null,
): array {
    return [
        'name'  => $name,
        'email' => $email,
        'age'   => $age,
    ];
}

print_r(createUser('Alice')); // ['name'=>'Alice', 'email'=>null, 'age'=>null]
?>
```

### Solution 3: Use a search-and-replace regex to fix all occurrences

Use a regex pattern to find and replace the deprecated pattern across your entire codebase.

```php
<?php
// Run from command line to find all instances:
// grep -rn "= null" --include="*.php" src/

// In your CI pipeline, add a static analysis check:
// phpstan analyse --level=9 src/ will flag implicit nullable deprecations

// Example of properly typed optional parameters:
function processOrder(
    int $orderId,
    ?string $couponCode = null,
    ?float $discountPercent = null,
    ?string $notes = null,
): array {
    return [
        'orderId'  => $orderId,
        'coupon'   => $couponCode,
        'discount' => $discountPercent,
        'notes'    => $notes,
    ];
}

$order = processOrder(123, 'SAVE20', 20.0);
print_r($order);
?>
```

## Prevention Tips

- Search for '= null' in parameter lists and replace 'Type $p = null' with '?Type $p = null'
- PHPStan at level 9 and Psalm detect implicit nullable deprecations automatically
- Update third-party libraries that trigger this deprecation — check their issue trackers
- The ?Type syntax has been supported since PHP 7.1, so this is safe to apply in all modern PHP versions

## Related Errors

- [PHP Deprecated Function Usage]({{< relref "/languages/php/php-deprecated" >}})
- [PHP Union Type Error]({{< relref "/languages/php/php80-union-type-error" >}})
- [PHP Intersection Type Error]({{< relref "/languages/php/php81-intersection-type" >}})
