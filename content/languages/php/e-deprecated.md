---
title: "[Solution] PHP E_DEPRECATED — Deprecated Feature Fix"
description: "Fix PHP E_DEPRECATED notices about deprecated functions and features. Learn to replace deprecated code with modern PHP alternatives."
languages: ["php"]
severities: ["notice"]
error-types: ["runtime-error"]
weight: 5
---

# [Solution] PHP E_DEPRECATED — Deprecated Feature Fix

`E_DEPRECATED` notices inform you that a function, feature, or syntax you are using has been deprecated and will be removed in a future PHP version. The script still runs, but you should update your code to avoid breakage in upcoming releases.

## Common Causes

- Using deprecated functions (e.g., `mysql_connect`, `each`, `create_function`)
- Using old-style constructors
- Relying on deprecated INI settings
- Using obsolete type casting or string interpolation patterns

## How to Fix

### 1. Replace Deprecated Functions

```php
// WRONG — mysql_connect is deprecated
<?php
$conn = mysql_connect('localhost', 'user', 'pass');
?>

// CORRECT — use mysqli or PDO
<?php
$conn = new mysqli('localhost', 'user', 'pass', 'database');
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
```

### 2. Replace Deprecated `each()` with `foreach`

```php
// WRONG — each() is deprecated since PHP 7.2
<?php
$arr = ['a' => 1, 'b' => 2];
while (list($key, $val) = each($arr)) {
    echo "$key: $val";
}
?>

// CORRECT — use foreach
<?php
$arr = ['a' => 1, 'b' => 2];
foreach ($arr as $key => $val) {
    echo "$key: $val";
}
?>
```

### 3. Replace `create_function` with Closures

```php
// WRONG — create_function is deprecated
<?php
$func = create_function('$a, $b', 'return $a + $b;');
echo $func(3, 5);
?>

// CORRECT — use anonymous function
<?php
$func = function($a, $b) {
    return $a + $b;
};
echo $func(3, 5);
?>
```

### 4. Enable `E_DEPRECATED` During Development

```php
<?php
error_reporting(E_ALL | E_DEPRECATED);
ini_set('display_errors', 1);
?>
```

## Examples

```php
<?php
// E_DEPRECATED: mysql_connect() deprecated
$conn = mysql_connect('localhost', 'user', 'pass');

// E_DEPRECATED: each() deprecated
each($array);

// E_DEPRECATED: create_function() deprecated
$fn = create_function('', 'return 1;');
?>
```

## Related Errors

- [PHP Deprecated Warning]({{< relref "/languages/php/deprecated-filter" >}})
- [PHP E_STRICT]({{< relref "/languages/php/e-strict" >}})
- [PHP E_USER_DEPRECATED]({{< relref "/languages/php/e-user-deprecated" >}})
- [PHP E_WARNING]({{< relref "/languages/php/e-warning" >}})
