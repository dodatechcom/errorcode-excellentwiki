---
title: "[Solution] PHP split() Deprecated — Replace with explode() Migration"
description: "Replace deprecated split() with explode() in PHP. Quick migration guide with code examples for string and regex splitting."
deprecated_function: "split"
replacement_function: "explode"
languages: ["php"]
deprecated_since: "PHP 5.3"
removed_in: "PHP 7.0"
error_message: "Deprecated: Function split() is deprecated"
weight: 20
---

# [Solution] PHP split() Deprecated — Replace with explode() Migration

The `split()` function was one of several POSIX-era functions removed from PHP in version 7.0. For simple string splitting, `explode()` is the direct replacement. For splitting by a regex pattern, use `preg_split()`. Both replacements are faster and actively maintained.

## What You'll See

On PHP 5.3 through 5.6:

```
Deprecated: Function split() is deprecated in /path/to/script.php on line X
```

On PHP 7.0+:

```
Fatal error: Uncaught Error: Call to undefined function split()
```

## Why Deprecated

PHP removed `split()` along with the other POSIX regex functions in PHP 7.0. The function had two use cases — splitting by a literal string and splitting by a regex — and each has a dedicated, better-performing replacement:

- `explode()` handles literal string splitting and is optimized internally.
- `preg_split()` handles regex-based splitting with full PCRE support.

Removing `split()` eliminated ambiguity and removed the dependency on the aging POSIX regex engine.

## Old Code (Deprecated)

```php
// Split by a comma
_csv = "apple,banana,cherry";
$fruits = split(",", $csv);
print_r($fruits);

// Split by a colon, limit to 3 parts
$path = "/usr/local/bin";
$parts = split(":", $path, 3);

// Split using a regex pattern (digits)
$data = "abc123def456";
$parts = split("[0-9]+", $data);
print_r($parts);

// Split by a regex and capture the delimiter
$line = "one::two::three";
$parts = split("(:+)", $line);
print_r($parts);
```

## New Code (Replacement)

```php
// Split by a comma — use explode()
$csv = "apple,banana,cherry";
$fruits = explode(",", $csv);
print_r($fruits);
// Output: Array ( [0] => apple [1] => banana [2] => cherry )

// Split by a colon, limit to 3 parts — explode() supports a limit parameter
$path = "/usr/local/bin";
$parts = explode(":", $path, 3);
// Note: explode() limit works differently than split() — it returns
// at most $limit elements, with the last containing the remainder.

// Split using a regex pattern — use preg_split()
$data = "abc123def456";
$parts = preg_split("/[0-9]+/", $data);
print_r($parts);
// Output: Array ( [0] => abc [1] => def [2] => )

// Split and capture the delimiter using preg_split()
$line = "one::two::three";
$parts = preg_split("/(:+)/", $line, -1, PREG_SPLIT_DELIM_CAPTURE);
print_r($parts);
// Output: Array ( [0] => one [1] => :: [2] => two [3] => :: [4] => three )
```

## Explode vs preg_split — When to Use Which

Use `explode()` when you are splitting by a fixed, literal string. It is faster because it does not invoke the regex engine.

Use `preg_split()` when you need to split by a pattern — for example, splitting on any whitespace character, multiple delimiters, or a numeric boundary.

```php
// explode() — literal delimiter
$fields = str_getcsv("John,Doe,\"New York\",NY");

// preg_split() — regex delimiter (any whitespace)
$words = preg_split("/\s+/", "hello   world\ttabs");
```

## Migration Steps

1. **Find all split() calls** in your project:

```bash
grep -rn "\bsplit\s*(" --include="*.php" /path/to/project/
```

2. **Determine the delimiter type.** If it is a plain string (comma, colon, dash), replace with `explode()`. If it is a regex character class or pattern, replace with `preg_split()`.

3. **Check the limit parameter.** `split($delim, $str, $limit)` and `explode($delim, $str, $limit)` behave slightly differently at boundary conditions. Test edge cases.

4. **If capturing delimiters**, add `PREG_SPLIT_DELIM_CAPTURE` to `preg_split()` flags.

5. **Run your test suite** to verify the output arrays are identical.

6. **Search for related deprecated functions** (`ereg`, `eregi`, `ereg_replace`) and migrate those as well:

```bash
grep -rn "ereg\|eregi\|ereg_replace" --include="*.php" /path/to/project/
```
