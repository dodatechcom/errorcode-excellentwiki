---
title: "[Solution] PHP Warning: mb_strtolower() — mbstring not available"
description: "Fix PHP Warning: mb_strtolower() Unable to load encoding. Install mbstring extension, check phpinfo(), use string functions."
languages: ["php"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 118
---

# PHP Warning: mb_strtolower() — mbstring not available

This warning means the mbstring (multibyte string) extension is not installed or enabled. The mbstring extension is essential for handling UTF-8 and other multibyte character encodings. Without it, functions like `mb_strtolower()`, `mb_strlen()`, and `mb_substr()` will fail.

## Common Causes

```php
// Cause 1: mbstring extension not installed
<?php
$result = mb_strtolower("HELLO");
// Warning: mb_strtolower(): Unable to load encoding "none"
// or Fatal error: Call to undefined function mb_strtolower()
?>
```

```php
// Cause 2: Extension disabled in php.ini
<?php
// ;extension=mbstring  (commented out in php.ini)
$result = mb_strlen("Hello World");
// Warning or fatal error depending on PHP version
?>
```

```php
// Cause 3: Wrong PHP version or SAPI
<?php
// CLI might have mbstring but FPM doesn't
$result = mb_substr("Hello", 0, 3);
?>
```

## How to Fix

### Fix 1: Install and Enable the mbstring Extension

Install mbstring for your PHP version and SAPI.

```bash
# Ubuntu/Debian
sudo apt-get install php-mbstring

# For specific PHP version
sudo apt-get install php8.1-mbstring
sudo apt-get install php8.2-mbstring
sudo apt-get install php8.3-mbstring

# RHEL/CentOS/Fedora
sudo yum install php-mbstring

# macOS with Homebrew
brew install php-mbstring

# After installing, restart your web server
sudo systemctl restart apache2
# or
sudo systemctl restart php8.1-fpm
```

```php
<?php
// Verify mbstring is loaded
if (!extension_loaded('mbstring')) {
    echo "mbstring is not loaded\n";
    echo "Install: sudo apt-get install php-mbstring\n";
    exit(1);
}

echo "mbstring version: " . phpversion('mbstring') . "\n";
echo "mbstring encoding: " . mb_internal_encoding() . "\n";
?>
```

### Fix 2: Check phpinfo() for mbstring Status

Verify mbstring is enabled in your PHP configuration.

```php
<?php
// Check mbstring availability
$checks = [
    'mbstring loaded'    => extension_loaded('mbstring'),
    'mbstring version'   => phpversion('mbstring') ?? 'Not installed',
    'mb_internal_encoding' => function_exists('mb_internal_encoding')
        ? mb_internal_encoding()
        : 'Function not available',
];

foreach ($checks as $check => $result) {
    echo "{$check}: {$result}\n";
}

// Full phpinfo for debugging
// phpinfo(INFO_MODULES);
?>
```

### Fix 3: Use Fallback String Functions

Provide fallback implementations when mbstring is unavailable.

```php
<?php
// Compatibility wrapper
function safe_strtolower(string $string): string
{
    if (function_exists('mb_strtolower')) {
        return mb_strtolower($string, 'UTF-8');
    }
    return strtolower($string);
}

function safe_strlen(string $string): int
{
    if (function_exists('mb_strlen')) {
        return mb_strlen($string, 'UTF-8');
    }
    return strlen($string);
}

function safe_substr(string $string, int $start, ?int $length = null): string
{
    if (function_exists('mb_substr')) {
        return mb_substr($string, $start, $length, 'UTF-8');
    }
    if ($length !== null) {
        return substr($string, $start, $length);
    }
    return substr($string, $start);
}

echo safe_strtolower("HELLO");  // hello
echo safe_strlen("Hello");      // 5
echo safe_substr("Hello World", 0, 5); // Hello
?>
```

### Fix 4: Configure mbstring in php.ini

Ensure mbstring settings are properly configured.

```ini
; php.ini — mbstring configuration
extension=mbstring

; Set default encoding
mbstring.language = Neutral
mbstring.internal_encoding = UTF-8
mbstring.http_input = auto
mbstring.http_output = UTF-8
mbstring.detect_order = auto
mbstring.substitute_character = none
```

## Examples

```php
<?php
// Complete mbstring compatibility layer
class MbCompat
{
    public static function isAvailable(): bool
    {
        return extension_loaded('mbstring');
    }

    public static function strtolower(string $str, string $encoding = 'UTF-8'): string
    {
        return self::isAvailable()
            ? mb_strtolower($str, $encoding)
            : strtolower($str);
    }

    public static function strtoupper(string $str, string $encoding = 'UTF-8'): string
    {
        return self::isAvailable()
            ? mb_strtoupper($str, $encoding)
            : strtoupper($str);
    }

    public static function strlen(string $str, string $encoding = 'UTF-8'): int
    {
        return self::isAvailable()
            ? mb_strlen($str, $encoding)
            : strlen($str);
    }

    public static function substr(string $str, int $start, ?int $length = null, string $encoding = 'UTF-8'): string
    {
        if (self::isAvailable()) {
            return mb_substr($str, $start, $length, $encoding);
        }
        return $length !== null
            ? substr($str, $start, $length)
            : substr($str, $start);
    }

    public static function strpos(string $haystack, string $needle, int $offset = 0, string $encoding = 'UTF-8'): int|false
    {
        return self::isAvailable()
            ? mb_strpos($haystack, $needle, $offset, $encoding)
            : strpos($haystack, $needle, $offset);
    }

    public static function str_contains(string $haystack, string $needle, string $encoding = 'UTF-8'): bool
    {
        return self::isAvailable()
            ? mb_strpos($haystack, $needle, 0, $encoding) !== false
            : str_contains($haystack, $needle);
    }
}

// Usage
$name = "Héllo Wörld";
echo MbCompat::strtolower($name);     // héllo wörld
echo "\n" . MbCompat::strlen($name);  // 11
echo "\n" . MbCompat::substr($name, 0, 5); // Héllo
?>
```

## Related Errors

- [PHP MBString Error](/languages/php/mbstring-error)
- [PHP intl Error](/languages/php/intl-error)
- [PHP Warning: strlen() expects](/languages/php/warning-in-strlen)
