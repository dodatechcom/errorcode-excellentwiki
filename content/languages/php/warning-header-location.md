---
title: "[Solution] PHP Warning: Cannot modify header information"
description: "Fix PHP Warning: Cannot modify header information. Use output buffering, check for early output, verify header() usage."
languages: ["php"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 116
---

# PHP Warning: Cannot modify header information — headers already sent

This warning means your script tried to send an HTTP header after PHP has already started outputting the response body. Once any output is sent (HTML, whitespace, or echo statements), headers can no longer be modified.

## Common Causes

```php
// Cause 1: Whitespace or BOM before <?php tag
<?php
// There's a blank line or BOM above this
header("Location: /dashboard");
?>
```

```php
// Cause 2: echo or print before header()
<?php
echo "Loading...";
header("Location: /dashboard");
// Warning: headers already sent
?>
```

```php
// Cause 3: Including files that produce output
<?php
include "header.php"; // This file outputs HTML
header("Location: /login");
?>
```

```php
// Cause 4: session_start() after output
<?php
echo "<p>Hello</p>";
session_start(); // Warning: cannot start session after output
?>
```

## How to Fix

### Fix 1: Enable Output Buffering

Use `ob_start()` to buffer all output and send headers later.

```php
<?php
ob_start(); // Start buffering output

// ... any code that might produce output ...

// Headers can still be sent even after output
header("Location: /dashboard");
ob_end_clean(); // Discard buffered output
exit;
?>
```

```ini
; php.ini — enable output buffering globally
output_buffering = 4096
```

### Fix 2: Move Headers Before Any Output

Place all header-sending code at the very top of your script.

```php
<?php
// All headers MUST come before any output
session_start();

if (!isset($_SESSION['user'])) {
    header("Location: /login");
    exit;
}

header("X-Content-Type-Options: nosniff");
header("X-Frame-Options: DENY");

// Now safe to output HTML
?>
<!DOCTYPE html>
<html>
<head><title>Dashboard</title></head>
<body>
    <h1>Welcome</h1>
</body>
</html>
```

### Fix 3: Check for Early Output from Included Files

Audit included files for whitespace or output before `<?php`.

```php
<?php
// Check file for BOM or trailing whitespace
function hasOutputBeforePhp(string $filePath): bool
{
    $content = file_get_contents($filePath);

    // Check for BOM
    if (str_starts_with($content, "\xEF\xBB\xBF")) {
        return true;
    }

    // Check for content before <?php
    $phpPos = strpos($content, '<?php');
    if ($phpPos === false) {
        return true;
    }

    $before = substr($content, 0, $phpPos);
    if (trim($before) !== '') {
        return true;
    }

    // Check for closing ?> followed by content
    $lastPhpPos = strrpos($content, '?>');
    if ($lastPhpPos !== false) {
        $after = substr($content, $lastPhpPos + 2);
        if (trim($after) !== '') {
            return true;
        }
    }

    return false;
}

$files = ['config.php', 'helpers.php', 'init.php'];
foreach ($files as $file) {
    if (hasOutputBeforePhp($file)) {
        echo "WARNING: {$file} has output before PHP code\n";
    }
}
?>
```

### Fix 4: Use Header Removal and Status Codes

Use modern header functions when appropriate.

```php
<?php
// Set HTTP status code instead of header for some cases
http_response_code(302);
header("Location: /new-page");

// Remove a previously sent header
header_remove("X-Powered-By");

// Replace a header
header("Content-Type: application/json");
// Later, replace it:
header("Content-Type: text/plain");
?>
```

## Examples

```php
<?php
// Complete redirect handler with output buffering
function redirect(string $url, int $status = 302): never
{
    if (headers_sent()) {
        // Headers already sent — use JavaScript fallback
        echo "<script>window.location.href='" . htmlspecialchars($url) . "';</script>";
        echo "<meta http-equiv='refresh' content='0;url=" . htmlspecialchars($url) . "'>";
        exit;
    }

    header("Location: {$url}", true, $status);
    exit;
}

// Middleware pattern for session protection
function requireAuth(): void
{
    ob_start();

    if (session_status() === PHP_SESSION_NONE) {
        session_start();
    }

    if (!isset($_SESSION['user_id'])) {
        redirect('/login');
    }

    ob_end_flush();
}

requireAuth();
echo "Welcome, " . htmlspecialchars($_SESSION['user_name'] ?? 'User');
?>
```

```php
<?php
// API response handler
function jsonResponse(array $data, int $statusCode = 200): never
{
    if (headers_sent()) {
        http_response_code(500);
        echo json_encode(['error' => 'Headers already sent']);
        exit;
    }

    http_response_code($statusCode);
    header('Content-Type: application/json; charset=utf-8');
    header('X-Content-Type-Options: nosniff');
    echo json_encode($data, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
    exit;
}

// Usage
jsonResponse(['status' => 'ok', 'data' => []], 200);
?>
```

## Related Errors

- [PHP Warning: Header Sent](/languages/php/warning-header-sent)
- [PHP Warning: Headers Already Sent](/languages/php/headers-sent)
- [PHP Session Start Error](/languages/php/session-start-error)
