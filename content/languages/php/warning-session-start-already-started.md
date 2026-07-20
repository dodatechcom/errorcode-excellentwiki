---
title: "[Solution] PHP Warning: session_start() — Session Cannot Be Started After Headers Sent"
description: "Fix PHP Warning: session_start() session cannot be started after headers sent. Call session_start() before output, use output buffering, check for whitespace."
languages: ["php"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 9
---

# PHP Warning: session_start() — Session Cannot Be Started After Headers Sent

This warning occurs when `session_start()` is called after PHP has already started sending output (HTML, whitespace, or a BOM). Sessions require a cookie header to be sent to the browser, and once output begins, headers can no longer be sent.

## Common Causes

```php
<?php
// Example 1: Whitespace before <?php tag
// file.php starts with a blank line then <?php
include "file.php";
session_start(); // Warning!
```

```php
<?php
// Example 2: Output before session_start()
echo "Welcome!";
session_start(); // Warning!
```

```php
<?php
// Example 3: Closing ?> tag with trailing newline in included file
// helper.php ends with ?> followed by newline
include "helper.php";
session_start(); // Warning!
```

```php
<?php
// Example 4: BOM (byte order mark) at start of file
// File saved with UTF-8 BOM before <?php
session_start(); // Warning!
```

```php
<?php
// Example 5: Auto-prepended file with output
// auto_prepend_file produces output before main script
session_start(); // Warning in main script
```

## How to Fix

### Fix 1: Call session_start() Before Any Output

Place `session_start()` at the very top of your script, before any HTML, whitespace, or includes.

```php
<?php
// Must be the very first thing — no blank lines before <?php
session_start([
    'name'            => 'APP_SESSION',
    'cookie_secure'   => true,
    'cookie_httponly'  => true,
    'cookie_samesite' => 'Strict',
    'use_strict_mode' => true,
]);

$_SESSION['user_id'] = $userId;
?>
<!DOCTYPE html>
<html>
<body>
    <h1>Welcome, <?= htmlspecialchars($_SESSION['user_id']) ?></h1>
</body>
</html>
```

### Fix 2: Use Output Buffering

Enable output buffering to allow `session_start()` after some output.

```php
<?php
ob_start(); // Start buffering output

include "includes/init.php";
include "includes/helpers.php";

session_start(); // Safe — output is buffered

ob_end_flush();
?>
<!DOCTYPE html>
<html>
<body>
    <p>Session started successfully</p>
</body>
</html>
```

```ini
; php.ini — enable globally
output_buffering = 4096
```

### Fix 3: Remove Closing PHP Tags and Trailing Whitespace

Closing `?>` tags and trailing newlines in included files are common invisible causes.

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

### Fix 4: Use a Framework Middleware Pattern

In modern frameworks, handle sessions in middleware that runs before any output.

```php
<?php
// Example: Simple middleware pattern
class SessionMiddleware {
    public function handle(callable $next): void {
        session_start([
            'cookie_secure'   => true,
            'cookie_httponly'  => true,
            'cookie_samesite' => 'Lax',
        ]);

        $next(); // Process request

        session_write_close();
    }
}

$middleware = new SessionMiddleware();
$middleware->handle(function() {
    // Request processing — session is available
    $_SESSION['last_activity'] = time();
});
```

## Examples

```php
<?php
// Scenario: Login page with session
// login.php — must start at top with no whitespace
session_start([
    'use_strict_mode' => true,
    'cookie_lifetime' => 3600,
]);

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $user = authenticateUser($_POST['username'], $_POST['password']);

    if ($user) {
        session_regenerate_id(true);
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['logged_in'] = true;
        header("Location: /dashboard");
        exit;
    }

    $error = "Invalid credentials";
}

// Now safe to send output
?>
<!DOCTYPE html>
<html>
<body>
    <form method="POST">
        <?php if (!empty($error)): ?>
            <p class="error"><?= htmlspecialchars($error) ?></p>
        <?php endif; ?>
        <input name="username" required>
        <input name="password" type="password" required>
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

## Related Errors

- [PHP Warning: Headers Already Sent](/languages/php/warning-headers-sent-already)
- [PHP Session Start Failed](/languages/php/session-start-error)
- [PHP Session Save Path Error](/languages/php/session-save-path-error)
