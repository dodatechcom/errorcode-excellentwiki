---
title: "[Solution] PHP 8.1 array_is_list() Error — Array Format Incompatible"
description: "Fix PHP 8.1 array_is_list() Error by checking array structure, validating keys, and using array_is_list() correctly. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 310
---

# PHP 8.1 array_is_list() Error — Array Format Incompatible

The array_is_list() Error occurs when using `array_is_list()` incorrectly, passing invalid arguments, or when array structures don't match expectations. PHP 8.1 introduced `array_is_list()` to check if an array is a "list" — an array with sequential integer keys starting at 0.

## Common Causes

```php
<?php
// Cause 1: Passing wrong argument type
result = array_is_list('not an array'); // TypeError

// Cause 2: Confusing associative arrays with lists
$data = ['name' => 'Alice', 'age' => 25];
array_is_list($data); // Returns false — not a sequential numeric list

// Cause 3: Assuming sparse arrays are lists
$data = [0 => 'a', 2 => 'c']; // Missing key 1
array_is_list($data); // Returns false

// Cause 4: Not handling the false case
$json = '{"data": {"0": "a", "1": "b"}}';
$parsed = json_decode($json, true);
// $parsed['data'] may not be a list even if keys are numeric

// Cause 5: Using array_is_list() before PHP 8.1
// array_is_list($arr); // Fatal error on PHP < 8.1
?>
```

## How to Fix

### Fix 1: Validate argument type before calling

```php
<?php
function ensureList(mixed $data): array {
    if (!is_array($data)) {
        throw new TypeError('Expected array, got ' . get_debug_type($data));
    }

    if (!array_is_list($data)) {
        throw new InvalidArgumentException('Expected a list (sequential 0-indexed array)');
    }

    return $data;
}

ensureList([1, 2, 3]);  // OK
ensureList([1, 3, 2]);  // OK (values don't matter, only keys)
ensureList(['a' => 1]); // InvalidArgumentException
?>
```

### Fix 2: Convert non-list arrays to lists when needed

```php
<?php
// Associative array
$data = ['name' => 'Alice', 'age' => 25, 'email' => 'alice@example.com'];

// Convert to list
$list = array_values($data);
array_is_list($list); // true

// Or use json_decode to get a list from JSON
$json = '{"users": [{"id": 1}, {"id": 2}]}';
$parsed = json_decode($json, true);
array_is_list($parsed['users']); // true
?>
```

### Fix 3: Handle both list and non-list cases

```php
<?php
function processItems(mixed $items): void {
    if (!is_array($items)) {
        throw new TypeError('Expected array');
    }

    if (array_is_list($items)) {
        // Process as sequential list
        foreach ($items as $index => $item) {
            echo "[$index] " . print_r($item, true) . "\n";
        }
    } else {
        // Process as associative array
        foreach ($items as $key => $value) {
            echo "$key: " . print_r($value, true) . "\n";
        }
    }
}

processItems(['Alice', 'Bob']);          // List mode
processItems(['name' => 'Alice']);       // Associative mode
?>
```

### Fix 4: Validate JSON-decoded arrays

```php
<?php
function parseJsonList(string $json): array {
    $data = json_decode($json, true);

    if (json_last_error() !== JSON_ERROR_NONE) {
        throw new InvalidArgumentException('Invalid JSON: ' . json_last_error_msg());
    }

    if (!is_array($data) || !array_is_list($data)) {
        throw new InvalidArgumentException('Expected a JSON array (list)');
    }

    return $data;
}

$items = parseJsonList('[1, 2, 3]');
?>
```

## Examples

```php
<?php
// Understanding what makes an array a "list"
$examples = [
    [] => true,                           // Empty array is a list
    [1, 2, 3] => true,                    // Sequential 0-indexed
    ['a', 'b', 'c'] => true,              // Sequential string values
    [0 => 'x', 1 => 'y'] => true,        // Explicit numeric keys
    [0 => 'x', 2 => 'y'] => false,       // Gap in keys
    ['a' => 1] => false,                  // String keys
    [1 => 'a', 2 => 'b'] => false,       // Doesn't start at 0
];

foreach ($examples as $arr => $expected) {
    $result = array_is_list($arr);
    echo var_export($arr, true) . ' => ' . var_export($result, true);
    echo $result === $expected ? " (correct)\n" : " (WRONG)\n";
}

// Practical use: validating API responses
function validateApiResponse(array $response): void {
    if (!isset($response['data']) || !array_is_list($response['data'])) {
        throw new InvalidArgumentException('API must return a list in "data" key');
    }
}
?>
```

## Related Errors

- [PHP 8.0 Union Type Error](/languages/php/php80-union-type-error/) — Type handling in PHP 8.x
- [PHP 8.1 Enum Error](/languages/php/php81-enums/) — PHP 8.1 feature
- [PHP 8.3 json_validate() Error](/languages/php/php83-json-validate/) — JSON validation in PHP 8.3
