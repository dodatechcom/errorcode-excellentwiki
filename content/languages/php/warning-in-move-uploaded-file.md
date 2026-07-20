---
title: "PHP Warning: move_uploaded_file() failed"
description: "Fix PHP Warning: move_uploaded_file() failed. Learn to check if temp file exists, verify directory permissions, and validate with is_uploaded_file()."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: move_uploaded_file() failed

This warning occurs when move_uploaded_file() cannot move the uploaded file to its destination due to file system issues or invalid input.

## Common Causes

- The uploaded temp file does not exist
- Destination directory lacks write permissions
- Attempting to move a non-uploaded file

## How to Fix

### Check Temp File Exists

```php
<?php
// Wrong — assuming file exists
move_uploaded_file($_FILES['file']['tmp_name'], $dest);

// Correct — verify it exists
$tmpName = $_FILES['file']['tmp_name'] ?? null;
if ($tmpName && file_exists($tmpName)) {
    move_uploaded_file($tmpName, $dest);
}
?>
```

### Verify Directory Permissions

```php
<?php
// Wrong — dest directory may not exist
move_uploaded_file($tmp, './uploads/doc.pdf');

// Correct — create dir and check permissions
$dir = './uploads';
if (!is_dir($dir)) {
    mkdir($dir, 0755, true);
}
if (is_writable($dir)) {
    move_uploaded_file($tmp, $dir . '/doc.pdf');
}
?>
```

### Validate with is_uploaded_file()

```php
<?php
// Wrong — directly moving without validation
move_uploaded_file($tmp, $dest);

// Correct — use is_uploaded_file
if (is_uploaded_file($tmp)) {
    move_uploaded_file($tmp, $dest);
}
?>
```

## Examples

```php
<?php
// This triggers the warning
$temp = '/tmp/phpXXX';
move_uploaded_file($temp, 'doc.pdf');
// Warning: move_uploaded_file(): failed with error code 2

// Correct
if (is_uploaded_file($temp)) {
    move_uploaded_file($temp, 'doc.pdf');
}
?>
```

## Related Errors

- [PHP Warning: fopen() failed]({{< relref "/languages/php/warning-fopen-failed" >}})
- [PHP Warning: file_put_contents() failed]({{< relref "/languages/php/warning-file-put-contents-failed" >}})
- [PHP Warning: file_get_contents() failed]({{< relref "/languages/php/warning-file-get-contents-failed" >}})
