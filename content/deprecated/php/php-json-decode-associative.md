---
title: "[Solution] Deprecated Function Migration: json_decode to json_decode with assoc flag"
description: "Migrate from deprecated json_decode without assoc flag."
deprecated_function: "json_decode($json)"
replacement_function: "json_decode($json, true)"
languages: ["php"]
deprecated_since: "Best Practice"
---

# [Solution] Deprecated Function Migration: json_decode to json_decode with assoc flag

The `json_decode($json)` has been deprecated in favor of `json_decode($json, true)`.

## Migration Guide

assoc flag returns arrays instead of objects.

## Before (Deprecated)

```php
$obj = json_decode($json);
```

## After (Modern)

```php
$arr = json_decode($json, true);
```

## Key Differences

- assoc flag returns arrays
