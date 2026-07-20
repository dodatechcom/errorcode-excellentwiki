---
title: "[Solution] PHP 8.0 String/Number Comparison Changes"
description: "Fix PHP 8.0 implicit float-to-int conversions and string/number comparison deprecations. Use strict comparisons and explicit casts."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1101
---

# PHP 8.0 String/Number Comparison Changes

PHP 8.0 changed how strings are compared to numbers. When a string is compared to an integer or float, PHP no longer silently converts the string to a number. This causes deprecation notices and potentially different comparison results than PHP 7.x.

## Common Causes

```php
<?php
// Cause 1: Comparing a numeric string to an integer
$result = "5" == 5; // Still works but behavior changed for edge cases

// Cause 2: Implicit float-to-int truncation in comparisons
$result = 0.1 + 0.2 == 0.3; // false due to floating point precision

// Cause 3: Loose comparison with mixed types
$value = "abc" == 0; // PHP 8.0: false (was true in PHP 7)

// Cause 4: Array key coercion from numeric strings
$array = ["1" => "one", 1 => "one"];
// PHP 8.0: These are now the same key

// Cause 5: Deprecated implicit float-to-int conversion
intdiv(1.5, 1); // Deprecated: implicit conversion from float to int
```

## How to Fix

### Fix 1: Use strict comparison operators

```php
<?php
// Use === and !== instead of == and !=
$value = "5";
$number = 5;

// Bad: loose comparison (behavior changed in PHP 8.0)
if ($value == $number) { /* ... */ }

// Good: strict comparison — always predictable
if ($value === $number) { /* ... */ }
```

### Fix 2: Cast types explicitly before comparison

```php
<?php
// Explicitly cast to the type you intend to compare
$string = "42";
$integer = 42;

// Cast string to int before comparing
if ((int) $string === $integer) {
    echo "Match";
}

// Cast to float when dealing with decimals
$float = 3.14;
$numericString = "3.14";
if ((float) $numericString === $float) {
    echo "Match";
}
```

### Fix 3: Use proper float comparison for decimal arithmetic

```php
<?php
// Bad: direct float equality (precision issues)
if (0.1 + 0.2 == 0.3) { /* ... */ }

// Good: compare with a tolerance (epsilon)
if (abs((0.1 + 0.2) - 0.3) < 0.0001) {
    echo "Values are approximately equal";
}

// Or use rounding
if (round(0.1 + 0.2, 10) === round(0.3, 10)) {
    echo "Values are equal";
}
```

### Fix 4: Fix implicit float-to-int in function calls

```php
<?php
// Bad: implicit float-to-int conversion
$result = intdiv(5.0, 2); // Deprecated in PHP 8.1

// Good: explicit cast
$result = intdiv((int) 5.0, 2);

// Or use floor/ceil as appropriate
$result = floor(5.0 / 2);
$result = (int) floor(5.0 / 2);
```

## Examples

```php
<?php
// PHP 8.0 comparison behavior changes

// String "0" vs integer 0
var_dump("0" == 0);   // true  (loose)
var_dump("0" === 0);  // false (strict)

// Non-numeric strings vs 0
var_dump("hello" == 0);  // false in PHP 8.0 (was true in PHP 7)
var_dump("hello" === 0); // false

// Numeric strings
var_dump("42" == 42);   // true  (loose)
var_dump("42" === 42);  // false (strict)
var_dump((int) "42" === 42); // true (explicit cast)
```

## Related Errors

- [PHP 8.0 Union Type Declaration]({{< relref "/languages/php/php80-union-type-declaration" >}}) — union type changes
- [PHP 8.0 Named Arguments]({{< relref "/languages/php/php80-named-argument" >}}) — named argument changes
- [PHP Deprecated]({{< relref "/languages/php/php-deprecated" >}}) — general deprecation warnings
