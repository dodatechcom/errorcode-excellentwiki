---
title: "[Solution] PHP Warning: Array to String Conversion"
description: "Fix PHP Warning: array to string conversion. Use print_r() or var_export(), check variable type, serialize array."
languages: ["php"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 8
---

# PHP Warning: Array to String Conversion

This warning occurs when an array is used in a context that expects a string, such as `echo`, string concatenation, or interpolation. PHP converts the array to the string literal `"Array"`, which is almost never the intended behavior.

## Common Causes

```php
<?php
// Example 1: Echoing an array directly
$data = ["name" => "Alice", "age" => 30];
echo $data;
// Warning: Array to string conversion
// Output: "Array"
```

```php
<?php
// Example 2: String concatenation with array
$items = ["apple", "banana", "cherry"];
$message = "Items: " . $items;
// Warning: Array to string conversion
```

```php
<?php
// Example 3: Variable interpolation
$user = ["name" => "Bob", "email" => "bob@example.com"];
echo "User: $user";
// Warning: Array to string conversion
```

```php
<?php
// Example 4: Database query returning array when string expected
$result = mysql_query("SELECT * FROM users WHERE id = 1");
$row = mysql_fetch_array($result);
$query = "INSERT INTO logs VALUES ('" . $row . "')";
// Warning: Array to string conversion
```

```php
<?php
// Example 5: json_encode() on nested structure
$config = ["debug" => true, "settings" => ["theme" => "dark"]];
$log = "Config: " . json_encode($config); // This works
// But if someone does:
$log = "Config: " . $config;
// Warning: Array to string conversion
```

## How to Fix

### Fix 1: Use print_r() or var_export() for Debugging

When you want to display array contents for debugging, use the appropriate function.

```php
<?php
$data = ["name" => "Alice", "age" => 30];

// For debugging — outputs human-readable format
print_r($data);

// Or for a string that can be evaluated
echo var_export($data, true);
// Output: ['name' => 'Alice', 'age' => 30]
```

### Fix 2: Check Variable Type Before String Operations

Always verify the variable is a string before using it in a string context.

```php
<?php
$value = getSetting("site_name");

if (is_array($value)) {
    $value = reset($value); // Take first element
}

echo "Site: " . (string) $value;
```

### Fix 3: Use json_encode() for Array-to-String Conversion

When you need to store or transmit an array as a string, serialize it properly.

```php
<?php
$config = ["theme" => "dark", "lang" => "en"];

// Serialize to JSON string
$jsonString = json_encode($config);
echo $jsonString; // {"theme":"dark","lang":"en"}

// Deserialize back
$config = json_decode($jsonString, true);
```

### Fix 4: Use serialize() for PHP-Specific Serialization

For PHP-specific storage (e.g., sessions, caching), use `serialize()`.

```php
<?php
$userData = ["name" => "Alice", "preferences" => ["theme" => "dark"]];

// Serialize for storage
$serialized = serialize($userData);
file_put_contents("/tmp/user_cache.dat", $serialized);

// Later: restore
$cached = file_get_contents("/tmp/user_cache.dat");
$userData = unserialize($cached);
```

### Fix 5: Extract Specific Values from Arrays

When you need a single string value from an array, extract it explicitly.

```php
<?php
$user = ["name" => "Alice", "email" => "alice@example.com"];

// WRONG: echo $user;
// CORRECT: extract the specific value you need
echo "Name: " . $user["name"];
echo "Email: " . $user["email"];

// Or format the entire array as a string
echo sprintf("User: %s (%s)", $user["name"], $user["email"]);
```

## Examples

```php
<?php
// Scenario: Logging user activity
function logActivity(array $user, string $action): void {
    // WRONG: will trigger warning
    // $log = "User " . $user . " performed " . $action;

    // CORRECT: extract specific fields
    $log = sprintf(
        "User %s (ID: %d) performed: %s",
        $user["name"],
        $user["id"],
        $action
    );

    file_put_contents("/var/www/logs/activity.log", $log . "\n", LOCK_EX);
}

logActivity(["id" => 42, "name" => "Alice"], "login");
// Output: User Alice (ID: 42) performed: login
```

## Related Errors

- [PHP Warning: Illegal String Offset](/languages/php/warning-illegal-string-offset)
- [PHP Warning: strlen() Expects String](/languages/php/warning-strlen-expects)
- [PHP Warning: count() Invalid](/languages/php/warning-count-invalid)
