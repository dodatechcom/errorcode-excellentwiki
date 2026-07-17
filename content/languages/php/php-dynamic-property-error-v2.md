---
title: "[Solution] PHP Dynamic Property Deprecated Error Fix"
description: "Fix PHP dynamic property deprecation warnings. Learn why dynamic properties are deprecated in PHP 8.2."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["dynamic-property", "deprecated", "php", "magic-method"]
weight: 5
---

# PHP Dynamic Property Deprecated Error Fix

A PHP dynamic property error occurs when you create properties on an object that are not declared in the class. This has been deprecated in PHP 8.2 and will become an error in PHP 9.0.

## What This Error Means

PHP 8.2 deprecated the creation of dynamic properties — assigning a value to a property that doesn't exist in the class definition. This was previously allowed via `__set()` magic method or implicit creation. Future PHP versions will throw an error instead of a deprecation warning.

## Common Causes

- Assigning to undeclared properties on objects
- Using stdClass implicitly
- Old code relying on dynamic property creation
- Frameworks or libraries that set undeclared properties

## How to Fix

### 1. Declare all properties in the class

```php
<?php
// WRONG: Dynamic property assignment
class User {
    public string $name;
}
$user = new User();
$user->name = 'Alice';
$user->email = 'alice@example.com'; // Deprecated: dynamic property

// CORRECT: Declare all properties
class User {
    public string $name;
    public string $email;
}
$user = new User();
$user->name = 'Alice';
$user->email = 'alice@example.com';
?>
```

### 2. Use #[AllowDynamicProperties] sparingly

```php
<?php
// CORRECT: Explicitly allow dynamic properties
#[AllowDynamicProperties]
class FlexibleObject {
    // This class allows dynamic properties
}

$obj = new FlexibleObject();
$obj->anything = 'value'; // Allowed
?>
```

### 3. Use ArrayObject for dynamic key-value pairs

```php
<?php
// WRONG: Dynamic properties on a regular class
class Config {
    public string $name = 'default';
}
$config = new Config();
$config->debug = true; // Deprecated

// CORRECT: Use ArrayObject or define properties
class Config extends ArrayObject {
    public function __construct(array $data = []) {
        parent::__construct($data);
    }
}

$config = new Config(['debug' => true, 'name' => 'production']);
echo $config['debug']; // true
?>
```

### 4. Migrate old code to use declared properties

```php
<?php
// WRONG: Legacy pattern
class Settings {
    public string $name;
}
$settings = new Settings();
$settings->theme = 'dark'; // Deprecated

// CORRECT: Use typed properties
class Settings {
    public string $name = '';
    public string $theme = 'light';
}
$settings = new Settings();
$settings->theme = 'dark';
?>
```

## Related Errors

- [PHP Deprecated function]({{< relref "/languages/php/php-deprecated-error-v2" >}})
- [PHP Readonly error]({{< relref "/languages/php/php-readonly-error-v2" >}})
- [PHP Parse error]({{< relref "/languages/php/parse-error" >}})
