---
title: "[Solution] PHP ArgumentCountError — Wrong Argument Count"
description: "Fix PHP ArgumentCountError by providing correct argument count, using variadic functions, and checking function signatures."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 59
---

# ArgumentCountError — Wrong Argument Count

ArgumentCountError is thrown when a function is called with too many or too few arguments. PHP 7.0+ throws this as an `Error` subclass instead of a warning. This includes both built-in and user-defined functions.

## Common Causes

```php
<?php
// Cause 1: Too few arguments
function greet(string $name, string $greeting = "Hello"): string {
    return "$greeting, $name!";
}
greet(); // ArgumentCountError: 0 arguments given, 1 expected

// Cause 2: Too many arguments
function add(int $a, int $b): int {
    return $a + $b;
}
add(1, 2, 3); // ArgumentCountError: 3 arguments given, 2 expected

// Cause 3: Missing required argument in built-in function
array_slice([1, 2, 3]); // ArgumentCountError: 0 arguments given, 2 expected

// Cause 4: Dynamic function call with wrong count
$func = 'strlen';
$func(); // ArgumentCountError

// Cause 5: Spread operator with insufficient values
function test(int $a, int $b, int $c) {}
$args = [1, 2];
test(...$args); // ArgumentCountError
?>
```

## How to Fix

### Fix 1: Provide correct argument count

```php
<?php
function greet(string $name, string $greeting = "Hello"): string {
    return "$greeting, $name!";
}

// Always provide required arguments
echo greet("World"); // "Hello, World!"
echo greet("World", "Hi"); // "Hi, World!"

// Check function signature before calling
$reflection = new ReflectionFunction('strlen');
echo "Required args: " . $reflection->getNumberOfRequiredParameters();
echo "Total args: " . $reflection->getNumberOfParameters();
?>
```

### Fix 2: Use variadic functions for flexible arguments

```php
<?php
// Use variadic parameters to accept any number of arguments
function sum(int ...$numbers): int {
    return array_sum($numbers);
}

echo sum(1, 2);       // 3
echo sum(1, 2, 3, 4); // 10
echo sum();            // 0

// Use union types for optional parameters
function logMessage(string $message, mixed ...$context): void {
    $contextStr = !empty($context) ? ' | ' . implode(', ', $context) : '';
    error_log($message . $contextStr);
}

logMessage("User login", "user_id=123", "ip=192.168.1.1");
?>
```

### Fix 3: Use match to validate and dispatch

```php
<?php
function process(string $type, mixed ...$args): string {
    $count = count($args);
    return match (true) {
        $type === 'string' && $count >= 1 => "Processing string: {$args[0]}",
        $type === 'number' && $count === 1 => "Processing number: {$args[0]}",
        $type === 'pair' && $count === 2 => "Processing pair: {$args[0]}, {$args[1]}",
        default => "Invalid arguments for type '$type'",
    };
}

echo process('string', 'hello');
echo process('pair', 1, 2);
?>
```

## Examples

```php
<?php
// Safe function caller that handles argument count errors
function safeCall(callable $func, array $args = []): mixed {
    try {
        $reflection = new ReflectionFunction($func);
        $required = $reflection->getNumberOfRequiredParameters();
        $total = $reflection->getNumberOfParameters();

        if (count($args) < $required) {
            throw new \ArgumentCountError(
                "Function expects at least $required arguments, " . count($args) . " given"
            );
        }

        return $func(...array_slice($args, 0, $total));
    } catch (\ArgumentCountError $e) {
        error_log("Argument count error: " . $e->getMessage());
        return null;
    }
}

// Usage
$len = safeCall('strlen', ['hello']); // 5
$len = safeCall('strlen');            // null (error logged)
?>
```

## Related Errors

- [PHP TypeError]({{< relref "/languages/php/typeerror" >}}) — type mismatch
- [PHP ValueError]({{< relref "/languages/php/valueerror" >}}) — invalid value
- [PHP Fatal Error]({{< relref "/languages/php/fatal-error" >}}) — fatal error
