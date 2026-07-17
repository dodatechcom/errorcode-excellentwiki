---
title: "[Solution] PHP First Class Callable: Syntax Error Fix"
description: "Fix PHP first class callable syntax errors. Learn how PHP 8.1 first class callables work."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["first-class-callable", "closure", "syntax", "php"]
weight: 5
---

# PHP First Class Callable: Syntax Error Fix

A PHP first class callable error occurs when you use incorrect syntax for creating first class callables. This feature was introduced in PHP 8.1.

## What This Error Means

PHP 8.1 introduced first class callable syntax using `Closure::fromCallable()` or the short syntax `strlen(...)`. This allows passing a function as a callable without wrapping it in a closure. Errors occur when the syntax is wrong or the function doesn't exist.

## Common Causes

- Wrong syntax for first class callables
- Using the syntax on non-callable expressions
- Missing the trailing parentheses `(...)`
- Using the feature on PHP versions before 8.1

## How to Fix

### 1. Use correct first class callable syntax

```php
<?php
// WRONG: Missing parentheses
// $callable = strlen; // Not a first class callable

// CORRECT: Use closure syntax
$callable = Closure::fromCallable('strlen');
$callable = strlen(...); // PHP 8.1+ short syntax
echo $callable('hello'); // 5
?>
```

### 2. Use for array functions

```php
<?php
// WRONG: Old way with Closure::fromCallable
// $callable = Closure::fromCallable('array_map'); // Works but verbose

// CORRECT: PHP 8.1+ short syntax
$mapper = array_map(...);
$result = $mapper(fn($x) => $x * 2, [1, 2, 3]);
// [2, 4, 6]
?>
```

### 3. Use with built-in functions

```php
<?php
// CORRECT: First class callable with built-in functions
$trimmer = trim(...);
$result = $trimmer('  hello  '); // "hello"

$filter = array_filter(...);
$result = $filter([1, 2, 3, 4], fn($n) => $n > 2);
// [3, 4]
?>
```

### 4. Pass callables to higher-order functions

```php
<?php
// CORRECT: Pass first class callables directly
$numbers = [1, 2, 3, 4, 5];

// Using with array_map
$squared = array_map(fn($x) => $x ** 2, $numbers);

// Using first class callable with method references
$obj = new StringableHelper();
$method = $obj->process(...);
$results = array_map($method, $numbers);
?>
```

## Related Errors

- [PHP Parse error]({{< relref "/languages/php/parse-error" >}})
- [PHP Deprecated function]({{< relref "/languages/php/php-deprecated-error-v2" >}})
- [PHP Named argument error]({{< relref "/languages/php/php-named-arg-error-v2" >}})
