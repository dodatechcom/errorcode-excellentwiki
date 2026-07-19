---
title: "[Solution] PHP Intersection Type Error Fix"
description: "Fix intersection type errors in PHP 8.1+. Learn how A&B types work and resolve declaration conflicts."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "php81", "intersection-types", "type-system", "fatal-error"]
severity: "error"
---

# Intersection Type Error

## Error Message

```
Fatal error: Declaration of Logger::process(Countable&Iterator $collection): void must be compatible with Processor::process(Countable $collection): void in /path/to/file.php:14
```

## Common Causes

- Using an intersection type (A&B) in a method override where the parent uses a single type
- Trying to pass an object that does not implement all interfaces in the intersection type
- Combining intersection types with union types incorrectly in method signatures
- Third-party packages compiled against a different PHP version with incompatible intersection type usage

## Solutions

### Solution 1: Ensure override signatures match the parent exactly

Child class methods must use the same or narrower intersection types as the parent declaration.

```php
<?php
interface Cacheable {
    public function cacheKey(): string;
}

interface Validatable {
    public function validate(): bool;
}

class BaseHandler {
    public function handle(Cacheable&Validatable $item): string {
        return $item->cacheKey();
    }
}

class SpecialHandler extends BaseHandler {
    // CORRECT: Same signature as parent
    public function handle(Cacheable&Validatable $item): string {
        if (!$item->validate()) {
            return 'invalid';
        }
        return $item->cacheKey();
    }
}
?>
```

### Solution 2: Use type checks before intersection type usage

Validate that an object implements all required interfaces before passing it to an intersection-typed parameter.

```php
<?php
interface Printable {
    public function render(): string;
}

interface Loggable {
    public function log(): void;
}

function processItem(Printable&Loggable $item): void {
    $item->log();
    echo $item->render();
}

// Safely check before calling
function safeProcess(object $item): void {
    if ($item instanceof Printable && $item instanceof Loggable) {
        processItem($item);
    } else {
        error_log('Item does not implement all required interfaces');
    }
}
?>
```

### Solution 3: Refactor intersection types using composition

When intersection types cause compatibility issues, create a combined interface that extends both.

```php
<?php
interface Cacheable {
    public function cacheKey(): string;
}

interface Validatable {
    public function validate(): bool;
}

// Create a combined interface
interface CacheableAndValidatable extends Cacheable, Validatable {}

class Product implements CacheableAndValidatable {
    public function __construct(
        private string $sku,
        private int $stock,
    ) {}

    public function cacheKey(): string {
        return "product:{$this->sku}";
    }

    public function validate(): bool {
        return $this->stock > 0;
    }
}

function process(CacheableAndValidatable $item): void {
    echo $item->cacheKey();
}
?>
```

## Prevention Tips

- Intersection types (A&B) require an object to implement ALL listed interfaces or extend all listed classes
- Use union types (A|B) when you want to accept ONE of several types instead of all of them
- PHPStan and Psalm detect intersection type mismatches — run them before deploying
- Consider combined interfaces (extending multiple interfaces) for cleaner API contracts

## Related Errors

- [PHP Union Type Error]({{< relref "/languages/php/php80-union-type-error" >}})
- [PHP Typed Property Error]({{< relref "/languages/php/php80-typed-property-error" >}})
- [PHP Parse Error]({{< relref "/languages/php/parse-error" >}})
