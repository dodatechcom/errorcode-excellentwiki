---
title: "[Solution] PHP Deprecated: each() Function is Deprecated"
description: "Fix PHP Deprecated: each() is deprecated. Use foreach(), current()/next(), or array_key/value functions instead."
languages: ["php"]
severities: ["deprecated"]
error-types: ["runtime-error"]
weight: 106
---

# PHP Deprecated: each() Function is Deprecated

The `each()` function was deprecated in PHP 7.2 and removed in PHP 8.0. It returned the current key-value pair from an array and advanced the internal pointer. Modern PHP provides better alternatives like `foreach` loops and pointer functions.

## Common Causes

```php
// Cause 1: Using each() in a while loop
<?php
$arr = ['a' => 1, 'b' => 2, 'c' => 3];
while (list($key, $value) = each($arr)) {
    echo "{$key}: {$value}\n";
}
// Deprecated: each()
?>
```

```php
// Cause 2: Using each() with internal pointer
<?php
$items = ['x' => 10, 'y' => 20];
$pair = each($items); // Deprecated
echo $pair['key'] . ' => ' . $pair['value'];
?>
```

```php
// Cause 3: Using each() to iterate and modify
<?php
$data = ['a' => 1, 'b' => 2];
while (list($k, $v) = each($data)) {
    $data[$k] = $v * 2;
}
?>
```

```php
// Cause 4: Using each() for first element access
<?php
$config = ['host' => 'localhost', 'port' => 3306];
$first = each($config); // Deprecated
?>
```

## How to Fix

### Fix 1: Replace with foreach()

The most common replacement is converting `while/each` loops to `foreach`.

```php
<?php
// BEFORE (deprecated)
$arr = ['a' => 1, 'b' => 2, 'c' => 3];
while (list($key, $value) = each($arr)) {
    echo "{$key}: {$value}\n";
}

// AFTER (modern)
$arr = ['a' => 1, 'b' => 2, 'c' => 3];
foreach ($arr as $key => $value) {
    echo "{$key}: {$value}\n";
}
?>
```

### Fix 2: Use current(), key(), next() for Pointer Access

If you need direct pointer control, use PHP's pointer functions.

```php
<?php
// BEFORE (deprecated)
$items = ['x' => 10, 'y' => 20];
$pair = each($items);

// AFTER — access first element
$items = ['x' => 10, 'y' => 20];
$key = key($items);
$value = current($items);
echo "{$key}: {$value}"; // x: 10

// Advance pointer manually
next($items);
$key = key($items);
$value = current($items);
echo "{$key}: {$value}"; // y: 20
?>
```

### Fix 3: Use array_keys() and array_values()

Extract keys and values as separate arrays when needed.

```php
<?php
// BEFORE (deprecated)
$colors = ['red' => '#ff0000', 'green' => '#00ff00', 'blue' => '#0000ff'];
while (list($name, $hex) = each($colors)) {
    echo "{$name}: {$hex}\n";
}

// AFTER
$colors = ['red' => '#ff0000', 'green' => '#00ff00', 'blue' => '#0000ff'];

foreach ($colors as $name => $hex) {
    echo "{$name}: {$hex}\n";
}

// Or use array_map for functional style
array_map(function ($name, $hex) {
    echo "{$name}: {$hex}\n";
}, array_keys($colors), array_values($colors));
?>
```

### Fix 4: Use First-Element Helpers for Initial Access

```php
<?php
// BEFORE (deprecated)
$config = ['host' => 'localhost', 'port' => 3306];
$first = each($config);
$firstKey = $first['key'];
$firstValue = $first['value'];

// AFTER — multiple approaches
$config = ['host' => 'localhost', 'port' => 3306];

// Option A: reset() + key()
reset($config);
$firstKey = key($config);
$firstValue = current($config);

// Option B: array_key_first() (PHP 8.1+)
$firstKey = array_key_first($config);
$firstValue = $config[$firstKey];

echo "{$firstKey}: {$firstValue}";
?>
```

## Examples

```php
<?php
// Complete migration examples
// Example 1: Enumerating form data
// BEFORE
while (list($field, $value) = each($_POST)) {
    echo "{$field}: {$value}\n";
}

// AFTER
foreach ($_POST as $field => $value) {
    echo "{$field}: {$value}\n";
}

// Example 2: Finding a value
// BEFORE
$found = false;
while (list($k, $v) = each($users)) {
    if ($v['email'] === $email) {
        $found = true;
        break;
    }
}

// AFTER
$found = false;
foreach ($users as $user) {
    if ($user['email'] === $email) {
        $found = true;
        break;
    }
}

// Example 3: Functional approach
// BEFORE
while (list($k, $v) = each($data)) {
    $data[$k] = strtoupper($v);
}

// AFTER
$data = array_map('strtoupper', $data);
?>
```

```php
<?php
// Safe helper for getting first element
function firstElement(array $array): array
{
    $key = array_key_first($array);
    if ($key === null) {
        return [null, null];
    }
    return [$key, $array[$key]];
}

$config = ['host' => 'localhost', 'port' => 3306];
[$firstKey, $firstValue] = firstElement($config);
echo "{$firstKey}: {$firstValue}";
?>
```

## Related Errors

- [PHP Deprecated: create_function()](/languages/php/warning-deprecated-create-function)
- [PHP Deprecated: mysql_* functions](/languages/php/warning-deprecated-mysql)
- [PHP Deprecated: Implicit Nullable Type](/languages/php/warning-deprecated-nullable)
