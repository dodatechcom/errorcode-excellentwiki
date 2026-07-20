---
title: "[Solution] PHP Deprecated: FILTER_SANITIZE_STRING Constant"
description: "Fix PHP Deprecated: FILTER_SANITIZE_STRING. Use htmlspecialchars() or filter_var() with FILTER_SANITIZE_FULL_SPECIAL_CHARS instead."
languages: ["php"]
severities: ["deprecated"]
error-types: ["runtime-error"]
weight: 109
---

# PHP Deprecated: FILTER_SANITIZE_STRING Constant

The `FILTER_SANITIZE_STRING` constant was deprecated in PHP 8.1 and removed in PHP 8.2. It was commonly used to strip tags and encode special characters from user input. Use `htmlspecialchars()` or `FILTER_SANITIZE_FULL_SPECIAL_CHARS` instead.

## Common Causes

```php
// Cause 1: Using FILTER_SANITIZE_STRING with filter_var
<?php
$clean = filter_var($_POST['name'], FILTER_SANITIZE_STRING);
// Deprecated in PHP 8.1+
?>
```

```php
// Cause 2: Using FILTER_SANITIZE_STRING in filter input
<?php
$name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
// Deprecated in PHP 8.1+
?>
```

```php
// Cause 3: Using FILTER_SANITIZE_STRING in a filter array
<?php
$filters = [
    'name'  => FILTER_SANITIZE_STRING,
    'email' => FILTER_SANITIZE_EMAIL,
];
$data = filter_input_array(INPUT_POST, $filters);
?>
```

```php
// Cause 4: Using it for HTML output escaping
<?php
$userInput = '<script>alert("XSS")</script>';
$safe = filter_var($userInput, FILTER_SANITIZE_STRING);
echo $safe; // Was used as XSS prevention — insufficient anyway
?>
```

## How to Fix

### Fix 1: Use htmlspecialchars() for HTML Output

The recommended replacement for most use cases is `htmlspecialchars()`.

```php
<?php
// BEFORE (deprecated)
$clean = filter_var($_POST['name'], FILTER_SANITIZE_STRING);

// AFTER — htmlspecialchars
$name = htmlspecialchars($_POST['name'] ?? '', ENT_QUOTES, 'UTF-8');
echo $name;
?>
```

### Fix 2: Use FILTER_SANITIZE_FULL_SPECIAL_CHARS

This filter is a direct replacement that encodes special characters.

```php
<?php
// BEFORE (deprecated)
$clean = filter_var($input, FILTER_SANITIZE_STRING);

// AFTER — FILTER_SANITIZE_FULL_SPECIAL_CHARS
$clean = filter_var($input, FILTER_SANITIZE_FULL_SPECIAL_CHARS);

// With filter_input
$name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_FULL_SPECIAL_CHARS);
?>
```

### Fix 3: Create a Sanitization Helper Function

Centralize your sanitization logic to make future migrations easier.

```php
<?php
function sanitizeString(string $input): string
{
    return htmlspecialchars($input, ENT_QUOTES, 'UTF-8');
}

function sanitizeArray(array $data): array
{
    return array_map(function ($value) {
        if (is_string($value)) {
            return htmlspecialchars($value, ENT_QUOTES, 'UTF-8');
        }
        if (is_array($value)) {
            return sanitizeArray($value);
        }
        return $value;
    }, $data);
}

// Usage
$cleanName = sanitizeString($_POST['name'] ?? '');
$cleanData = sanitizeArray($_POST);
?>
```

### Fix 4: Use Multiple Filters for Different Needs

Different sanitization needs require different approaches.

```php
<?php
// For HTML output escaping
$name = htmlspecialchars($raw, ENT_QUOTES, 'UTF-8');

// For email
$email = filter_var($raw, FILTER_SANITIZE_EMAIL);

// For URL
$url = filter_var($raw, FILTER_SANITIZE_URL);

// For integers
$age = filter_var($raw, FILTER_SANITIZE_NUMBER_INT);

// For stripping all HTML tags
$stripped = strip_tags($raw);

// For removing all non-alphanumeric characters
$clean = preg_replace('/[^a-zA-Z0-9]/', '', $raw);
?>
```

## Examples

```php
<?php
// Complete form sanitization pattern
function sanitizeFormData(array $data, array $rules): array
{
    $sanitized = [];

    foreach ($data as $key => $value) {
        if (!isset($rules[$key])) {
            $sanitized[$key] = htmlspecialchars($value, ENT_QUOTES, 'UTF-8');
            continue;
        }

        $filter = $rules[$key];

        switch ($filter) {
            case 'html':
                $sanitized[$key] = htmlspecialchars($value, ENT_QUOTES, 'UTF-8');
                break;
            case 'email':
                $sanitized[$key] = filter_var($value, FILTER_SANITIZE_EMAIL);
                break;
            case 'int':
                $sanitized[$key] = (int) filter_var($value, FILTER_SANITIZE_NUMBER_INT);
                break;
            case 'float':
                $sanitized[$key] = (float) filter_var($value, FILTER_SANITIZE_NUMBER_FLOAT, FILTER_FLAG_ALLOW_FRACTION);
                break;
            case 'stripped':
                $sanitized[$key] = strip_tags($value);
                break;
            default:
                $sanitized[$key] = htmlspecialchars($value, ENT_QUOTES, 'UTF-8');
        }
    }

    return $sanitized;
}

$rules = [
    'name'    => 'html',
    'email'   => 'email',
    'age'     => 'int',
    'bio'     => 'stripped',
    'website' => 'html',
];

$sanitized = sanitizeFormData($_POST, $rules);
?>
```

```php
<?php
// Search and replace helper
// To find all occurrences in your codebase:
// grep -rn "FILTER_SANITIZE_STRING" --include="*.php" .

// Replace patterns:
// FILTER_SANITIZE_STRING -> FILTER_SANITIZE_FULL_SPECIAL_CHARS
// filter_var($x, FILTER_SANITIZE_STRING) -> htmlspecialchars($x, ENT_QUOTES, 'UTF-8')
?>
```

## Related Errors

- [PHP Deprecated: Implicit Nullable Type](/languages/php/warning-deprecated-nullable)
- [PHP Deprecated: mysql_* functions](/languages/php/warning-deprecated-mysql)
- [PHP Warning: Header Location](/languages/php/warning-header-location)
