---
title: "[Solution] PHP DNF Type: Syntax Error Fix"
description: "Fix PHP Disjunctive Normal Form (DNF) type syntax errors. Learn PHP 8.2 intersection and union types."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["dnf", "disjunctive-normal-form", "type", "php", "intersection"]
weight: 5
---

# PHP DNF Type: Syntax Error Fix

A PHP DNF type error occurs when you use incorrect syntax for Disjunctive Normal Form types. PHP 8.2 allows combining intersection types with union types in function parameters.

## What This Error Means

PHP 8.2 introduced Disjunctive Normal Form (DNF) types, which allow combining intersection types (`A&B`) with union types (`A|B`) in parentheses. For example, `(A&B)|null` means "an object that implements both A and B, or null."

## Common Causes

- Using DNF types on PHP versions before 8.2
- Incorrect parentheses placement
- Mixing DNF with scalar types incorrectly
- Missing parentheses around intersection in union

## How to Fix

### 1. Use correct DNF type syntax

```php
<?php
// WRONG: Missing parentheses (PHP 8.2 error)
// function process(Countable&Iterator|null $value): void {}

// CORRECT: Use parentheses for DNF
function process((Countable&Iterator)|null $value): void {
    if ($value !== null) {
        echo "Count: " . $value->count() . "\n";
    }
}
?>
```

### 2. Use DNF for nullable intersection types

```php
<?php
// CORRECT: Nullable intersection type
function render((Stringable&JsonSerializable)|null $data): string {
    return match (true) {
        $data === null => 'null',
        $data instanceof JsonSerializable => json_encode($data),
        default => (string) $data,
    };
}
?>
```

### 3. Combine with class types

```php
<?php
interface Cacheable {
    public function cacheKey(): string;
}

interface Expirable {
    public function expiresAt(): DateTimeInterface;
}

// CORRECT: DNF type with interfaces
function store((Cacheable&Expirable)|null $item): void {
    if ($item === null) {
        return;
    }
    echo "Caching " . $item->cacheKey() . " until " . $item->expiresAt()->format('c');
}
?>
```

### 4. Use return type DNF

```php
<?php
// CORRECT: DNF in return type
function fetchData(): (Arrayable&JsonSerializable)|null {
    if ($this->data === null) {
        return null;
    }
    return $this->data;
}
?>
```

## Related Errors

- [PHP Parse error]({{< relref "/languages/php/parse-error" >}})
- [PHP Deprecated function]({{< relref "/languages/php/php-deprecated-error-v2" >}})
- [PHP Enum error]({{< relref "/languages/php/php-enumerator-error-v2" >}})
