---
title: "PHP Warning: sprintf() format string issues"
description: "Fix PHP Warning: sprintf() format string issues. Learn to check format specifiers, escape percent signs, and validate argument count."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: sprintf() format string issues

This warning occurs when `sprintf()`, `printf()`, or `vsprintf()` encounter mismatches between format specifiers and the provided arguments.

## Common Causes

- Too few or too many arguments for the format string
- Unescaped percent signs in the format string
- Incorrect specifier characters

## How to Fix

### Check Format Specifiers

```php
<?php
// Wrong — too many arguments
$result = sprintf('%s has %d items', $name, $count, $extra);

// Correct — match specifiers to arguments
$result = sprintf('%s has %d items', $name, $count);
?>
```

### Escape % with %%

```php
<?php
// Wrong — unescaped percent sign
$result = sprintf('Discount: 50% off', $product);

// Correct — use %% for literal percent
$result = sprintf('Discount: 50%% off', $product);
?>
```

### Validate Argument Count

```php
<?php
// Wrong — too few arguments
$result = sprintf('%s %s', $first);

// Correct — provide all required arguments
$result = sprintf('%s %s', $first, $last);
?>
```

## Examples

```php
<?php
// This triggers the warning
$result = sprintf('Hello %s, you have %d messages', $name);
// Warning: sprintf(): Too few arguments

// Correct
$result = sprintf('Hello %s, you have %d messages', $name, $count);
$result = sprintf('Progress: %d%%', 75); // 'Progress: 75%'
?>
```

## Related Errors

- [PHP Warning: sprintf() too few arguments]({{< relref "/languages/php/warning-sprintf-too-few" >}})
- [PHP Warning: number_format()]({{< relref "/languages/php/warning-number-format" >}})
- [PHP Warning: sprintf()]({{< relref "/languages/php/warning-in-sprintf" >}})
