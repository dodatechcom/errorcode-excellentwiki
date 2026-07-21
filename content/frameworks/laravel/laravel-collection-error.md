---
title: "[Solution] Laravel Collection Error"
description: "Collection method not working."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Collection method not working.

## Common Causes

Wrong method.

## How to Fix

Check methods.

## Example

```php
$users = User::all()->filter(fn($u) => $u->active);
```
