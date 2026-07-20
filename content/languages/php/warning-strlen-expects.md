---
title: "[Solution] PHP Warning: strlen() Expects Parameter 1 to Be String"
description: "Fix PHP Warning: strlen() expects parameter 1 to be string. Cast to string, check type, use mb_strlen() for multibyte strings."
languages: ["php"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 8
---

# PHP Warning: strlen() Expects Parameter 1 to Be String

This warning occurs when `strlen()` receives a non-string value. The function expects exactly one string parameter and returns its byte length. Passing `null`, an array, or an object triggers this warning.

## Common Causes

```php
<?php
// Example 1: Passing null to strlen()
$value = null;
echo strlen($value);
// Warning: strlen(): Passing null to parameter #1 ($string) of type string is deprecated (PHP 8.1+)
```

```php
<?php
// Example 2: Passing an array
$data = [1, 2, 3];
echo strlen($data);
// Warning: strlen(): Passing null to parameter #1 ($string) of type string is deprecated
```

```php
<?php
// Example 3: Function returns non-string
$result = json_decode('{"key": null}', true);
$value = $result["key"]; // null
echo strlen($value);
// Warning: strlen(): Passing null to parameter #1 is deprecated
```

```php
<?php
// Example 4: Boolean value
$flag = true;
echo strlen($flag);
// Warning: strlen(): Passing null to parameter #1 is deprecated
```

```php
<?php
// Example 5: Integer from database
$count = 0;
echo strlen($count);
// Warning: strlen(): Passing null to parameter #1 is deprecated
```

## How to Fix

### Fix 1: Cast to String Before Calling

Ensure the value is a string before passing it to `strlen()`.

```php
<?php
$value = getExternalData(); // May be null, int, etc.

// Cast to string
echo strlen((string) $value);
```

### Fix 2: Use the Null Coalescing Operator

Provide a default empty string for potentially null values.

```php
<?php
$value = getDataFromDatabase(); // May return null
echo strlen($value ?? "");
```

### Fix 3: Use mb_strlen() for Multibyte Strings

For UTF-8 and multibyte strings, `mb_strlen()` is more appropriate and handles null safely with a default.

```php
<?php
$value = "café"; // 4 characters, 5 bytes

echo strlen($value);    // 5 (byte count)
echo mb_strlen($value, "UTF-8"); // 4 (character count)

// mb_strlen handles null with a deprecation warning in PHP 8.1+
$value = null;
echo mb_strlen($value ?? "", "UTF-8"); // 0
```

### Fix 4: Create a Safe Wrapper Function

Centralize string length checking with type safety.

```php
<?php
function safeStrlen(mixed $value): int {
    if ($value === null) {
        return 0;
    }
    return strlen((string) $value);
}

echo safeStrlen(null);    // 0
echo safeStrlen("hello"); // 5
echo safeStrlen(12345);   // 5
```

### Fix 5: Validate Input Type in Functions

When writing functions that accept strings, use type declarations.

```php
<?php
function processString(string $value): int {
    return strlen($value);
}

// This will throw a TypeError instead of a warning
// processString(null); // TypeError
processString("hello"); // 5
```

## Examples

```php
<?php
// Scenario: Validating input length
function validateUsername(mixed $username): bool {
    $length = strlen((string) ($username ?? ""));
    return $length >= 3 && $length <= 20;
}

echo validateUsername("alice");   // true
echo validateUsername(null);      // false
echo validateUsername("ab");      // false
```

## Related Errors

- [PHP Warning: strpos() Empty Needle](/languages/php/warning-strpos-not-found)
- [PHP Warning: count() Invalid](/languages/php/warning-count-invalid)
- [PHP Warning: Illegal String Offset](/languages/php/warning-illegal-string-offset)
