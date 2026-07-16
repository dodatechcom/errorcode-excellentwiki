---
title: "[Solution] PHP ereg() Deprecated — Replace with preg_match() Migration"
description: "Replace deprecated ereg() with preg_match() in PHP. Migration guide with before/after code examples and bulk conversion script."
deprecated_function: "ereg"
replacement_function: "preg_match"
languages: ["php"]
deprecated_since: "PHP 5.3"
removed_in: "PHP 7.0"
error_message: "Deprecated: Function ereg() is deprecated"
tags: ["regex", "posix", "pcre", "ereg"]
weight: 10
---

# [Solution] PHP ereg() Deprecated — Replace with preg_match() Migration

The `ereg()` function was removed from PHP because PCRE (Perl Compatible Regular Expressions) provides better performance, richer features, and broader industry support. Migrating to `preg_match()` is straightforward once you understand the key differences in syntax. The PCRE engine used by `preg_match()` is faster and more secure than the old POSIX regex functions.

## What You'll See

If your code still calls `ereg()`, `eregi()`, `ereg_replace()`, or `eregi_replace()` on PHP 7.0+, you will see:

```
Deprecated: Function ereg() is deprecated in /path/to/script.php on line X
```

On PHP 7.0+, the error becomes fatal:

```
Fatal error: Uncaught Error: Call to undefined function ereg()
```

## Why Deprecated

PHP deprecated all POSIX regex functions (`ereg`, `eregi`, `ereg_replace`, `eregi_replace`, `split`) in PHP 5.3 and removed them entirely in PHP 7.0. The PCRE extension (`preg_*` functions) replaced them because:

- **Performance**: PCRE is significantly faster for complex patterns.
- **Features**: PCRE supports non-greedy matching, lookaheads, named groups, and other advanced syntax.
- **Industry standard**: PCRE is based on Perl's regex engine and is used across many languages and platforms.
- **Security**: The POSIX regex engine in PHP had known vulnerabilities with certain crafted patterns.

## Old Code (Deprecated)

```php
// Basic match with ereg
$email = "user@example.com";
if (ereg("^[a-zA-Z0-9._]+@[a-zA-Z0-9._]+$", $email)) {
    echo "Valid email";
}

// Case-insensitive match with eregi
if (eregi("^hello", "Hello World")) {
    echo "Starts with hello";
}

// Replace with ereg_replace
$date = "2024-01-15";
$formatted = ereg_replace("([0-9]{4})-([0-9]{2})-([0-9]{2})", "\\3/\\2/\\1", $date);
echo $formatted; // 15/01/2024

// Sub-pattern capture with ereg
if (ereg("([a-z]+)@([a-z]+)", $email, $matches)) {
    echo "User: " . $matches[1] . ", Domain: " . $matches[2];
}
```

## New Code (Replacement)

```php
// Basic match with preg_match — note the delimiters and anchoring
$email = "user@example.com";
if (preg_match("/^[a-zA-Z0-9._]+@[a-zA-Z0-9._]+$/", $email)) {
    echo "Valid email";
}

// Case-insensitive match with preg_match — use the 'i' modifier
if (preg_match("/^hello/i", "Hello World")) {
    echo "Starts with hello";
}

// Replace with preg_match_replace
$date = "2024-01-15";
$formatted = preg_replace("/(\d{4})-(\d{2})-(\d{2})/", "$3/$2/$1", $date);
echo $formatted; // 15/01/2024

// Sub-pattern capture with preg_match
if (preg_match("/([a-z]+)@([a-z]+)/", $email, $matches)) {
    echo "User: " . $matches[1] . ", Domain: " . $matches[2];
}

// Named capture groups (PCRE advantage)
if (preg_match("/(?P<user>[a-z]+)@(?P<domain>[a-z]+)/", $email, $matches)) {
    echo "User: " . $matches['user'] . ", Domain: " . $matches['domain'];
}
```

## Key Syntax Differences

| POSIX (Old) | PCRE (New) |
|---|---|
| `ereg("pattern", $str)` | `preg_match("/pattern/", $str)` |
| `eregi("pattern", $str)` | `preg_match("/pattern/i", $str)` |
| `ereg_replace("p", "r", $str)` | `preg_replace("/p/", "r", $str)` |
| `\\1` (back-reference) | `$1` or `$1` in replacement |
| No delimiters required | Delimiters required (usually `/`) |

The most common mistake is forgetting to wrap the pattern in delimiters. Use `/`, `~`, `#`, or any non-alphanumeric character that does not appear in your pattern.

## Migration Steps

1. **Find all POSIX regex calls** in your codebase:

```bash
grep -rn "ereg\|eregi\|ereg_replace\|eregi_replace" --include="*.php" /path/to/project/
```

2. **Wrap every pattern in delimiters** (`/pattern/`). Escape any `/` characters inside the pattern.

3. **Replace `eregi()` calls** by adding the `i` modifier after the closing delimiter instead.

4. **Replace back-references** in `ereg_replace()`. Change `\\1` to `$1` in the replacement string.

5. **Test thoroughly.** PCRE and POSIX regex have subtle differences in character class behavior and anchoring.

6. **Search for leftover split() calls** since `split()` was also deprecated alongside `ereg()`:

```bash
grep -rn "\bsplit\s*(" --include="*.php" /path/to/project/
```

For large codebases, consider using a scripted sed replacement or a tool like [Rector](https://getrector.com/) to automate the conversion.
