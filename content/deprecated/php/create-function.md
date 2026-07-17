---
title: "[Solution] PHP create_function() Deprecated — Use Anonymous Functions"
description: "Replace deprecated create_function() with anonymous functions (closures) in PHP. Modern PHP patterns with code examples."
deprecated_function: "create_function"
replacement_function: "anonymous function"
languages: ["php"]
deprecated_since: "PHP 7.2"
removed_in: "PHP 8.0"
error_message: "Deprecated: create_function() is deprecated"
weight: 50
---

# [Solution] PHP create_function() Deprecated — Use Anonymous Functions

The `create_function()` function was deprecated in PHP 7.2 and removed in PHP 8.0. It was essentially an `eval()` wrapper that created a named function at runtime. Modern PHP uses anonymous functions (closures) with the `function () {}` syntax, which is cleaner, faster, and more secure.

## What You'll See

On PHP 7.2 through 7.4:

```
Deprecated: create_function() is deprecated in /path/to/script.php on line X
```

On PHP 8.0+:

```
Fatal error: Uncaught Error: Call to undefined function create_function()
```

## Why Deprecated

`create_function()` was problematic for several reasons:

- **Security**: It internally used `eval()`, which is a serious security risk if user input reaches the function body.
- **Debugging**: Stack traces showed the function as `"{closure}"` with no useful context.
- **Performance**: The `eval()` call had overhead that anonymous functions avoid.
- **Readability**: The string-based syntax was hard to read and maintain.
- **Scoping**: It could not capture variables from the surrounding scope (no closures).

Anonymous functions are a first-class language feature in PHP 5.3+ and provide all the same functionality without the drawbacks.

## Old Code (Deprecated)

```php
// Simple callback
$multiplier = create_function('$x', 'return $x * 2;');
echo $multiplier(5); // 10

// Used with array functions
$numbers = [1, 2, 3, 4, 5];
$squared = array_map(create_function('$n', 'return $n * $n;'), $numbers);
print_r($squared);

// Used with usort
$items = ["banana", "apple", "cherry"];
usort($items, create_function('$a, $b', 'return strcasecmp($a, $b);'));
print_r($items);

// String transformation
$text = "hello world";
$upper = create_function('$str', 'return strtoupper($str);');
echo $upper($text);
```

## New Code (Replacement)

```php
// Simple callback — anonymous function syntax
$multiplier = function ($x) {
    return $x * 2;
};
echo $multiplier(5); // 10

// Short arrow function (PHP 7.4+) — single expression
$multiplier = fn($x) => $x * 2;
echo $multiplier(5); // 10

// Used with array functions
$numbers = [1, 2, 3, 4, 5];
$squared = array_map(fn($n) => $n * $n, $numbers);
print_r($squared);
// Output: Array ( [0] => 1 [1] => 4 [2] => 9 [3] => 16 [4] => 25 )

// Used with usort
$items = ["banana", "apple", "cherry"];
usort($items, fn($a, $b) => strcasecmp($a, $b));
print_r($items);

// String transformation
$text = "hello world";
$upper = fn($str) => strtoupper($str);
echo $upper($text);

// Closures can capture outer variables (create_function could not)
$tax_rate = 0.08;
$calculate_tax = function ($amount) use ($tax_rate) {
    return $amount * $tax_rate;
};
echo $calculate_tax(100); // 8
```

## Syntax Comparison

| Pattern | Old (`create_function`) | New (Anonymous function) |
|---|---|---|
| Simple function | `create_function('$x', 'return $x * 2;')` | `fn($x) => $x * 2` |
| Multi-line body | `create_function('$x', '$r = $x * 2; return $r;')` | `function ($x) { $r = $x * 2; return $r; }` |
| Capture outer var | Not possible | `fn($x) => $x + $offset` (auto-capture) or `use ($var)` |
| Callback for usort | `create_function('$a,$b', '...')` | `fn($a, $b) => strcmp($a, $b)` |

Arrow functions (`fn()`) automatically capture outer variables by value, so you do not need the `use` keyword. For multi-line functions, use the full `function () {}` syntax.

## Migration Steps

1. **Find all create_function() calls**:

```bash
grep -rn "create_function" --include="*.php" /path/to/project/
```

2. **Replace each call** with an anonymous function or arrow function. Extract the parameter list and body from the string arguments.

3. **If the body references outer variables**, use `use ($var)` for traditional closures or rely on arrow function auto-capture (PHP 7.4+).

4. **Review security**. If any `create_function()` body was building SQL or executing shell commands with user input, rewrite it with proper escaping or prepared statements.

5. **Run your test suite** to verify all callbacks produce the same results.

6. **Search for related deprecated patterns** like `each()` and `ereg()` that may also need migration:

```bash
grep -rn "ereg\|each\s*(" --include="*.php" /path/to/project/
```
