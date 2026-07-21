---
title: "[Solution] Laravel Model Fill Error"
description: "Mass assignment blocked."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Mass assignment blocked.

## Common Causes

Not in fillable.

## How to Fix

Set fillable.

## Example

```php
protected $fillable = ['name', 'email'];
```
