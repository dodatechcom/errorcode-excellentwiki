---
title: "[Solution] PHP Deprecated: create_function() is Deprecated"
description: "Fix PHP Deprecated: create_function() is deprecated. Use anonymous functions (closures), refactor to named functions, or use arrow functions."
languages: ["php"]
severities: ["deprecated"]
error-types: ["runtime-error"]
weight: 107
---

# PHP Deprecated: create_function() is Deprecated

The `create_function()` function was deprecated in PHP 7.2 and removed in PHP 8.0. It created anonymous functions from strings at runtime, but it had security risks (string-eval equivalent), poor performance, and lacked proper scoping. Replace it with closures, named functions, or arrow functions.

## Common Causes

```php
// Cause 1: Using create_function() for callbacks
<?php
$func = create_function('$a, $b', 'return $a + $b;');
echo $func(2, 3); // Deprecated: create_function()
?>
```

```php
// Cause 2: Using create_function() with usort
<?php
$numbers = [3, 1, 4, 1, 5];
usort($numbers, create_function('$a, $b', 'return $a - $b;'));
?>
```

```php
// Cause 3: Using create_function() for string transformations
<?php
$names = ['alice', 'bob', 'charlie'];
$upper = array_map(create_function('$name', 'return strtoupper($name);'), $names);
?>
```

```php
// Cause 4: Using create_function() for conditional logic
<?php
$formatter = create_function('$val', 'if ($val > 100) return number_format($val); return $val;');
echo $formatter(1500); // Deprecated
?>
```

## How to Fix

### Fix 1: Replace with Anonymous Functions (Closures)

Use PHP closures as the direct replacement for `create_function()`.

```php
<?php
// BEFORE (deprecated)
$func = create_function('$a, $b', 'return $a + $b;');
echo $func(2, 3);

// AFTER — closure
$func = function (int $a, int $b): int {
    return $a + $b;
};
echo $func(2, 3);
?>
```

### Fix 2: Replace with Arrow Functions (PHP 7.4+)

For simple single-expression functions, use arrow functions for cleaner syntax.

```php
<?php
// BEFORE (deprecated)
$numbers = [3, 1, 4, 1, 5];
usort($numbers, create_function('$a, $b', 'return $a - $b;'));

// AFTER — arrow function
$numbers = [3, 1, 4, 1, 5];
usort($numbers, fn($a, $b) => $a - $b);

// Simple transformations
$names = ['alice', 'bob', 'charlie'];
$upper = array_map(fn($name) => strtoupper($name), $names);
print_r($upper); // ['ALICE', 'BOB', 'CHARLIE']
?>
```

### Fix 3: Refactor to Named Functions

When the function is reusable, give it a proper name.

```php
<?php
// BEFORE (deprecated)
$formatter = create_function('$val', 'if ($val > 100) return number_format($val); return (string)$val;');

// AFTER — named function
function formatValue(int|float $val): string
{
    if ($val > 100) {
        return number_format($val);
    }
    return (string) $val;
}

echo formatValue(1500); // 1,500
echo formatValue(50);   // 50
?>
```

### Fix 4: Use Callable Arrays or Closures for Callbacks

For callbacks in array functions, use proper closures.

```php
<?php
// BEFORE (deprecated)
$data = [
    ['name' => 'Alice', 'age' => 30],
    ['name' => 'Bob', 'age' => 25],
    ['name' => 'Charlie', 'age' => 35],
];

usort($data, create_function('$a, $b', 'return $a["age"] - $b["age"];'));

// AFTER — closure
usort($data, fn($a, $b) => $a['age'] - $b['age']);

// Or use arrow function with <=> (spaceship operator)
usort($data, fn($a, $b) => $a['age'] <=> $b['age']);

// Or named function for complex logic
function sortByAge(array $a, array $b): int
{
    return $a['age'] <=> $b['age'];
}
usort($data, 'sortByAge');
?>
```

## Examples

```php
<?php
// Complete migration patterns

// Pattern 1: Simple callback
// BEFORE: $greet = create_function('$name', 'return "Hello, " . $name . "!";');
// AFTER:
$greet = fn(string $name): string => "Hello, {$name}!";

// Pattern 2: Array transformation
// BEFORE: array_map(create_function('$x', 'return $x * 2;'), $arr);
// AFTER:
$result = array_map(fn($x) => $x * 2, $arr);

// Pattern 3: Filtering
// BEFORE: array_filter($arr, create_function('$x', 'return $x > 10;'));
// AFTER:
$result = array_filter($arr, fn($x) => $x > 10);

// Pattern 4: Sorting with context
// BEFORE: create_function with string comparison
// AFTER:
usort($data, function (array $a, array $b) use ($sortField) {
    return $a[$sortField] <=> $b[$sortField];
});

// Pattern 5: Closure with use keyword
function multiplier(int $factor): Closure
{
    return fn(int $n): int => $n * $factor;
}

$double = multiplier(2);
$triple = multiplier(3);
echo $double(5);  // 10
echo $triple(5);  // 15
?>
```

```php
<?php
// Migration helper: search for create_function usage
// Run in terminal: grep -rn "create_function" --include="*.php" .

// Automated replacement strategy:
// 1. Create_function with simple body -> arrow function
// 2. Create_function with complex body -> closure
// 3. Create_function used once -> inline closure
// 4. Create_function used multiple times -> named function
?>
```

## Related Errors

- [PHP Deprecated: each()](/languages/php/warning-deprecated-each)
- [PHP Deprecated: mysql_* functions](/languages/php/warning-deprecated-mysql)
- [PHP Deprecated: Implicit Nullable Type](/languages/php/warning-deprecated-nullable)
