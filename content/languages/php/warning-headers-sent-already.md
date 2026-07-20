---
title: "[Solution] PHP Warning: Cannot Modify Header Information — Headers Already Sent"
description: "Fix PHP Warning: Cannot modify header information — headers already sent. Use output_buffering, call header() before output, or use ob_start()."
languages: ["php"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 8
---

# PHP Warning: Cannot Modify Header Information — Headers Already Sent

This warning occurs when you call `header()`, `setcookie()`, or `session_start()` after PHP has already begun sending output to the browser. HTTP headers must be sent before any body content, and once output has started, headers can no longer be modified.

## Common Causes

```php
<?php
// Example 1: Output before header()
echo "Welcome!";
header("Location: /dashboard"); // Warning!
```

```php
<?php
// Example 2: Whitespace before <?php tag in an included file
// included_file.php starts with a blank line before <?php
include "included_file.php";
header("Location: /login"); // Warning!
```

```php
<?php
// Example 3: BOM (byte order mark) at start of file
// File saved with UTF-8 BOM before <?php
header("Content-Type: application/json"); // Warning!
```

```php
<?php
// Example 4: session_start() after output
echo "<p>Hello</p>";
session_start(); // Warning!
```

```php
<?php
// Example 5: Closing ?> tag with trailing newline in included file
// helper.php ends with ?> followed by a newline
include "helper.php";
header("X-Custom: value"); // Warning!
```

## How to Fix

### Fix 1: Enable output_buffering in php.ini

Output buffering lets PHP accumulate all output in memory and send it at once, allowing headers to be sent even after output has technically started.

```ini
; php.ini
output_buffering = 4096
```

```php
<?php
// With output_buffering enabled, this now works
echo "Some output";
header("Location: /dashboard"); // OK — buffered
exit;
```

### Fix 2: Call header() Before Any Output

Place all header-setting code at the very top of your script, before any HTML, whitespace, or includes that produce output.

```php
<?php
// Must be the very first thing — no blank lines before <?php
header("Location: /login");
exit;

// All output comes after
?>
<!DOCTYPE html>
<html>
<body>
    <p>This is never reached</p>
</body>
</html>
```

### Fix 3: Use ob_start() as a Runtime Buffer

When you cannot control output order (e.g., in a framework or template system), use `ob_start()` to buffer output at runtime.

```php
<?php
ob_start(); // Start buffering all output

// Code that might produce output
include "includes/init.php";
include "includes/header.php";

// Now safe to send headers
header("Location: /welcome");
ob_end_clean(); // Discard buffered output
exit;
```

### Fix 4: Remove Closing PHP Tags and Trailing Whitespace

Closing `?>` tags and trailing newlines in included files are common invisible causes of this warning.

```php
<?php
// CORRECT: File ends without closing ?> tag
function helper() {
    return "value";
}
// No closing tag, no trailing whitespace
```

```bash
# Find and fix files with trailing whitespace
find . -name "*.php" -exec sed -i 's/[[:space:]]*$//' {} \;

# Check for BOM characters
hexdump -C suspect_file.php | head -5
```

## Examples

```php
<?php
// Scenario: Redirect after processing
$success = processOrder($data);

if ($success) {
    header("Location: /order-success");
    exit;
}

// WRONG: output happens before redirect in error case
echo "Processing...";
header("Location: /error"); // Warning if $success is false path taken output first

// CORRECT: Buffer output
ob_start();
echo "Processing...";
if ($success) {
    ob_end_clean();
    header("Location: /order-success");
    exit;
}
ob_end_flush();
```

## Related Errors

- [PHP Warning: Session Cannot Be Started After Headers Sent](/languages/php/warning-session-start-already-started)
- [PHP Fatal Error](/languages/php/fatal-error)
- [PHP Session Start Failed](/languages/php/session-start-error)
