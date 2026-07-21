---
title: "[Solution] Deprecated Function Migration: magic quotes to addslashes"
description: "Migrate from deprecated magic quotes to addslashes."
deprecated_function: "magic quotes automatic escaping"
replacement_function: "addslashes($str)"
languages: ["php"]
deprecated_since: "PHP 5.4"
---

# [Solution] Deprecated Function Migration: magic quotes to addslashes

The `magic quotes automatic escaping` has been deprecated in favor of `addslashes($str)`.

## Migration Guide

Magic quotes were removed.

## Before (Deprecated)

```php
$safe = $input;  // magic quotes auto-escaped
```

## After (Modern)

```php
$safe = addslashes($input);
```

## Key Differences

- addslashes is explicit
