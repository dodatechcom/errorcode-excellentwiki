---
title: "PHP Warning: json_encode() failed"
description: "Fix PHP Warning: json_encode() failed. Learn to check for UTF-8 encoding, handle special characters, and use JSON_THROW_ON_ERROR."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: json_encode() failed

This warning occurs when `json_encode()` encounters data that cannot be serialized to JSON, such as non-UTF-8 strings, resources, or objects with circular references.

## Common Causes

- Non-UTF-8 encoded strings
- Objects with circular references
- Resources or other non-serializable types

## How to Fix

### Check for UTF-8 Encoding

```php
<?php
// Wrong — non-UTF-8 string
$json = json_encode($data);

// Correct — ensure UTF-8 encoding
$data = mb_convert_encoding($data, 'UTF-8', mb_detect_encoding($data));
$json = json_encode($data);
?>
```

### Handle Special Characters

```php
<?php
// Wrong — may fail on special characters
$json = json_encode($data);

// Correct — use JSON_UNESCAPED_UNICODE and other flags
$json = json_encode($data, JSON_UNESCAPED_UNICODE | JSON_HEX_TAG);
?>
```

### Use JSON_THROW_ON_ERROR

```php
<?php
// Wrong — silent failure
$json = json_encode($data);

// Correct — throw on error
try {
    $json = json_encode($data, JSON_THROW_ON_ERROR);
} catch (JsonException $e) {
    echo 'JSON encode error: ' . $e->getMessage();
}
?>
```

## Examples

```php
<?php
// This triggers the warning
$data = ["name" => "México", "value" => "\xB1\x31"]; // invalid UTF-8
$json = json_encode($data);
// Warning: json_encode(): Invalid UTF-8 sequence

// Correct
$data = ["name" => "México", "value" => "1"];
$json = json_encode($data, JSON_UNESCAPED_UNICODE);
?>
```

## Related Errors

- [PHP Warning: json_decode() failed]({{< relref "/languages/php/warning-json-decode-failed" >}})
- [PHP Warning: serialize()]({{< relref "/languages/php/json-encode-error" >}})
- [PHP Warning: json_last_error()]({{< relref "/languages/php/json-decode-error" >}})
