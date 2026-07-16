---
title: "[Solution] PHP each() Deprecated — Replace with foreach() Migration"
description: "Replace deprecated each() with foreach() in PHP. Modern iteration patterns with code examples and performance benefits."
deprecated_function: "each"
replacement_function: "foreach"
languages: ["php"]
deprecated_since: "PHP 7.2"
removed_in: "PHP 8.0"
error_message: "Deprecated: each() is deprecated"
tags: ["each", "foreach", "iteration", "array"]
weight: 30
---

# [Solution] PHP each() Deprecated — Replace with foreach() Migration

The `each()` function was deprecated in PHP 7.2 and removed in PHP 8.0. It was commonly used in older PHP code to iterate over arrays by returning the current key-value pair and advancing the internal pointer. Modern PHP code should use `foreach` loops, which are cleaner, faster, and more readable.

## What You'll See

On PHP 7.2 through 7.4:

```
Deprecated: each() is deprecated in /path/to/script.php on line X
```

On PHP 8.0+:

```
Fatal error: Uncaught Error: Call to undefined function each()
```

## Why Deprecated

`each()` had several drawbacks:

- **Readability**: It obscures the intent of the loop compared to `foreach`.
- **Internal pointer**: It relies on the array's internal pointer, which can lead to subtle bugs if the pointer is moved unexpectedly.
- **Performance**: `foreach` is optimized internally in the PHP engine and runs faster.
- **Limited functionality**: `each()` cannot iterate over objects or generators, while `foreach` can.

## Old Code (Deprecated)

```php
// Basic each() iteration
$colors = ["red", "green", "blue"];
while (list($key, $value) = each($colors)) {
    echo "$key => $value\n";
}

// each() with a for-style loop
$names = ["Alice" => 30, "Bob" => 25, "Charlie" => 35];
reset($names);
while (list($name, $age) = each($names)) {
    echo "$name is $age years old\n";
}

// Using each() to get the current element without a loop
$fruits = ["apple", "banana", "cherry"];
$current = each($fruits);
print_r($current);
// Output: Array ( [1] => apple [value] => apple [0] => 0 [key] => 0 )
```

## New Code (Replacement)

```php
// Basic foreach iteration — clean and direct
$colors = ["red", "green", "blue"];
foreach ($colors as $key => $value) {
    echo "$key => $value\n";
}

// foreach with associative arrays
$names = ["Alice" => 30, "Bob" => 25, "Charlie" => 35];
foreach ($names as $name => $age) {
    echo "$name is $age years old\n";
}

// When you only need the current element (replacing each() for single-use)
$fruits = ["apple", "banana", "cherry"];
$first_key = array_key_first($fruits);  // PHP 7.3+
$first_value = $fruits[$first_key];
echo "First: $first_key => $first_value\n";

// Get both key and value of the current element without a loop
$key = key($fruits);
$value = current($fruits);
echo "Current: $key => $value\n";

// Iterating with both key and value in foreach
$scores = ["math" => 95, "science" => 88, "english" => 92];
foreach ($scores as $subject => $score) {
    $grade = $score >= 90 ? "A" : ($score >= 80 ? "B" : "C");
    echo "$subject: $score ($grade)\n";
}
```

## Key Differences

| Pattern | Old (`each()`) | New (`foreach`) |
|---|---|---|
| Key-value iteration | `while (list($k, $v) = each($arr))` | `foreach ($arr as $k => $v)` |
| Value only | `while (list(, $v) = each($arr))` | `foreach ($arr as $v)` |
| Reset pointer first | `reset($arr)` required | Not needed |
| Modifying values | `each()` does not allow it | `foreach ($arr as &$v)` with reference |

The `foreach` loop handles the internal pointer automatically, so you never need to call `reset()` before iterating.

## Migration Steps

1. **Find all each() calls** in your codebase:

```bash
grep -rn "\beach\s*(" --include="*.php" /path/to/project/
```

2. **Replace `while` + `list()` + `each()` patterns** with `foreach`. The conversion is almost always a direct translation:

```php
// Before
reset($arr);
while (list($k, $v) = each($arr)) { ... }

// After
foreach ($arr as $k => $v) { ... }
```

3. **Replace standalone `each()` calls** (used to get one element) with `key()` and `current()`, or use `array_key_first()` on PHP 7.3+.

4. **If modifying values**, use the reference syntax `foreach ($arr as &$value)` and unset the reference afterward to avoid accidental modifications.

5. **Run your test suite.** The `foreach` loop resets the pointer internally, so any code that depends on the pointer position after the loop may behave differently.
