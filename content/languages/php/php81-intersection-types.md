---
title: "[Solution] PHP 8.1 Intersection Type Error — Invalid Intersection Type"
description: "Fix PHP 8.1 Intersection Type Error by using correct syntax (Type1&Type2) and checking class/interface compatibility. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 309
---

# PHP 8.1 Intersection Type Error — Invalid Intersection Type

An Intersection Type Error occurs when the intersection type syntax is wrong or when the types in an intersection are incompatible. PHP 8.1 introduced intersection types using `&`, allowing parameters, return types, and properties to require that a value implements multiple types simultaneously.

## Common Causes

```php
<?php
// Cause 1: Using | instead of &
function process(Countable|Iterator $collection) { // Wrong — this is a union type
    // This means Countable OR Iterator, not both
}

// Cause 2: Intersection with scalar types
function handle(Countable&int $value) { // Error — int cannot implement interfaces
    // Scalars can't implement interfaces
}

// Cause 3: Incompatible class and interface in child class
interface Printable { public function render(): string; }
class Widget { public string $name = 'widget'; }

class SpecialWidget extends Widget implements Printable {
    public function render(): string { return $this->name; }
}

class BadWidget extends SpecialWidget {
    // Error — narrowing intersection type
    public function render(Printable&Widget $item): string { }
}

// Cause 4: Intersection type with same type
function process(Countable&Countable $value) { // Error — redundant
    // Same type twice is not meaningful
}

// Cause 5: Using intersection with union without DNF (pre-8.2)
function handle(Printable&Widget|null $value) { // Error on PHP 8.1
    // DNF types require PHP 8.2
}
?>
```

## How to Fix

### Fix 1: Use `&` separator for intersection types

```php
<?php
// Wrong — union type (OR)
// function process(Countable|Iterator $collection) { }

// Correct — intersection type (AND)
function process(Countable&Iterator $collection): void {
    $collection->rewind();
    echo $collection->count() . " items\n";
}
?>
```

### Fix 2: Only use classes and interfaces in intersection types

```php
<?php
// Wrong — scalar type in intersection
// function handle(Countable&int $value) { }

// Correct — use interfaces and classes
interface Cacheable {
    public function getCacheKey(): string;
}

interface Serializable2 {
    public function serialize(): string;
}

function process(Cacheable&Serializable2 $item): void {
    $key = $item->getCacheKey();
    $data = $item->serialize();
}
?>
```

### Fix 3: Implement proper interface requirements

```php
<?php
interface Loggable {
    public function toLog(): string;
}

interface Cacheable {
    public function cacheKey(): string;
}

class Document implements Loggable, Cacheable {
    public function toLog(): string {
        return "Document: {$this->title}";
    }

    public function cacheKey(): string {
        return "doc_{$this->id}";
    }
}

// Parameter requires both interfaces
function store(Loggable&Cacheable $item): void {
    error_log($item->toLog());
    cache()->set($item->cacheKey(), $item);
}
?>
```

### Fix 4: Use PHPDoc for backward compatibility

```php
<?php
/**
 * @param Countable&Iterator $collection
 */
function process($collection) {
    $collection->rewind();
    echo $collection->count() . " items\n";
}
?>
```

## Examples

```php
<?php
interface Identifiable {
    public function getId(): string;
}

interface Validatable {
    public function validate(): bool;
}

interface Serializable3 {
    public function toArray(): array;
}

class UserModel implements Identifiable, Validatable, Serializable3 {
    public function __construct(
        private string $id,
        private string $name,
    ) {}

    public function getId(): string { return $this->id; }
    public function validate(): bool { return !empty($this->name); }
    public function toArray(): array { return ['id' => $this->id, 'name' => $this->name]; }
}

// Requires all three interfaces
function saveUser(Identifiable&Validatable&Serializable3 $user): void {
    if (!$user->validate()) {
        throw new InvalidArgumentException('Invalid user');
    }
    $data = $user->toArray();
    saveToDatabase($user->getId(), $data);
}

$user = new UserModel('1', 'Alice');
saveUser($user);
?>
```

## Related Errors

- [PHP 8.0 Union Type Declaration Error](/languages/php/php80-union-type-declaration/) — Using `|` for union types
- [PHP 8.2 DNF Type Error](/languages/php/php82-disjunctive-normal-form/) — Combining `&` and `|` in types
- [PHP 8.0 Union Type Error](/languages/php/php80-union-type-error/) — Union type runtime errors
