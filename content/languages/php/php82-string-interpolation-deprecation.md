---
title: "[Solution] PHP 8.2 Deprecated String Interpolation ${}"
description: "Fix PHP 8.2 deprecated ${} string interpolation. Replace deprecated syntax with {$var} or {${var}} patterns."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1105
---

# PHP 8.2 Deprecated String Interpolation `${}`

PHP 8.2 deprecates two forms of complex variable interpolation in strings: `"${expr}"` and `"${
expr}"` (with curly brace on new line). These forms are deprecated in favor of `"{$var}"` or `"{${$var}}"` syntax. Using the deprecated forms triggers a deprecation notice.

## Common Causes

```php
<?php
// Cause 1: Using deprecated ${} syntax (curly brace dollar)
$name = "World";
echo "Hello ${name}"; // Deprecated in PHP 8.2

// Cause 2: Using deprecated multiline ${} syntax
$var = "test";
echo "Value is ${
var
}"; // Deprecated in PHP 8.2

// Cause 3: Using ${} with expressions
$data = ['key' => 'value'];
echo "Item is ${$data['key']}"; // Deprecated

// Cause 4: Nested deprecated interpolation
$outer = 'name';
$inner = 'John';
echo "Hello ${$outer}"; // Deprecated
```

## How to Fix

### Fix 1: Replace ${var} with {$var}

```php
<?php
// Bad: deprecated ${} syntax
$name = "World";
echo "Hello ${name}";

// Good: use {} syntax
echo "Hello {$name}";
```

### Fix 2: Replace multiline ${} with proper syntax

```php
<?php
// Bad: deprecated multiline ${}
$value = "test";
echo "The value is ${
value
}";

// Good: use single-line {}
echo "The value is {$value}";

// Good: for readability with concatenation
echo "The value is " . $value;
```

### Fix 3: Replace ${$var} with appropriate syntax

```php
<?php
// Bad: deprecated ${$var} syntax
$key = 'name';
echo "${$key}";

// Good: use $$var (still valid, though avoid when possible)
echo "{$$key}";

// Better: use an explicit approach
$values = ['name' => 'John', 'age' => 30];
echo $values[$key];
```

### Fix 4: Fix complex interpolation with method calls

```php
<?php
// Bad: deprecated syntax with complex expressions
$obj = new stdClass();
$obj->name = "Test";

// Deprecated
echo "Name is ${$obj->name}";

// Good: use method syntax or direct access
echo "Name is {$obj->name}";

// For array access in interpolation
$user = ['name' => 'Jane'];
echo "Name is {$user['name']}";
```

## Examples

```php
<?php
// Complete examples of string interpolation fixes

$name = "Alice";
$age = 30;
$items = ['fruit' => 'apple', 'color' => 'red'];

// Before (PHP 8.1 — deprecated in 8.2)
echo "Hello ${name}";
echo "Age: ${age}";
echo "Item: ${items['fruit']}";

// After (PHP 8.2+ compatible)
echo "Hello {$name}";
echo "Age: {$age}";
echo "Item: {$items['fruit']}";

// Complex expressions still work with {}
echo "Double: {$age * 2}";
echo "Ternary: " . ($age > 18 ? 'adult' : 'minor');
echo "Method: " . strtoupper($name);

// Array/string interpolation
echo "Name: {$name}, Age: {$age}";
```

## Related Errors

- [PHP Deprecated]({{< relref "/languages/php/php-deprecated" >}}) — general deprecation warnings
- [PHP 8.2 Readonly Classes]({{< relref "/languages/php/php82-readonly-classes" >}}) — readonly class changes
- [PHP 8.2 Disjunctive Normal Form]({{< relref "/languages/php/php82-disjunctive-normal-form" >}}) — type system changes
