---
title: "[Solution] PHP E_STRICT — Strict Standards Fix"
description: "Fix PHP E_STRICT strict standards notices. Learn to comply with strict mode coding standards for deprecated practices and potential compatibility issues."
languages: ["php"]
severities: ["notice"]
error-types: ["runtime-error"]
tags: ["e-strict", "strict", "standards"]
weight: 5
---

# [Solution] PHP E_STRICT — Strict Standards Fix

`E_STRICT` notifications alert you to code that may not be strictly compatible with the current PHP version but will still execute. Enabling `E_STRICT` helps you write forward-compatible code and catch practices that will become errors in future PHP versions.

## Common Causes

- Calling methods statically that should not be called statically
- Using deprecated features not yet removed from PHP
- Missing return type declarations in strict contexts
- Passing non-strict-compatible types to functions

## How to Fix

### 1. Enable `E_STRICT` in Development

```php
<?php
error_reporting(E_ALL | E_STRICT);
?>
```

### 2. Avoid Calling Non-Static Methods Statically

```php
// WRONG — calling non-static method statically
<?php
class Logger {
    public function log($msg) {
        echo $msg;
    }
}
Logger::log("test"); // E_STRICT
?>

// CORRECT
<?php
$logger = new Logger();
$logger->log("test");
?>
```

### 3. Add Proper Type Declarations

```php
// WRONG — implicit type coercion
<?php
function add($a, $b) {
    return $a + $b;
}
add("5", 3);
?>

// CORRECT
<?php
declare(strict_types=1);
function add(int $a, int $b): int {
    return $a + $b;
}
add(5, 3);
?>
```

### 4. Use Modern PHP Practices

```php
// WRONG — deprecated constructor style
<?php
class OldClass {
    function OldClass() { }
}
?>

// CORRECT
<?php
class NewClass {
    public function __construct() { }
}
?>
```

## Examples

```php
<?php
// E_STRICT: Non-static method should not be called statically
class Foo {
    public function bar() { return 42; }
}
Foo::bar();

// E_STRICT: Only variables should be assigned by reference
$a = 5;
(&$a) = 10;
?>
```

## Related Errors

- [PHP E_DEPRECATED]({{< relref "/languages/php/e-deprecated" >}})
- [PHP Deprecated Warning]({{< relref "/languages/php/deprecated-filter" >}})
- [PHP E_WARNING]({{< relref "/languages/php/e-warning" >}})
- [PHP E_NOTICE]({{< relref "/languages/php/e-notice" >}})
