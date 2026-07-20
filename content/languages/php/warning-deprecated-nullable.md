---
title: "[Solution] PHP Deprecated: Implicit Nullable Type Declaration"
description: "Fix PHP Deprecated: Implicit nullable type. Use explicit nullable syntax (?Type), update type declarations to be compatible with PHP 8.4+."
languages: ["php"]
severities: ["deprecated"]
error-types: ["runtime-error"]
weight: 110
---

# PHP Deprecated: Implicit Nullable Type Declaration

In PHP 8.4, the implicit nullable type declaration was deprecated. When a parameter with a type hint has a default value of `null`, PHP previously treated it as implicitly nullable. You must now use the explicit `?Type` syntax to declare nullable parameters.

## Common Causes

```php
// Cause 1: Implicit nullable with class type hint
<?php
function processUser(User $user = null): void
{
    // Deprecated in PHP 8.4 — implicit nullable
    if ($user === null) {
        echo "No user provided";
    }
}
?>
```

```php
// Cause 2: Implicit nullable with scalar type
<?php
function formatDate(DateTime $date = null, string $format = 'Y-m-d'): string
{
    // $date is implicitly nullable
    $d = $date ?? new DateTime();
    return $d->format($format);
}
?>
```

```php
// Cause 3: Implicit nullable in method signatures
<?php
class UserService
{
    public function findUser(string $email = null): ?array
    {
        // Deprecated — implicit nullable
        if ($email === null) {
            return null;
        }
        // ...
    }
}
?>
```

```php
// Cause 4: Implicit nullable with interface type
<?php
function handleRequest(Request $request = null): Response
{
    // Deprecated — implicit nullable
    $req = $request ?? new Request();
    return new Response();
}
?>
```

## How to Fix

### Fix 1: Use Explicit Nullable Syntax (?Type)

Add the `?` prefix to make the nullable declaration explicit.

```php
<?php
// BEFORE (deprecated in PHP 8.4)
function processUser(User $user = null): void
{
    // ...
}

// AFTER — explicit nullable
function processUser(?User $user = null): void
{
    // ...
}

// BEFORE
function formatDate(DateTime $date = null, string $format = 'Y-m-d'): string
{
    // ...
}

// AFTER
function formatDate(?DateTime $date = null, string $format = 'Y-m-d'): string
{
    // ...
}
?>
```

### Fix 2: Update All Method Signatures in Classes

Systematically update every method with implicit nullable parameters.

```php
<?php
// BEFORE (deprecated)
class UserService
{
    public function findUser(string $email = null): ?array {}
    public function updateUser(int $id, User $user = null): bool {}
    public function deleteUser(int $id, bool $force = false, string $reason = null): void {}
}

// AFTER — explicit nullable
class UserService
{
    public function findUser(?string $email = null): ?array {}
    public function updateUser(int $id, ?User $user = null): bool {}
    public function deleteUser(int $id, bool $force = false, ?string $reason = null): void {}
}
?>
```

### Fix 3: Use Union Types for Alternative Syntax

PHP 8.0+ supports union types as an alternative way to express nullable.

```php
<?php
// Explicit nullable with ? syntax
function process(?string $input): string
{
    return $input ?? 'default';
}

// Union type alternative (PHP 8.0+)
function processAlt(string|null $input): string
{
    return $input ?? 'default';
}

// Both approaches work identically
echo process(null);    // default
echo processAlt(null); // default
?>
```

### Fix 4: Use a Script to Find All Occurrences

Search your codebase for implicit nullable parameters.

```php
<?php
// Search pattern for implicit nullable parameters:
// Look for: type_hint $param = null
// Replace with: ?type_hint $param = null

// grep -rn "= null" --include="*.php" .

// Then review each match:
// - If preceded by a type hint, add ? prefix
// - If no type hint, no change needed
?>
```

```php
<?php
// Example: finding and fixing with regex
// Search: /\b([A-Z]\w+)\s+\$(\w+)\s*=\s*null/
// Replace: ?\1 $\2 = null

// BEFORE:
function handle(string $name = null, int $count = null, \DateTime $date = null): void {}

// AFTER:
function handle(?string $name = null, ?int $count = null, ?\DateTime $date = null): void {}
?>
```

## Examples

```php
<?php
// Complete migration example

// BEFORE (deprecated implicit nullable)
class Database
{
    public function __construct(string $host = null, int $port = null, string $dbname = null)
    {
        $this->host = $host ?? 'localhost';
        $this->port = $port ?? 3306;
        $this->dbname = $dbname ?? 'test';
    }

    public function query(string $sql, array $params = null): array
    {
        // ...
    }
}

// AFTER (explicit nullable)
class Database
{
    public function __construct(
        ?string $host = null,
        ?int $port = null,
        ?string $dbname = null
    ) {
        $this->host = $host ?? 'localhost';
        $this->port = $port ?? 3306;
        $this->dbname = $dbname ?? 'test';
    }

    public function query(string $sql, ?array $params = null): array
    {
        $params = $params ?? [];
        // ...
        return [];
    }
}

// Usage is identical
$db = new Database();
$db->query("SELECT 1");
?>
```

```php
<?php
// Helper to verify nullable declarations are explicit
function validateNullableSyntax(string $filename): array
{
    $content = file_get_contents($filename);
    $warnings = [];

    // Match implicit nullable: type $param = null (without ?)
    if (preg_match_all('/\b([A-Z]\w+(?:\\\\\w+)*)\s+\$(\w+)\s*=\s*null/', $content, $matches)) {
        foreach ($matches[0] as $i => $match) {
            $warnings[] = "Line contains implicit nullable: {$match}";
        }
    }

    return $warnings;
}

$issues = validateNullableSyntax(__DIR__ . '/UserService.php');
foreach ($issues as $issue) {
    echo $issue . "\n";
}
?>
```

## Related Errors

- [PHP Deprecated: FILTER_SANITIZE_STRING](/languages/php/warning-deprecated-filter-has-constant)
- [PHP Deprecated: create_function()](/languages/php/warning-deprecated-create-function)
- [PHP Deprecated: each()](/languages/php/warning-deprecated-each)
