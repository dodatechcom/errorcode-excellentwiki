---
title: "[Solution] PHP Warning: function_name() Expects Exactly N Parameters"
description: "Fix PHP Warning: function_name() expects exactly N parameters. Check function signature, provide correct parameters, use func_get_args()."
languages: ["php"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 8
---

# PHP Warning: function_name() Expects Exactly N Parameters

This warning occurs when you call a built-in or user-defined PHP function with a number of arguments that doesn't match its expected signature. The function may produce incorrect behavior or silently ignore extra parameters.

## Common Causes

```php
<?php
// Example 1: Extra argument to strlen()
echo strlen("hello", "world");
// Warning: strlen() expects exactly 1 parameter, 2 given
```

```php
<?php
// Example 2: Missing required argument
function createUser(string $name, string $email): void {
    // ...
}
createUser("Alice");
// Warning: createUser() expects exactly 2 parameters, 1 given
```

```php
<?php
// Example 3: Wrong argument type causes wrong count
array_push($array); // Missing second argument
// Warning: array_push() expects at least 2 parameters, 1 given
```

```php
<?php
// Example 4: Spread operator with wrong count
$params = ["only_one"];
str_replace("search", "replace", ...$params);
// Warning: str_replace() expects at least 2 parameters, 1 given
```

```php
<?php
// Example 5: Calling with no arguments when required
function processData(string $input): string {
    return strtoupper($input);
}
processData();
// Warning: processData() expects exactly 1 parameter, 0 given
```

## How to Fix

### Fix 1: Check the Function Signature

Always verify the expected parameter count in the [PHP documentation](https://www.php.net/manual/en/) before calling a function.

```php
<?php
// WRONG: strlen() expects exactly 1 argument
echo strlen("hello", "world");

// CORRECT
echo strlen("hello"); // 5
```

### Fix 2: Match the Parameter Count Exactly

Ensure your call matches the function definition.

```php
<?php
function greet(string $name, string $greeting = "Hello"): string {
    return "{$greeting}, {$name}!";
}

// WRONG: too many arguments
greet("Alice", "Hi", "extra");

// CORRECT
greet("Alice");         // Uses default greeting
greet("Alice", "Hi");   // Overrides default
```

### Fix 3: Use Variadic Parameters for Flexible Arguments

Define functions that accept a variable number of arguments using `...`.

```php
<?php
function sum(...$numbers): int {
    return array_sum($numbers);
}

// Accepts any number of arguments
echo sum(1, 2, 3);     // 6
echo sum(1, 2, 3, 4);  // 10
```

### Fix 4: Use func_get_args() for Dynamic Handling

Access arguments dynamically inside a function.

```php
<?php
function flexible(): string {
    $args = func_get_args();
    return "Received " . count($args) . " arguments";
}

echo flexible("a", "b", "c"); // "Received 3 arguments"
```

### Fix 5: Validate Before Calling

Check argument count and provide meaningful errors.

```php
<?php
function callFunction(callable $func, array $args): mixed {
    $reflection = new ReflectionFunction($func);
    $required = $reflection->getNumberOfRequiredParameters();
    $total = $reflection->getNumberOfParameters();

    if (count($args) < $required) {
        throw new \InvalidArgumentException(
            "Function requires {$required}-{$total} parameters, " . count($args) . " provided"
        );
    }

    return $func(...$args);
}

callFunction("strtoupper", ["hello"]);       // HELLO
callFunction("array_push", [$arr, "value"]); // Works
```

## Examples

```php
<?php
// Scenario: Processing user data with validation
function registerUser(string $name, string $email, string $password, int $role = 0): array {
    return [
        'name' => $name,
        'email' => $email,
        'password' => password_hash($password, PASSWORD_DEFAULT),
        'role' => $role,
    ];
}

// Correct usage
$user = registerUser("Alice", "alice@example.com", "secret123");
$admin = registerUser("Bob", "bob@example.com", "admin456", 1);
```

## Related Errors

- [PHP Warning: strlen() Expects String](/languages/php/warning-strlen-expects)
- [PHP Warning: sprintf() Too Few Arguments](/languages/php/warning-sprintf-too-few)
- [PHP Notice: Undefined Variable](/languages/php/notice-undefined-variable)
