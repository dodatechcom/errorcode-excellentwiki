---
title: "PHP array_key_exists(): Argument #2 must be of type array"
description: "Fix PHP array_key_exists() type error. Learn why Argument #2 must be an array and how to resolve this type mismatch."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["array-key-exists", "type-error", "argument", "array", "fatal-error"]
weight: 5
---

# PHP array_key_exists(): Argument #2 must be of type array

This error occurs when `array_key_exists()` receives a value that is not an array as its second argument. In PHP 7.4, this was a warning; in PHP 8.0+, it throws a `TypeError`.

## Common Causes

- Variable is null, false, or an object instead of an array
- Function returns a non-array value that is passed directly to `array_key_exists()`
- Array was overwritten with a non-array value elsewhere in the code
- Using `array_key_exists()` on an object (use `property_exists()` instead)

## How to Fix

### Verify Variable is an Array

```php
<?php
$key = 'name';
if (is_array($data) && array_key_exists($key, $data)) {
    echo $data[$key];
}
?>
```

### Use isset() as Alternative

```php
<?php
// isset() returns false for null values, but is faster
if (isset($data[$key])) {
    echo $data[$key];
}
?>
```

### Cast to Array if Safe

```php
<?php
$result = getSomething();
$arr = (array) $result;
if (array_key_exists('key', $arr)) {
    // key exists
}
?>
```

### Handle Object Properties Separately

```php
<?php
$obj = new stdClass();
if (is_object($obj)) {
    echo property_exists($obj, 'key') ? $obj->key : 'not found';
}
?>
```

## Examples

```php
<?php
// Example 1: Null value
$data = null;
array_key_exists('name', $data);
// TypeError: array_key_exists(): Argument #2 ($array) must be of type array, null given
// Fix: if (is_array($data) && array_key_exists('name', $data))

// Example 2: Boolean value
$result = false;
array_key_exists('key', $result);
// TypeError: Argument #2 must be of type array, bool given
// Fix: cast to array or check type first

// Example 3: Object instead of array
$resp = json_decode('{"key": "value"}');
array_key_exists('key', $resp);
// TypeError: Argument #2 must be of type array, stdClass given
// Fix: use property_exists($resp, 'key') or json_decode($json, true)
?>
```

## Related Errors

- [PHP Undefined Array Key]({{< relref "/languages/php/undefined-index" >}})
- [PHP Notice: Undefined Variable]({{< relref "/languages/php/notice-undefined-variable" >}})
- [PHP Warning: Trying to get property of non-object]({{< relref "/languages/php/trying-to-get-property" >}})
