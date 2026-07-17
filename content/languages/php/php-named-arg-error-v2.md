---
title: "[Solution] PHP Named Argument Error Fix"
description: "Fix PHP named argument errors. Learn how PHP 8.0 named arguments work and common mistakes."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Named Argument Error Fix

A PHP named argument error occurs when you use incorrect parameter names, mix positional and named arguments in the wrong order, or pass unexpected named arguments.

## What This Error Means

PHP 8.0 introduced named arguments, allowing you to pass arguments by name instead of position. The parameter name must match exactly. Named arguments must come after positional arguments and cannot be skipped when mixed.

## Common Causes

- Misspelled parameter names
- Passing named arguments to functions without named parameters
- Mixing positional and named arguments incorrectly (positional after named)
- Using reserved keyword as parameter name
- Passing unknown named arguments

## How to Fix

### 1. Use correct parameter names

```php
<?php
function createUser(string $name, int $age, string $email): array {
    return compact('name', 'age', 'email');
}

// WRONG: Misspelled parameter name
// createUser($name: 'Alice', $age: 30, $emial: 'alice@example.com');

// CORRECT: Exact parameter name
createUser(name: 'Alice', age: 30, email: 'alice@example.com');
?>
```

### 2. Don't mix positional and named incorrectly

```php
<?php
function connect(string $host, int $port, string $db): void {
    echo "Connecting to $host:$port/$db\n";
}

// WRONG: Positional after named
// connect(host: 'localhost', 3306, 'mydb');

// CORRECT: Named arguments only, or positional only
connect(host: 'localhost', port: 3306, db: 'mydb');
// OR
connect('localhost', 3306, 'mydb');
?>
```

### 3. Only use valid parameter names

```php
<?php
// WRONG: Using reserved word or wrong name
// Some functions have names that can't be used as named args

// CORRECT: Check the function signature first
// Look at: function foo(Type $param)
// Use: foo(param: value)
?>
```

### 4. Don't pass unexpected named arguments

```php
<?php
// WRONG: Extra named argument
// array_map(callback: 'strlen', array: $arr, extra: true);

// CORRECT: Only named arguments the function accepts
array_map('strlen', $arr);
?>
```

## Related Errors

- [PHP Match error]({{< relref "/languages/php/php-match-error-v2" >}})
- [PHP Parse error]({{< relref "/languages/php/parse-error" >}})
- [PHP Deprecated function]({{< relref "/languages/php/php-deprecated-error-v2" >}})
