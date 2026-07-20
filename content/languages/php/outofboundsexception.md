---
title: "[Solution] PHP OutOfBoundsException — Index or Key Out of Range"
description: "Fix PHP OutOfBoundsException by checking array bounds, validating key existence, and using isset()/array_key_exists()."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# OutOfBoundsException — Index or Key Out of Range

This exception is thrown when an index or key is outside the valid range of a data structure. It commonly occurs when accessing array elements, string characters, or collection items using an index that does not exist or is beyond the valid boundaries.

## Common Causes

- Accessing an array index that does not exist
- Using a negative index where only positive values are valid
- Accessing a string position beyond its length
- Key not found in a keyed collection or data structure

## How to Fix

### Fix 1: Check Array Bounds Before Access

Validate that the index is within the valid range before accessing.

```php
<?php
function getElement(array $items, int $index)
{
    if ($index < 0 || $index >= count($items)) {
        throw new OutOfBoundsException(
            "Index $index is out of range. Valid: 0-" . (count($items) - 1)
        );
    }
    return $items[$index];
}
?>
```

### Fix 2: Use isset() or array_key_exists() for Key Validation

Check if a key exists before accessing the value.

```php
<?php
function getValue(array $data, string $key)
{
    if (!array_key_exists($key, $data)) {
        throw new OutOfBoundsException("Key '$key' does not exist in array");
    }
    return $data[$key];
}
?>
```

### Fix 3: Validate String Position Bounds

Check string length before accessing character positions.

```php
<?php
function getChar(string $str, int $position): string
{
    if ($position < 0 || $position >= strlen($str)) {
        throw new OutOfBoundsException(
            "Position $position is out of range for string of length " . strlen($str)
        );
    }
    return $str[$position];
}
?>
```

### Fix 4: Use Safe Access Patterns

Wrap access in try-catch or use safe defaults.

```php
<?php
function safeGet(array $items, int $index, $default = null)
{
    try {
        if (!isset($items[$index])) {
            throw new OutOfBoundsException("Index $index not found");
        }
        return $items[$index];
    } catch (OutOfBoundsException $e) {
        error_log($e->getMessage());
        return $default;
    }
}
?>
```

## Examples

```php
<?php
// Example 1: Array index out of bounds
$colors = ['red', 'green', 'blue'];
echo $colors[5];
// OutOfBoundsException or undefined offset warning
// Fix: check $index < count($colors)

// Example 2: Key not found in associative array
$users = ['alice' => 1, 'bob' => 2];
echo $users['charlie'];
// OutOfBoundsException: Key 'charlie' not found
// Fix: use array_key_exists('charlie', $users)

// Example 3: String position out of range
$str = 'hello';
echo $str[10];
// OutOfBoundsException or undefined offset
// Fix: check $position < strlen($str)
?>
```

## Related Errors

- [PHP OutOfRangeException]({{< relref "/languages/php/outofrangeexception" >}})
- [PHP Undefined array key]({{< relref "/languages/php/undefined-index" >}})
- [PHP LengthException]({{< relref "/languages/php/lengthexception" >}})
