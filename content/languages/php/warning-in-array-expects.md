---
title: "[Solution] PHP Warning: in_array() Expects Parameter 2 to Be Array"
description: "Fix PHP Warning: in_array() expects parameter 2 to be array. Pass an array as the second argument, validate input type, check variable type."
languages: ["php"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 8
---

# PHP Warning: in_array() Expects Parameter 2 to Be Array

This warning occurs when `in_array()` receives a non-array value as its second parameter. The function requires an array to search within, and passing `null`, a string, or any other scalar type triggers this warning.

## Common Causes

```php
<?php
// Example 1: Variable is null instead of array
$haystack = null;
$found = in_array("needle", $haystack);
// Warning: in_array() expects parameter 2 to be array, null given
```

```php
<?php
// Example 2: Function returns non-array
$result = someDatabaseQuery();
$found = in_array("value", $result);
// Warning: in_array() expects parameter 2 to be array, string given
```

```php
<?php
// Example 3: Variable accidentally reassigned
$items = ["a", "b", "c"];
$items = $items[0]; // Now it's a string "a"
$found = in_array("b", $items);
// Warning: in_array() expects parameter 2 to be array, string given
```

```php
<?php
// Example 4: JSON decode returning non-array
$json = '"not_an_array"';
$data = json_decode($json);
$found = in_array("value", $data);
// Warning: in_array() expects parameter 2 to be array, string given
```

```php
<?php
// Example 5: Filtered array result
$data = array_filter([1, 2, 3, null, 5]);
$found = in_array(4, $data); // Works — array_filter returns array
// But if $data is reassigned incorrectly, this can fail
```

## How to Fix

### Fix 1: Pass an Array as the Second Argument

Always ensure the haystack is actually an array.

```php
<?php
$haystack = ["apple", "banana", "cherry"];
$found = in_array("banana", $haystack); // true
```

### Fix 2: Validate Input Type Before Calling

Check the variable type before passing it to `in_array()`.

```php
<?php
function safeInArray(mixed $needle, mixed $haystack, bool $strict = false): bool {
    if (!is_array($haystack)) {
        return false;
    }
    return in_array($needle, $haystack, $strict);
}

$data = getExternalData(); // Might return null, string, etc.
$found = safeInArray("value", $data);
```

### Fix 3: Use the Null Coalescing Operator

Provide a default empty array when the variable might be null.

```php
<?php
$items = getItemsFromDatabase(); // May return null
$found = in_array("needle", $items ?? []);
```

### Fix 4: Cast to Array When Appropriate

If the value could be a single item or an array, normalize it.

```php
<?php
$value = getSetting("allowed_types"); // Might return string or array

// Normalize to array
$allowedTypes = is_array($value) ? $value : [$value];

$found = in_array("jpg", $allowedTypes);
```

## Examples

```php
<?php
// Scenario: Checking user permissions
function hasPermission(string $permission, array|null $userPermissions): bool {
    if (!is_array($userPermissions)) {
        return false;
    }
    return in_array($permission, $userPermissions, true);
}

// Works with array
echo hasPermission("edit", ["read", "write", "edit"]); // true

// Works with null
echo hasPermission("edit", null); // false — no warning
```

## Related Errors

- [PHP Warning: array_merge() Expects Array](/languages/php/warning-array-merge-requires)
- [PHP Warning: count() Invalid](/languages/php/warning-count-invalid)
- [PHP Warning: foreach() Cannot Iterate](/languages/php/warning-foreach-cannot-iterate)
