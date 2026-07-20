---
title: "[Solution] PHP Notice: Undefined Array Key — Accessing Non-existent Key"
description: "Fix PHP Notice: Undefined array key. Use isset(), null coalescing ??, array_key_exists() to safely access array keys."
languages: ["php"]
severities: ["notice"]
error-types: ["runtime-error"]
weight: 105
---

# PHP Notice: Undefined Array Key — Accessing Non-existent Key

This notice occurs when you access an array element using a key that does not exist. PHP returns `null` for the missing key and emits a notice. In PHP 8.0+, this was upgraded from a notice to a warning. It is commonly triggered by form data, API responses, or configuration arrays.

## Common Causes

```php
// Cause 1: Accessing a key that does not exist
<?php
$config = ['host' => 'localhost', 'port' => 3306];
echo $config['password']; // Notice: Undefined array key "password"
?>
```

```php
// Cause 2: Uninitialized array
<?php
$data = [];
echo $data['name']; // Notice: Undefined array key "name"
?>
```

```php
// Cause 3: Missing superglobal key from form submission
<?php
$email = $_POST['email']; // Notice if form not submitted via POST
?>
```

```php
// Cause 4: Array from explode or split with missing element
<?php
$parts = explode(",", "one,two,three");
echo $parts[5]; // Notice: Undefined array key 5
?>
```

```php
// Cause 5: Foreach on modified array during iteration
<?php
$items = [1, 2, 3, 4, 5];
foreach ($items as $index => $value) {
    if ($value === 3) {
        unset($items[$index]); // Can cause notices on next access
    }
}
?>
```

## How to Fix

### Fix 1: Use isset() Before Accessing

Check whether the key exists before reading its value.

```php
<?php
$config = ['host' => 'localhost', 'port' => 3306];

if (isset($config['password'])) {
    $password = $config['password'];
} else {
    $password = ''; // Default value
}

echo $password;
?>
```

### Fix 2: Use the Null Coalescing Operator

The `??` operator provides a default value when a key is missing.

```php
<?php
$config = ['host' => 'localhost', 'port' => 3306];

// Provide defaults for all expected keys
$host = $config['host'] ?? 'localhost';
$port = $config['port'] ?? 3306;
$password = $config['password'] ?? '';
$charset = $config['charset'] ?? 'utf8mb4';

echo "{$host}:{$port} ({$charset})";
?>
```

### Fix 3: Use array_key_exists() for Null Values

Use `array_key_exists()` when the value might legitimately be `null`.

```php
<?php
$data = ['name' => 'Alice', 'email' => null];

// isset() returns false for null values — but the key exists
if (array_key_exists('email', $data)) {
    echo "Email key exists: " . var_export($data['email'], true);
} else {
    echo "Email key does not exist";
}
?>
```

### Fix 4: Validate Superglobal Access

Always use the null coalescing operator for superglobal arrays.

```php
<?php
// Safe access to $_GET and $_POST
$page = $_GET['page'] ?? 'home';
$sort = $_GET['sort'] ?? 'asc';
$pageNum = isset($_GET['p']) ? (int) $_GET['p'] : 1;

// Safe access to $_SERVER
$ip = $_SERVER['REMOTE_ADDR'] ?? '0.0.0.0';
$referer = $_SERVER['HTTP_REFERER'] ?? '';

echo "Page: {$page}, IP: {$ip}";
?>
```

### Fix 5: Use a Helper Function for Nested Access

Handle deeply nested arrays safely.

```php
<?php
function arrayGet(array $array, string $key, mixed $default = null): mixed
{
    return $array[$key] ?? $default;
}

function arrayGetNested(array $array, string $path, mixed $default = null): mixed
{
    $keys = explode('.', $path);
    $current = $array;

    foreach ($keys as $key) {
        if (!is_array($current) || !array_key_exists($key, $current)) {
            return $default;
        }
        $current = $current[$key];
    }

    return $current;
}

$data = ['user' => ['profile' => ['name' => 'Alice']]];

$name = arrayGetNested($data, 'user.profile.name', 'Unknown');
$bio = arrayGetNested($data, 'user.profile.bio', 'No bio');
?>
```

## Examples

```php
<?php
// Complete safe array access pattern
function processUserData(array $rawData): array
{
    $name = trim($rawData['name'] ?? '');
    $email = filter_var($rawData['email'] ?? '', FILTER_SANITIZE_EMAIL);
    $age = isset($rawData['age']) ? (int) $rawData['age'] : null;
    $preferences = $rawData['preferences'] ?? [];

    $theme = $preferences['theme'] ?? 'light';
    $notifications = $preferences['notifications'] ?? true;

    return [
        'name'  => $name,
        'email' => $email,
        'age'   => $age,
        'theme' => $theme,
        'notifications' => $notifications,
    ];
}

$raw = ['name' => 'Alice', 'email' => 'alice@example.com'];
$user = processUserData($raw);
print_r($user);
?>
```

```php
<?php
// Safe array access with validation
function getInput(string $key, callable $validator, mixed $default = null): mixed
{
    $value = $_REQUEST[$key] ?? $default;

    if ($validator($value)) {
        return $value;
    }

    return $default;
}

$username = getInput('username', function ($v) {
    return is_string($v) && strlen($v) >= 3;
}, 'guest');

echo "Hello, {$username}";
?>
```

## Related Errors

- [PHP Notice: Undefined Index](/languages/php/notice-undefined-index)
- [PHP Notice: Undefined Variable](/languages/php/notice-undefined-variable)
- [PHP Warning: Undefined Array Key](/languages/php/warning-undefined-array-key)
