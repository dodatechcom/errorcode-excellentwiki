---
title: "[Solution] PHP Warning: array_merge() Expects Parameter 1 to Be Array"
description: "Fix PHP Warning: array_merge() expects parameter 1 to be array. Ensure arguments are arrays, cast to array, validate input."
languages: ["php"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 8
---

# PHP Warning: array_merge() Expects Parameter 1 to Be Array

This warning occurs when `array_merge()` receives a non-array value as one of its parameters. All arguments passed to `array_merge()` must be arrays; passing `null`, a string, or any other scalar type triggers this warning.

## Common Causes

```php
<?php
// Example 1: First parameter is null
$defaults = null;
$userConfig = ["theme" => "dark"];
$merged = array_merge($defaults, $userConfig);
// Warning: array_merge(): Argument #1 ($array1) must be of type array, null given
```

```php
<?php
// Example 2: Function returns non-array
$extras = getSettings(); // Returns string instead of array
$merged = array_merge(["base" => true], $extras);
// Warning: array_merge(): Argument #1 must be of type array, string given
```

```php
<?php
// Example 3: Variable reassigned to scalar
$config = ["debug" => false];
$config = $config["debug"]; // Now it's false
$merged = array_merge($config, ["verbose" => true]);
// Warning: array_merge(): Argument #1 must be of type array, bool given
```

```php
<?php
// Example 4: json_decode returning non-array
$json = '{"key": "value"}';
$data = json_decode($json);
$merged = array_merge(["extra" => true], $data);
// Warning: array_merge(): Argument #1 must be of type array, stdClass given
```

```php
<?php
// Example 5: Nested merge with non-array value
$base = ["a" => 1];
$overrides = "not_an_array";
$merged = array_merge($base, $overrides);
// Warning: array_merge(): Argument #2 must be of type array, string given
```

## How to Fix

### Fix 1: Ensure All Arguments Are Arrays

Validate or cast every argument before merging.

```php
<?php
$defaults = ["theme" => "light", "lang" => "en"];
$userConfig = getUserSettings(); // May not be array

// Cast to array if needed
$userConfig = is_array($userConfig) ? $userConfig : [];
$merged = array_merge($defaults, $userConfig);
```

### Fix 2: Use the Null Coalescing Operator

Provide a default empty array for potentially null values.

```php
<?php
$base = getBaseConfig() ?? [];
$overrides = getOverrides() ?? [];
$merged = array_merge($base, $overrides);
```

### Fix 3: Create a Safe Wrapper Function

Centralize the merge logic with type checking.

```php
<?php
function safeArrayMerge(array ...$arrays): array {
    $result = [];
    foreach ($arrays as $index => $item) {
        if (!is_array($item)) {
            trigger_error(
                "array_merge(): Argument #" . ($index + 1) . " must be of type array, " . gettype($item) . " given",
                E_USER_WARNING
            );
            continue;
        }
        $result = array_merge($result, $item);
    }
    return $result;
}

$merged = safeArrayMerge($data1, $data2, $data3);
```

### Fix 4: Use Array Union Operator for Associative Arrays

For associative arrays, the `+` operator is an alternative that does not require type checking.

```php
<?php
$defaults = ["theme" => "light", "lang" => "en"];
$overrides = ["theme" => "dark"];

// + operator works with arrays only, but is more concise
$merged = $defaults + $overrides;
// Result: ["theme" => "dark", "lang" => "en"]
```

## Examples

```php
<?php
// Scenario: Merging configuration layers
function loadConfig(): array {
    $system = ["debug" => false, "log_level" => "info"];
    $file = json_decode(file_get_contents("config.json"), true) ?? [];
    $env = $_ENV["APP_CONFIG"] ?? [];

    // All values are guaranteed to be arrays or empty arrays
    return array_merge($system, $file, is_array($env) ? $env : []);
}

$config = loadConfig();
```

## Related Errors

- [PHP Warning: in_array() Expects Array](/languages/php/warning-in-array-expects)
- [PHP Warning: count() Invalid](/languages/php/warning-count-invalid)
- [PHP Warning: array_key_exists()](/languages/php/array-key-exists)
