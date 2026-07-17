---
title: "[Solution] PHP Warning: Cannot Modify Header Information — Headers Already Sent Fix"
description: "Fix PHP Warning: Cannot modify header info headers already sent. Learn output buffering, redirect ordering, and ob_start techniques."
languages: ["php"]
severities: ["warning"]
error_types: ["runtime"]
date: 2026-07-15
---

# PHP Warning: Cannot Modify Header Information (Headers Already Sent)

This warning means your script tried to send an HTTP header — such as a redirect, cookie, or content type — after PHP has already started outputting response body content. Once output begins, headers can no longer be modified because they must be sent before the body.

## Common Causes

- HTML, whitespace, or a BOM (byte order mark) before the `<?php` tag
- Calling `session_start()` after output has been sent
- Placing `header("Location: ...")` after `echo` statements
- Including files that produce output before the redirect

## Solutions

### 1. Enable Output Buffering

Output buffering lets PHP accumulate output in memory and send it all at once, giving you more flexibility with header placement.

```ini
; php.ini
output_buffering = 4096
```

```php
// Now safe even if output was sent — buffering holds it
header("Location: /dashboard");
exit;
```

### 2. Move Redirects Before Any Output

Place all header-sending code at the very top of your script, before any HTML or whitespace.

```php
<?php
// This must be at the absolute top — no blank lines before it
session_start();

if (!isset($_SESSION["user"])) {
    header("Location: /login");
    exit; // Always call exit after a redirect
}

// Then HTML can follow
?>
<!DOCTYPE html>
<html>
<!-- ... -->
</html>
```

### 3. Use `ob_start()` as a Buffer

When you need headers after some output (e.g., in an included file), use output buffering manually.

```php
<?php
ob_start(); // Start buffering output

// Process that might produce output
include "includes/init.php";

// Now safe to send headers
header("Location: /welcome");
ob_end_clean(); // Discard any buffered output
exit;
```

### 4. Strip BOM and Trailing Whitespace

Invisible characters before `<?php` cause this error. Check your files with a hex editor or use:

```bash
# Check for BOM
hexdump -C yourfile.php | head -5

# Remove trailing whitespace from all PHP files
find . -name "*.php" -exec sed -i 's/[[:space:]]*$//' {} \;
```

## Prevention Tips

- Ensure opening `<?php` tags have no preceding whitespace or BOM
- Use `header_remove()` and `http_response_code()` if you need to change headers
- Prefer framework middleware for redirects and session handling

## Related Errors

- [PHP Fatal Error](/languages/php/fatal-error)
- [PHP Deprecated Filter](/languages/php/deprecated-filter)
