---
title: "[Solution] PHP session_register() Deprecated — Use $_SESSION Superglobal"
description: "Replace deprecated session_register() with $_SESSION superglobal in PHP. Migration guide with session handling best practices."
deprecated_function: "session_register"
replacement_function: "$_SESSION"
languages: ["php"]
deprecated_since: "PHP 4.2"
removed_in: "PHP 5.4"
error_message: "Deprecated: session_register() is deprecated"
tags: ["session-register", "superglobal", "session", "php"]
weight: 28
---

# [Solution] PHP session_register() Deprecated — Use $_SESSION Superglobal

The `session_register()` function was deprecated in PHP 4.2 and removed in PHP 5.4. It registered a variable as a session variable, automatically making it available in the `$_SESSION` superglobal array. The modern approach is to work directly with the `$_SESSION` superglobal, which gives you full control over session data and is consistent with how all other superglobals (`$_GET`, `$_POST`, `$_REQUEST`) work in PHP.

## What You'll See

On PHP 4.2-5.3:

```
Deprecated: session_register() is deprecated in /path/to/script.php on line X
```

On PHP 5.4+:

```
Fatal error: Uncaught Error: Call to undefined function session_register()
```

## Old Code (Deprecated)

```php
<?php
session_start();

// Register session variables — deprecated
session_register("user_id");
session_register("username");
session_register("is_logged_in");

// Access registered variables as regular variables (not $_SESSION)
$user_id = 12345;
$username = "alice";
$is_logged_in = true;

// Later in the same or another page
if ($is_logged_in) {
    echo "Welcome, $username (ID: $user_id)";
}

// Unregister
session_unregister("user_id");
```

## New Code (Replacement)

```php
<?php
session_start();

// Set session variables directly in $_SESSION
$_SESSION["user_id"] = 12345;
$_SESSION["username"] = "alice";
$_SESSION["is_logged_in"] = true;

// Access through $_SESSION — explicit and consistent
if (!empty($_SESSION["is_logged_in"])) {
    $username = $_SESSION["username"];
    $user_id = $_SESSION["user_id"];
    echo "Welcome, $username (ID: $user_id)";
}

// Unset a specific session variable
unset($_SESSION["user_id"]);

// Destroy the entire session
session_unset();       // clear $_SESSION contents
session_destroy();     // destroy the session on the server
```

## Complete Session Handling Pattern

```php
<?php
session_start();

// --- Login ---
function login_user($username, $password) {
    // Validate credentials (simplified)
    $user = authenticate($username, $password);
    if ($user) {
        // Regenerate session ID to prevent session fixation
        session_regenerate_id(true);

        $_SESSION["user_id"] = $user["id"];
        $_SESSION["username"] = $user["name"];
        $_SESSION["is_logged_in"] = true;
        $_SESSION["login_time"] = time();
        return true;
    }
    return false;
}

// --- Check if logged in ---
function is_logged_in() {
    return !empty($_SESSION["is_logged_in"]) && !empty($_SESSION["user_id"]);
}

// --- Get current user ---
function current_user() {
    if (!is_logged_in()) {
        return null;
    }
    return [
        "id" => $_SESSION["user_id"],
        "name" => $_SESSION["username"],
    ];
}

// --- Logout ---
function logout_user() {
    $_SESSION = [];

    if (ini_get("session.use_cookies")) {
        $params = session_get_cookie_params();
        setcookie(session_name(), "", time() - 42000,
            $params["path"], $params["domain"],
            $params["secure"], $params["httponly"]
        );
    }

    session_destroy();
}

// --- Flash messages (common pattern) ---
function set_flash($key, $message) {
    $_SESSION["flash"][$key] = $message;
}

function get_flash($key) {
    if (isset($_SESSION["flash"][$key])) {
        $message = $_SESSION["flash"][$key];
        unset($_SESSION["flash"][$key]);
        return $message;
    }
    return null;
}
```

## Migration Steps

1. **Find all session_register calls**:

```bash
grep -rn "session_register" --include="*.php" /path/to/project/
```

2. **Replace each `session_register("var")` with direct `$_SESSION["var"]` assignment**.

3. **Replace all bare variable access** of session-registered variables with `$_SESSION["var"]` access.

4. **Replace `session_unregister("var")` with `unset($_SESSION["var"])`**.

5. **Add session security best practices**:

```php
<?php
// Add at the top of your session handling code
session_start([
    "cookie_httponly" => true,     // Prevent JavaScript access
    "cookie_secure" => true,       // HTTPS only
    "cookie_samesite" => "Lax",   // CSRF protection
    "use_strict_mode" => true,     // Reject uninitialized session IDs
]);

// Regenerate ID after login
session_regenerate_id(true);
```

6. **Search for related deprecated patterns**:

```bash
grep -rn "session_is_registered\|session_unregister" --include="*.php" /path/to/project/
```

## Security Best Practices

| Practice | Implementation |
|---|---|
| Set `cookie_httponly` | Prevents JavaScript access to session cookie |
| Set `cookie_secure` | Only send cookie over HTTPS |
| Set `cookie_samesite` | Prevents CSRF with `Lax` or `Strict` |
| Regenerate session ID | Call `session_regenerate_id(true)` after login |
| Use `use_strict_mode` | Reject uninitialized session IDs |
| Validate session data | Don't trust `$_SESSION` contents without validation |

## Related Errors

- [ereg_replace() → preg_replace()](ereg-replace-to-preg-replace) — PHP regex migration.
- [create_function() → anonymous functions](create-function) — PHP function migration.
