---
title: "[Solution] PHP 8.1 Never Return Type Issues"
description: "Fix PHP 8.1 never return type errors. Use never for functions that always throw exceptions or call exit."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1103
---

# PHP 8.1 Never Return Type Issues

PHP 8.1 introduced the `never` return type for functions that are guaranteed to never return a value. This includes functions that always throw an exception or call `exit()`/`die()`. Using `never` incorrectly — such as returning a value from a never function — causes a fatal error.

## Common Causes

```php
<?php
// Cause 1: Returning a value from a never function
function throwError(string $msg): never {
    throw new \Exception($msg);
    return "something"; // Fatal error: never returns a value
}

// Cause 2: Not throwing or exiting in a never function
function stop(): never {
    $x = 1; // No throw or exit — fatal error
}

// Cause 3: Using never with union types
function bad(int|string $val): never|int { // Invalid: never cannot be in union
    throw new \Exception("$val");
}

// Cause 4: Extending a non-never method with never in child class
class Base {
    protected function fail(): int|string {
        return 0;
    }
}
class Child extends Base {
    protected function fail(): never { // Fatal error: incompatible override
        throw new \Exception();
    }
}
```

## How to Fix

### Fix 1: Ensure never functions always throw or exit

```php
<?php
// Good: always throws
function throwError(string $message): never {
    throw new \RuntimeException($message);
}

// Good: always exits
function halt(): never {
    exit(1);
}

// Good: always dies
function fatalError(string $msg): never {
    die($msg);
}
```

### Fix 2: Remove return statements from never functions

```php
<?php
// Bad: return after throw
function fail(): never {
    throw new \Exception("Failed");
    return false; // Unreachable — fatal error in PHP 8.1
}

// Good: only throw
function fail(): never {
    throw new \Exception("Failed");
}
```

### Fix 3: Do not use never in union types

```php
<?php
// Bad: never cannot be part of a union type
function process(int $code): never|string {
    if ($code === 0) {
        throw new \Exception("Invalid");
    }
    return "ok";
}

// Good: use the actual return type
function process(int $code): string {
    if ($code === 0) {
        throw new \Exception("Invalid");
    }
    return "ok";
}
```

### Fix 4: Use never for error handlers and fallback methods

```php
<?php
// Good use cases for never
class Router
{
    public function handle(string $route): never
    {
        throw new \RuntimeException("No handler for route: $route");
    }
}

class ErrorHandler
{
    public static function critical(string $msg): never
    {
        error_log($msg);
        http_response_code(500);
        exit(1);
    }
}
```

## Examples

```php
<?php
// Practical never return type examples

// Exception factory method
function notFound(string $resource): never {
    throw new \InvalidArgumentException("Resource not found: $resource");
}

// Guard clause helper
function requireAuth(?User $user): never {
    if ($user === null) {
        throw new \RuntimeException("Authentication required");
    }
}

// Static assert helper for impossible states
function impossibleState(string $state): never {
    throw new \LogicException("Unexpected state: $state");
}

// Usage
try {
    $user = getUser();
    requireAuth($user); // Returns void or throws never
    processUser($user);
} catch (\RuntimeException $e) {
    echo $e->getMessage();
}
```

## Related Errors

- [PHP 8.1 Return Type Declaration]({{< relref "/languages/php/php81-return-type-declaration" >}}) — return type deprecations
- [TypeError]({{< relref "/languages/php/typeerror" >}}) — type mismatch errors
- [PHP Deprecated]({{< relref "/languages/php/php-deprecated" >}}) — deprecation warnings
