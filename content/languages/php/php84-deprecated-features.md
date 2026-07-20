---
title: "[Solution] PHP 8.4 Comprehensive Deprecation List"
description: "Fix PHP 8.4 deprecated features. Follow migration guide, update deprecated code, check PHP 8.4 changelog."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1106
---

# PHP 8.4 Comprehensive Deprecation List

PHP 8.4 removes and deprecates numerous features that were marked deprecated in earlier versions. This includes implicit nullable types, dynamic properties, various function signatures, and several legacy patterns. Failing to update deprecated code will cause deprecation notices and eventual removal in PHP 9.0.

## Common Causes

```php
<?php
// Cause 1: Implicit nullable type declarations (deprecated)
function greet(?string $name = null) {} // OK — explicit nullable
function process(string $val = null) {} // Deprecated: implicit nullable

// Cause 2: Using deprecated functions
each($array); // Deprecated since PHP 7.2, removed
create_function('$a', 'return $a'); // Removed

// Cause 3: Using deprecated class constants
$a = $date::RFC3339; // Some constants renamed/deprecated

// Cause 4: Relying on deprecated behavior
regorba(); // Deprecated mbstring functions
mbereg();  // Deprecated regex functions

// Cause 5: Using removed/deprecated ini directives
ini_set('assert.active', 1); // Deprecated
```

## How to Fix

### Fix 1: Replace implicit nullable with explicit nullable types

```php
<?php
// Bad: implicit nullable (deprecated in PHP 8.4)
function process(string $val = null) {
    echo $val;
}

// Good: explicit nullable
function process(?string $val = null) {
    echo $val;
}

// Same for classes
class Config
{
    // Bad
    private Logger $logger = null;

    // Good
    private ?Logger $logger = null;
}
```

### Fix 2: Replace deprecated function calls

```php
<?php
// Bad: deprecated each()
$key = 'name';
each($array);

// Good: use foreach or array functions
foreach ($array as $k => $v) {
    // ...
}

// Or use key()/current()/next()
$key = key($array);
$value = current($array);
next($array);

// Replace create_function with anonymous functions
// Bad
$func = create_function('$a', 'return $a * 2;');

// Good
$func = fn($a) => $a * 2;
```

### Fix 3: Update deprecated mbstring regex functions

```php
<?php
// Bad: deprecated mb_ereg functions
mbereg('/pattern/', $string);

// Good: use mb_ preg functions
preg_match('/pattern/u', $string);

// Or with multibyte support
preg_match('/\p{L}+/u', $string);
```

### Fix 4: Update deprecated ini settings and assertions

```php
<?php
// Bad: deprecated assertion functions
assert('1 + 1 === 2');

// Good: use if statements or dedicated testing
if (1 + 1 !== 2) {
    throw new \LogicException("Math is broken");
}

// Or use a test framework assertion
$this->assertEquals(2, 1 + 1);
```

### Fix 5: Follow the PHP 8.4 migration guide

```php
<?php
// Key changes to address:

// 1. Serializable interface deprecated
// Bad
class MyClass implements Serializable {
    public function serialize() { /* ... */ }
    public function unserialize($data) { /* ... */ }
}

// Good: use __serialize() / __unserialize()
class MyClass {
    public function __serialize(): array {
        return ['key' => $this->value];
    }
    public function __unserialize(array $data): void {
        $this->value = $data['key'];
    }
}

// 2. Check php -i for deprecated extensions
// 3. Review php84 migration guide: https://www.php.net/releases/8.4/en.php
```

## Examples

```php
<?php
// Preparing codebase for PHP 8.4

// 1. Audit for implicit nullable types
// Run: grep -rn "= null)" src/
// Replace all string $param = null with ?string $param = null

// 2. Replace deprecated array functions
$arr = [1, 2, 3];

// array_key_exists() on objects — deprecated
// Bad
array_key_exists('prop', $object);

// Good
property_exists($object, 'prop') || method_exists($object, '__get');

// 3. Update PHP version in composer.json
// "require": { "php": ">=8.1" }  →  "php": ">=8.4"

// 4. Run Rector or PHP CS Fixer for automated fixes
// vendor/bin/rector process src/ --set=php84
// vendor/bin/php-cs-fixer fix src/ --rules=@PHP84Migration
```

## Related Errors

- [PHP Deprecated]({{< relref "/languages/php/php-deprecated" >}}) — general deprecation warnings
- [PHP 8.4 Property Hooks]({{< relref "/languages/php/php84-property-hooks" >}}) — new feature
- [PHP 8.4 Asymmetric Visibility]({{< relref "/languages/php/php84-asymmetric-visibility" >}}) — new feature
- [Rector Error]({{< relref "/languages/php/rector-error" >}}) — automated migration
