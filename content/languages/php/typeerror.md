---
title: "[Solution] PHP TypeError — Type Mismatch Error"
description: "Fix PHP TypeError by using proper type declarations, casting values, and validating input types."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 58
---

# TypeError — Type Mismatch Error

TypeError is thrown when a function receives an argument of the wrong type, or when a return value doesn't match the declared type. PHP 7.0+ introduced scalar type declarations and return type hints that trigger TypeError instead of warnings.

## Common Causes

```php
<?php
// Cause 1: Passing wrong type to typed parameter
function add(int $a, int $b): int {
    return $a + $b;
}
add("hello", 5); // TypeError: Argument #1 must be of type int, string given

// Cause 2: Return type mismatch
function getNumber(): int {
    return "not a number"; // TypeError
}

// Cause 3: Nullable type violation
function process(string $data): void {
    echo $data;
}
process(null); // TypeError in PHP 7.x (allowed in PHP 8.0+ with nullable)

// Cause 4: Passing wrong type to built-in function
strlen(12345); // TypeError in PHP 8.0+

// Cause 5: Union type violation
function setStatus(string|int $status): void {
    echo $status;
}
setStatus(true); // TypeError: bool not in union type
?>
```

## How to Fix

### Fix 1: Use proper type declarations

```php
<?php
// Declare types clearly and use appropriate types
function add(int|float $a, int|float $b): int|float {
    return $a + $b;
}

// Use union types for multiple accepted types
function processData(string|int $data): string {
    return (string)$data;
}

// Use nullable types when null is valid
function find(int $id): ?array {
    $result = database::find($id);
    return $result ?: null;
}
?>
```

### Fix 2: Cast values before passing

```php
<?php
function add(int $a, int $b): int {
    return $a + $b;
}

// Cast values to match expected types
$userInput = $_GET['value'] ?? '0';
$result = add((int)$userInput, 5);

// Validate before type casting
function processInput(mixed $input): string {
    if (!is_string($input) && !is_int($input)) {
        throw new TypeError("Expected string or int, got " . get_debug_type($input));
    }
    return (string)$input;
}
?>
```

### Fix 3: Use match for type checking

```php
<?php
function process(mixed $value): string {
    return match (get_debug_type($value)) {
        'string' => "String: $value",
        'int' => "Integer: $value",
        'float' => "Float: $value",
        'bool' => $value ? 'true' : 'false',
        default => throw new TypeError("Unsupported type: " . get_debug_type($value)),
    };
}

echo process("hello"); // "String: hello"
echo process(42);      // "Integer: 42"
?>
```

## Examples

```php
<?php
// Handling TypeError in a flexible function
function safeCall(callable $callback, mixed ...$args): mixed {
    try {
        return $callback(...$args);
    } catch (TypeError $e) {
        error_log("Type error calling function: " . $e->getMessage());
        return null;
    }
}

// Using union types for flexibility
function formatValue(string|int|float $value): string {
    return match (get_debug_type($value)) {
        'string' => trim($value),
        'int' => number_format($value),
        'float' => number_format($value, 2),
    };
}
?>
```

## Related Errors

- [PHP ValueError]({{< relref "/languages/php/valueerror" >}}) — invalid value
- [PHP ArgumentCountError]({{< relref "/languages/php/argumentcounterror" >}}) — wrong argument count
- [PHP Fatal Error]({{< relref "/languages/php/fatal-error" >}}) — fatal error
