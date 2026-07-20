---
title: "[Solution] PHP 8.2 DNF Type Error — Disjunctive Normal Form Type Error"
description: "Fix PHP 8.2 DNF Type Error by using correct syntax (A&B|C), checking type compatibility, and understanding PHP 8.2 requirements. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 312
---

# PHP 8.2 DNF Type Error — Disjunctive Normal Form Type Error

A Disjunctive Normal Form (DNF) Type Error occurs when combining intersection and union types with incorrect syntax or incompatible types. PHP 8.2 introduced DNF types, allowing you to combine intersection types (`&`) and union types (`|`) in the form `(A&B)|C` to express "either a type that is both A and B, or type C."

## Common Causes

```php
<?php
// Cause 1: Wrong syntax — missing parentheses
function process(Printable&Stringable|string $value) { // Error on PHP < 8.2
    // DNF requires parentheses around intersections
}

// Cause 2: Using DNF on PHP 8.1 or earlier
// function handle((A&B)|C $value) { } // Error on PHP < 8.2

// Cause 3: Scalar types in intersection
function handle((Countable&int)|string $value) { // Error — int can't implement Countable
}

// Cause 4: Intersection with non-nullable but union with null
function process((A&B)|null $value) { // Valid DNF, but A&B might not work together
}

// Cause 5: Combining two unions without parentheses
function handle(A|B&C|D $value) { // Ambiguous — needs explicit grouping
}
?>
```

## How to Fix

### Fix 1: Use parentheses around intersection groups

```php
<?php
interface Printable {
    public function render(): string;
}

interface Stringable {
    public function __toString(): string;
}

// Correct DNF syntax — intersection in parentheses, then union
function format((Printable&Stringable)|null $value): string {
    if ($value === null) {
        return '';
    }
    // At this point, $value is both Printable AND Stringable
    return $value->render() . ' (' . (string)$value . ')';
}
?>
```

### Fix 2: Only use classes and interfaces in intersections

```php
<?php
interface Cacheable {
    public function cacheKey(): string;
}

interface Exportable {
    public function toArray(): array;
}

// Correct — interfaces in intersection, scalars in union only
function export((Cacheable&Exportable)|string $item): array {
    if (is_string($item)) {
        return ['raw' => $item];
    }
    return $item->toArray();
}
?>
```

### Fix 3: Use DNF types with nullable for common patterns

```php
<?php
interface HasId {
    public function getId(): string;
}

interface Validatable {
    public function validate(): bool;
}

// Common pattern: either an object with both interfaces, or null
function save((HasId&Validatable)|null $entity): bool {
    if ($entity === null) {
        return false;
    }

    if (!$entity->validate()) {
        return false;
    }

    saveToDatabase($entity->getId());
    return true;
}
?>
```

### Fix 4: Check PHP version before using DNF types

```php
<?php
// Option A: Upgrade PHP to 8.2+

// Option B: Use PHPDoc for backward compatibility
/**
 * @param (Countable&Iterator)|null $collection
 */
function processCollection($collection): void {
    if ($collection === null) {
        echo "No collection\n";
        return;
    }

    $collection->rewind();
    echo $collection->count() . " items\n";
}
?>
```

## Examples

```php
<?php
// DNF types with class and interface
interface Identifiable {
    public function getId(): string;
}

abstract class AbstractEntity {
    abstract public function tableName(): string;
}

class User extends AbstractEntity implements Identifiable {
    public function __construct(private string $id, private string $name) {}
    public function getId(): string { return $this->id; }
    public function tableName(): string { return 'users'; }
}

// DNF: either something that is both Identifiable+AbstractEntity, or a string ID
function findById((Identifiable&AbstractEntity)|string $ref): ?AbstractEntity {
    if (is_string($ref)) {
        // Look up by string ID
        return findUserById($ref);
    }
    // $ref is already an entity
    return $ref;
}

$user = new User('1', 'Alice');
echo findById($user)->tableName();  // users
echo findById('2')->tableName();    // users (from DB lookup)
?>
```

## Related Errors

- [PHP 8.0 Union Type Declaration Error](/languages/php/php80-union-type-declaration/) — Basic union types
- [PHP 8.1 Intersection Type Error](/languages/php/php81-intersection-types/) — Basic intersection types
- [PHP 8.4 Asymmetric Visibility Error](/languages/php/php84-asymmetric-visibility/) — PHP 8.4 type features
