---
title: "[Solution] PHP Warning: strpos() — Empty Needle"
description: "Fix PHP Warning: strpos() empty needle. Check needle value, validate before calling, handle empty strings."
languages: ["php"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 8
---

# PHP Warning: strpos() — Empty Needle

This warning occurs when `strpos()` receives an empty string as the needle (the substring to search for). Starting from PHP 8.0, an empty needle is no longer allowed and throws this warning.

## Common Causes

```php
<?php
// Example 1: Empty string variable
$needle = "";
$pos = strpos("hello world", $needle);
// Warning: strpos(): Passing null to parameter #1 ($haystack) of type string is deprecated (PHP 8.1+)
```

```php
<?php
// Example 2: Variable from user input
$search = $_GET["search"] ?? "";
$pos = strpos("hello world", $search);
// Warning: strpos(): Empty needle
```

```php
<?php
// Example 3: Trimmed result is empty
$needle = "   ";
$pos = strpos("hello world", trim($needle));
// Warning: strpos(): Empty needle
```

```php
<?php
// Example 4: Array value that is empty
$data = ["key" => ""];
$pos = strpos("hello world", $data["key"]);
// Warning: strpos(): Empty needle
```

```php
<?php
// Example 5: String interpolation with empty variable
$name = "";
$pos = strpos("Hello, World!", "Hello, $name");
// Warning: strpos(): Empty needle
```

## How to Fix

### Fix 1: Validate the Needle Before Searching

Always check that the needle is not empty before calling `strpos()`.

```php
<?php
$needle = getUserInput();

if (!empty($needle)) {
    $pos = strpos("hello world", $needle);
} else {
    $pos = false;
}
```

### Fix 2: Use the Null Coalescing Operator

Provide a default value for potentially null or empty needles.

```php
<?php
$search = $_GET["search"] ?? "";
$pos = !empty($search) ? strpos("hello world", $search) : false;
```

### Fix 3: Create a Safe Wrapper Function

Centralize the logic with built-in validation.

```php
<?php
function safeStrpos(string $haystack, ?string $needle): int|false {
    if ($needle === null || $needle === "") {
        return false;
    }
    return strpos($haystack, $needle);
}

$pos = safeStrpos("hello world", "");   // false
$pos = safeStrpos("hello world", "world"); // 6
```

### Fix 4: Use str_contains() for Boolean Checks (PHP 8.0+)

If you only need to check existence (not position), `str_contains()` is a cleaner alternative.

```php
<?php
$needle = getUserInput();

// Instead of: strpos($haystack, $needle) !== false
// Use:
if (!empty($needle) && str_contains($haystack, $needle)) {
    // Found
}
```

### Fix 5: Handle Edge Cases in Search Functions

When building search functionality, normalize input before searching.

```php
<?php
function searchContent(string $content, mixed $query): int|false {
    $query = trim((string) ($query ?? ""));

    if ($query === "") {
        return false;
    }

    return strpos($content, $query);
}

$pos = searchContent("PHP is great", null);     // false
$pos = searchContent("PHP is great", "PHP");    // 0
$pos = searchContent("PHP is great", "");       // false
```

## Examples

```php
<?php
// Scenario: Searching through a log file
$logContent = file_get_contents("/var/www/logs/app.log");
$searchTerm = $_GET["q"] ?? "";

if (empty($searchTerm)) {
    echo "Please enter a search term";
    return;
}

$position = strpos($logContent, $searchTerm);
if ($position !== false) {
    echo "Found at position: {$position}";
} else {
    echo "Not found";
}
```

## Related Errors

- [PHP Warning: strlen() Expects String](/languages/php/warning-strlen-expects)
- [PHP Warning: sprintf() Too Few Arguments](/languages/php/warning-sprintf-too-few)
- [PHP Notice: Undefined Index](/languages/php/notice-undefined-index)
