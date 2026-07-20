---
title: "[Solution] PHP Warning: foreach() — Argument Must Be of Type array|object"
description: "Fix PHP Warning: foreach() argument must be of type array|object. Check variable type, cast to array, validate before loop."
languages: ["php"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 8
---

# PHP Warning: foreach() — Argument Must Be of Type array|object

This warning occurs when `foreach` is used on a variable that is not an array or an object implementing `Traversable`. PHP cannot iterate over scalar values, `null`, or non-iterable types.

## Common Causes

```php
<?php
// Example 1: Variable is null
$data = null;
foreach ($data as $item) {
    echo $item;
}
// Warning: foreach() argument must be of type array|object, null given
```

```php
<?php
// Example 2: Function returns non-array
$result = databaseQuery(); // Returns string on error
foreach ($result as $row) {
    // Warning: foreach() argument must be of type array|object
}
```

```php
<?php
// Example 3: Boolean value
$flag = false;
foreach ($flag as $value) {
    // Warning: foreach() argument must be of type array|object
}
```

```php
<?php
// Example 4: Integer value
$count = 5;
foreach ($count as $num) {
    // Warning: foreach() argument must be of type array|object
}
```

```php
<?php
// Example 5: JSON decode returning object when array expected
$json = '{"name": "Alice"}';
$data = json_decode($json); // stdClass, not array
foreach ($data as $key => $value) {
    // Works for objects, but if json_decode returns null
}
$json = "invalid";
$data = json_decode($json); // null
foreach ($data as $item) {
    // Warning: foreach() argument must be of type array|object, null given
}
```

## How to Fix

### Fix 1: Check Variable Type Before Iterating

Always verify the variable is iterable before using `foreach`.

```php
<?php
$data = getExternalData();

if (is_array($data)) {
    foreach ($data as $item) {
        echo $item;
    }
}
```

### Fix 2: Use the Null Coalescing Operator

Provide a default empty array for potentially null values.

```php
<?php
$data = getItems(); // May return null

foreach ($data ?? [] as $item) {
    echo $item;
}
```

### Fix 3: Cast to Array When Safe

If the variable could be a scalar, cast it to an array.

```php
<?php
$value = getSetting("tags"); // May return string or array

// Normalize to array
$tags = is_array($value) ? $value : [$value];

foreach ($tags as $tag) {
    echo $tag . "\n";
}
```

### Fix 4: Handle JSON Decode Results Safely

Always check the result of `json_decode()` before iterating.

```php
<?php
$json = getUserInput();
$data = json_decode($json, true);

if (!is_array($data)) {
    $data = [];
}

foreach ($data as $key => $value) {
    echo "{$key}: {$value}\n";
}
```

### Fix 5: Use Traversable Check for Objects

Check if an object implements `Traversable` before iterating.

```php
<?php
function processItems(mixed $items): void {
    if (is_array($items)) {
        foreach ($items as $item) {
            echo $item . "\n";
        }
    } elseif ($items instanceof Traversable) {
        foreach ($items as $item) {
            echo $item . "\n";
        }
    }
}
```

## Examples

```php
<?php
// Scenario: Processing user-submitted tags
function processTags(mixed $input): array {
    $tags = [];

    $data = is_array($input) ? $input : [];

    foreach ($data as $tag) {
        $tag = trim((string) $tag);
        if (!empty($tag)) {
            $tags[] = $tag;
        }
    }

    return $tags;
}

$tags = processTags($_POST["tags"] ?? null);
echo "Tags: " . implode(", ", $tags);
```

## Related Errors

- [PHP Warning: count() Invalid](/languages/php/warning-count-invalid)
- [PHP Warning: in_array() Expects Array](/languages/php/warning-in-array-expects)
- [PHP Notice: Undefined Variable](/languages/php/notice-undefined-variable)
