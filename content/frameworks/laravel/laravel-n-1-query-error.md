---
title: "[Solution] Laravel N+1 Query Error"
description: "N+1 causing perf issues."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

N+1 causing perf issues.

## Common Causes

Missing eager loading.

## How to Fix

Use with().

## Example

```php
$users = User::with('posts')->get();
```
