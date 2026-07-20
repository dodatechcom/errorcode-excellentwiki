---
title: "[Solution] PHP 8.0 Named Argument Error — Named Argument Doesn't Match Parameter"
description: "Fix PHP 8.0 Named Argument Error by checking parameter names, using correct order, and verifying function signatures. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 303
---

# PHP 8.0 Named Argument Error — Named Argument Doesn't Match Parameter

A Named Argument Error occurs when you pass a named argument that doesn't match any parameter name in the function signature, or when the argument is used incorrectly with positional arguments. PHP 8.0 introduced named arguments, allowing you to reference parameters by name rather than position.

## Common Causes

```php
<?php
// Cause 1: Typo in parameter name
function createUser(string $name, int $age, string $email): array {
    return compact('name', 'age', 'email');
}

createUser(name: 'Alice', ages: 25, email: 'alice@example.com');
// Error — "ages" doesn't match any parameter

// Cause 2: Named argument after variadic parameter
function logMessage(string ...$messages): void {
    foreach ($messages as $msg) {
        echo $msg . "\n";
    }
}
logMessage(messages: ['hello', 'world']); // Error

// Cause 3: Mixing positional and named args incorrectly
createUser('Alice', email: 'alice@example.com', age: 25);
// Error — positional args must come before named args

// Cause 4: Duplicate argument names
createUser(name: 'Alice', name: 'Bob'); // Error — duplicate

// Cause 5: Using named arguments with internal functions that use references
strlen(string: 'hello'); // Error — "string" isn't a named parameter
?>
```

## How to Fix

### Fix 1: Check the exact parameter names in the function signature

```php
<?php
// Check function signature first
function createUser(string $name, int $age, string $email): array {
    return compact('name', 'age', 'email');
}

// Correct — use exact parameter names
createUser(name: 'Alice', age: 25, email: 'alice@example.com');
?>
```

### Fix 2: Place all positional arguments before named arguments

```php
<?php
function configure(string $host, int $port, bool $ssl): void {
    echo "$host:$port ssl=" . ($ssl ? 'on' : 'off') . "\n";
}

// Correct — positional first, then named
configure('localhost', 3306, ssl: true);

// Wrong — positional after named
// configure('localhost', ssl: true, 3306); // Error
?>
```

### Fix 3: Avoid named arguments with variadic parameters

```php
<?php
function logMessages(string ...$messages): void {
    foreach ($messages as $msg) {
        echo $msg . "\n";
    }
}

// Correct — use positional args with variadic
logMessages('hello', 'world', 'foo');

// Or restructure to use named parameters explicitly
function logBatch(array $messages): void {
    foreach ($messages as $msg) {
        echo $msg . "\n";
    }
}
logBatch(messages: ['hello', 'world', 'foo']);
?>
```

### Fix 4: Verify the function accepts named arguments

```php
<?php
// Some built-in or C-level functions don't support named arguments
// Check PHP docs for the function

// Wrong — built-in function, parameter name not guaranteed
// str_replace(search: 'foo', subject: 'foobar', replace: 'bar');

// Correct — use positional
str_replace('foo', 'bar', 'foobar');
?>
```

## Examples

```php
<?php
// Advanced named argument usage
class HttpClient {
    public function __construct(
        private string $baseUrl,
        private int $timeout = 30,
        private bool $verifySsl = true,
    ) {}

    public function request(string $method, string $path, array $headers = []): mixed {
        // Implementation
        return null;
    }
}

// Creating with only some named args (skipping defaults)
$client = new HttpClient(
    baseUrl: 'https://api.example.com',
    timeout: 60,
);

// Calling with named arguments
$client->request(
    method: 'POST',
    path: '/users',
    headers: ['Content-Type' => 'application/json'],
);

// Named arguments with array unpacking
$options = ['timeout' => 120, 'verifySsl' => false];
$client2 = new HttpClient(baseUrl: 'https://api.test.com', ...$options);
?>
```

## Related Errors

- [PHP 8.0 Union Type Error](/languages/php/php80-union-type-error/) — Type mismatch in union-typed parameters
- [PHP 8.0 Match Expression Error](/languages/php/php80-match-expression/) — Match expression case errors
- [PHP 8.0 First Class Callable Syntax Error](/languages/php/php80-first-class-callable/) — Callable syntax issues
