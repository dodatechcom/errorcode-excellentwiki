---
title: "[Solution] PHP ereg_replace() Deprecated — Replace with preg_replace()"
description: "Replace deprecated ereg_replace() with preg_replace() in PHP. Migration guide with delimiter rules, back-reference changes, and bulk conversion."
deprecated_function: "ereg_replace"
replacement_function: "preg_replace"
languages: ["php"]
deprecated_since: "PHP 5.3"
removed_in: "PHP 7.0"
error_message: "Deprecated: Function ereg_replace() is deprecated"
tags: ["ereg-replace", "preg-replace", "regex", "posix", "pcre"]
weight: 25
---

# [Solution] PHP ereg_replace() Deprecated — Replace with preg_replace()

The `ereg_replace()` function was deprecated in PHP 5.3 and removed in PHP 7.0. It used POSIX regular expressions to search and replace patterns in strings. The replacement is `preg_replace()`, which uses PCRE (Perl Compatible Regular Expressions) — a faster, more secure, and more feature-rich engine. The main syntax differences are: PCRE requires delimiters around the pattern, and back-references in the replacement string use `$1` instead of `\1`.

## What You'll See

On PHP 5.3-5.6:

```
Deprecated: Function ereg_replace() is deprecated in /path/to/script.php on line X
```

On PHP 7.0+:

```
Fatal error: Uncaught Error: Call to undefined function ereg_replace()
```

## Old Code (Deprecated)

```php
// Basic replacement with ereg_replace
$date = "2024-01-15";
$formatted = ereg_replace("([0-9]{4})-([0-9]{2})-([0-9]{2})", "\\3/\\2/\\1", $date);
echo $formatted;  // 15/01/2024

// Case-insensitive replacement
$text = "Hello World";
$result = ereg_replace("hello", "Hi", $text);
echo $result;  // "Hello World" (ereg_replace is case-sensitive by default)

// ereng_replace for case-insensitive
$result = eregi_replace("hello", "Hi", $text);
echo $result;  // "Hi World"

// Replace with back-references
$name = "John Doe";
$formatted = ereg_replace("([a-z]+) ([a-z]+)", "\\1. \\2", $name);
echo $formatted;  // "J. D" (only first char matched by [a-z]+)

// Remove non-alphanumeric characters
$dirty = "Hello, World! 123";
$clean = ereg_replace("[^a-zA-Z0-9]", "", $dirty);
echo $clean;  // "HelloWorld123"
```

## New Code (Replacement)

```php
// Basic replacement with preg_replace — add delimiters and update back-references
$date = "2024-01-15";
$formatted = preg_replace("/([0-9]{4})-([0-9]{2})-([0-9]{2})/", "$3/$2/$1", $date);
echo $formatted;  // 15/01/2024

// Case-insensitive replacement — add 'i' modifier
$text = "Hello World";
$result = preg_replace("/hello/i", "Hi", $text);
echo $result;  // "Hi World"

// Named back-references (PCRE advantage)
$name = "John Doe";
$formatted = preg_replace("/(\w+) (\w+)/", "$1. $2", $name);
echo $formatted;  // "J. D"

// With named groups
$formatted = preg_replace("/(?P<first>\w+) (?P<last>\w+)/", "${first}. ${last}", $name);
echo $formatted;  // "J. D"

// Remove non-alphanumeric characters
$dirty = "Hello, World! 123";
$clean = preg_replace("/[^a-zA-Z0-9]/", "", $dirty);
echo $clean;  // "HelloWorld123"
```

## Key Syntax Differences

| POSIX (Old) | PCRE (New) |
|---|---|
| `ereg_replace("pattern", "replacement", $str)` | `preg_replace("/pattern/", "replacement", $str)` |
| `eregi_replace("pattern", "repl", $str)` | `preg_replace("/pattern/i", "repl", $str)` |
| `\\1` back-reference in replacement | `$1` back-reference in replacement |
| No delimiters required | Delimiters required (wrap in `/pattern/`) |
| `[^0-9]` in character class | Same — `[^0-9]` works identically |

## Delimiter Rules

PCRE requires delimiters around the pattern. Choose any non-alphanumeric character that does not appear in the pattern:

```php
// Common delimiter choices
preg_replace("/pattern/", "replacement", $str);   // forward slashes (most common)
preg_replace("~pattern~", "replacement", $str);   // tilde (good when pattern has /)
preg_replace("#pattern#", "replacement", $str);   // hash

// If your pattern contains the delimiter, escape it
preg_replace("/path\/to\/file/", "replacement", $str);  // escape slashes
// OR use a different delimiter
preg_replace("~path/to/file~", "replacement", $str);
```

## Migration Steps

1. **Find all ereg_replace calls**:

```bash
grep -rn "ereg_replace\|eregi_replace" --include="*.php" /path/to/project/
```

2. **Wrap patterns in delimiters** (usually `/pattern/`).

3. **Replace back-references**: Change `\\1` to `$1`, `\\2` to `$2`, etc.

4. **Replace case-insensitive calls**: Change `eregi_replace()` to `preg_replace("/pattern/i", ...)`.

5. **Test thoroughly** — PCRE and POSIX regex have subtle differences in character class behavior and anchoring.

6. **Also check for related deprecated functions**:

```bash
grep -rn "ereg\|eregi\|split\b" --include="*.php" /path/to/project/
```

For large codebases, consider using [Rector](https://getrector.com/) to automate the conversion.

## Related Errors

- [ereg() → preg_match()](ereg-to-preg-match) — matching without replacement.
- [session_register() → $_SESSION](session-register) — PHP session migration.
