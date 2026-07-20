---
title: "[Solution] PHP Warning: implode() — Invalid Separator / Glue Parameter"
description: "Fix PHP Warning: implode() invalid separator. Use string as separator, check for array argument order, validate parameters."
languages: ["php"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 8
---

# PHP Warning: implode() — Invalid Separator / Glue Parameter

This warning occurs when `implode()` receives an invalid glue parameter or incorrect argument order. The function expects the glue (separator) as the first argument and the array as the second. Passing an array as glue or using the deprecated two-argument syntax incorrectly triggers this warning.

## Common Causes

```php
<?php
// Example 1: Reversed parameters
$items = ["a", "b", "c"];
echo implode($items, ", ");
// Warning: implode(): Invalid separator (PHP 7.4+)
```

```php
<?php
// Example 2: Array passed as glue
$glue = [",", " "];
echo implode($glue, ["a", "b"]);
// Warning: implode(): Invalid separator
```

```php
<?php
// Example 3: Null glue
$glue = null;
echo implode($glue, ["a", "b"]);
// Warning: implode(): Passing null to parameter #1 ($separator) of type array|string is deprecated (PHP 8.1+)
```

```php
<?php
// Example 4: Integer passed as glue
echo implode(123, ["a", "b"]);
// Warning: implode(): Invalid separator (implicit int-to-string)
```

```php
<?php
// Example 5: Deprecated syntax with array as first arg (PHP 7.4)
echo implode(["a", "b"], ", ");
// Deprecated in PHP 7.4, error in PHP 8.0
```

## How to Fix

### Fix 1: Use the Correct Parameter Order

Always pass the glue (string) first and the array second.

```php
<?php
$items = ["apple", "banana", "cherry"];

// WRONG: reversed
echo implode($items, ", ");

// CORRECT: glue first, array second
echo implode(", ", $items);
// Output: apple, banana, cherry
```

### Fix 2: Ensure Glue Is a String

Validate the glue parameter before calling `implode()`.

```php
<?php
function safeImplode(array $array, string $glue = ", "): string {
    if (!is_string($glue)) {
        $glue = (string) $glue;
    }
    return implode($glue, $array);
}

$items = ["a", "b", "c"];
echo safeImplode($items, ", "); // a, b, c
echo safeImplode($items);       // a, b, c (default glue)
```

### Fix 3: Use the Null Coalescing Operator

Handle potentially null glue values.

```php
<?php
$separator = getUserSeparator(); // May return null
$items = ["one", "two", "three"];

echo implode($separator ?? ", ", $items);
```

### Fix 4: Validate Before Calling

Check argument types before using `implode()`.

```php
<?php
function joinValues(mixed $glue, mixed $array): string {
    if (!is_string($glue)) {
        $glue = (string) $glue;
    }

    if (!is_array($array)) {
        $array = (array) $array;
    }

    return implode($glue, $array);
}

echo joinValues(", ", ["a", "b"]);     // a, b
echo joinValues(null, ["x", "y"]);     // x, y
echo joinValues(123, ["p", "q"]);      // p, q
```

## Examples

```php
<?php
// Scenario: Building a breadcrumb trail
function buildBreadcrumb(array $segments, string $separator = " / "): string {
    return implode($separator, array_map("htmlspecialchars", $segments));
}

$parts = ["Home", "Products", "Electronics", "Phones"];
echo buildBreadcrumb($parts);
// Output: Home / Products / Electronics / Phones

echo buildBreadcrumb($parts, " > ");
// Output: Home > Products > Electronics > Phones
```

## Related Errors

- [PHP Warning: array_merge() Expects Array](/languages/php/warning-array-merge-requires)
- [PHP Warning: strlen() Expects String](/languages/php/warning-strlen-expects)
- [PHP Warning: sprintf() Too Few Arguments](/languages/php/warning-sprintf-too-few)
