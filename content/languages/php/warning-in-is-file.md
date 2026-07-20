---
title: "PHP Warning: is_file() / is_dir() / file_exists() invalid type"
description: "Fix PHP Warning: is_file, is_dir, and file_exists invalid type. Learn to cast to string, check variable type, and handle null values."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: is_file() / is_dir() / file_exists() invalid type

This warning occurs when functions like `is_file()`, `is_dir()`, or `file_exists()` receive a non-string argument. These functions expect a valid path string.

## Common Causes

- Passing null or uninitialized variables
- Passing boolean or integer values
- Variable type is not a string

## How to Fix

### Cast to String

```php
<?php
// Wrong — passing null or integer
$result = is_file($path);

// Correct — cast to string
$result = is_file((string) $path);
?>
```

### Check Variable Type

```php
<?php
// Wrong — non-string value
$result = is_file($path);

// Correct — type check
if (is_string($path)) {
    $result = is_file($path);
} else {
    $result = false;
}
?>
```

### Handle Null Values

```php
<?php
// Wrong — null causes warning
$result = file_exists($path);

// Correct — null coalescing
$path = $path ?? '';
$result = file_exists($path);
?>
```

## Examples

```php
<?php
// This triggers the warning
$path = null;
$result = is_file($path);
// Warning: is_file() expects parameter 1 to be string, null given

// Correct
$result = is_file($path ?? '');
$path = '/etc/passwd';
$result = is_file($path); // true
?>
```

## Related Errors

- [PHP Warning: move_uploaded_file()]({{< relref "/languages/php/warning-in-move-uploaded-file" >}})
- [PHP Warning: fopen() failed]({{< relref "/languages/php/warning-fopen-failed" >}})
- [PHP Warning: file_put_contents() failed]({{< relref "/languages/php/warning-file-put-contents-failed" >}})
