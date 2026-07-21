---
title: "[Solution] Deprecated Function Migration: compact() to array literal"
description: "Migrate from deprecated compact() to array literal."
deprecated_function: "compact('name', 'age')"
replacement_function: "['name' => $name, 'age' => $age]"
languages: ["php"]
deprecated_since: "Best Practice"
---

# [Solution] Deprecated Function Migration: compact() to array literal

The `compact('name', 'age')` has been deprecated in favor of `['name' => $name, 'age' => $age]`.

## Migration Guide

compact() creates arrays from variable names.

## Before (Deprecated)

```php
$name = 'Alice';
$age = 30;
$arr = compact('name', 'age');
```

## After (Modern)

```php
$name = 'Alice';
$age = 30;
$arr = ['name' => $name, 'age' => $age];
```

## Key Differences

- compact creates variables from strings
