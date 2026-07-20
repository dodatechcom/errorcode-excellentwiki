---
title: "[Solution] PHPStan Static Analysis Error Fix"
description: "Fix PHPStan analysis errors. Check reported errors, add type hints, suppress specific rules, increase analysis level."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1110
---

# PHPStan Static Analysis Error

PHPStan static analysis errors indicate code that PHPStan detects as potentially incorrect, type-unsafe, or violating best practices. These errors are reported during analysis and range from level 0 (basic checks) to level 9 (strictest checks). Addressing them improves code quality and prevents runtime bugs.

## Common Causes

```php
<?php
// Cause 1: Missing type declarations
function processData($data) { // Missing parameter type
    return $data->invalidMethod(); // Method doesn't exist
}

// Cause 2: Possibly null access
$user = findUser($id);
echo $user->name; // Variable $user might be null

// Cause 3: Incorrect return type
function getCount(): int {
    if (empty($items)) {
        return null; // PHPStan: must return int, got null
    }
    return count($items);
}

// Cause 4: Undefined method or property
$obj = new stdClass();
$obj->nonExistentMethod(); // Method does not exist

// Cause 5: Always falsy/unreachable code
if (false) {
    echo "Dead code"; // PHPStan: condition is always false
}
```

## How to Fix

### Fix 1: Add proper type declarations

```php
<?php
// Bad: no types
function process($data) {
    return $data->id;
}

// Good: explicit types
function process(array $data): int {
    return $data['id'];
}

// For complex types, use PHPDoc
/**
 * @param array<string, mixed> $data
 * @return array{id: int, name: string}
 */
function process(array $data): array {
    return [
        'id' => (int) $data['id'],
        'name' => (string) $data['name'],
    ];
}
```

### Fix 2: Handle nullable types properly

```php
<?php
// Bad: PHPStan warns about null access
$user = findUser($id);
echo $user->name;

// Good: check for null first
$user = findUser($id);
if ($user === null) {
    throw new \RuntimeException("User not found");
}
echo $user->name;

// Or use null-safe operator (PHP 8.0+)
echo $user?->name;
```

### Fix 3: Fix return type mismatches

```php
<?php
// Bad: returning null from non-nullable function
function getCount(): int {
    if (empty($items)) {
        return null; // PHPStan error
    }
    return count($items);
}

// Good: use nullable return type
function getCount(): ?int {
    if (empty($items)) {
        return null;
    }
    return count($items);
}

// Or ensure valid return
function getCount(): int {
    return count($items ?? []);
}
```

### Fix 4: Suppress specific rules when needed

```php
<?php
// phpstan.neon configuration
parameters:
    level: 6
    ignoreErrors:
        - '#Call to an undefined method stdClass::nonExistentMethod\(\)#'
        - '#Variable \$maybeNull might not be defined#'

// Or inline suppression
/** @phpstan-ignore-next-line */
$dynamicObj->dynamicMethod();
```

### Fix 5: Increase analysis level gradually

```bash
# Start with lower level
phpstan analyse src/ --level=0

# Increase level incrementally
phpstan analyse src/ --level=4

# Use baseline for existing errors
phpstan analyse src/ --generate-baseline

# Then fix new errors only
phpstan analyse src/
```

## Examples

```php
<?php
// PHPStan-annotated code example

/**
 * Find a user by ID
 *
 * @param int $id
 * @return User|null
 */
function findUser(int $id): ?User
{
    $result = $db->query("SELECT * FROM users WHERE id = ?", [$id]);
    return $result->fetchObject(User::class);
}

// Usage with proper null handling
$user = findUser($id);
if ($user === null) {
    return new Response('User not found', 404);
}

// PHPStan knows $user is User here
return new Response($user->toJSON(), 200);
```

## Related Errors

- [Psalm Error]({{< relref "/languages/php/psalm-error" >}}) — Psalm analysis errors
- [TypeError]({{< relref "/languages/php/typeerror" >}}) — type mismatch runtime errors
- [Rector Error]({{< relref "/languages/php/rector-error" >}}) — automated code fixes
