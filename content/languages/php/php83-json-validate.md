---
title: "[Solution] PHP 8.3 json_validate() Error — Invalid JSON Validation"
description: "Fix PHP 8.3 json_validate() Error by checking JSON syntax, validating data structure, and using proper options. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 313
---

# PHP 8.3 json_validate() Error — Invalid JSON Validation

The json_validate() Error occurs when `json_validate()` is used incorrectly, called with invalid arguments, or when JSON that appears valid is rejected due to structural issues. PHP 8.3 introduced `json_validate()` as a dedicated function to check whether a JSON string is syntactically valid without decoding it.

## Common Causes

```php
<?php
// Cause 1: Wrong argument type
json_validate(123); // TypeError — expects string

// Cause 2: Assuming json_validate() returns decoded data
$valid = json_validate('{"name": "Alice"}');
echo $valid->name; // Error — json_validate returns bool, not array

// Cause 3: Confusing validation with parsing
$json = '{"name": "Alice", "age": 25}';
if (json_validate($json)) {
    // JSON is valid, but you still need to decode it
    $data = json_decode($json, true); // Don't forget this step
}

// Cause 4: Using json_validate() before PHP 8.3
// json_validate('[]'); // Fatal error on PHP < 8.3

// Cause 5: Not handling edge cases with depth and flags
$json = str_repeat('{"a":', 1000) . '1' . str_repeat('}', 1000);
json_validate($json); // May fail with depth limit
?>
```

## How to Fix

### Fix 1: Always pass a string argument

```php
<?php
function safeJsonValidate(mixed $input): bool {
    if (!is_string($input)) {
        return false;
    }
    return json_validate($input);
}

echo safeJsonValidate('{"key": "value"}'); // true
echo safeJsonValidate(123);                // false
echo safeJsonValidate(null);               // false
?>
```

### Fix 2: Use json_validate() then json_decode() for two-step validation

```php
<?php
function parseJson(string $json): array {
    if (!json_validate($json)) {
        throw new InvalidArgumentException(
            'Invalid JSON: ' . json_last_error_msg()
        );
    }

    $data = json_decode($json, true);

    if (!is_array($data)) {
        throw new RuntimeException('JSON did not decode to array');
    }

    return $data;
}

// Usage
try {
    $data = parseJson('{"users": [{"name": "Alice"}]}');
    echo $data['users'][0]['name']; // Alice
} catch (InvalidArgumentException $e) {
    echo "JSON error: " . $e->getMessage();
}
?>
```

### Fix 3: Use options for strict validation

```php
<?php
$json = '{"name": "Alice", "age": 25}';

// Basic validation
$valid = json_validate($json);

// With depth limit (default is 512)
$valid = json_validate($json, depth: 512);

// Check for specific JSON types
function validateJsonStructure(string $json, array $requiredKeys): bool {
    if (!json_validate($json)) {
        return false;
    }

    $data = json_decode($json, true);
    if (!is_array($data)) {
        return false;
    }

    foreach ($requiredKeys as $key) {
        if (!array_key_exists($key, $data)) {
            return false;
        }
    }

    return true;
}

$valid = validateJsonStructure($json, ['name', 'age']);
?>
```

### Fix 4: Handle edge cases gracefully

```php
<?php
function robustJsonCheck(string $input): array {
    $result = [
        'valid' => json_validate($input),
        'error' => null,
        'data' => null,
    ];

    if (!$result['valid']) {
        $result['error'] = json_last_error_msg();
        return $result;
    }

    $result['data'] = json_decode($input, true, 512, JSON_THROW_ON_ERROR);
    return $result;
}

// Empty string
echo robustJsonCheck('')->valid ? 'valid' : 'invalid'; // invalid

// Empty object
echo robustJsonCheck('{}')->valid ? 'valid' : 'invalid'; // valid

// Deeply nested
$deep = json_encode(['level' => ['level' => ['level' => 1]]]);
echo robustJsonCheck($deep)->valid ? 'valid' : 'invalid'; // valid
?>
```

## Examples

```php
<?php
// Practical use cases for json_validate()
class ApiRequest {
    public static function validateBody(string $body, array $schema): bool {
        if (!json_validate($body)) {
            return false;
        }

        $data = json_decode($body, true);
        return self::matchesSchema($data, $schema);
    }

    private static function matchesSchema(array $data, array $schema): bool {
        foreach ($schema as $key => $type) {
            if (!array_key_exists($key, $data)) {
                return false;
            }
            if (get_debug_type($data[$key]) !== $type) {
                return false;
            }
        }
        return true;
    }
}

$body = '{"name": "Alice", "age": 25}';
$schema = ['name' => 'string', 'age' => 'integer'];
echo ApiRequest::validateBody($body, $schema) ? 'valid' : 'invalid'; // valid

// Using json_validate() for config file checking
function checkConfigFile(string $path): void {
    $content = file_get_contents($path);

    if ($content === false) {
        throw new RuntimeException("Cannot read file: $path");
    }

    if (!json_validate($content)) {
        throw new InvalidArgumentException(
            "Invalid JSON in config file: " . json_last_error_msg()
        );
    }

    echo "Config file is valid JSON\n";
}
?>
```

## Related Errors

- [PHP 8.1 array_is_list() Error](/languages/php/php81-array-is-list/) — Array validation
- [PHP 8.0 Match Expression Error](/languages/php/php80-match-expression/) — Control flow errors
- [PHP 8.4 Property Hook Error](/languages/php/php84-property-hooks/) — PHP 8.4 features
