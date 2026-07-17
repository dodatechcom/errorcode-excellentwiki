---
title: "PHP Cannot modify header information — headers already sent"
description: "Fix PHP Cannot modify header information: headers already sent. Learn why output before headers causes this error."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Cannot modify header information — headers already sent

This warning occurs when you try to send HTTP headers (like redirects or cookies) after PHP has already started sending output to the browser. Once any output is sent, headers cannot be modified.

## Common Causes

- Echo, print, or HTML output before `header()` calls
- Whitespace or BOM (Byte Order Mark) before `<?php` tag
- Session starting automatically sends headers, blocking later changes
- `include` or `require` files with trailing `?>` or whitespace

## How to Fix

### Move All header() Calls Before Output

```php
<?php
// Headers first
session_start();
header('Location: /login');
exit;

// No output above this line
?>
```

### Remove BOM and Leading Whitespace

```bash
# Check for BOM
hexdump -C file.php | head -3
# Remove BOM if present
sed -i '1s/^\xEF\xBB\xBF//' file.php
```

### Use Output Buffering

```ini
; php.ini
output_buffering = On
```

Or enable it in code:

```php
<?php
ob_start();
// Your code with headers
header('Location: /dashboard');
exit;
?>
```

### Avoid Closing PHP Tag

```php
<?php
// Good: no closing tag, no trailing whitespace
function setup() {
    session_start();
    ini_set('session.cookie_httponly', 1);
}
```

## Examples

```php
<?php
// Example 1: HTML before header
?>
<html>
<body>
<?php
header('Location: /login');
// Warning: Cannot modify header information — headers already sent
?>
```

```php
<?php
// Example 2: Whitespace after closing tag
header('Location: /login');
?> <?php // trailing space after ?>
// Warning: headers already sent

// Example 3: Session auto-start
session_start(); // sends session cookie header
header('Set-Cookie: custom=value');
// Warning: Cannot modify header information
// Fix: call header() before session_start()
?>
```

## Related Errors

- [PHP Warning: count()]({{< relref "/languages/php/warning-count" >}})
- [PHP Fatal Error: Allowed memory size exhausted]({{< relref "/languages/php/fatal-error" >}})
- [PHP Notice: Undefined Variable]({{< relref "/languages/php/notice-undefined-variable" >}})
