---
title: "[Solution] laravel Collection Error Laravel"
description: "Collection method not found."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Collection method not found.

## Common Causes

Wrong method.

## How to Fix

Check methods.

## Example

```php
$users = User::all()->filter(fn($u) => $u->active)->values();
```
