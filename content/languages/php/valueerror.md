---
title: "[Solution] PHP ValueError — Invalid Value Error"
description: "Fix PHP ValueError by validating value ranges, checking function requirements, and using proper enums."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 60
---

# ValueError — Invalid Value Error

ValueError is thrown when a function receives a valid type but an invalid value. Introduced in PHP 8.0, this replaces many warnings and notices with proper exceptions for better error handling.

## Common Causes

```php
<?php
// Cause 1: Invalid range for numeric value
$int = intval("99999999999999999999"); // ValueError in PHP 8.0+

// Cause 2: Invalid enum value
enum Status { case Active; case Inactive; }
$status = Status::from('deleted'); // ValueError: deleted is not a valid case

// Cause 3: Invalid offset or index
str_repeat("x", -1); // ValueError

// Cause 4: Invalid value for string functions
substr("hello", 0, -10); // ValueError: Length must be non-negative

// Cause 5: Invalid hex value
hex2bin("zzzz"); // ValueError
?>
```

## How to Fix

### Fix 1: Validate value ranges before use

```php
<?php
function repeatString(string $str, int $count): string {
    if ($count < 0) {
        throw new ValueError("Count must be non-negative, got $count");
    }
    return str_repeat($str, $count);
}

// Or use try-catch
try {
    $result = repeatString("x", -1);
} catch (ValueError $e) {
    echo "Error: " . $e->getMessage();
}
?>
```

### Fix 2: Use try-catch with enum::tryFrom()

```php
<?php
enum Status: string {
    case Active = 'active';
    case Inactive = 'inactive';
}

// Use tryFrom to safely get enum values
$status = Status::tryFrom($_GET['status'] ?? '');
if ($status === null) {
    http_response_code(400);
    echo "Invalid status value";
}

// Or catch ValueError from from()
try {
    $status = Status::from($_GET['status'] ?? '');
} catch (ValueError $e) {
    http_response_code(400);
    echo "Invalid status: " . $e->getMessage();
}
?>
```

### Fix 3: Check function requirements

```php
<?php
function safeHexDecode(string $data): string|false {
    if (strlen($data) % 2 !== 0) {
        return false;
    }
    if (!ctype_xdigit($data)) {
        return false;
    }
    return hex2bin($data);
}

// Or handle the ValueError
try {
    $decoded = hex2bin($_GET['data'] ?? '');
} catch (ValueError $e) {
    http_response_code(400);
    echo "Invalid hex data";
}
?>
```

## Examples

```php
<?php
// Handling ValueError in input processing
function processOffset(string $string, int $offset): string {
    try {
        return substr($string, $offset);
    } catch (ValueError $e) {
        error_log("Invalid offset $offset: " . $e->getMessage());
        return $string;
    }
}

// Safe enum handling
function getStatus(string $input): Status {
    $status = Status::tryFrom($input);
    if ($status === null) {
        throw new ValueError("Unknown status: $input. Valid: active, inactive");
    }
    return $status;
}

echo processOffset("hello", 2);   // "llo"
echo processOffset("hello", -10); // "hello" (fallback)
?>
```

## Related Errors

- [PHP TypeError]({{< relref "/languages/php/typeerror" >}}) — type mismatch
- [PHP UnhandledMatchError]({{< relref "/languages/php/unhandledmatcherror" >}}) — match failure
- [PHP Fatal Error]({{< relref "/languages/php/fatal-error" >}}) — fatal error
